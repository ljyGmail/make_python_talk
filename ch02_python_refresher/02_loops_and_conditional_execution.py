# * Conditional Execution
x = 5
if x > 0:
    print('x is positive')
else:
    print('x is nonpositive')

x = 5
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is zero')
else:
    print('x is negative')

score = 88
if score >= 90:
    print('grade is A')
elif score >= 80:
    print('grade is B')
elif score >= 70:
    print('grade is C')
elif score >= 60:
    print('grade is D')
else:
    print('grade is F')

# * Loops
# ** The while loop
n = 0
while n < 3:
    n = n+1
    print(n)
print('finished')

# ** The for loop
for n in range(3):
    n = n+1
    print(n)
print('finished')

# * Loops in Loops
for letter in ["A", "B", "C"]:
    for num in (1, 2):
        print(f"this is {letter}{num}")

# * Loop Commands
# ** continue
for n in (1, 2, 3):
    if n == 2:
        continue
    print(n)
print('finished')

# ** break
for n in (1, 2, 3):
    if n == 2:
        break
    print(n)
print('finished')

# ** pass
for n in (1, 2, 3):
    if n == 2:
        pass
    print(n)
print('finished')
