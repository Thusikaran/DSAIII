# RABIN KARP

# Compute hash value
def compute_hash(pattern):
    hash_value = 0
    power = 0

    reversed_pattern = pattern[::-1]

    for char in reversed_pattern:
        hash_value += (127 ** power) * ord(char)
        power += 1

    return hash_value

# Sliding function
def rabin_karp(pattern, string):
    occurrences = []
    pattern_hash = compute_hash(pattern)
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length - pattern_length + 1):
        substring = string[i:i + pattern_length]
        if pattern_hash == compute_hash(substring):
            if pattern == substring:
                occurrences.append(i)
    return occurrences

pattern_input = input("Enter the pattern: ")
string_input = input("Enter the string: ")

# Handle |
if "|" in pattern_input:
    sub_patterns = pattern_input.split("|")

    pattern_dict = {}
    for sub_pattern in sub_patterns:
        pattern_dict[sub_pattern] = rabin_karp(sub_pattern, string_input)
    print(pattern_dict)

# Handle \b (word boundaries)
elif (pattern_input[:2] == "\\b") and (pattern_input[-2:] == "\\b"):
    print(rabin_karp(pattern_input[2:-2], string_input))

# Handle ^
elif pattern_input[0] == "^":
    matches = rabin_karp(pattern_input[1:], string_input)
    if 0 in matches:
        print(True)
    else:
        print(False)

# Handle $
elif pattern_input[-1] == "$":
    matches = rabin_karp(pattern_input[0:-1], string_input)
    if (len(string_input) - len(pattern_input[:-1])) in matches:
        print(True)
    else:
        print(False)
