from typing import List

def main():
    safe = 0

    def check_increasing(level: List[int]) -> bool:
        current = level[0]
        for num in level[1:]:
            if num < current:
                return False
            else:
                current = num
        return True

    def check_decreasing(level: List[int]) -> bool:
        current = level[0]
        for num in level[1:]:
            if num > current:
                return False
            else:
                current = num
        return True

    def check_differs(level: List[int]) -> bool:
        first = 0
        second = 1
        end = len(level) - 1
        while second <= end:
            val = abs(level[first] - level[second])
            if val > 3 or val < 1:
                return False
            else:
                first += 1
                second += 1
        return True

        

    def converter(input: str):
        return [int(x) for x in list(input.split())]

    with open("./input.txt", "r") as file:
        for line in file.readlines():
            current_levels = converter(line)
            if (check_increasing(current_levels) 
                or check_decreasing(current_levels)) and check_differs(current_levels):
                safe += 1 

    print(safe)

if __name__ == "__main__":
    main()

    