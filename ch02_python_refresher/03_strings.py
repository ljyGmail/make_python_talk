# * String Indexing
msg = "hello"
print(msg[1])

print(msg[-3])

# * String Slicing
msg = "hello"
print(msg[0:3])

# * String Methods
# ** replace()
inp = "University of Kentucky"
inp1 = inp.replace(' ', '+')
print(inp1)

# ** lower()
inp = "Department of Education"
inp1 = "department of education"
print(inp.lower() == inp1.lower())

# ** find()
email = "John.Smith@uky.edu"
pos1 = email.find(".")
print(pos1)

pos2 = email.find("@")
print(pos2)

last_name = email[(1+pos1):pos2]
print(last_name)

email = "John.Smith@uky.edu"
pos = email.find("uky.edu")
print(pos)

# ** split()
msg = "Please think of an integer"
words = msg.split()
print(words)

email = "John.Smith@uky.edu"
(name, domain) = email.split('@')
(first, last) = name.split('.')
print(f"last name is {last}")

# ** join()
mylink = ('&')
strlist = ['University', 'of', 'Kentucky']
joined_string=mylink.join(strlist)
print(joined_string)
