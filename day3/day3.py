from typing import Iterable
from string import ascii_letters


PRIORITY_TABLE = {letter: priority + 1 for priority, letter in enumerate(ascii_letters)}


def task1():
    with open("day3/input.txt") as inputfile:
        priority_sum = 0
        for rucksack in inputfile:
            rucksack = rucksack.strip()
            compartment_size = int(len(rucksack) / 2)

            compartment1 = set(rucksack[:compartment_size])
            compartment2 = set(rucksack[compartment_size:])

            overlap = compartment1.intersection(compartment2)
            priority_sum += PRIORITY_TABLE[overlap.pop()]
        print(priority_sum)


def task2():
    with open("day3/input.txt") as inputfile:
        priority_sum = 0

        while True:
            try:
                next_set = (
                    next(inputfile).strip(),
                    next(inputfile).strip(),
                    next(inputfile).strip(),
                )
                rucksacks = [set(x) for x in next_set]

                overlap = rucksacks[0].intersection(rucksacks[1])
                overlap = overlap.intersection(rucksacks[2])

                priority_sum += PRIORITY_TABLE[overlap.pop()]
            except StopIteration:
                break
        print(priority_sum)


if __name__ == "__main__":
    task1()
    task2()
