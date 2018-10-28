

f = open('data1.txt','r')
text = f.read()
print(text)
print(f.tell())
f.close()

f = open('data2.txt', 'w')
f.write('hello\nworld\ntree')
f.close()

f = open('data2.txt', 'r')
f.read()
print(f.tell())         # after reading the cursor will be always at the end
f.seek(0)               # seek will put the cursor in the position we want
print(f.tell())

f = open('data2.txt','r+')
text = f.read()         # reads and puts the cursor at the end
print(text)
print(f.tell())         # tells me where the cursor is
f.write('my name is cesar')     # adds text to the last cursor position
f.flush()               # the function works in the console where everything is in memory ram
print(text)
f.close()               # saves the changes to document and closes it

f = open('data2.txt', 'a+')     # append will let you add content but just at the end
text = f.read()
print(text)
f.seek(0)
f.write('this is my house')
f.close()

f = open('data2.txt', 'r')
text = f.read()
print(text)
f.close()


f = open('data3.txt','w+')
f.write('this is my castle and i will defend it')
f.close()

f = open('data3.txt','r')
text = f.read()
print (text)

f = open('data4.txt','w+')
f.write('line 1\nline 2\nline 3\nline 4')
f.close()

# this are the challenges

f = open('data4.txt', 'r+')
text = f.read()
f.write('\nline 5')
f.close()

f = open('data4.txt', 'r+')
f.write('over 1')
f.close()

f = open('data4.txt', 'r+')
f.seek(16)
f.write('over 2')
f.close()
