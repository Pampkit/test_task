import re
import os


# first

def prime_numbers(low, high):
    if not (isinstance(low, int)) or not (
            isinstance(high, int)):
        return []
    if low > high or low < 0 or high < 0:
        return []
    a = []
    for num in range(low, high + 1):
        check = 0
        if num != 1:
            for i in range(2, num + 1):
                if num % i == 0:
                    check += 1
            if check == 1:
                a.append(num)
    return a


# third

def roman_numerals_to_int(roman_numeral):
    if not (isinstance(roman_numeral, str)):
        return None
    pattern = re.compile(r"""
                                    ^M{0,3}
                                    (CM|CD|D?C{0,3})?
                                    (XC|XL|L?X{0,3})?
                                    (IX|IV|V?I{0,3})?$
                """, re.VERBOSE)

    R_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_numeral:
        if i not in R_list.keys() or not (re.match(pattern, roman_numeral)):
            return None
    last_simv = roman_numeral[-1]
    result = R_list[last_simv]
    check_si = 0
    for i in roman_numeral[-2::-1]:
        if R_list[i] >= R_list[last_simv]:
            result += R_list[i]
        else:
            check_si += 1
            result -= R_list[i]
        last_simv = i
    return result


# second

def text_stat(filename):
    if not (isinstance(filename, str)) or not (
            os.path.exists(filename)):  # Проверка данных
        return {"error": "Некорректное имя файла"}
    mn_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mn_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
             'о', 'п',
             'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю',
             'я']
    mn_all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'а', 'б', 'в', 'г',
              'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
              'о', 'п',
              'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю',
              'я']

    with open(filename, "r", encoding='utf-8') \
            as f:
        count_letter = 0
        text = f.read()
        text = re.sub(r"[#%!@*-]", "", text).lower()
        dict_letter = {i: text.count(i) for i in mn_all}
        for i in text:
            if i in mn_all:
                count_letter += 1

        list_words = list(map(str, text.split()))
        count_words = len(list_words)
        dict_count_words = {'word_amount': count_words}
        tes = []
        for i in mn_all:
            count_let_word = 0
            for j in list_words:
                if j.count(i) > 0:
                    count_let_word += 1
            tes.append((dict_letter.get(i) / count_letter, count_let_word / count_words))

        dict_frequency_letter = {mn_all[i]: tes[i] for i in
                                 range(len(mn_all))}

        count_paragraph = text.count('\n\n') + 1
        dict_count_paragraph = {'paragraph_amount': count_paragraph}

        count_multy_words = 0
        for i in list_words:
            if len(set(i) & set(mn_en)) > 0 and len(set(i) & set(mn_ru)) > 0:
                count_multy_words += 1

        bilingual_word_amount = {'bilingual_word_amount': count_multy_words}

        finish_dict = {**dict_frequency_letter, **dict_count_words,
                       **dict_count_paragraph, **bilingual_word_amount}
        return finish_dict
