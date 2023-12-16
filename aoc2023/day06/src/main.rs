fn main() {
    let mut races: Vec<_> = vec![];

    for line in include_str!("input2.txt").lines() {
        let value: Vec<usize> = line
            .split(" ")
            .filter_map(|s| s.parse::<usize>().ok())
            .collect();
        races.push(value);
    }

    let variations = races[0]
        .iter()
        .zip(races[1].iter())
        .map(|(time, distance)| { (0..*time).filter(|i| (time - i) * i > *distance) }.count())
        .product::<usize>();

    println!("{:?}", variations);
}
