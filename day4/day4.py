from dataclasses import dataclass


@dataclass
class SectionAssignment(object):
    start: int
    end: int

    @classmethod
    def from_string(cls, assignment: str) -> "SectionAssignment":
        start, end = assignment.split("-")
        return cls(int(start), int(end))

    @staticmethod
    def full_overlap(first: "SectionAssignment", second: "SectionAssignment") -> bool:
        if first.start <= second.start and first.end >= second.end:
            return True
        elif first.start >= second.start and first.end <= second.end:
            return True
        else:
            return False

    @staticmethod
    def any_overlap(first: "SectionAssignment", second: "SectionAssignment") -> bool:
        if first.start <= second.end and first.end >= second.start:
            return True
        elif second.start <= first.end and second.end >= first.start:
            return True
        else:
            return False


def main():
    with open("day4/input.txt") as inputfile:
        num_fully_overlapping = 0
        num_partially_overlapping = 0
        for line in inputfile:
            elf1, elf2 = line.split(",")
            elf1 = SectionAssignment.from_string(elf1)
            elf2 = SectionAssignment.from_string(elf2)

            if SectionAssignment.full_overlap(elf1, elf2):
                num_fully_overlapping += 1
            if SectionAssignment.any_overlap(elf1, elf2):
                num_partially_overlapping += 1

        print(num_fully_overlapping)
        print(num_partially_overlapping)


if __name__ == "__main__":
    main()
