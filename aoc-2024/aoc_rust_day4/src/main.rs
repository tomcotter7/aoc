use std::fs;
use std::collections::HashMap;

fn count_xmas( vct: Vec<Vec<char>> ) -> i32 {
    
    let next_letter: HashMap<char, char> = HashMap::from([
        ('X', 'M'),
        ('M', 'A'),
        ('A', 'S'),
        ('S', 'X')
    ]);

    let mut current_letter: char = 'X';

    let mut count: i32 = 0;
    
    for i in 0..vct.len() {
        println!("{:?}", vct[i]);
        for j in 0..vct[i].len() {
            if vct[i][j] == current_letter {
                if current_letter == 'S' {
                    count += 1;
                }
                current_letter = next_letter[&current_letter];
            } else {
                if vct[i][j] == 'X' {
                    current_letter = 'M';
                } else {
                    current_letter = 'X';
                }
            }
        }

        println!("{}", count);
        println!("--");
        let mut row = vct[i].clone();
        row.reverse();

        println!("{:?}", row);

        for j in 0..row.len() {
            if row[j] == current_letter {
                if current_letter == 'S' {
                    count += 1;
                }
                current_letter = next_letter[&current_letter];
            } else {
                if row[j] == 'X' {
                    current_letter = 'M';
                } else {
                    current_letter = 'X';
                }
            }
        }

        println!("{}", count);
        println!("**");
    }

    return count;
}

fn part1() {
    
    let file = fs::read_to_string("test.txt").unwrap();
    let lines = file.lines()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let rows = lines.clone();

    let mut columns = Vec::new();
    for i in 0..rows.len() {
        let mut column = Vec::new();
        for j in 0..lines.len() {
            column.push(rows[j][i]);
        }
        columns.push(column);
    }

    let mut diagonals = Vec::new();
    for i in 0..rows.len() {
        let mut diagonal = Vec::new();
        let mut opposite_diagonal = Vec::new();
        let width = rows[i].len() - 1;
        for j in 0..i+1 {
            diagonal.push(rows[i - j][j]);
            opposite_diagonal.push(rows[i - j][width - j]);
        }

        diagonals.push(diagonal);
        diagonals.push(opposite_diagonal);
    }

    let mut rows_copy = rows.clone();
    rows_copy.reverse();
    let max: usize = rows_copy.len() / 2;
    for i in 0..max+1 {
        let mut diagonal = Vec::new();
        let mut opposite_diagonal = Vec::new();
        let width = rows_copy[i].len() - 1;
        for j in 0..i+1 {
            diagonal.push(rows_copy[i - j][j]);
            opposite_diagonal.push(rows_copy[i - j][width - j]);
        }

        diagonals.push(diagonal);
        diagonals.push(opposite_diagonal);
    }


    let diagonals = diagonals.into_iter().filter(|d| d.len() >= 4).collect::<Vec<Vec<char>>>();


    let mut total_xmas: i32 = 0;

    // total_xmas += count_xmas(rows);

    // println!("{}", total_xmas);
    // total_xmas += count_xmas(columns);

    // println!("{}", total_xmas); 
    total_xmas += count_xmas(diagonals);

    println!("{}", total_xmas);

    println!("{}", total_xmas);
}

fn main() {
    part1();
}

