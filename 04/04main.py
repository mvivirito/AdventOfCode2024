def main():
    xmas_grid = []
    with open('04/input.txt') as f:
        for line in f.readlines():
            xmas_grid.append(list(line.strip()))

    print(xmas_grid)


if __name__ == '__main__':
    main()