package main

import (
	"fmt"
	"math"
	"math/bits"
)

// Hello returns a greeting for the named person.
func main() {
	//Hello world
	//hello_world()
	//Define variables
	//define_variables()
	/*Data type*/
	data_type()
}

func define_variables() {
	fmt.Println("=====================")
	// Define Variables
	var a int
	a = 1
	var b int = 0
	fmt.Println(a)
	fmt.Println(b)
	var c, d = 2, 3
	fmt.Println(c)
	fmt.Println(d)
	var (
		name    string
		address string
		age     int
	)
	name = "hiepnh"
	address = "HCM"
	age = 25
	fmt.Println(name, address, age)
}

func hello_world() {
	fmt.Println("=====================")
	//Print to console
	fmt.Println("Hello world!")
}

func data_type()  {
	fmt.Println("=====================")
	//	Bool
	var a = true
	fmt.Println(a)
	//string
	//int int8 int16 int32 int64: (số nguyên)
	b := 10
	fmt.Println(b)
	//uint uint8 uint16 uint32 uint64 uintptr: (số nguyên dương)
	var c uint8 = 100
	fmt.Println(c)
	//byte alias for uint8
	fmt.Println(b)
	//rune alias for int32
	fmt.Println(b)
	//float32 float64()
	fmt.Println(b)
	//complex64 complex128 (số phức)
	fmt.Println(b)

	// Range
	fmt.Println("Range Min int8: ", math.MinInt8)
	fmt.Println("Range Min int8: ", math.MaxInt8)
	// Bits
	fmt.Println("Bits int8: ", bits.OnesCount8(math.MaxInt8))

	// Rune
	var myString string = "Có dấu"
	runes := []rune(myString)
	fmt.Println(myString)
	for i:=0; i<len(myString); i++ {
		fmt.Printf( "%c", myString[i])
	}
	for i:=0; i<len(runes); i++ {
		fmt.Printf("%c", myString[i])
	}
}
