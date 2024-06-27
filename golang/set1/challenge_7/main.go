package main

import (
	"crypto/aes"
	"encoding/base64"
	"fmt"
	"io"
	"os"
)

func main() {
	file, err := os.Open("7.txt")
	if err != nil {
		panic(err)
	}

	key := []byte("YELLOW SUBMARINE")
	fileContent, err := io.ReadAll(file)
	if err != nil {
		panic(err)
	}

	cipherText, err := base64.StdEncoding.DecodeString(string(fileContent))
	if err != nil {
		panic(err)
	}
	text, err := decryptAES128ECB(cipherText, key)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(text))
}

func decryptAES128ECB(data, key []byte) ([]byte, error) {
	cipher, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	decrypted := make([]byte, len(data))
	size := 16

	for bs, be := 0, size; bs < len(data); bs, be = bs+size, be+size {
		cipher.Decrypt(decrypted[bs:be], data[bs:be])
	}

	return decrypted, nil
}
