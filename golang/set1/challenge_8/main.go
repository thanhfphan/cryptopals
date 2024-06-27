package main

import (
	"encoding/hex"
	"fmt"
	"io"
	"os"
)

// Remember that the problem with ECB is that it is stateless and deterministic;
// the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
func main() {
	file, err := os.Open("8.txt")
	if err != nil {
		panic(err)
	}
	fileContent, err := io.ReadAll(file)
	if err != nil {
		panic(err)
	}

	mapCount := map[string]int{}
	// blockSize := aes.BlockSize
	for i := 0; i < len(fileContent); i++ {
		if i+32 > len(fileContent) {
			break
		}
		hexdata := fileContent[i : i+32]
		hexbyte, err := hex.DecodeString(string(hexdata))
		if err != nil {
			continue
		}
		block := hex.EncodeToString(hexbyte)
		mapCount[block]++
	}

	for k, v := range mapCount {
		if v > 1 {
			fmt.Printf("Block: %s Count: %d\n", k, v)
		}
	}
	fmt.Println("Finish Detect AES in ECB mode")
}
