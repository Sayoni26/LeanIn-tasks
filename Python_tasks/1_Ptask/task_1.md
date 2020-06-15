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

n=input()
if n>=1 and n<=100:
    if n%2!=0:
        print("weird")
    if n%2==0 and in range(2,6)
        print("not weird")    
    if n%2==0 and in range(6,21)
        print("weird")
    if n%2==0 and n>20
        print("not weird")

