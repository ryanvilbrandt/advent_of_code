from collections import defaultdict
from time import mktime
import re
from typing import List

day_4_example = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""

GUARD_REG = "\[1518\-(\d+)\-(\d+) (\d+):(\d+)\] (.*)"
ID_REG = "Guard #(\d+) begins shift"


class Guard:

    def __init__(self, month, day, hour, minute, text):
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.text = text
        self.epoch = mktime((1970, self.month, self.day, self.hour, self.minute,
                             0, 0, 0, 0))
        m = re.match(ID_REG, text)
        if m:
            self.id = int(m.group(1))
        elif text == "falls asleep":
            self.id = "asleep"
        elif text == "wakes up":
            self.id = "awake"
        else:
            raise ValueError(f"Bad text: {text}")

    def __str__(self):
        return (f"Guard(id={self.id}, month={self.month}, day={self.day}, hour={self.hour}, " +
                f"minute={self.minute}, epoch={self.epoch}, text={self.text})")

    def __repr__(self):
        return str(self)

    @staticmethod
    def make(in_str):
        m = re.match(GUARD_REG, in_str)
        return Guard(*m.groups())


def preprocess_input(in_str):
    output = []
    for s in in_str.split('\n'):
        if not s:
            continue
        output.append(Guard.make(s))
    return output


def get_sleep_count(times: List[Guard]) -> int:
    """
    :param times: List of Guard objects
    :return: Guard id with max minutes asleep
    """
    sleep_count = {}
    last_guard = None
    last_time = None
    for t in times:
        if t.id == "asleep":
            last_time = t.epoch
        elif t.id == "awake":
            sleep_count[last_guard] += (t.epoch - last_time) / 60
        else:
            last_guard = int(t.id)
            if last_guard not in sleep_count:
                sleep_count[last_guard] = 0
            last_time = t.epoch
    print(sleep_count)
    return max(sleep_count, key=sleep_count.get)


def get_max_minute_asleep(times: List[Guard], guard_id: int):
    minute_count = defaultdict(int)
    last_guard = None
    sleep_time = None
    for t in times:
        if t.id == "asleep":
            sleep_time = t.epoch
        elif t.id == "awake":
            if last_guard != guard_id:
                continue
            current_minute = sleep_time
            while current_minute < t.epoch:
                minute_count[(current_minute / 60) % 60] += 1
                current_minute += 60
        else:
            last_guard = t.id
    return max(minute_count, key=minute_count.get)


def find_guard_code(in_str):
    times = preprocess_input(in_str)
    times = sorted(times, key=lambda x: x.epoch)
    guard = get_sleep_count(times)
    print(guard)
    minute = get_max_minute_asleep(times, guard)
    print(minute)
    return guard * minute


print(find_guard_code(day_4_example))
print()
with open("day 4.input") as f:
    print(find_guard_code(f.read()))


def calc_guard_sleep_minutes(times: List[Guard]):
    guard_sleep_minutes = {}
    last_guard = None
    sleep_time = None
    for t in times:
        if t.id == "asleep":
            sleep_time = t.epoch
        elif t.id == "awake":
            current_minute = sleep_time
            while current_minute < t.epoch:
                guard_sleep_minutes[last_guard][(current_minute / 60) % 60] += 1
                current_minute += 60
        else:
            last_guard = int(t.id)
            if last_guard not in guard_sleep_minutes:
                guard_sleep_minutes[last_guard] = defaultdict(int)
    return guard_sleep_minutes


def calc_max_minute(guard_minutes):
    sleepiest_guard = 0
    max_minute = 0
    last_max_minute_count = 0
    for g in guard_minutes:
        if not guard_minutes[g]:
            continue
        m = max(guard_minutes[g], key=guard_minutes[g].get)
        if guard_minutes[g][m] > last_max_minute_count:
            sleepiest_guard = g
            max_minute = m
            last_max_minute_count = guard_minutes[g][m]
    return sleepiest_guard, max_minute, last_max_minute_count


def find_guard_code_b(in_str):
    times = preprocess_input(in_str)
    times = sorted(times, key=lambda x: x.epoch)
    minutes = calc_guard_sleep_minutes(times)
    guard_id, minute, count = calc_max_minute(minutes)
    print(guard_id, minute, count)
    return guard_id * minute


print(find_guard_code_b(day_4_example))
print()
with open("day 4.input") as f:
    print(find_guard_code_b(f.read()))
