scores = {'blue': 10, 'white': 12}

dict1 = dict()
dict2 = {}

dict3 = {}
dict3['yellow'] = 6
print(dict3)

# * Access Values in a Dictionary
print(scores['blue'])
print(scores['white'])

scores = {'blue': 10, 'white': 12}
print(scores['blue'])
print(scores['white'])
print(scores.get('yellow'))
print(scores.get('yellow', 0))

# * Use Dictionary Methods
scores = {'blue': 10, 'white': 12}
teams = list(scores.keys())
print(teams)

points = list(scores.values())
print(points)

print(list(scores.items()))

# * How to Use Dictionaries
scores2 = {'blue': [5, 5, 10], 'white': [5, 7, 12]}
print(scores2['white'][1])

news = (
    '''Python is an interpreted, high-level, and general-purpose programming
language. Python's design philosophy emphasizes code readability with
its notable use of significant whitespace.
Its language constructs and object-oriented approach aim to help
programmers write clear, logical code for small- and large-scale
projects.
''')
wdcnt = dict()
wd = news.split()
for w in wd:
    wdcnt[w] = wdcnt.get(w, 0) + 1
print(wdcnt)

for w in list(wdcnt.keys()):
    if wdcnt[w] == max(list(wdcnt.values())):
        print(w)

# * Switch Keys and Values
spanish = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

english = {y: x for x, y in spanish.items()}
print(english)

# * Combine Two Dictionaries
spanish_english = {**spanish, **english}
print(spanish_english)
