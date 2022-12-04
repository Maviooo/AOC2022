def findSame(lineOne, lineTwo, lineThree):
    for x in lineOne:
        for y in lineTwo:
            for z in lineThree:
                if z == y and y == x:
                    return z

def main():
    file1 = open('day3_input.txt', 'r')
    Lines = file1.readlines()
    sameItems = ""
    pioritySum = 0
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    for lineOne, lineTwo, lineThree in zip(Lines[0::3], Lines[1::3], Lines[2::3]):
        sameItems += findSame(lineOne, lineTwo, lineThree)
    for x in sameItems:
        for leter, number in zip(charList, numbers):
            if x == leter:
                pioritySum += number
                break
    print(pioritySum)
    return 0 

if __name__ == "__main__":
    main()