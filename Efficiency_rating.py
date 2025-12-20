import math


def calculate_entropy(sentence):
    """
    Простой расчет энтропии Шеннона.

    Формула: H = -Σ p(i) * log₂(p(i))
    где p(i) - вероятность i-го символа
    """
    freq_dict = get_dict_with_frequencies_in_text(sentence)
    entropy = 0
    for prob in freq_dict.values():
        if prob > 0:
            entropy = entropy + prob * math.log2(prob)
    return entropy * -1


def get_n(dictionary_with_frequencies, text):
    dict_with_chars = get_dict_with_frequencies_in_text(text)

    print()
    print(dict_with_chars)

    result = 0
    for k, v in dict_with_chars.items():
        for item, value in dictionary_with_frequencies.items():
            if k == item:
                result = result + (len(value) * v)

    return result


def get_dict_with_frequencies_in_text(text):
    dict_with_chars = {}

    len1 = len(text)
    for i in range(0, len1):
        dict_with_chars[text[i]] = dict_with_chars.get(text[i], 0) + 1

    excluded_chars = []
    for i in range(0, len1):
        if text[i] not in excluded_chars:
            dict_with_chars[text[i]] = dict_with_chars.get(text[i]) / len1
            excluded_chars.append(text[i])
    return dict_with_chars


def analyze_coding_efficiency(sentence, huffman_codes, shannon_codes):
    entropy = calculate_entropy(sentence)

    huffman_avg_len = get_n(huffman_codes, sentence)
    shannon_avg_len = get_n(shannon_codes, sentence)

    print("\n" + "=" * 60)
    print("АНАЛИЗ ЭФФЕКТИВНОСТИ КОДИРОВАНИЯ")
    print("=" * 60)
    print(f"Энтропия текста: {entropy:.4f} бит/символ")
    print(f"\nСредняя длина кода:")
    print(f"  Хаффман: {huffman_avg_len:.4f} бит/символ")
    print(f"  Шеннон-Фано: {shannon_avg_len:.4f} бит/символ")
    print("Информация на один элементарный символ для алгоритма Хаффмана -", entropy/huffman_avg_len, "из 1")
    print("Информация на один элементарный символ для алгоритма Шеннона-Фано -", entropy/shannon_avg_len, "из 1")
