my_str = "X-DSPAM-Confidence:0.8475"
# find the indexes corresponding to the number-part of the string:
i = my_str.find(":")
# Use slicing to extract the number-part:
num_part = my_str[i+1:]
# Use the float function to convert to floating point number:
num_part = float(num_part)
