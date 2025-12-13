import math


def calculate_entropy(freq_dict):
    """
    Простой расчет энтропии Шеннона.

    Формула: H = -Σ p(i) * log₂(p(i))
    где p(i) - вероятность i-го символа
    """
    entropy = 0
    for prob in freq_dict.values():
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy


def calculate_average_code_length(code_dict, freq_dict):
    """
    Расчет средней длины кода.

    Формула: L = Σ p(i) * l(i)
    где p(i) - вероятность, l(i) - длина кода
    """
    avg_length = 0
    for symbol, code in code_dict.items():
        if symbol in freq_dict:
            avg_length += freq_dict[symbol] * len(code)
    return avg_length


# Пример использования в вашей программе:
def analyze_coding_efficiency(sentence, huffman_codes, shannon_codes, freq_dict):
    entropy = calculate_entropy(freq_dict)

    huffman_avg_len = calculate_average_code_length(huffman_codes, freq_dict)
    shannon_avg_len = calculate_average_code_length(shannon_codes, freq_dict)


    print("\n" + "=" * 60)
    print("АНАЛИЗ ЭФФЕКТИВНОСТИ КОДИРОВАНИЯ")
    print("=" * 60)
    print(f"Энтропия текста: {entropy:.4f} бит/символ")
    print(f"\nСредняя длина кода:")
    print(f"  Хаффман: {huffman_avg_len:.4f} бит/символ")
    print(f"  Шеннон-Фано: {shannon_avg_len:.4f} бит/символ")

