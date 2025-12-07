def huffman_encoding_debug(freq_dict):
    main_dict = freq_dict.copy()
    encoded_dict = {symbol: "" for symbol in main_dict}

    step = 1
    while len(main_dict) > 1:
        print(f"\n--- Шаг {step} ---")
        # sorted_items = sorted(main_dict.items(), key=lambda item: item[1])
        sorted_items = sorted(main_dict.items(), key=lambda item: (item[1], tuple(-ord(c) for c in item[0])))
        print("Отсортированные элементы:", sorted_items)

        first_key, first_freq = sorted_items[0]
        second_key, second_freq = sorted_items[1]
        print(f"Объединяем: '{first_key}'({first_freq}) и '{second_key}'({second_freq})")

        for char in first_key:
            encoded_dict[char] = "1" + encoded_dict[char]
        for char in second_key:
            encoded_dict[char] = "0" + encoded_dict[char]

        new_key = first_key + second_key
        new_freq = first_freq + second_freq
        main_dict[new_key] = new_freq
        del main_dict[first_key]
        del main_dict[second_key]

        print("Текущие коды:", {k: v for k, v in encoded_dict.items() if k in freq_dict})
        print("Текущие узлы с вероятностями:", main_dict)
        step += 1

    final_dict = {symbol: encoded_dict[symbol] for symbol in freq_dict}
    return final_dict


# frequency_dict = {"a": 15, "b": 7, "c": 6, "d": 6, "e": 5}
frequency_dict = {" ": 0.145, "о": 0.095, "е": 0.074, "а": 0.065, "и": 0.063, "т": 0.057, "н": 0.055, "c": 0.047,
                  "р": 0.041, "в": 0.039, "л": 0.036, "к": 0.029, "м": 0.027, "д": 0.025, "п": 0.024, "у": 0.021,
                  "я": 0.019, "ы": 0.016, "б": 0.015, "з": 0.015, "ь": 0.015, "ъ": 0.015,  "г": 0.014, "ч": 0.013,
                  "й": 0.01, "х": 0.009, "ж": 0.008, "ю": 0.007, "ш": 0.006, "щ": 0.003, "э": 0.003, "ф": 0.002}
sentence = input("Введите текст:").lower()
# for char in sentence:
#     char_frequency = frequency_dict.get(char)
#     if isinstance(char_frequency, int):
#         frequency_dict[char] = char_frequency + 1
#     else:
#         frequency_dict[char] = 1

freq_dict_for_sentence = {}

for char in sentence:
    freq_dict_for_sentence[char] = frequency_dict.get(char)

print(freq_dict_for_sentence)

result = huffman_encoding_debug(freq_dict_for_sentence)
print("\nФинальные коды:", result)
print("Сжатое предложение: ", end="")
for c in sentence:
    print(result[c], end="")

input()
