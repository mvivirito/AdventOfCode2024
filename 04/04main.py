def main():
    xmas_grid = []
    with open('04/input.txt') as f:
        for line in f.readlines():
            xmas_grid.append(list(line.strip()))

    ROWS = len(xmas_grid)
    COLS = len(xmas_grid[0])
    global total
    total = 0

    def scan_letter(grid, r, c, proper_letter):
        global total
        if min(r, c) > 0 and r < ROWS and c < COLS:
            current_letter = grid[r][c]
            if current_letter != proper_letter:
                return 
            if current_letter == 'X':
                next_letter = 'M'
            elif current_letter == 'M':
                next_letter = 'A'
            elif current_letter == 'A':
                next_letter = 'S'
            elif current_letter == 'S':
                total += 1
                return
            scan_letter(grid, r-1, c-1, next_letter)
            scan_letter(grid, r-1, c, next_letter)
            scan_letter(grid, r-1, c+1, next_letter)
            scan_letter(grid, r, c-1, next_letter)
            scan_letter(grid, r, c+1, next_letter)
            scan_letter(grid, r+1, c-1, next_letter)
            scan_letter(grid, r+1, c, next_letter)
            scan_letter(grid, r+1, c+1, next_letter)

    for r in range(ROWS):
        for c in range(COLS):
            current_letter = xmas_grid[r][c]
            if current_letter == 'X':
                scan_letter(xmas_grid, r, c, current_letter)


if __name__ == '__main__':
    main()
    print(total)