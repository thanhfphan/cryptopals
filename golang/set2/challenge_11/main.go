package main

import (
	"bytes"
	"crypto/aes"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"io"
	mrand "math/rand"
)

func randomKey() []byte {
	key := make([]byte, 16)

	_, err := io.ReadFull(rand.Reader, key)
	if err != nil {
		panic(err)
	}

	return key
}

func genPlaintext() []byte {
	r1 := make([]byte, mrand.Intn(5))
	_, err := io.ReadFull(rand.Reader, r1)
	if err != nil {
		panic(err)
	}

	key := "YELLOW SUBMARINEYELLOW SUBMARINE"

	r2 := make([]byte, mrand.Intn(10))
	_, err = io.ReadFull(rand.Reader, r2)
	if err != nil {
		panic(err)
	}

	result := append(r1[:], key...)
	result = append(result, r2...)
	return result
}

func IsECBMode(ciphertext []byte, blockSize int) bool {
	decodeMap := map[string]bool{}
	for i := 0; i < len(ciphertext); i += blockSize {
		key := string(ciphertext[i : i+blockSize])
		if decodeMap[key] {
			return true
		}
		decodeMap[key] = true
	}

	return false
}

func main() {
	key := randomKey()
	plaintext := genPlaintext()
	fmt.Println("Plaintext: ", hex.EncodeToString(plaintext))

	var (
		ciphertext []byte
		err        error
	)
	if mrand.Int()%2 == 0 {
		fmt.Println("Mode CBC")
		ciphertext, err = EncryptCBC(plaintext, key)
		if err != nil {
			panic(err)
		}
	} else {
		fmt.Println("Mode ECB")
		ciphertext, err = EncryptECB(plaintext, key)
		if err != nil {
			panic(err)
		}
	}

	isECBMode := IsECBMode(ciphertext, aes.BlockSize)
	fmt.Println("Is ECB Mode: ", isECBMode)

}

func EncryptCBC(plaintext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	blockSize := block.BlockSize()
	plaintext = PKCS7Padding(plaintext, blockSize)

	ciphertext := make([]byte, blockSize+len(plaintext))
	iv := ciphertext[:blockSize]

	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		return nil, err
	}

	prevBlock := iv
	for i := 0; i < len(plaintext); i += blockSize {
		currentBlock := plaintext[i : i+blockSize]
		xorBlock := make([]byte, blockSize)
		XORBytes(xorBlock, currentBlock, prevBlock)
		// blockSize *2 cause we need to skip IV block
		block.Encrypt(ciphertext[i+blockSize:i+blockSize*2], xorBlock)
		prevBlock = ciphertext[i+blockSize : i+blockSize*2]
	}

	return ciphertext, nil
}

func XORBytes(desc, src, b []byte) []byte {
	l := len(src)
	if len(b) < l {
		l = len(b)
	}

	if len(desc) < l {
		panic("xorbytes: len(desc) < l")
	}

	for i := range l {
		desc[i] = src[i] ^ b[i]
	}

	return desc
}

func EncryptECB(plaintext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	blockSize := block.BlockSize()
	plaintext = PKCS7Padding(plaintext, blockSize)

	ciphertext := make([]byte, len(plaintext))
	for i := 0; i < len(plaintext); i += blockSize {
		block.Encrypt(ciphertext[i:i+blockSize], plaintext[i:i+blockSize])
	}

	return ciphertext, nil
}

func DecryptECB(ciphertext, key []byte) ([]byte, error) {
	cipher, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	size := cipher.BlockSize()
	if len(ciphertext)%size != 0 {
		return nil, fmt.Errorf("ciphertext is not a multiple of the block size")
	}
	plaintext := make([]byte, len(ciphertext))
	for bs, be := 0, size; bs < len(ciphertext); bs, be = bs+size, be+size {
		cipher.Decrypt(plaintext[bs:be], ciphertext[bs:be])
	}

	plaintext, err = PKCS7Unpadding(plaintext)
	if err != nil {
		return nil, err
	}

	return plaintext, nil
}

func DecryptCBC(ciphertext, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	blockSize := block.BlockSize()
	if blockSize > len(ciphertext) {
		return nil, fmt.Errorf("invalid len ciphertext")
	}

	iv := ciphertext[:blockSize]
	preBlock := iv
	ciphertext = ciphertext[blockSize:]
	plaintext := make([]byte, len(ciphertext))
	for i := 0; i < len(ciphertext); i += blockSize {
		currentBlock := ciphertext[i : i+blockSize]
		decryptedBlock := make([]byte, blockSize)
		block.Decrypt(decryptedBlock, currentBlock)
		XORBytes(plaintext[i:i+blockSize], decryptedBlock, preBlock)
		preBlock = currentBlock
	}

	plaintext, err = PKCS7Unpadding(plaintext)
	if err != nil {
		return nil, err
	}

	return plaintext, nil
}

func PKCS7Padding(plaintext []byte, blockSize int) []byte {
	paddingLen := blockSize - len(plaintext)%blockSize
	p := byte(paddingLen)
	padding := bytes.Repeat([]byte{p}, paddingLen)
	return append(plaintext, padding...)
}

func PKCS7Unpadding(paddedText []byte) ([]byte, error) {
	l := len(paddedText)
	// fmt.Println(string(paddedText))
	paddingLen := int(paddedText[l-1])
	if paddingLen >= l {
		return nil, fmt.Errorf("padding length is greater than the length of the text")
	}
	return paddedText[:l-paddingLen], nil
}
