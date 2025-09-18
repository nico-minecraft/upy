import random

# 1) Remove a random element from a set
raffle = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Monica"}
element = random.choice(list(raffle))  # choose a random element
raffle.remove(element)  # remove it using set methods
print("Removed element:", element)
print("Set after removal:", raffle)

# 2) Check if the square root of 25 is equal to 5
result = (25 ** 0.5) == 5
print("Is the square root of 25 equal to 5?:", result)

# 3) Text analysis
text = input("Enter a text: ").strip()
letters = input("Enter three letters separated by spaces: ").lower().split()

# First: count how many times each chosen letter appears
for letter in letters:
    print(f"The letter '{letter}' appears {text.lower().count(letter)} times.")

# Second: count number of words
words = text.split()
print("Number of words in the text:", len(words))

# Third: first and last character
print("First character of the text:", text[0])
print("Last character of the text:", text[-1])

# Fourth: reversed word order
reversed_text = " ".join(words[::-1])
print("Text with reversed word order:")
print(reversed_text)

# Fifth: check if "Python" is in the text
print("Is the word 'Python' in the text?:", "python" in text.lower())
