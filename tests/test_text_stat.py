from main import text_stat
import pytest


@pytest.mark.parametrize("a, expected_result",
                         [(r'..\text_files\text.txt', {'a': (0.0, 0.0), 'b': (0.0, 0.0),
                                                    'c': (0.0, 0.0), 'd': (0.0, 0.0), 'e': (0.0, 0.0), 'f': (0.0, 0.0), 'g': (0.0, 0.0), 'h': (0.0, 0.0), 'i': (0.0, 0.0), 'j': (0.0, 0.0), 'k': (0.0, 0.0), 'l': (0.0, 0.0), 'm': (0.0, 0.0), 'n': (0.0, 0.0), 'o': (0.0, 0.0), 'p': (0.0, 0.0), 'q': (0.0, 0.0), 'r': (0.0, 0.0), 's': (0.0, 0.0), 't': (0.0, 0.0), 'u': (0.0, 0.0), 'v': (0.0, 0.0), 'w': (0.0, 0.0), 'x': (0.0, 0.0), 'y': (0.0, 0.0), 'z': (0.0, 0.0), 'а': (0.08955223880597014, 0.45), 'б': (0.014925373134328358, 0.1), 'в': (0.05223880597014925, 0.35), 'г': (0.007462686567164179, 0.05), 'д': (0.007462686567164179, 0.05), 'е': (0.09701492537313433, 0.5), 'ё': (0.0, 0.0), 'ж': (0.014925373134328358, 0.1), 'з': (0.029850746268656716, 0.2), 'и': (0.11194029850746269, 0.55), 'й': (0.014925373134328358, 0.1), 'к': (0.03731343283582089, 0.25), 'л': (0.014925373134328358, 0.1), 'м': (0.014925373134328358, 0.1), 'н': (0.09701492537313433, 0.45), 'о': (0.07462686567164178, 0.4), 'п': (0.022388059701492536, 0.15), 'р': (0.022388059701492536, 0.15), 'с': (0.05223880597014925, 0.25), 'т': (0.1044776119402985, 0.5), 'у': (0.014925373134328358, 0.1), 'ф': (0.0, 0.0), 'х': (0.007462686567164179, 0.05), 'ц': (0.014925373134328358, 0.1), 'ч': (0.014925373134328358, 0.1), 'ш': (0.0, 0.0), 'щ': (0.0, 0.0), 'ь': (0.007462686567164179, 0.05), 'ы': (0.03731343283582089, 0.25), 'ъ': (0.0, 0.0), 'э': (0.0, 0.0), 'ю': (0.007462686567164179, 0.05), 'я': (0.014925373134328358, 0.1),
                                                                             'word_amount': 20, 'paragraph_amount': 1, 'bilingual_word_amount': 0}),
                          (r'..\text_files\text_a.txt', {'a': (0.05333333333333334, 0.24),
                                                     'b': (0.0, 0.0), 'c': (0.04666666666666667, 0.2), 'd': (0.02666666666666667, 0.16), 'e': (0.16666666666666666, 0.64), 'f': (0.0, 0.0), 'g': (0.02, 0.12), 'h': (0.0, 0.0), 'i': (0.08666666666666667, 0.44), 'j': (0.006666666666666667, 0.04), 'k': (0.0, 0.0), 'l': (0.04, 0.2), 'm': (0.02666666666666667, 0.16), 'n': (0.08666666666666667, 0.4), 'o': (0.04666666666666667, 0.28), 'p': (0.02666666666666667, 0.16), 'q': (0.006666666666666667, 0.04), 'r': (0.06666666666666667, 0.36), 's': (0.08666666666666667, 0.44), 't': (0.12, 0.6), 'u': (0.07333333333333333, 0.36), 'v': (0.013333333333333334, 0.08), 'w': (0.0, 0.0), 'x': (0.0, 0.0), 'y': (0.0, 0.0), 'z': (0.0, 0.0), 'а': (0.0, 0.0), 'б': (0.0, 0.0), 'в': (0.0, 0.0), 'г': (0.0, 0.0), 'д': (0.0, 0.0), 'е': (0.0, 0.0), 'ё': (0.0, 0.0), 'ж': (0.0, 0.0), 'з': (0.0, 0.0), 'и': (0.0, 0.0), 'й': (0.0, 0.0), 'к': (0.0, 0.0), 'л': (0.0, 0.0), 'м': (0.0, 0.0), 'н': (0.0, 0.0), 'о': (0.0, 0.0), 'п': (0.0, 0.0), 'р': (0.0, 0.0), 'с': (0.0, 0.0), 'т': (0.0, 0.0), 'у': (0.0, 0.0), 'ф': (0.0, 0.0), 'х': (0.0, 0.0), 'ц': (0.0, 0.0), 'ч': (0.0, 0.0), 'ш': (0.0, 0.0), 'щ': (0.0, 0.0), 'ь': (0.0, 0.0), 'ы': (0.0, 0.0), 'ъ': (0.0, 0.0), 'э': (0.0, 0.0), 'ю': (0.0, 0.0), 'я': (0.0, 0.0),
                                                                               'word_amount': 25, 'paragraph_amount': 1, 'bilingual_word_amount': 0}),
                          (r'..\text_files\text_b.txt', {'a': (0.044270833333333336,
                                                           0.208955223880597), 'b': (0.0078125, 0.04477611940298507), 'c': (0.026041666666666668, 0.14925373134328357), 'd': (0.033854166666666664, 0.19402985074626866), 'e': (0.07552083333333333, 0.3880597014925373), 'f': (0.0026041666666666665, 0.014925373134328358), 'g': (0.015625, 0.08955223880597014), 'h': (0.0, 0.0), 'i': (0.07291666666666667, 0.29850746268656714), 'j': (0.0078125, 0.04477611940298507), 'k': (0.0, 0.0), 'l': (0.033854166666666664, 0.19402985074626866), 'm': (0.026041666666666668, 0.14925373134328357), 'n': (0.033854166666666664, 0.1791044776119403), 'o': (0.026041666666666668, 0.11940298507462686), 'p': (0.018229166666666668, 0.1044776119402985), 'q': (0.0, 0.0), 'r': (0.018229166666666668, 0.08955223880597014), 's': (0.044270833333333336, 0.2537313432835821), 't': (0.059895833333333336, 0.29850746268656714), 'u': (0.08072916666666667, 0.34328358208955223), 'v': (0.015625, 0.08955223880597014), 'w': (0.0, 0.0), 'x': (0.0026041666666666665, 0.014925373134328358), 'y': (0.0, 0.0), 'z': (0.0, 0.0), 'а': (0.010416666666666666, 0.04477611940298507), 'б': (0.005208333333333333, 0.029850746268656716), 'в': (0.0234375, 0.13432835820895522), 'г': (0.015625, 0.05970149253731343), 'д': (0.0, 0.0), 'е': (0.015625, 0.07462686567164178), 'ё': (0.0, 0.0), 'ж': (0.0, 0.0), 'з': (0.0026041666666666665, 0.014925373134328358), 'и': (0.03125, 0.13432835820895522), 'й': (0.0078125, 0.04477611940298507), 'к': (0.005208333333333333, 0.029850746268656716), 'л': (0.010416666666666666, 0.05970149253731343), 'м': (0.0, 0.0), 'н': (0.026041666666666668, 0.1044776119402985), 'о': (0.059895833333333336, 0.23880597014925373), 'п': (0.010416666666666666, 0.05970149253731343), 'р': (0.026041666666666668, 0.11940298507462686), 'с': (0.033854166666666664, 0.14925373134328357), 'т': (0.03125, 0.13432835820895522), 'у': (0.0078125, 0.04477611940298507), 'ф': (0.0, 0.0), 'х': (0.0, 0.0), 'ц': (0.0026041666666666665, 0.014925373134328358), 'ч': (0.0026041666666666665, 0.014925373134328358), 'ш': (0.0026041666666666665, 0.014925373134328358), 'щ': (0.0026041666666666665, 0.014925373134328358), 'ь': (0.0078125, 0.04477611940298507), 'ы': (0.0078125, 0.04477611940298507), 'ъ': (0.0, 0.0), 'э': (0.0, 0.0), 'ю': (0.0026041666666666665, 0.014925373134328358), 'я': (0.0026041666666666665, 0.014925373134328358),
                                                                               'word_amount': 67, 'paragraph_amount': 3, 'bilingual_word_amount': 4}),
                          (5, {"error": "Некорректное имя файла"}),
                          (r'..\text_files\text_c.txt', {"error": "Некорректное имя "
                                                               "файла"})])
def test_prime_numbers(a, expected_result):
    assert text_stat(a) == expected_result