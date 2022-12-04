import re

def main():
    file1 = open('day4_input.txt', 'r')
    Lines = file1.readlines()
    isIn = 0
    for line in Lines:
        sectors = list(map(int, re.split('-|,',line.rstrip())))
        if sectors[0] <= sectors[2] and sectors[1] >= sectors[3]:
            isIn += 1
        elif sectors[2] <= sectors[0] and sectors[3] >= sectors[1]:
            isIn += 1
    print(isIn)
if __name__ == "__main__":
    main()