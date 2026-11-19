# Banner
print(" LET PLAY with a WORD!!!! ")

#  Ask the user for a word

word = input("Please enter a word: ")

# Show the length of the word
print(f"The length of your word is: {len(word)}")

# Display word in all uppercase
print(f"In uppercase: {word.upper()}")

# Display word repeated 3 times

print("Repeated 3 times:")
print((word + "\n") * 3)
