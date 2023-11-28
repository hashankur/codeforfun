package main

import (
	"fmt"
	"unicode"

	"github.com/hashankur/codeforfun/languages/go/util"
)

func main() {
	part1(util.Reader())
	part2(util.Reader())
}

func part1(lines []string) {
	var commonLetter string
	sum := 0

	for _, line := range lines {
		one, two := splitStringInHalf(line)
		for _, letter1 := range one {
			for _, letter2 := range two {
				if letter1 == letter2 {
					if commonLetter != string(letter1) {
						commonLetter = string(letter1)
					}
				}

			}
		}
		sum = sumOfPriorities(commonLetter, sum)
		commonLetter = ""
	}
	fmt.Println(sum)
}

func part2(lines []string) {
	var commonLetter string
	sum := 0
	group := [...]string{"", "", ""}
	count := 0

	for _, line := range lines {
		group[count] = line
		count++
		if count >= 3 {
			count = 0
			for _, letter1 := range group[0] {
				for _, letter2 := range group[1] {
					if letter1 == letter2 {
						for _, letter3 := range group[2] {
							if letter1 == letter3 {
								if commonLetter != string(letter1) {
									commonLetter = string(letter1)
								}
							}
						}
					}
				}
			}
			sum = sumOfPriorities(commonLetter, sum)
			commonLetter = ""
		}
	}
	fmt.Println(sum)
}

func splitStringInHalf(str string) (string, string) {
	mid := len(str) / 2
	return str[:mid], str[mid:]
}

func sumOfPriorities(commonLetter string, sum int) int {
	if unicode.IsLower(rune(commonLetter[0])) {
		sum += int(rune(commonLetter[0]) - 96)
	} else {
		sum += int(rune(commonLetter[0]) - 38)
	}
	return sum
}
