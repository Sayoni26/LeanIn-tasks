**Task**
Given an integer,**n**, perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of **2** to **5**, print Not Weird
* If n is even and in the inclusive range of **6** to **20**, print Weird
* If n is even and greater than **20**, print Not Weird

**Input Format**

A single line containing a positive integer,**n** .

**Constraints**
>1 <= n <= 100

**Output Format**

Print Weird if the number is weird; otherwise, print Not Weird.

**Sample Input 0**

3
**Sample Output 0**
>Weird
n=int(input("enter the number"))
if n>=1 and n<=100:
    if n%2!=0:
        print("weird")
    elif n>=2 and n<=5:
        print("not weird")
    elif n>=6 and n<=20:
        print("weird")
    else:
        print("not weird")
else:
    ("invalid number")