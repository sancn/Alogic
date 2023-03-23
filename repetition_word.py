# string=input("Enter the string,to count repetition of words: ")
# repeat_count=0

# for i in string:
#     if i in string:
#         repeat_count +=1
#     else:
#         repeat_count=1
# print(repeat_count)



# word_list = string.split()

# word_repet = {}

# for word in word_list:
#     if word in word_repet:
#         word_repet[word] += 1
#     else:
#         word_repet[word] = 1

# max_count = max(word_repet.values())

# print("Maximum repetition count: ", max_count)


# def max_repetition(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     max_count = 0
#     max_char = ''
#     for char, count in char_count.items():
#         if count > max_count:
#             max_count = count
#             max_char = char
#     return max_char, max_count


# char_count = {}
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# max_count = 0
# for count in char_count.values():
#     if count > max_count:
#         max_count = count


string=input("Enter the string,to count repetition of words: ")

char_count = {}
for char in string:
#     char_count.setdefault(char, 0)
#     char_count[char] += 1

# max_count = max(char_count.values())



    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

    max_count = 0
    for count in char_count.values():
        if count > max_count:
            max_count = count
print(f"Maximum repetition of a character in:{string} is :", max_count)
