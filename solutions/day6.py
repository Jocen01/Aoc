f = open(r"C:\Users\Jonathan\code@lth\advent_of_code\input\6\input")
word = f.read().strip()
detected = False
for i in range(len(word)):
    if len(set(word[i:i+14])) != 14:
        detected = True
    elif detected:
        print(i+14)
        break