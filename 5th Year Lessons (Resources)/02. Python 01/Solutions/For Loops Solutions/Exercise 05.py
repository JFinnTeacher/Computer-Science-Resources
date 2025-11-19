'''
Exercise 05
Word Analyser
'''
# Get user input Asks user to enter a sentence
sentence=input('Please enter a sentence: ')

# Initialise a counter to count the number of vowels
vowel_count=0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a vowel
    if char.lower() in 'aeiou':
        vowel_count+=1

# Display the number of vowels in the sentence
print('The number of vowels in the sentence is:', vowel_count)