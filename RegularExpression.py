import re
x = ' we just recieved $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)

print('\n=============================================================\n')

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@[a-zA-Z]+.[a-zA-Z]+\S', s)
print(lst)
