//! Advent of Code day 2

use std::fs;

fn main() {
    let mut safe: u32 = 0;
    let mut un_safe: u32 = 0;
    for line in fs::read_to_string("./input").unwrap().lines() {
        // Parse a single report
        let report: Vec<i32> = line
                                .trim()
                                .split(" ")
                                .map(|x| x.parse::<i32>().unwrap())
                                .collect();

        // Check for safe and unsafe reports
        let mut is_safe = true;
        let mut prev_diff = 0i32;
        for ctr in 0..(report.len()-1) {
            let diff = report[ctr+1] - report[ctr];
            let abs_diff = diff.abs();
            if abs_diff < 1 || abs_diff > 3 {
                is_safe = false;
                break;
            }
            if ctr == 0 {
                prev_diff = diff;
                continue;
            }
            if prev_diff * diff < 0 {
                is_safe = false;
                break;
            }
            prev_diff = diff;
        }
        if is_safe {
            safe += 1;
        } else {
            un_safe += 1;
        }
    }
    println!("Safe: {}, unsafe: {}", safe, un_safe);
}
