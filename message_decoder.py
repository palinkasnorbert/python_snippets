"""
Part 3 - Coding Exercise: Decoding a Message from a Text File

In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

  1
 2 3
4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers

and your function should return the string "I love computers".
"""
"""
high level steps
- open and process the text file into a dictionary num:word pairs
X sort the dictionary by keys
- get line number from file
- create a function which builds the cipher-key staircase list
  - [[1], [2, 3], [4, 5, 6]]
- create a function which decodes the message by returning elements from the staircase list
  - get the last item of all element"""


code_dict = {
    3: "love",
    6: "computers",
    2: "dogs",
    4: "cats",
    1: "I",
    5: "you",
}

sorted_dict = dict(sorted(code_dict.items()))  # sort dict by keys

word_list = list(sorted_dict.values())  # create word list from sorted

message = " ".join([str(word) for word in word_list])  # create string message

step = 1
subsets = []

while len(word_list) != 0:  # while the word list is longer than 0
    if len(word_list) >= step:  # if the word list is longer than step
        subsets.append(
            word_list[0:step]
        )  # append word list items from 0 to step to subsets
        word_list = word_list[
            step:
        ]  # shorten the word list with slicing starting from step
        step += 1

print(word_list)
print(message)
print(subsets)
