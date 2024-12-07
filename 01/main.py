def main():
    group1 = [] 
    group2 = [] 
    with open("./input.txt", "r") as file:
        for line in file.readlines():
            groups = line.split()
            group1.append(int(groups[0]))
            group2.append(int(groups[1]))

    group1.sort()
    group2.sort()
    groups = list(zip(group1, group2))
    total = 0
    for group in groups:
        total += abs(group[0] - group[1])

    print(total)


if __name__ == "__main__":
    main()

    
