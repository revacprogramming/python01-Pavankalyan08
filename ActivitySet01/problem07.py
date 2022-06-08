# Strings
text = "X-DSPAM-Confidence:    0.8475"
index=text.find(" ")
edf=text[index+4:]
print(edf)
