def read_input(file: str) -> list[list[int]]:
    f = open(file).readlines()
    return [[int(i) for i in line.split(" ")] for line in f]


def is_report_valid_fast(report: list[int]) -> bool:
    if len(report) < 2 or report[0] == report[1]:
        return False

    is_asc = report[0] < report[1]

    return all(
        abs(b - a) <= 3 and (b > a if is_asc else b < a)
        for a, b in zip(report, report[1:])
    )


def is_report_valid(report: list[int]) -> bool:
    if len(report) < 2 or report[0] == report[1]:
        return False

    is_asc = report[0] < report[1]

    for i in range(len(report) - 1):
        c = report[i]
        n = report[i + 1]
        if abs(n - c) > 3 or (is_asc and (n <= c)) or (not is_asc and (n >= c)):
            return False
    return True


def is_report_valid_on2(report: list[int]) -> bool:
    if is_report_valid_fast(report):
        return True

    for i in range(len(report)):
        nr = report[:i] + report[i + 1 :]
        if is_report_valid_fast(nr):
            return True
    return False


def is_report_valid_2(report: list[int], changes: int = 1) -> bool:
    if len(report) < 2:
        return False

    is_asc = report[0] < report[1]
    for i in range(len(report) - 1):
        c = report[i]
        n = report[i + 1]

        invalid = abs(n - c) > 3 or (is_asc and (n <= c)) or (not is_asc and (n >= c))

        if invalid and changes > 0:
            prev_removed = report[: i - 1] + report[i:]
            first_removed = report[:i] + report[i + 1 :]
            second_removed = report[: i + 1] + report[i + 2 :]
            return (
                is_report_valid_2(prev_removed, 0)
                or is_report_valid_2(first_removed, 0)
                or is_report_valid_2(second_removed, 0)
            )
        elif invalid:
            return False

    return True


reports: list[list[int]] = read_input("input.txt")

total_valid_reports = 0

for report in reports:
    on2 = is_report_valid_on2(report)
    mine = is_report_valid_2(report)
    if on2 != mine:
        print(on2, mine, report)

    if mine:
        total_valid_reports += 1

print(total_valid_reports)
