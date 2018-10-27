# w to write document # r to read document

'''f = open('newfile.txt','w')
f.write("hello\n")
f.close()'''

# creates a new file and puts some text in it

# a will append content to the document

f = open('newfile.txt', 'a')
f.write("world")
f.close()

# everytime we play the fuction will add content in the document

# we can add a list of strings

f = open('newfile1.txt', 'a')
lines = ['first', 'second', 'third', 'forth']
text = '\n'.join(lines)
f.writelines(text)
f.close()