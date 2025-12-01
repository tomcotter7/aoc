use std::fs;
use regex::Regex;

fn part1() {
    
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let file = fs::read_to_string("test.txt").unwrap();

    let funcs = re.captures_iter(&file).map(|m| {
        let a = m.get(1).map_or(0, |m| m.as_str().parse().unwrap());
        let b = m.get(2).map_or(0, |m| m.as_str().parse().unwrap());
        return a * b;
    }).sum::<i32>();

    println!("{:?}", funcs);
}

fn part2() {
    
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)").unwrap();
    let file = fs::read_to_string("input.txt").unwrap();

    let mut flag = true;

    let funcs = re.captures_iter(&file).map(|m| {
        let op = m.get(0).map_or("", |m| m.as_str());
        if op == "do()" {
            flag = true;
        } else if op == "don't()" {
            flag = false;
        } else {
            let a = m.get(1).map_or(0, |m| m.as_str().parse().unwrap());
            let b = m.get(2).map_or(0, |m| m.as_str().parse().unwrap());
            if flag {
                return a * b;
            }
        }
        return 0;
    }).sum::<i32>();

    println!("{:?}", funcs);
}

fn main() {

    part1();
    part2();
}
