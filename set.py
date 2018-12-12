#Sets

#Introduction to Sets https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
   return (sum(set(array))/len(set(array)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
# Set.add() https://www.hackerrank.com/challenges/py-set-add/
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
myset = set()
for _ in range(n):
    myset.add(input())
print(len(myset))

#Set .discard(), .remove() & .pop() https://www.hackerrank.com/challenges/py-set-discard-remove-pop/
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd = input()
    if cmd.split()[0] == 'remove':
        s.remove(int(cmd.split()[1]))
    elif cmd.split()[0] == 'discard':
        s.discard(int(cmd.split()[1]))
    elif cmd == 'pop':
        s.pop()
print(sum(s))

#Set .union() Operation https://www.hackerrank.com/challenges/py-set-union/
# Enter your code here. Read input from STDIN. Print output to STDOUT
na = int(input())
a = set(map(int, input().split()))
nb = input()
b = set(map(int, input().split()))

print(len(a.union(b)))

# Set .intersection() Operation https://www.hackerrank.com/challenges/py-set-intersection-operation/
# Enter your code here. Read input from STDIN. Print output to STDOUT
na = int(input())
a = set(map(int,input().split()))
nb = int(input())
b = set(map(int, input().split()))

print(len(a&b))

# Set .difference() Operation https://www.hackerrank.com/challenges/py-set-difference-operation/
# Enter your code here. Read input from STDIN. Print output to STDOUT
na = int(input())
a = set(map(int,input().split()))
nb = int(input())
b = set(map(int, input().split()))

print(len(a-b))

# Set .symmetric_difference() Operation https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/
na = int(input())
a = set(map(int,input().split()))
nb = int(input())
b = set(map(int, input().split()))

print(len(a^b))


#Symmetric Difference https://www.hackerrank.com/challenges/symmetric-difference/
# Enter your code here. Read input from STDIN. Print output to STDOUT
na = input()
a = set(map(int, input().split()))
nb = input()
b = set(map(int, input().split()))
#aub = a.union(b)
#aib = a.intersection(b)
#print(*sorted(list(aub.difference(aib))), sep = '\n')
print(*sorted(list(a^b)), sep='\n')

#No Idea! https://www.hackerrank.com/challenges/no-idea/
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for each_elem in arr:
    if each_elem in a:
        happiness += 1
    elif each_elem in b:
        happiness -= 1
print(happiness)

# The Captain's Room https://www.hackerrank.com/challenges/py-the-captains-room/ 
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_list = list(map(int, input().split()))
room_set = set(room_list)
print(((sum(room_set)*k)-(sum(room_list)))//(k-1))

# Check Subset https://www.hackerrank.com/challenges/py-check-subset/
# Enter your code here. Read input from STDIN. Print output to STDOUT
import timeit
n = int(input())
for i in range(n):
    no_elem_a = int(input())
    a = set(map(int, input().split()))
    no_elem_b = int((input()))
    b = set(map(int, input().split()))
    print(a.issubset(b))


# Check Strict Superset https://www.hackerrank.com/challenges/py-check-strict-superset/
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = set(map(int, input().split()))
n = int(input())
true = 0
for _ in range(n):
    b = set(map(int, input().split()))
    if a.issuperset(b):
        true += 1
if true == n:
    print('True')
else:
    print('False')
        


