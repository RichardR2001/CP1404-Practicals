"""
Word Occurences
Count the number of same words in a sentence
Created on 16-12-2021 by Richard Reynard
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_count = word_to_count.get(word, 0)
    word_to_count[word] = word_count + 1


words = list(word_to_count.keys())
words.sort()

longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {word_to_count[word]}")