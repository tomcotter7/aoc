use std::fs;
use std::collections::HashMap;

fn apply_steps(stone: i64, n: i64, dp: &mut HashMap<String, i64>) -> i64 {
    if n == 0 {
        return 1;
    }

    let key = format!("{}-{}", stone, n);
    let value = dp.get(&key);

    match value {
        Some(prev) => {
            return *prev
        },
        None => {
            let str_stone = stone.to_string();
            let stone_length = str_stone.len();
            if stone == 0 {
                let result = apply_steps(1, n -1, dp);
                dp.insert(key, result);
                return result
            } else if stone_length % 2 == 0 {
                let left_half = &str_stone[0..stone_length / 2];
                let right_half = &str_stone[stone_length / 2..stone_length];
                let left = apply_steps(left_half.parse().unwrap(), n - 1, dp);
                let right = apply_steps(right_half.parse().unwrap(), n - 1, dp);
                let total = left + right;
                dp.insert(key, total);
                return total;
            } else {
                let result = apply_steps(stone * 2024, n - 1, dp);
                dp.insert(key, result);
                return result
            }
   
        }
    }
}

fn main() {

    let input = fs::read_to_string("input.txt").unwrap();
    let mut dp: HashMap<String, i64> = HashMap::new();
    let result: i64 = input.split(" ")
        .filter_map(|x| {
            let y = x.trim();
            y.parse().ok()
        })
        .map(|stone| apply_steps(stone, 75, &mut dp))
        .sum();

    println!("{:?}", result);
}
