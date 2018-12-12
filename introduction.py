# Introduction
#Say "Hello, World!" With Python https://www.hackerrank.com/challenges/py-hello-world/problem
print("Hello, World!")

#Python If-Else https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python3

N = int(input())

if N%2 == 0:
    if 2 <= N <= 5:
        print('Not Weird')
    elif 6 <= N <= 20 :
        print('Weird')
    elif N > 20:
        print('Not Weird')
else:
    print('Weird')

#Arithmetic Operators https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division https://www.hackerrank.com/challenges/python-division/problem
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops https://www.hackerrank.com/challenges/python-loops/problem
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i*i)

#Write a function https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0 and (year% 400 == 0 or year%100 != 0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))

#Print function https://www.hackerrank.com/challenges/python-print/problem
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    print(*arr, sep='')
