import re
from collections import deque

crate_line = r"(   |\[\w\])( |\n)"
crate_regex = re.compile(crate_line)

# Yes, this is super ugly
# I did not have the spare time to do it properly.
def main():
    stacks = None
    stacking = True
    with open("day5/input.txt") as inputfile:
        for line in inputfile:
            if stacking:
                if line == "\n":
                    stacking = False
                    continue
                crates = crate_regex.findall(line)
                if stacks is None:
                    stacks = [deque() for _ in crates]
                for index, crate in enumerate(crates):
                    crate = crate[0]
                    if "[" in crate:
                        stacks[index].append(crate)
            else:
                numbers = re.findall("\d+", line)
                amount, fromstack, tostack = [int(x) for x in numbers]
                # TASK 1
                # for _ in range(amount):
                #     to_move = stacks[fromstack - 1].popleft()
                #     stacks[tostack - 1].appendleft(to_move)

                # TASK 2
                to_move = deque()
                for _ in range(amount):
                    to_move.appendleft(stacks[fromstack - 1].popleft())
                stacks[tostack - 1].extendleft(to_move)

        for stack in stacks:
            print(stack[0][1], end="")
        print()


if __name__ == "__main__":
    main()
