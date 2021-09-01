package main

import (
	"C"
	"log"
)

//export helloWorld
func helloWorld() {
	log.Println("Welcome to GO executed in Python!")
}

//export multiply
func multiply(a int, b int) int {
	return (a * b)
}

func main() {
}
