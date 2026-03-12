text = input()
count = 0
vowel = ["a", "e", "i", "o", "u"]

for i in range(len(text)):
    if text[i] in vowel:
        count += 1

print(count)