import re

def main():
    file1 = open('day4_input.txt', 'r')
    Lines = file1.readlines()
    overlap = 0
    for line in Lines:
        sectors = list(map(int, re.split('-|,',line.rstrip())))
        if sectors[2] <= sectors[1] and sectors[2] >= sectors[0]:
            overlap += 1
            print(sectors)
        elif sectors[0] <= sectors[3] and sectors[0] >= sectors[2]:
            overlap += 1
            print(sectors)
    print(overlap)
if __name__ == "__main__":
    main()