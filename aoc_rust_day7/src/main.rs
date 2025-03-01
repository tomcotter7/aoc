use std::fs;

fn reaches_value(target: i64, values: Vec<i64>) -> bool {
    
    if values.len() == 0 {
        return false;
    } else if values.len() == 1 {
        return values[0] == target;
    } else {
        let first = values[0];
        let second = values[1];
        let mut new_values_a = vec![first + second];
        new_values_a.extend(&values[2..]);

        let mut new_values_m = vec![first * second];
        new_values_m.extend(&values[2..]);

        let concatenated = first.to_string() + &second.to_string();
        let concatenated = concatenated.parse::<i64>().unwrap();
        let mut new_values_c = vec![concatenated];
        new_values_c.extend(&values[2..]);

        return reaches_value(target, new_values_a) || reaches_value(target, new_values_m) || reaches_value(target, new_values_c);
    }
}

fn main() {
    let file = fs::read_to_string("input.txt").unwrap();
    let lines = file.lines(); 

    let mut total = 0;
    for line in lines {
        let parts: Vec<&str> = line.split(":").collect();
        let target = parts[0].parse::<i64>().unwrap();
        let values: Vec<i64> = parts[1].split(" ")
            .map(|x| x.trim())
            .filter(|x| x.len() > 0)
            .map(|x| x.parse::<i64>().unwrap())
            .collect();
        if reaches_value(target, values) {
            total += target;
        }
    }

    println!("Total: {}", total);   
}
