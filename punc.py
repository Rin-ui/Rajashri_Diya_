str1 = "hello, we are Diya and Rajashri."

punctuation = [',', '.', '@']

# Split the string into words
res = str1.split()

cleaned_res = []

# Remove punctuation from each word
for word in res:
    for char in punctuation:
        word = word.replace(char, '')
    cleaned_res.append(word)

# Join the cleaned words back into a single string
cleaned_str = ' '.join(cleaned_res)

print(cleaned_str)
