sentence = input("Please enter a text you want to check = ")

wordCount = 0
characterCount = 0

characterCount = len(sentence)
wordList = sentence.split()
wordCount = len(wordList)

print(f"Word Count = {wordCount}")
print(f"Character Count = {characterCount}")