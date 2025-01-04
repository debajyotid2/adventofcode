//! Advent of Code day 2

use std::fs;

fn is_safe(report: &Vec<i32>) -> bool {
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
            return false;
        }
        prev_diff = diff;
    }
    return is_safe;
}

fn main() {
    let mut safe_pure: u32 = 0;
    let mut unsafe_pure: u32 = 0;

    let mut safe_dampened: u32 = 0;
    let mut unsafe_dampened: u32 = 0;
    
    for line in fs::read_to_string("./input").unwrap().lines() {
        // Parse a single report
        let report: Vec<i32> = line
                                .trim()
                                .split(" ")
                                .map(|x| x.parse::<i32>().unwrap())
                                .collect();

        // Part 1: Without problem dampener
        // Check for safe and unsafe reports
        if is_safe(&report) {
            safe_pure += 1;
        } else {
            unsafe_pure += 1;
        }

        // Part 2: With problem dampener
        // Check for safe and unsafe reports
        if is_safe(&report) {
            safe_dampened += 1;
        } else {
            let mut safe: bool = false;
            for idx in 0..report.len() {
                let mut copied = report.clone();
                copied.remove(idx);
                if is_safe(&copied) {
                    safe = true;
                    break;
                }
            }
            if safe {
                safe_dampened += 1;
            } else {
                unsafe_dampened += 1;
            }
        }
    }
    println!("Part 1: safe: {}, unsafe: {}", &safe_pure, &unsafe_pure);
    println!("Part 2: safe: {}, unsafe: {}", &safe_dampened, &unsafe_dampened);
}
