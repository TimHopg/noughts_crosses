a = range(1, 100)
total = 0
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

