Consider a list (list = []). You can perform the following commands:

* insert i e: Insert integer e at position i.
* print: Print the list.
* remove e: Delete the first occurrence of integer e.
* append e: Insert integer e at the end of the list.
* sort: Sort the list.
* pop: Pop the last element from the list.
* reverse: Reverse the list.

Initialize your list and read in the value of **n** followed by **n** lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

**Input Format**

The first line contains an integer, **n** , denoting the number of commands.
Each line **i** of the **n** subsequent lines contains one of the commands described above.

**Constraints**

* The elements added to the list must be integers.

**Output Format**

For each command of type print, print the list on a new line.

**Sample Input 0**

>12

>insert 0 5

>insert 1 10

>insert 0 6

>print

>remove 6

>append 9

>append 1

>sort

>print

>pop

>reverse

>print

**Sample Output 0**

>[6, 5, 10]

>[1, 5, 9, 10]

>[9, 5, 1]

nlist=[3,2,5,4]
#for inserting e at i position
e=int(input("insert"))
i=int(input())
nlist.insert(i,e)
print(nlist)

#for removing e from list
nlist.remove(e)
print(nlist)

#adding e to the list
nlist.append(e)
print(nlist)

#for sorting
nlist.sort()
print(nlist)

#for poping the last variable of the list
last=len(nlist)-1
nlist.pop(last)
print(nlist)

#reversing the list
nlist.reverse()
print(nlist)

