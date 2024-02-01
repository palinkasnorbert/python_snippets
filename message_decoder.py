"""
Part 3 - Coding Exercise: Decoding a Message from a Text File

In this exercise, you will develop a function named decode(message_file). This function should read an encoded
message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible,
but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the
arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

  1
 2 3
4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in
this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message
words are:

1: I
3: love
6: computers

and your function should return the string "I love computers".

high level steps
- open and process the text file into a dictionary num:word pairs
- get line number from file
X sort the dictionary by keys
X create a function which builds the cipher-key staircase list -> group_words()
    - [[1], [2, 3], [4, 5, 6]]
X create a function which decodes the message by returning elements from the staircase list
    X get the last item of all element
    X print out message as string space separated
    # message = " ".join([str(word) for word in word_list])  # create string message
"""

word_dict = {
    3: "love",
    6: "computers",
    2: "dogs",
    4: "cats",
    1: "I",
    5: "you",
    9: "land",
    8: "sun",
    7: "too",
    11: "huge",
    13: "such",
    12: "noun",
    10: "student",
    15: 42,
    14: "complete",
    16: "play",
    17: "cook"
}


def sort_group_words(code_dict: dict) -> list:
    sorted_dict = dict(sorted(code_dict.items()))  # sort dict by keys

    word_list = list(sorted_dict.values())  # create word list from sorted

    step = 1    # set step counter
    subsets = []    # init subsets list

    while len(word_list) != 0:  # while the word list is longer than 0
        if len(word_list) >= step:  # if the word list is longer than step
            subsets.append(
                word_list[0:step]
            )  # append word list items from 0 to step to subsets
            word_list = word_list[step:]  # shorten the word list with slicing starting from step until end
            step += 1   # add 1 to the counter
        else:
            subsets.append(word_list[0:step])
            word_list = []
    return subsets

def print_message():
    final_message = " ".join(str(item[-1]) for item in sort_group_words(word_dict))
    print(final_message)

'''
# Step by step logic building: from loops to list comprehensions. #

### First version: lists & loops ###

raw_message = []

for item in group_words(word_dict): # get every last list item from the function result
    raw_message.append(item[-1])    # append them to the raw_message list

message = []

for word in raw_message:        # convert every word in the raw_message list to string
    message.append(str(word))   # append them to the message list

final_message = " ".join(message)   # join message list items together to get a string

### Second version: list comprehensions ###

raw_message = [item[-1] for item in group_words(word_dict)]

message = [str(word) for word in raw_message]

final_message = " ".join(message)

### Third version: using only one list comprehension for all the steps ###

final_message = " ".join(str(item[-1]) for item in sort_group_words(word_dict))
'''

print_message()