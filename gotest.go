package main

import (
	"encoding/hex"
	"fmt"
	"log"
)

func main(){
	src := "48656c6c6f20476f7068657221"
	decoded, err := hex.DecodeString(src)
	if err != nil{
		log.Fatal(err)
	}
	fmt.Println("%s\n", string(decoded[:]))	
}
