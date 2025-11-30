def huffman_encoding_debug(freq_dict):
    main_dict = freq_dict.copy()
    encoded_dict = {symbol: "" for symbol in main_dict}

    step = 1
    while len(main_dict) > 1:
        print(f"\n--- Шаг {step} ---")
        sorted_items = sorted(main_dict.items(), key=lambda item: item[1])
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


frequency_dict = {"a": 15, "b": 7, "c": 6, "d": 6, "e": 5}
result = huffman_encoding_debug(frequency_dict)
print("\nФинальные коды:", result)