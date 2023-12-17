package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/hashankur/codeforfun/aoc2022/util"
)

func main() {
	part1(util.Reader())
	part2(util.Reader())
}

func part1(lines []string) {
	count := 0

	for _, line := range lines {

		pair := strings.Split(line, ",")
		e1Start, e1End := splitToInts(pair[0])
		e2Start, e2End := splitToInts(pair[1])

		// Convert strings to ints before comparison to avoid nasty side effects
		if (e1Start >= e2Start && e1End <= e2End) || (e1End >= e2End && e1Start <= e2Start) {
			count++
		}
	}
	fmt.Println(count)
}

func part2(lines []string) {
	count := 0
	isCommon := false

	for _, line := range lines {
		pair := strings.Split(line, ",")
		e1Start, e1End := splitToInts(pair[0])
		e2Start, e2End := splitToInts(pair[1])
		for i := e1Start; i <= e1End; i++ {
			for i2 := e2Start; i2 <= e2End; i2++ {
				if i == i2 {
					count++
					isCommon = true
					break
				}
			}
			if isCommon {
				isCommon = false
				break
			}
		}
	}
	fmt.Println(count)
}

func splitToInts(s string) (int, int) {
	parts := strings.Split(s, "-")
	start, _ := strconv.Atoi(parts[0])
	end, _ := strconv.Atoi(parts[1])
	return start, end
}
