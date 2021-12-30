# In this exercise, the user is prompted for a file name (mbox.txt) and the file is read line by line.
# PREPROCESSING:
# For each line, a first filter is used to reject lines of no interest.
# Lines of interest are analyzed/parsed to extract number data.
# The number data (string) is transformed to type float and stored in a var "span_conf".
# PROCESSING:
# A variable that contains the running sum of spam_conf is updated in each iteration.
#RESULTS:
# The final spam_conf is divided by the number of iterations (count) to find the avg_spam_conf.