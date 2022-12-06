def main():
    elf_calories = []
    calorie_count = 0
    with open("day1/input.txt", "r") as inputfile:
        lines = inputfile.readlines()
        # Added because readlines skips the final newline separator
        lines.extend(["\n", "\n"])
        for line in lines:
            if line != "\n":
                calorie_count += int(line)
            else:
                elf_calories.append(calorie_count)
                calorie_count = 0
    elf_calories = sorted(elf_calories)
    print(elf_calories[-1], elf_calories[-3:], sum(elf_calories[-3:]))


if __name__ == "__main__":
    main()
