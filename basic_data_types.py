#Basic Data Types
# List Comprehension https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k] for i in range(x+1)
                    for j in range(y+1) 
                    for k in range(z+1) 
                    if ((i+j+k) != n)])

#Find the Runner-Up Score! https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst = list(arr)    
    z = max(lst)

    while z == max(lst):
        lst.remove(max(lst))

    print(max(lst))


# Nested loops https://www.hackerrank.com/challenges/nested-list
if __name__ == '__main__':
    arr = []
    #res_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    res = sorted(list(set([score for name, score in arr])))[1]
    print(*sorted(name for name, score in arr if score == res), sep='\n')

# Finding percentage https://www.hackerrank.com/challenges/finding-the-percentage

def average_marks(name):
    scores = student_marks[name]
    avg = sum(scores)/len(scores)
    return ("{0:.2f}".format(round(avg,2)))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(average_marks(query_name))

#List https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(int(N)):
        function = input()
        #list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
        if function.split(' ')[0] == 'insert':
            lst.insert(int(function.split(' ')[1]), int(function.split(' ')[2]))
        #list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
        elif function.split(' ')[0] == 'remove':
            lst.remove(int(function.split(' ')[1]))
        #list.append(elem) -- adds a single element to the end of the list.
        elif function.split(' ')[0] == 'append':
            lst.append(int(function.split(' ')[1]))
        #list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
        elif function == 'pop':
            lst.pop(len(lst)-1)
        #list.sort() -- sorts the list in place (does not return it). 
        elif function == 'sort':
            lst.sort()
        #list.reverse() -- reverses the list in place (does not return it)
        elif function == 'reverse':
            lst.reverse()
        elif function == 'print':
            print(lst)

#Tuple https://www.hackerrank.com/challenges/python-tuples/
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))






   


