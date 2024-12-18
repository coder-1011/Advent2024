file_path = "day4_1input.txt"

# Read lines from the file and remove any trailing newlines
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Assign lines to lin
lin = lines[:]

# Extend lin with the concatenated columns
lin.extend(["".join([row[i] for row in lines]) for i in range(len(lines[0]))])

# Diagonal extraction function
def find_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])

    main_diagonals = {}
    anti_diagonals = {}

    for r in range(rows):
        for c in range(cols):
            key_main = r - c  # For main diagonals (r - c)
            if key_main not in main_diagonals:
                main_diagonals[key_main] = []
            main_diagonals[key_main].append(grid[r][c])

            key_anti = r + c  # For anti-diagonals (r + c)
            if key_anti not in anti_diagonals:
                anti_diagonals[key_anti] = []
            anti_diagonals[key_anti].append(grid[r][c])

    return main_diagonals, anti_diagonals

# Extract main and anti-diagonals
main_diagonals, anti_diagonals = find_diagonals(lines)

# Extend lin with the concatenated diagonals (converted to strings)
lin.extend(["".join(i) for i in main_diagonals.values()])
lin.extend(["".join(i) for i in anti_diagonals.values()])

# Output the result for verification (optional)
print(lin)
print(len(lin), len(lin[0]))

# Count occurrences of "XMAS" and "SAMX" across all lines in lin
result = sum(line.count("XMAS") + line.count("SAMX") for line in lin)

# Print the result of the count
print(f"Total occurrences of 'XMAS' and 'SAMX': {result}")
