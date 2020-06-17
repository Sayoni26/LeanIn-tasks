1. Write a Python program to calculate the length of string 
p=input()
print(len(p))
string=input("enter the string:")
print(len(string))

2. Write a Python program to count the number of characters (character frequency) in a string.
**Sample String** : 'google.com'
**Expected Result** : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str =input()
i=0
dict={}
while(i<len(str)):
    s=str[i]
    val=(str.count(str[i]))
    i+=1
    if s not in dict:
          dict[s]=val
print(dict)

3. Write a Python function to reverses a string if it's length is a multiple of 4.
s=input("enter string")
if (len(s)%4==0):
    rev=s[::-1]
    print(rev)
string=input("enter the string:")
freq={}
for i in string: 
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1
print ("Count of all characters in is :\n "+  str(freq))

3. Write a Python function to reverses a string if it's length is a multiple of 4.
string=input("enter the string:") 
if len(string)%4==0:
    string=string[::-1]
    print(string)
else:
    print("string length not divisble by 4")
    
    
4. Write a Python program to convert a string in a list.
s=input("enter string:")
print(list(s))

5. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
s1=input("enter string:")
s2=input("enter string:")
i=0
while i<=len(s2)-1:
    if s1[i] in s2:
        f=s1+s2[i]
    i=i+1
print(f)


**Example :**
**Original Substrings:**
>abcdpqr

>xyzabcd

**After concatenating uncommon characters:**
>pqrxyz
s1=input("first string:")
s2=input("second string:")
i=0
while i<=(len(s2)-1):
    if s1[i] in s2:
        fs=s1+s2[i]
    i=i+1
print(fs)        

