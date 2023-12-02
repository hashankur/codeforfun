fn main() {
    part1();
    part2();
}

fn part1() {
    let mut sum = 0;
    let mut impossible = false;

    for (id, line) in include_str!("input.txt").lines().enumerate() {
        line.split_once(": ").into_iter().for_each(|(_, game)| {
            impossible = false;
            let sets = game.split("; ");
            for set in sets {
                let handful = set.split(", ");
                for cubes in handful {
                    if let Some((num, colour)) = cubes.split_once(' ') {
                        let num = num.parse::<u32>().unwrap();
                        if (colour == "red" && num > 12)
                            || (colour == "green" && num > 13)
                            || (colour == "blue" && num > 14)
                        {
                            impossible = true;
                        }
                        // println!("{}, {} {}", num, colour, impossible);
                    };
                }
            }
            // println!();
        });
        if !impossible {
            sum += id + 1;
        }
    }
    println!("{sum}");
}

fn part2() {
    let mut sum = 0;
    let mut r = 0;
    let mut g = 0;
    let mut b = 0;

    for line in include_str!("input.txt").lines() {
        line.split_once(": ").into_iter().for_each(|(_, game)| {
            r = 0;
            g = 0;
            b = 0;

            let sets = game.split("; ");
            for set in sets {
                let handful = set.split(", ");
                for cubes in handful {
                    if let Some((num, colour)) = cubes.split_once(' ') {
                        let num = num.parse::<u32>().unwrap();
                        match colour {
                            "red" => {
                                if colour == "red" && r < num {
                                    r = num
                                }
                            }
                            "green" => {
                                if g < num {
                                    g = num
                                }
                            }
                            "blue" => {
                                if b < num {
                                    b = num
                                }
                            }
                            _ => {}
                        }
                    };
                }
            }
        });
        sum += r * g * b;
    }
    println!("{sum}");
}
