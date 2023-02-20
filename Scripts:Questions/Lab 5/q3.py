def Is_substring(short_string,long_string):
    if short_string in long_string:
        p = long_string.rfind(short_string)
        return True, p
    else:
        p = len(long_string)
        return False, p
            

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
check, index = Is_substring(str1,str2)
if check:
    print(str1,"is a substring of",str2)
    print("The last occurrence of",str1,"is at index",index)
else:
    print("It is not a substring")
    print("The length of the second string is",index)
    