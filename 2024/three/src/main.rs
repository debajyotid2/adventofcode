//! Advent of code day three
#![allow(dead_code)]

use std::fs;
use regex::Regex;

fn mul_from_expr(expr: &str) -> i64 {
    let mut sum_prod = 0i64;
    let pattern = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    for cap in pattern.captures_iter(expr) {
        let (_, vals): (&str, [&str; 2]) = cap.extract();
        let a: i64 = vals.iter().nth(0).unwrap().parse().unwrap();
        let b: i64 = vals.iter().nth(1).unwrap().parse().unwrap();
        sum_prod += a * b; 
    }
    return sum_prod;
}

fn part_one(input: &String) -> i64 {
    let mut sum_prod = 0i64;
    for line in input.lines() {
        sum_prod += mul_from_expr(&line);
    }
    return sum_prod;
}

struct Tokenizer {
    expr: String,
    tokens: Vec<String>
}

impl Tokenizer {
    pub fn new() -> Self {
        Tokenizer{ expr: String::new(), tokens: vec![String::from("do()")] }
    }

    fn reset_or_add(&mut self, last_char: char, chr: char) {
        if self.expr.is_empty() {
            return;
        }
        if !self.expr.ends_with(last_char) {
            self.expr.clear();
        } else {
            self.expr.push(chr);
        }
    }

    pub fn tokenize(&mut self, input: &str) {
        for chr in input.chars() {
            match chr {
                'm' | 'd' => {
                    if !self.expr.is_empty() {
                        self.expr.clear();
                    } else {
                        self.expr.push(chr);
                    }
                },
                'u' => self.reset_or_add('m', chr),
                'o' => self.reset_or_add('d', chr),
                'n' => self.reset_or_add('o', chr),
                '\'' => self.reset_or_add('n', chr),
                'l' => self.reset_or_add('u', chr),
                't' => self.reset_or_add('\'', chr),
                '(' => {
                    if self.expr.is_empty() {
                        continue;
                    }
                    if !"otl".contains(self.expr.chars().last().unwrap()) {
                        self.expr.clear();
                    } else {
                        self.expr.push(chr);
                    }
                },
                ')' => {
                    if self.expr.is_empty() {
                        continue;
                    }
                    let end_chr: char = self.expr.chars().last().unwrap();
                    if !end_chr.is_ascii_digit() && end_chr != '(' {
                        self.expr.clear();
                    } else {
                        self.expr.push(chr);
                        self.tokens.push(self.expr.clone());
                        self.expr = String::new();
                    }
                }
                '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => {
                    if self.expr.is_empty() {
                        continue;
                    }
                    let end_chr = self.expr.chars().last().unwrap();
                    if !end_chr.is_ascii_digit() && !"(,".contains(end_chr) {
                        self.expr.clear();
                    } else {
                        self.expr.push(chr);
                    }
                }
                ',' => {
                    if self.expr.is_empty() {
                        continue;
                    }
                    if !self.expr.chars().last().unwrap().is_ascii_digit() {
                        self.expr.clear();
                    } else {
                        self.expr.push(chr);
                    }
                }
                _ => {
                    if !self.expr.is_empty() {
                        self.expr.clear();
                    }
                }
            }
        }
    }

    pub fn get_tokens(&self) -> Vec<String> {
        self.tokens.clone()
    }

    pub fn evaluate(&self) -> i64 {
        let mut do_cond = false;
        let mut sum_prod = 0i64;
        for token in self.tokens.iter() {
            if *token == "do()" {
                do_cond = true;
            } else if *token == "don't()" {
                do_cond = false;
            } else if do_cond {
                sum_prod += mul_from_expr(token);
            }
        }
        return sum_prod;
    }
}

fn part_two(input: &String) -> i64 {
    let mut tokenizer = Tokenizer::new();
    for line in input.lines() {
        tokenizer.tokenize(line);
    }
    tokenizer.evaluate()
}

fn main() {
    let input: String = fs::read_to_string("input").unwrap();
    // let input = String::from("mul(1,2)\nmul(3,4)\n");
    println!("Part one answer: {}", part_one(&input));
    println!("Part two answer: {}", part_two(&input));
}
