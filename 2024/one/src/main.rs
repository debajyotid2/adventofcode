//! Advent of Code day 1

use std::fs;
use std::iter::zip;

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
    for (a, b) in zip(arr1, arr2) {
        dist = dist + (a-b).abs() as i64;
    }
    println!("{}", dist);
}
