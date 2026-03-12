text = input()

count = 1

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        print(count, text[i-1], sep="", end="")
        count = 1

print(count, text[-1], sep="")