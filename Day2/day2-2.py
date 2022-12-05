def main():
    file1 = open('input_day2', 'r')
    Lines = file1.readlines()
    score = 0
    for line in Lines:
        if line[2] == "X":
            if line[0] == "A":
                score += 3
            elif line[0] == "B":
                score += 1
            else:
                score += 2
        if line[2] == "Y":
            score += 3
            if line[0] == "A":
                score += 1
            elif line[0] == "B":
                score += 2
            else:
                score += 3
        if line[2] == "Z":
            score += 6
            if line[0] == "A":
                score += 2
            elif line[0] == "B":
                score += 3
            else: 
                score += 1
    print(score)
    return 0

if __name__ == '__main__':
    main()