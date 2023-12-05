def find_word_occurrence_index(input_string, target_word):
    words = input_string.split()
    index = -1
    occurrence_count = 0
    
    for i, word in enumerate(words):
        if word == target_word:
            if occurrence_count == 0:
                index = i
            occurrence_count += 1
    
    return index

# Example usage
input_string = "This is a test string. This string is just a test."
target_word = "string"
index = find_word_occurrence_index(input_string, target_word)

if index != -1:
    print(f"The index of the occurrence of '{target_word}' is: {index}")
else:
    print(f"'{target_word}' was not found in the string.")
