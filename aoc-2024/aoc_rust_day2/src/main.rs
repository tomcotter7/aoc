fn part1() {

    let result: i32 = std::fs::read_to_string("input.txt")
        .unwrap()
        .lines()
        .filter_map(|line| {
            let levels: Vec<i32> = line
                .split_whitespace()
                .filter_map(|x| x.parse().ok())
                .collect();

            if !(levels.windows(2).all(|w| w[0] <= w[1]) || levels.windows(2).all(|w| w[0] >= w[1])) {
                return None;
            }

            levels.windows(2)
                .all(|w| {
                    let diff = (w[0] - w[1]).abs();
                    diff >= 1 && diff <= 3
                }).then_some(1)
        })
        .sum::<i32>();

    println!("Result: {}", result);
}

fn is_safe(ipt: &Vec<i32>) -> bool {


    if !(ipt.windows(2).all(|w| w[0] <= w[1]) || ipt.windows(2).all(|w| w[0] >= w[1])) {
        return false;
    }

    ipt.windows(2).all(|w| {
        let diff = (w[0] - w[1]).abs();
        diff >= 1 && diff <= 3
    })
}

fn part2() {
    
    let lines: Vec<Vec<i32>> = std::fs::read_to_string("input.txt")
        .unwrap()
        .lines()
        .map(| line | {
            line.split(" ")
                .map(|x| x.parse::<i32>().unwrap())
                .collect::<Vec<i32>>()
        })
        .collect();

    let mut results: Vec<bool> = Vec::new();

    for report in lines {
        if is_safe(&report) {
            results.push(true);
            continue;
        }
        let mut found = false;
        for i in 0..report.len() {
            let mut report_copy = report.clone();
            report_copy.remove(i);
            if is_safe(&report_copy) {
                results.push(true);
                found = true;
                break;
            }
        }

        if !found {
            results.push(false);
        }

    }

    let result = results.iter().map(|x| if *x { 1 } else { 0 }).sum::<i32>();
    println!("Result: {}", result);
}

fn main() {
    part1();
    part2();
}
