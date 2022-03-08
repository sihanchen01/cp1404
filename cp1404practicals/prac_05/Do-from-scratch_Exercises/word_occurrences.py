user_input_string = input("Enter a string: ")
while user_input_string != "":
    word_counts = {}
    user_input_list = user_input_string.split()
    for word in user_input_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    print(f"Text: {user_input_string}")
    sorted_word_counts = {k: v for k, v in sorted(
        word_counts.items(), key=lambda item: item[0])}
    longest_len = max([len(k) for k in word_counts.keys()])
    for word, counts in sorted_word_counts.items():
        print(f"{word:{longest_len + 1}}: {counts}")
    print()
    user_input_string = input("Enter a string: ")
