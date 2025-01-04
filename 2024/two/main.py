"""
Advent of code day two
"""
from copy import deepcopy

Report = list[int]

def is_safe(report: Report) -> bool:
    is_safe = True
    prev_diff = 0
    for ctr in range(len(report)-1):
        diff = report[ctr+1] - report[ctr]
        if not 1 <= abs(diff) <= 3:
            is_safe = False
        if ctr == 0:
            prev_diff = diff
            continue
        if prev_diff * diff < 0:
            return False
        prev_diff = diff
    return is_safe

def check_pure(reports: list[Report]) -> tuple[int, int, list[Report], list[Report]]:
    safe, unsafe = 0, 0
    safe_reports, unsafe_reports = [], []
    for report in reports:
        if is_safe(report):
            safe_reports.append(report)
            safe += 1
        else:
            unsafe_reports.append(report)
            unsafe += 1
    print(f"{safe=}, {unsafe=}")
    return safe, unsafe, safe_reports, unsafe_reports

def check_dampened(reports: list[Report]) -> tuple[int, int, list[Report], list[Report]]:
    safe, unsafe = 0, 0
    safe_reports, unsafe_reports = [], []
    for report in reports:
        if is_safe(report):
            safe_reports.append(report)
            safe += 1
        else:
            safe_cond = False
            for idx in range(len(report)):
                copied = deepcopy(report)
                copied.pop(idx)
                if is_safe(copied):
                    safe_cond = True
                    break
            if safe_cond:
                safe_reports.append(report)
                safe += 1
            else:
                unsafe_reports.append(report)
                unsafe += 1
    print(f"{safe=}, {unsafe=}")
    return safe, unsafe, safe_reports, unsafe_reports


def main():
    with open("./input", "r") as f:
        reports = [list(map(lambda x: int(x), line.strip().split(" "))) for line in f.readlines()]
    print("*********Checking pure**************")
    safe_pure, unsafe_pure, safe_reports_pure, unsafe_reports_pure = check_pure(reports)
    print("************************************")
    print("*********Checking dampened**********")
    safe_dampened, unsafe_dampened, safe_reports_dampened, unsafe_reports_dampened = check_dampened(reports)
    print("************************************")

if __name__=="__main__":
    main()

