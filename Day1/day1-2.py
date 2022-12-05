
def main():
    file1 = open('input_day1', 'r')
    Lines = file1.readlines()
    elfs = []
    currnetIndex = 0 
    temp = 0  
    # Strips the newline character
    for line in Lines:
        if line == "\n":
            elfs.append(temp)
            temp = 0 
            currnetIndex += 1
        else:
          temp += int(line)
    print(sum(sorted(elfs, reverse=True)[:3]))
    return 0

if __name__ == '__main__':
    main()