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

func decryptAES128ECB(ciphertext, key []byte) ([]byte, error) {
	cipher, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}

	size := cipher.BlockSize()
	if len(ciphertext)%size != 0 {
		return nil, fmt.Errorf("ciphertext is not a multiple of the block size")
	}
	decrypted := make([]byte, len(ciphertext))
	for bs, be := 0, size; bs < len(ciphertext); bs, be = bs+size, be+size {
		cipher.Decrypt(decrypted[bs:be], ciphertext[bs:be])
	}

	return decrypted, nil
}
