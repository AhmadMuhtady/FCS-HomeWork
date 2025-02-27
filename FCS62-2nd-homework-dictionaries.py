# Complete each question using Python dictionaries

# Write a function that takes two dictionaries and returns a new dictionary that 
# combines both. If there are duplicate keys, values from should override those from .

# Example:
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 10, "d": 4}

# merge_dictionaries(dict1, dict2)
# Expected Output:
# {"a": 1, "b": 10, "c": 3, "d": 4}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "d": 4}
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}
print(merge_dictionaries(dict1, dict2))

# 2 - Write a program that takes a sentence as input and prints a dictionary where:
# are words in the sentence.
# are the number of times each word appears.
# Example:
# "apple orange banana apple orange apple"

# Expected Output:
# {"apple": 3, "orange": 2, "banana": 1}
example_2 = "apple orange banana apple orange apple"
def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
print(count_words(example_2))
