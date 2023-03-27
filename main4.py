

def consensus_sequence(l: list):
    """
    Составляет консенсус-строку из N строк одиннаковой длины.
    :param l: Лист строк одиннаковой длины
    :return: консенсус-строка
    """
    final_sequence = ''
    list_length = len(l)
    seq_length = len(l[0])
    # print(seq_length, 'длина строки')   # print sequence length

    # checking string length
    for i in l:
        if len(i) != seq_length:
            raise ValueError("different sequence length")
    # проверяем какой символ встречается чаще всего и добавляем его в финальную строку
    for char in range(seq_length):
        temp_dict = {}
        for seq in l:
            # print(seq[char])
            if seq[char] not in temp_dict:
                temp_dict[seq[char]] = 1
            else:
                temp_dict[seq[char]] += 1
        # print(temp_dict, 'final temp_dict. let\'s check max')
        # print(max(temp_dict), 'max in temp_dict')

        max_frequent = max(temp_dict.values())
        max_frequent_key = [k for k, v in temp_dict.items() if v == max_frequent]
        max_frequent_key = min(max_frequent_key)

        # print(max_frequent_key, 'most frequent key is')
        final_sequence += max_frequent_key

    print(final_sequence)
    return final_sequence

l = [
    'ATTA',
    'ACTA',
    'AGCA',
    'ACAA'
]

consensus_sequence(l)