//! Advent of Code day 1

use std::fs;

fn main() {
    let mut arr1 = Vec::<i32>::new();
    let mut arr2 = Vec::<i32>::new();

    // Parse data
    for line in fs::read_to_string("input").unwrap().lines() {
        let data: Vec<i32> = line
                                .trim()
                                .split(" ")
                                .filter(|x| *x != "")
                                .map(|x| x.parse::<i32>().unwrap())
                                .collect();
        arr1.push(data[0]);
        arr2.push(data[1]);
    };

    // Sort
    arr1.sort();
    arr2.sort();

    // Part 1: Calculate Manhattan distance
    let mut dist: i64 = 0;
    for ctr in 0..arr1.len() {
        dist += (arr1[ctr] - arr2[ctr]).abs() as i64;
    }
    println!("Distance: {}", dist);
    
    // Part 2: Calculate similarity score
    let mut score: i64 = 0;
    for a in arr1.iter() {
        let counts: i64 = arr2.iter().filter(|b| *b == a).count() as i64;
        score += (*a as i64) * counts;
    }
    println!("Score: {}", score);

}
