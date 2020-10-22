# Variables

## Swapping neighbors

File name: `swap_neighbors.py`

Please write a program that reads data separated by spaces from the keyboard. Then it prints the data, swapped pairwise (i.e. `data[0]` is swapped with `data[1]`, `data[2]` swapped with `data[3]`, etc.). If the number of data items is odd, the last item should remain in place.

Example:

    Enter the data: 1 2 3 4 5 6 7 8 9
    2 1 4 3 6 5 8 7 9


## Delete every third

File name: `remove3.py`

Please write a program that reads some text from the keyboard and then deletes every third character (starting with the third). The remaining characters should be printed on the screen.

Example:

    Enter text: To be or not to be...
    Tobeorno t b..


## The most frequent letter
File name: `most_frequent.py`

Please write a program that reads a line of text, and then prints the most frequent letter in it. The program should ignore case, and the most frequent letter should be capitalized. If there is more than one letter that appears most frequently, it is enough to print any of them. (for those of you who are ambitious: in such case, write down all the letters that appear most of the times, each in a separate line)

Example:

    Write the text: To be or not to be
    O

In the advanced version:

    Enter text: Abba
    A
    B

Tip: I suggest creating a dictionary that stores for each letter the number of its occurrences. The number of occurrences of a given letter can be found using the `count` method for a text string (please search for its documentation yourself).