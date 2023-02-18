str1 = input("Please enter the first string: ")
str2 = input("Please enter the second string: ")

if len(str1) != len(str2):
    print("it is not an anagram")

str1 = sorted(str1)
str2 = sorted(str2)

anagram = True
for i in range(0,len(str1)):
    if str1[i] != str2[i]:
        anagram = False
    if anagram == False:
        print("Its not an anagram")
        break
if anagram == True:
    print("It is an anagram")