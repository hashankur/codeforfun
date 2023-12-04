use std::collections::HashSet;

fn main() {
    part1();
    part2();
}

fn part1() {
    let mut sum = 0;

    for line in include_str!("input.txt").lines() {
        let common_numbers = common_numbers(line);

        let base: u32 = 2;
        if !common_numbers.is_empty() {
            sum += base.pow(common_numbers.len() as u32 - 1);
        }
    }
    println!("{sum}");
}

fn part2() {}

fn common_numbers(line: &str) -> Vec<i32> {
    let parts: Vec<&str> = line.split("|").collect();
    let left_numbers: Vec<i32> = parts[0]
        .trim()
        .split(' ')
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();
    let right_numbers: Vec<i32> = parts[1]
        .trim()
        .split(' ')
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    let mut hash_set = HashSet::new();

    for num in left_numbers {
        hash_set.insert(num);
    }

    let common_numbers = right_numbers
        .into_iter()
        .filter(|num| hash_set.contains(num))
        .collect::<Vec<_>>();
    common_numbers
}
