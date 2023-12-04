#Explanation:
#To implement a string compression method in Python, we can use the following algorithm:

#Initialize an empty string compressed and a variable count to 1.
#Traverse the input string character by character.
#If the current character is the same as the previous character, increment the count variable.
#If the current character is different from the previous character, append the previous character and its count to the compressed_string.
#Reset the count variable to 1.
#Append the last character and its count to the compressed_string.
#Return the compressed_string.


def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))

    compressed_string = ''.join(compressed)

    # Return the original string if the compressed string is not shorter
    return compressed_string if len(compressed_string) < len(s) else s

# Example usage:
original_string = 'aabcccccaaa'
compressed_string = compress_string(original_string)
print("Original String:", original_string)
print("Compressed String:", compressed_string)
