# 1) Comparison of operations
num1 = 64 * 3
num2 = 24 * 8
my_bool = num1 != num2
print("Exercise 1 -> num1:", num1, "num2:", num2, "Is num1 != num2?:", my_bool)

# 2) Check if words are NOT in the text
word1 = "success"
word2 = "technology"
text = "When something is important enough, you do it even if the odds are not in your favor."
my_bool2 = word1 not in text and word2 not in text
print("Exercise 2 -> Are 'success' and 'technology' not in the text?:", my_bool2)

# 3) Job application requirements
knows_python = False
knows_english = True

if knows_python and knows_english:
    print("Exercise 3 -> You meet the requirements to apply")
elif not knows_python and not knows_english:
    print("Exercise 3 -> To apply, you need to know Python and English")
elif not knows_english:
    print("Exercise 3 -> To apply, you need English skills")
elif not knows_python:
    print("Exercise 3 -> To apply, you need Python skills")

# 4) Sum of even and odd numbers
number_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0

for num in number_list:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Exercise 4 -> Sum of even numbers:", sum_even, "Sum of odd numbers:", sum_odd)

# 5) While loop from 50 to 0 showing only multiples of 5
print("Exercise 5 -> Numbers divisible by 5:")
num = 50
while num >= 0:
    if num % 5 == 0:
        print(num)
    num -= 1

# 6) For loop that stops at first negative
number_list2 = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
print("Exercise 6 -> Numbers until a negative is found:")
for n in number_list2:
    if n < 0:
        break
    print(n)

# 7) Sum of squares from 1 to 15
sum_squares = 0
for i in range(1, 16):
    sum_squares += i ** 2

print("Exercise 7 -> Sum of squares from 1 to 15:", sum_squares)
