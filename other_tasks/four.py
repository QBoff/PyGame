class PasswordError(Exception):
    pass


class LetterError(PasswordError):
    pass


class LengthError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


excombos = ['qwertyuiop', 'asdfghjkl',
            'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю'
                                                       'qwertyuiop'[
                                                           ::-1], 'asdfghjkl'[::-1],
            'zxcvbnm'[::-1], 'йцукенгшщзхъ'[::-
                                                           1], 'фывапролджэё'[::-1], 'ячсмитьбю'[::-1]
            ]

mwords = [i for i in open("top-9999-words.txt", mode="r",
                          encoding="utf-8").read().split()]

test_passwords = [i for i in open(
    "top 10000 passwd.txt", mode="r", encoding="utf-8").read().split()]


def check_excombos(ps):
    for combo in excombos:
        for j in range(len(combo) - 2):
            if combo[j: j + 3] in ps.lower():
                raise SequenceError


def check_mwords(ps):
    for combo in mwords:
        if combo in ps:
            raise WordError


def check_len(ps):
    if len(ps) <= 8:
        raise LengthError


def check_small_and_big(ps):
    kol_alpha = 0
    kol_small = 0
    for i in ps:
        if i.isupper():
            kol_alpha += 1
        if i.islower():
            kol_small += 1
    if kol_small >= 1 and kol_alpha >= 1:
        pass
    else:
        raise LetterError


def check_digits(ps):
    kol_nums = 0
    for i in ps:
        if i in "1234567890":
            kol_nums += 1
    if kol_nums >= 1:
        pass
    else:
        raise DigitError


RESL = {"DigitError": 0,
        "LengthError": 0,
        "LetterError": 0,
        "SequenceError": 0,
        "WordError": 0}

"""
если пароль не соответствует
нескольким критериям одновременно
лично я буду добавлять его во все ошибки которым он не соответсвет.
"""

for psf in test_passwords:
    try:
        check_excombos(psf)
    except SequenceError:
        RESL["SequenceError"] += 1

    try:
        check_len(psf)
    except LengthError:
        RESL["LengthError"] += 1

    try:
        check_mwords(psf)
    except WordError:
        RESL["WordError"] += 1

    try:
        check_small_and_big(psf)
    except LetterError:
        RESL["LetterError"] += 1

    try:
        check_digits(psf)
    except DigitError:
        RESL["DigitError"] += 1

for i in RESL:
    print(i, "-", RESL[i])
