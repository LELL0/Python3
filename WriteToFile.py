import string
import random
import time

fhand = open("WriteToFile_OUTPUT.txt", 'w')

letters = string.ascii_uppercase

length = int(input("name length: "))

numNames = int(input("number of names to generate: "))

print("Generating...")

beforeLoop = time.time_ns()

for n in range(numNames):

    if (n == numNames/4):
        print("25% done")
    elif (n == numNames/2):
        print("50% done")
    elif (n == (numNames*3)/4):
        print("75% done")

    fhand.write(''.join(random.choice(letters) for i in range(length))+"\n")

afterLoop = time.time_ns()

elapsed = (afterLoop-beforeLoop)*10**-9
print("time elapsed: ", elapsed)

print("Done")
