#1
def anagram_number():
    num = str(input("Nhập số nguyên: "))    
    reverse_num = num[::-1]
    if int(num) == int(reverse_num):
        print('True')
    else:
        print('False')
    pass
# anagram_number()

#2
def roman_to_int():
    roman = input("Nhập chữ số la mã cần chuyển đổi: ")
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in roman_dict:
            num += roman_dict[roman[i:i+2]]
            i += 2
        else:
            num += roman_dict[roman[i]]
        i += 1
    print("Số la mã ",roman," có giá trị bằng ",num)
# roman_to_int()