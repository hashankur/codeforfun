fn main() {
    part1();
    part2();
}

fn part1() {
    // let input = std::fs::read_to_string("src/input.txt").unwrap();

    let mut sum = 0;
    for line in include_str!("input.txt").lines() {
        let mut nums = vec![];
        for letter in line.chars() {
            if letter.is_numeric() {
                nums.push(letter);
            }
        }
        // println!("{:?}", nums);
        let concat = format!("{}{}", nums[0], (nums[nums.len() - 1]));
        sum += concat.parse::<u32>().unwrap();
    }
    println!("{sum}");
}

fn part2() {}
