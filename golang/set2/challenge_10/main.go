package main

import (
	"bytes"
	"crypto/aes"
	"crypto/rand"
	"encoding/hex"
	"fmt"
	"io"
)

func main() {
	plaintext := []byte("xin the gioi chao")
	key := []byte("topsecret_popoiu")
	fmt.Println("Plaintext: ", string(plaintext))

	ciphertext, err := EncryptCBC(plaintext, key)
	if err != nil {
		panic(err)
	}
	fmt.Println("Cipher text(hex): ", hex.EncodeToString(ciphertext))

	decrypttext, err := DecryptCBC(ciphertext, key)
	if err != nil {
		panic(err)
	}
	fmt.Println("Decrypt text:", string(decrypttext))

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
	plaintext := make([]byte, len(ciphertext)-blockSize)
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
