package main

import (
	"bytes"
	"fmt"
)

func main() {
	plainText := []byte("YELLOW SUBMARINE")
	// blockSize := aes.BlockSize
	blockSize := 20
	newPlainText := PKCS7Padding(plainText, blockSize)

	fmt.Println("Len plainText", len(plainText))
	fmt.Println("Len newPlainText", len(newPlainText))
	fmt.Println(string(newPlainText))
}

func PKCS7Padding(plaintext []byte, blockSize int) []byte {
	paddingLen := blockSize - len(plaintext)%blockSize
	p := byte(paddingLen)
	padding := bytes.Repeat([]byte{p}, paddingLen)
	return append(plaintext, padding...)
}
