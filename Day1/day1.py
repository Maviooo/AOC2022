
def main():
    file1 = open('input_day1', 'r')
    Lines = file1.readlines()
    indexOfMax = 0
    currnetIndex = 0 
    max = 0
    temp = 0  
    # Strips the newline character
    for line in Lines:
        if line == "\n":
            if( temp > max):
                max = temp
                indexOfMax = currnetIndex
            temp = 0 
            currnetIndex += 1
        else:
          temp += int(line)
    print(indexOfMax)
    print(max)
    return 0

if __name__ == '__main__':
    main()