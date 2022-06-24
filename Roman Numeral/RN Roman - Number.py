invalid = ['A', 'B', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']
def romanNumeral():
    if roman.isalpha() and not any(invalid in roman for invalid in invalid):
        return True
    return False

def row0(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case " ":
            return value
        case _:
            print("Invalid Roman Numeral")
            return 0

def row1(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "M":
            value += 1000
            return row1(value, roman, charValue)
        case "D":
            value += 500
            return row2(value, roman, charValue)
        case "C":
            value += 100
            return row8(value, roman, charValue)
        case "L":
            value += 50
            return row4(value, roman, charValue)
        case "X":
            value += 10
            return row9(value, roman, charValue)
        case "V":
            value += 5
            return row6(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row2(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "C":
            value += 100
            return row8(value, roman, charValue)
        case "L":
            value += 50
            return row4(value, roman, charValue)
        case "X":
            value += 10
            return row9(value, roman, charValue)
        case "V":
            value += 5
            return row6(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row3(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "C":
            value += 100
            return row3(value, roman, charValue)
        case "L":
            value += 50
            return row4(value, roman, charValue)
        case "X":
            value += 10
            return row9(value, roman, charValue)
        case "V":
            value += 5
            return row6(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row4(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "L":
            value += 50
            return row5(value, roman, charValue)
        case "X":
            value += 10
            return row9(value, roman, charValue)
        case "V":
            value += 5
            return row6(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row5(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "X":
            value += 10
            return row5(value, roman, charValue)
        case "V":
            value += 5
            return row6(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row6(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "V":
            value += 5
            return row7(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row7(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "I":
            value += 1
            return row7(value, roman, charValue)
        case " ":
            return value

def row8(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "M":
            value += 800
            return row4(value, roman, charValue)
        case "D":
            value += 300
            return row4(value, roman, charValue)
        case "C":
            value += 100
            return row3(value, roman, charValue)
        case "L":
            value += 50
            return row5(value, roman, charValue)
        case "X":
            value += 10
            return row9(value, roman, charValue)
        case "V":
            value += 5
            return row7(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row9(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "C":
            value += 80
            return row6(value, roman, charValue)
        case "L":
            value += 30
            return row6(value, roman, charValue)
        case "X":
            value += 10
            return row5(value, roman, charValue)
        case "V":
            value += 5
            return row7(value, roman, charValue)
        case "I":
            value += 1
            return row10(value, roman, charValue)
        case " ":
            return value

def row10(value, roman, charValue):
    charValue += 1
    match roman[charValue]:
        case "X":
            value += 8
            return row0(value, roman, charValue)
        case "V":
            value += 3
            return row0(value, roman, charValue)
        case "I":
            value += 1
            return row8(value, roman, charValue)
        case " ":
            return value

import sys
        
if __name__ == "__main__":
    roman = str(input("What Roman Numeral should be converted: ")).upper()
    if not romanNumeral():
        print("Not a roman numeral")
        input()
        sys.exit()
    roman += " "
    charValue = -1
    value = 0
    print(roman+"=",row1(value, roman, charValue))
    input()