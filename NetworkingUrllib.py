import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().strip()
    print(line)
    for letter in words:
        counts[letter] = counts.get(letter, 0)+1

print("\n", counts, "\n")
