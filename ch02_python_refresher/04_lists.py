# * Create a List
lst = [1, "a", "hello"]
lst1 = []
lst2 = list()

# * Access Elements in a List
lst = [1, "a", "hello"]
print(lst[2])

for x in range(len(lst)):
    print(lst[x])

# * Use a List of Lists

llst = [[1, 2, 3, 5],
        [2, 2, 6, 8],
        [2, 3, 5, 9],
        [3, 5, 4, 7],
        [1, 3, 5, 0]]

print('the value of llst[1][2] is', llst[1][2])
print('the value of llst[3][2] is', llst[3][2])
print('the value of llst[1][3] is', llst[1][3])

# * Add or Multipy Lists
lst = [1, "a", "hello"]
print(lst + lst)
print(lst * 3)

# * List Methods
# ** enumerate()
names = ['Adam', 'Kate', 'Peter']

for x, name in enumerate(names):
    print(x, name)

for x, name in enumerate(names, start=1):
    print(x, name)

# ** append()
lst = [1, "a", "hello"]
lst.append(2)
print(lst)

# lst.append(2, 3)
# TypeError: append() takes exactly one arguments (2 given)

lst.append([2, 3])
print(lst)

lst = [1, "a", "hello"]
print(lst + [2, 3])

# ** remove()
lst = [1, "a", "hello", 2]
lst.remove("a")
print(lst)

# ** index()
lst = [1, "a", "hello", 2]
print(lst.index("a"))

# ** count()
lst = [1, "a", "hello", 2, 1]
print(lst.count(1))
print(lst.count("a"))

# ** sort()
# lst.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

lst = [5, 47, 12, 9, 4, -1]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

lst = ['a', 'hello', 'ba', 'ahello', '2', '-1']
lst.sort()
print(lst)

# * Use Built-in Functions with Lists
lst = [5, 47, 12, 9, 4, -1]
print("the range of the numbers is", max(lst) - min(lst))
print("the mean of the numbers is", sum(lst) / len(lst))

# ** list()
msg = "hello"
letters = list(msg)
print(letters)
