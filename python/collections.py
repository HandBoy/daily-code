"""
Differences and Applications of List, Tuple, Set and Dictionary in Python?

    List:   Receive differents types of value and your values are mutables.
    Tuple:  Is similar to a List but with one difference, it is imutable.
    Set:    Unordered  collection data, mutable and has no duplicate elements.
    Dict:   The keys are imutables and unique. The values are unordered.


"""

# List
list_one = ["one", "two", "three", 89, 5, 1.2]
list_one[0] = "eita"
print(list_one)
print(list_one[0])

# Tuple
tuple_one = ("one", "two", "three", 89, 5, 1.2)
# tuple_one[0] = "eita" TypeError: 'tuple' object does not support item assignment
print(tuple_one)
print(tuple_one[0])

# Set
set_one = set(list_one)
print(set_one)

# Dict
dict_one = {3: "Monday", 2: "Tuesday", 4: "Wednesday"}
print(dict_one)


a = {(1, 2): "abc"}