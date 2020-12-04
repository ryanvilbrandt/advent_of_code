import re


def check_passport_simple(passport):
    for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if field not in passport:
            return False
    return True


def check_passport_complex(passport):
    if not (m := re.search(r"byr:(\d{4})\b", passport)) or not 1920 <= int(m.group(1)) <= 2002:
        return False

    if not (m := re.search(r"iyr:(\d{4})\b", passport)) or not 2010 <= int(m.group(1)) <= 2020:
        return False

    if not (m := re.search(r"eyr:(\d{4})\b", passport)) or not 2020 <= int(m.group(1)) <= 2030:
        return False

    if not (m := re.search(r"hgt:(\d+)(cm|in)\b", passport)) or \
            m.group(2) == "cm" and not 150 <= int(m.group(1)) <= 193 or \
            m.group(2) == "in" and not 59 <= int(m.group(1)) <= 76:
        return False

    if not re.search(r"hcl:#[0-9a-f]{6}\b", passport):
        return False

    if not re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", passport):
        return False

    if not re.search(r"pid:\d{9}\b", passport):
        return False

    if not re.search(r"cid:", passport):
        pass

    return True


def check_passports(passports, check_type="SIMPLE"):
    total = 0
    for passport in passports.split("\n\n"):
        func = check_passport_simple if check_type == "SIMPLE" else check_passport_complex
        total += 1 if func(passport) else 0
    return total
