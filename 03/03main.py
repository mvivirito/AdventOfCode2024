import re

def main():
    pattern = "mul\(\d+,\d+\)"
    total = 0
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            matches = re.findall(pattern, line)
            for match in matches:
                match = match.replace("mul(", "")
                match = match.replace(")", "")
                numbers = match.split(",")
                total += int(numbers[0]) * int(numbers[1])
    
    print(total)
    
if __name__ == "__main__":
    main()

    