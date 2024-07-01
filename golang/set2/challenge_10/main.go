package main

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
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

	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext[blockSize:], plaintext)

	return ciphertext, nil
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
	ciphertext = ciphertext[blockSize:]

	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(ciphertext, ciphertext)

	ciphertext, err = PKCS7Unpadding(ciphertext)
	if err != nil {
		return nil, err
	}

	return ciphertext, nil
}

func PKCS7Padding(plaintext []byte, blockSize int) []byte {
	paddingLen := blockSize - len(plaintext)%blockSize
	p := byte(paddingLen)
	padding := bytes.Repeat([]byte{p}, paddingLen)
	return append(plaintext, padding...)
}

func PKCS7Unpadding(paddedText []byte) ([]byte, error) {
	len := len(paddedText)
	paddingLen := int(paddedText[len-1])
	if paddingLen >= len {
		return nil, fmt.Errorf("padding length is greater than the length of the text")
	}
	return paddedText[:len-paddingLen], nil
}
