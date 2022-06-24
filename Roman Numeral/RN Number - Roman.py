import sys

conversion = [[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]

def NumberToRoman(number):
    roman = ""
    for i in range(len(conversion)):
        while number >= conversion[i][0]:
            roman += conversion[i][1]
            number -= conversion[i][0]
    return roman

if __name__ == "__main__":
    number = int(input("What number would you like to convert into a Roman numeral?"))
    if number < 1 or number > 4999:
        print("Number must be between 1 and 4999")
        sys.exit()
    for i in range(1,50):
        print(i, "is", NumberToRoman(i))