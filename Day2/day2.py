def main():
    file1 = open('input_day2', 'r')
    Lines = file1.readlines()
    score = 0
    for line in Lines:
        if line[2] == "X": 
            score += 1
            if line[0] == "A":
                score += 3
            elif line[0] == "C":
                score += 6
        if line[2] == "Y":
            score += 2
            if line[0] == "B":
                score += 3
            elif line[0] == "A":
                score += 6
        if line[2] == "Z":
            score += 3
            if line[0] == "C":
                score += 3
            elif line[0] == "B":
                score += 6
    print(score)
    return 0

if __name__ == '__main__':
    main()