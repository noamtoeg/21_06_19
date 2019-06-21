num = input("type a number: ")
num = int(num)

list = list(range(num))
# print(list)

n = 0
fact = 1
for n in list:
    n = n + 1
    fact = fact * n

# print(list)
print(fact)
