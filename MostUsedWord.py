counts = dict()
line = input('\nEnter a line of text: ')
words = line.split()

print('The words are: ', words)
print('Counting...')

for word in words:
    # it will add 1 to the value of the key:word if id does now exist it will create one with a value:0+1
    counts[word] = counts.get(word, 0) + 1

print('Counts: ', counts)
