from collections import Counter

with open("output.txt", 'r') as file:
    text = file.read().lower()

words = text.split()
word_count = Counter(words)

# Get the top 30 most common words
common_words = word_count.most_common(30)

# Save to CSV
import csv
with open("top_30_words.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Word", "Count"])
    writer.writerows(common_words)

print("Top 30 words saved to top_30_words.csv")
