import string
paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()
for symbol in string.punctuation:
    paragraph = paragraph.replace(symbol, "")
words = paragraph.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_words = sorted(
    word_counts.items(),
    key=lambda item: item[1],
    reverse=True
)
print("\nTop 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")