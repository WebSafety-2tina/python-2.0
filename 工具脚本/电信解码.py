list = [116,114,98,107,122,]

result = []

for i in list:
    if i > 57:
        i -= 4
    result.append(chr(i))

print(''.join(result))
