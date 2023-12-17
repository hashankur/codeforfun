package main

import (
	"fmt"
	"github.com/hashankur/codeforfun/aoc2022/util"
	"sort"
	"strconv"
)

func main() {
	part1(util.Reader())
	part2(util.Reader())
}

func part1(lines []string) {
	maxCalories := 0
	currentCalories := 0

	for _, line := range lines {
		if line != "" {
			num, err := strconv.Atoi(line)
			if err != nil {
				panic(err)
			}
			currentCalories += num
		}

		if line == "" {
			if maxCalories < currentCalories {
				maxCalories = currentCalories
			}
			currentCalories = 0
		}
	}
	fmt.Println(maxCalories)
}

func part2(lines []string) {
	currentCalories := 0
	totalCalories := []int{}

	for _, line := range lines {
		if line != "" {
			num, err := strconv.Atoi(line)
			if err != nil {
				panic(err)
			}
			currentCalories += num
		}

		if line == "" {
			totalCalories = append(totalCalories, currentCalories)
			currentCalories = 0
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(totalCalories)))
	fmt.Println(totalCalories[0] + totalCalories[1] + totalCalories[2])
}
