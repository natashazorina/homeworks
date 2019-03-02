words = "мама папа мама папа мама мама"
word_list = words.split()

from collections import defaultdict
word_count_dict = defaultdict(int)

for word in word_list:
    word_count_dict[word] += 1
    if word_count_dict[word] > 3:
        print(word)
        word_count_dict[word] = -1000000
