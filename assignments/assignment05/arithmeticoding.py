import numpy as np

# Input string
s = 'Ranvijay'
print(f'The entered string is: {s}')

# Length of the string
length = len(s)
print(f'The length of the string is: {length}')

# Get unique characters from the string
unique_chars = sorted(set(s))
print(f'The unique characters are: {"".join(unique_chars)}')

# Length of the unique characters string
len_unique = len(unique_chars)
print(f'The length of unique character string is: {len_unique}')

# General lookup table

# Get zeros of length of unique characters
z = np.zeros(len_unique, dtype=int)
p = np.zeros(len_unique)

for i in range(len_unique):
    # Count occurrences of each character
    z[i] = s.count(unique_chars[i])

    # Probability of those occurrences
    p[i] = z[i] / length

print('Occurrences:', z)
print('Probabilities:', p)

# Cumulative sum of probabilities
cpr = np.cumsum(p)

newcpr = np.concatenate(([0], cpr))

print('Cumulative probabilities:', cpr)
print('New cumulative probabilities:', newcpr)

# Creating the interval lookup table
interval = np.zeros((len_unique, 2))

for i in range(len_unique):
    interval[i, 0] = newcpr[i]
    interval[i, 1] = cpr[i]

print('The lookup table is:')
print(interval)

# Encoder Table
low = 0.0
high = 1.0

for i in range(length):
    for j in range(len_unique):
        # If the character matches
        if s[i] == unique_chars[j]:
            pos = j
            print(f'Matched character at position: {pos + 1}')

            # Calculate the tag value
            range_val = high - low
            high = low + (range_val * interval[pos, 1])
            low = low + (range_val * interval[pos, 0])
            break

# Displaying tag value
tag = low
print(f'Tag value: {tag}')
