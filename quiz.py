f = open('book.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

f = open('book.txt', 'r')
lines = f.read()
f.close()
print(lines)