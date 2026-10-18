s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."

# Find the length of each string
s1_chars = len(s1)
s2_chars = len(s2)
s3_chars = len(s3)

# Find total length of the three strings
total_chars = s1_chars + s2_chars + s3_chars

print("Total characters in string s1, s2 and s3 are {} characters".format(total_chars))

# Use split() to split each string by space to find number of words in each string
s1_words = s1.split()
s2_words = s2.split()
s3_words = s3.split()

# Find total number of words in the three strings
total_words = len(s1_words) + len(s2_words) + len(s3_words)

print("Total words in string s1, s2 and s3 are {} words".format(total_words))

# Remove space in the string
s2_wo_spaces = s2.replace(" ", "")
s3_wo_spaces = s3.replace(" ", "")

# Find the secret code
secret_code = (
    s1[-20]
    + s1[-3]
    + s1[-81]
    + s2_wo_spaces[43]
    + s2_wo_spaces[3]
    + s3_wo_spaces[-31]
    + s3_wo_spaces[-9]
)
print("The secret code is {}".format(secret_code))
