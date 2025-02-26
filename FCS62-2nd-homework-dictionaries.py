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


