use std::collections::HashMap;

fn main() {
    part1();
    part2();
}

fn part1() {
    let mut directions = "";
    let mut nodes = HashMap::new();

    for (i, line) in include_str!("input.txt").lines().enumerate() {
        if i < 1 {
            directions = line;
        } else if i < 2 {
            continue;
        } else {
            let (node, instructions) = line.split_once(" = ").unwrap();
            let (i1, i2) = instructions[1..instructions.len() - 1]
                .split_once(", ")
                .unwrap();
            nodes.insert(node, (i1, i2));
        }
    }

    let directions = directions.chars().cycle();
    let mut current = nodes.get("AAA").unwrap();
    let mut node = "";
    let mut count = 0;

    for letter in directions {
        let (n1, n2) = current;
        match letter {
            'L' => {
                current = nodes.get(n1).unwrap();
                node = n1
            }
            'R' => {
                current = nodes.get(n2).unwrap();
                node = n2
            }
            _ => unreachable!(),
        }
        count += 1;
        if node == "ZZZ" {
            break;
        }
    }

    println!("{count}");
}
