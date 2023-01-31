x = 0
i = 1
while x <= 100:
    if x % 3 == 0:
        print(f'{i}º - {x}')
        i += 1
    if i == 11:
        break
    x += 1
