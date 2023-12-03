fn main() {
    part1();
    part2();
}

fn part1() {
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

fn part2() {
    let mut sum = 0;
    let spelled_nums: [&str; 9] = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    for line in include_str!("input.txt").lines() {
        let mut nums = vec![];
        let mut lnums = vec![];

        for (i, letter) in line.chars().enumerate() {
            if letter.is_numeric() {
                nums.push((i, letter));
            }
        }
        for num in spelled_nums {
            let v: Vec<_> = line.match_indices(num).collect();
            if !v.is_empty() {
                for x in v {
                    lnums.push(x);
                }
            }
        }
        // println!("{:?}", line);
        for (i, colour) in lnums.iter() {
            let c = spelled_nums.iter().position(|r| r == colour).unwrap();
            nums.push((*i, char::from_digit(c as u32 + 1, 10).unwrap()));
        }
        nums.sort();
        // println!("{:?}", nums);
        lnums.sort();
        // println!("{:?}", lnums);
        let concat = format!("{}{}", nums[0].1, (nums[nums.len() - 1].1));
        // println!("{:?}", concat);
        sum += concat.parse::<u32>().unwrap();
    }
    println!("{sum}");
}
