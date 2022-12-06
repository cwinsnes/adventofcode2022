from enum import IntEnum


class RockPaperScissors(IntEnum):
    """Representations of values for Rock Paper Scissors."""

    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def beats(first: "RockPaperScissors", other: "RockPaperScissors"):
        return (first) % 3 == (other + 1) % 3

    @staticmethod
    def from_string(choice_string: str) -> "RockPaperScissors":
        match (choice_string):
            case "X" | "A":
                return RockPaperScissors.ROCK
            case "Y" | "B":
                return RockPaperScissors.PAPER
            case "Z" | "C":
                return RockPaperScissors.SCISSOR


def find_matching_strat(
    enemy_choice: RockPaperScissors, current_strategy: str
) -> RockPaperScissors:
    match (current_strategy):
        case "Y":  # DRAW
            return enemy_choice
        case "X":  # LOSE
            return RockPaperScissors((enemy_choice + 1) % 3 + 1)
        case "Z":  # WIN
            return RockPaperScissors((enemy_choice % 3) + 1)


def main():
    with open("day2/input.txt") as inputfile:
        task1_total_score = 0
        task2_total_score = 0
        for iteration, line in enumerate(inputfile):
            enemy, hero = line.split()
            enemy = RockPaperScissors.from_string(enemy)
            strategy_choice = find_matching_strat(enemy, hero)
            hero = RockPaperScissors.from_string(hero)

            task1_total_score += hero
            task2_total_score += strategy_choice

            # Task 1
            if enemy == hero:
                task1_total_score += 3
            elif RockPaperScissors.beats(hero, enemy):
                task1_total_score += 6

            # Task 2
            if enemy == strategy_choice:
                task2_total_score += 3
            elif RockPaperScissors.beats(strategy_choice, enemy):
                task2_total_score += 6

        print("Task 1:", task1_total_score)
        print("Task 2:", task2_total_score)


if __name__ == "__main__":
    main()
