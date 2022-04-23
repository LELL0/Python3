fhand = open('file1.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

print('\n##########################################\n')

fhand = open('file1.txt')
for line in fhand:
    if line.startswith('e'):
        continue
    print(line.strip())

print('\n##########################################\n')

fhand = open('file1.txt')
for line in fhand:
    if not 'e' in line:
        continue
    print(line.strip())

print('\n##########################################\n')

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('e'):
        count += 1
print('there were ', count, ' subject lines in ', fname)

print('\n##########################################\n')

fname = input('Enter the file name: ')
valid = False
while(not valid):
    try:
        fhand = open(fname)
        valid = True
    except:
        valid = False
        print('File cannot be opened: ', fname)
        fname = input('Enter the file name: ')


count = 0
for line in fhand:
    if line.startswith('e'):
        count += 1
print('there were ', count, ' subject lines in ', fname)

print('\n################## END ##################\n')
