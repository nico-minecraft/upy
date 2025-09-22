lista = ["a", "b", "c"]
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

for index, n in enumerate(lista):
    print(index, n)

print(min(numlist))
print(max(numlist))

print("el maximo es:", max(numlist))

name = "Nicolas"
print(min(name.lower()))

#randint uniform random choice shuffle 
import random
print(random.randint(1, 100))
print(random.uniform(1, 100))
print(random.random())
print(random.choice(numlist))
random.shuffle(numlist)
