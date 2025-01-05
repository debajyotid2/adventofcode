"""
Advent of code day three
"""
import re

def mul_from_expr(expr: str) -> int:
    sum_prod = 0
    mul_pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(mul_pattern, expr)
    for a, b in matches:
        sum_prod += int(a) * int(b)
    return sum_prod

def part_one(input: list[str]) -> int:
    sum_prod = 0
    for line in input:
        sum_prod += mul_from_expr(line)
    return sum_prod

class Tokenizer:
    def __init__(self):
        self.expr = ""
        self.tokens = ["do()"]

    def reset_or_add(self, last_char: str, char: str):
        if self.expr == "":
            return
        if self.expr[-1] != last_char:
            self.expr = ""
        else:
            self.expr += char

    def tokenize(self, input: str):
        for char in input:
            match char:
                case 'm' | 'd':
                    if self.expr != "":
                        self.expr = ""
                    else:
                        self.expr += char
                case 'u':
                    self.reset_or_add('m', char)
                case 'o':
                    self.reset_or_add('d', char)
                case 'n':
                    self.reset_or_add('o', char)
                case "'":
                    self.reset_or_add('n', char)
                case 'l':
                    self.reset_or_add('u', char)
                case 't':
                    self.reset_or_add("'", char)
                case '(':
                    if self.expr == "":
                        continue
                    if self.expr[-1] not in "otl":
                        self.expr = ""
                    else:
                        self.expr += char
                case ')':
                    if self.expr == "":
                        continue
                    if not self.expr[-1].isdigit() and self.expr[-1] != '(':
                        self.expr = ""
                    else:
                        self.expr += char
                        self.tokens.append(self.expr)
                        self.expr = ""
                case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                    if self.expr == "":
                        continue
                    if not self.expr[-1].isdigit() and self.expr[-1] not in "(,":
                        self.expr = ""
                    else:
                        self.expr += char
                case ',':
                    if self.expr == "":
                        continue
                    if not self.expr[-1].isdigit():
                        self.expr = ""
                    else:
                        self.expr += char
                case _:
                    if len(self.expr) != 0:
                        self.expr = ""

    def get_tokens(self) -> list[str]:
        return self.tokens

    def evaluate(self) -> int:
        do = False
        sum_prod = 0
        for token in self.tokens:
            if token == "do()":
                do = True
            elif token == "don't()":
                do = False
            elif do:
                sum_prod += mul_from_expr(token)
        return sum_prod

def part_two(input: list[str]) -> int:
    tokenizer = Tokenizer()
    for line in input:
        tokenizer.tokenize(line)
    return tokenizer.evaluate()

def main():
    with open("input", "r") as f:
        lines = f.readlines()   
    print(f"Part one answer: {part_one(lines)}")
    print(f"Part two answer: {part_two(lines)}")

if __name__=="__main__":
    main()
