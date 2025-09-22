from collections import Counter
import re

def word_frequency_counter(text):
     # Remove punctuation and make lowercase
     words = re.findall(r'\b\w+\b', text.lower())
     return Counter(words)

if __name__ == "__main__":
     filename = input("Enter the filename: ")
     try:
          with open(filename, 'r', encoding='utf-8') as file:
               text = file.read()
          frequencies = word_frequency_counter(text)
          for word, count in frequencies.most_common():
               print(f"{word}: {count}")
     except FileNotFoundError:
          print("File not found.")