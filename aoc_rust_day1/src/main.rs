use std::fs;
use std::collections::HashMap;

fn part1() {

    let file = fs::read_to_string("input.txt").unwrap();

    let mut first = Vec::new();
    let mut second = Vec::new();

    for line in file.lines() {
        let nums = line.split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        first.push(nums[0]);
        second.push(nums[1]);
    }

    first.sort_unstable();
    second.sort_unstable();

    let total = first.iter().zip(second.iter())
        .map(|(x, y)| (x - y).abs())
        .sum::<i32>();

    println!("Total: {}", total);
}

fn part2() {

    let file = fs::read_to_string("input.txt").unwrap();
    let mut first = Vec::new();
    let mut counts = HashMap::new();

    for line in file.lines() {
        let nums = line.split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        let y = nums[1];
        *counts.entry(y).or_insert(0) += 1;
        first.push(nums[0]);
    }

    let total = first.iter()
        .map(|x| counts.get(x).unwrap_or(&0) * x)
        .sum::<i32>();

    println!("Total: {}", total);

}


fn main() {
    part1();
    part2();
}
