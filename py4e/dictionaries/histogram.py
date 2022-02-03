# Exercise 1, p147
import string

# create an empty dictionary, words_histogram:
words_hist = {}

with open('words.txt') as f:
    line = 'text'
    while line:
        line = f.readline()
        # strip spaces from both sides and make all letters lowercase:
        line = line.strip().lower()
        # eliminate punctuations:

        print(repr(line))
        # make a list with all the words in the line
        # for every word in the list:
        # put in words_histogram

# show the histogram, printing each key and its value in different lines.