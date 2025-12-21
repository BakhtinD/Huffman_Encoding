import time

import Efficiency_rating

codes = {}


def huffman_encode(freq_dict):
    main_dict = freq_dict.copy()
    encoded_dict = {symbol: "" for symbol in main_dict}

    step = 1
    while len(main_dict) > 1:
        print(f"\n--- Шаг {step} ---")
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


def shannon_fano_encode(dictionary, prefix=""):
    global codes
    if len(dictionary) == 1:
        symbol = list(dictionary.keys())[0]
        codes[symbol] = prefix
        return None

    else:
        sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
        freq_for_all_chars = sum(dictionary.values())
        middle_of_all_chars = freq_for_all_chars / 2
        print("middle: ", middle_of_all_chars)
        freq_sum = 0
        group1 = {}
        group2 = {}
        for symbol, freq in sorted_items:
            print("element: ", symbol, freq)
            if abs(freq_sum - middle_of_all_chars) > abs(freq_sum + freq - middle_of_all_chars) or len(group1) == 0:
                group1[symbol] = freq
                freq_sum += freq
            else:
                group2[symbol] = freq

    print("group1: ", group1)
    print("group2: ", group2)
    if len(group1) > 0:
        shannon_fano_encode(group1, prefix + "0")
    if len(group2) > 0:
        shannon_fano_encode(group2, prefix + "1")

    return codes


# frequency_dict = {" ": 0.145, "о": 0.095, "е": 0.074, "а": 0.065, "и": 0.063, "т": 0.057, "н": 0.055, "с": 0.047,
#                   "р": 0.041, "в": 0.039, "л": 0.036, "к": 0.029, "м": 0.027, "д": 0.025, "п": 0.024, "у": 0.021,
#                   "я": 0.019, "ы": 0.016, "б": 0.015, "з": 0.015, "ь": 0.015, "ъ": 0.015, "г": 0.014, "ч": 0.013,
#                   "й": 0.01, "х": 0.009, "ж": 0.008, "ю": 0.007, "ш": 0.006, "щ": 0.003, "э": 0.003, "ф": 0.002}
sentence = input("Введите текст:").lower()

freq_dict_for_sentence = Efficiency_rating.get_dict_with_frequencies_in_text(sentence)

# for char in sentence:
#     freq_dict_for_sentence[char] = frequency_dict.get(char, 0.001)

# print(frequency_dict)
print(freq_dict_for_sentence)
huffman_time = time.perf_counter()
huffman_result = huffman_encode(freq_dict_for_sentence)
huffman_time = time.perf_counter() - huffman_time
shannon_time = time.perf_counter()
shannon_fano_result = shannon_fano_encode(freq_dict_for_sentence)
shannon_time = time.perf_counter() - shannon_time
print("Время, за которое выполнилось кодирование Хаффмана:", huffman_time)
print("Время, за которое выполнилось кодирование Шеннона-Фано:", shannon_time)

print("\nФинальные коды Хаффмана:", huffman_result)
print("\nФинальные коды символов методом Шеннона-Фано :", shannon_fano_result)
print("Сжатое предложение Хаффмана: ", end="")
for c in sentence:
    print(huffman_result[c], end="")
print()
print("Сжатое предложение Шеннона-Фано: ", end="")
for c in sentence:
    print(shannon_fano_result[c], end="")
    # codes.clear()




# Efficiency_rating.analyze_coding_efficiency(sentence, huffman_result, shannon_fano_result, frequency_dict)
# print(Efficiency_rating.get_n(huffman_result, sentence))
# print(Efficiency_rating.get_n(shannon_fano_result, sentence))
Efficiency_rating.analyze_coding_efficiency(sentence, huffman_result, shannon_fano_result)
input()
