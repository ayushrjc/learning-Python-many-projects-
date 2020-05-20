import re
text = input("Enter any text")

# qsn1
print(re.findall(r'\b\w{5}\b',text))

# qsn2
print(re.findall(r'\b[A-Z][a-z]*\b',text))


# qsn3
print(re.findall(r'^[a-zA-Z0-9_]*$',text))


# qsn4
with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

# qsn 5
def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_words('about.txt'))

