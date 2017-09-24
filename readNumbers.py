
obj = open("numbers.txt", "r")
data = obj.read()

num = data.split(',')

for i in num:
    print i

