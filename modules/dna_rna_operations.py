# Создадим словари комплементарности

dna_complenent_dict = {
    "A": "T",
    "a": "t",
    "T": "A",
    "t": "a",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g"
}

rna_complenent_dict = {
    "A": "U",
    "a": "u",
    "U": "A",
    "u": "a",
    "G": "C",
    "g": "c",
    "C": "G",
    "c": "g"
}


# Функция транскрипции - меняет в T на U

def transcribe(nk_str: list[str]) -> list[str]:
    """
    Транскрибирует последовательности ДНК в РНК.

    Аргументы:
    nk_str -- список строк с последовательностями ДНК или РНК.

    Возвращает:
    Список строк с последовательностями РНК.
    """
    # Если у нас на вход подается список с одной строкой
    # то вынесем эту строку в новую переменную
    if len(nk_str) == 1:
        one_string = nk_str[0]
        # Заменим основания методом строк .replace()
        trans_rna = one_string.replace("T", "U").replace("t", "u")
        return trans_rna
    else:
        # Заменим основания в списке методом строк .replace()
        trans_rna = [nk.replace("T", "U").replace("t", "u") for nk in nk_str]
        return trans_rna


# Функция, которая разворачивает последовательность
def reverse(nk_str: list[str]) -> list[str]:
    """
    Возвращает развернутую последовательности ДНК или РНК.

    Аргументы:
    nk_str -- список строк с последовательностями ДНК или РНК.

    Возвращает:
    Список строк с развернутыми последовательностями ДНК или РНК.
    """
    if len(nk_str) == 1:
        one_string = nk_str[0]
        transcript_rna = one_string[::-1]
        return transcript_rna
    else:
        transcript_rna = [nk[::-1] for nk in nk_str]
        return transcript_rna


# Функция, которая возвращает комплементарную последовательность
def complement(nk_str: list[str]) -> list[str]:
    """
    Возвращает комплементарные последовательности ДНК или РНК.

    Аргументы:
    nk_str -- список строк с последовательностями ДНК или РНК.

    Возвращает:
    Список строк с комплементарными последовательностями.
    """

    if len(nk_str) == 1:
        for nk in nk_str:
            if "T" in nk or "t" in nk:
                comp_seq = "".join(dna_complenent_dict.get(n, n) for n in nk)
            elif "U" in nk or "u" in nk:
                comp_seq = "".join(rna_complenent_dict.get(n, n) for n in nk)
            return comp_seq
    # Если передан список строк
    else:
        comp_seqs = []

        for nk in nk_str:
            if 'T' in nk.upper() and 'U' in nk.upper():
                return "Некорректная последовательность: содержит 'T' и 'U'"

            # Определение комплементарной последовательности
            if "T" in nk or "t" in nk:
                comp_seq = "".join(dna_complenent_dict.get(n, n) for n in nk)
                comp_seqs.append(comp_seq)
            elif "U" in nk or "u" in nk:
                comp_seq = "".join(rna_complenent_dict.get(n, n) for n in nk)
                comp_seqs.append(comp_seq)  # Добавляем результат в список

        return comp_seqs


# Функция, которая возвращает комплементарную последовательность
# и разворачивает ее
def reverse_complement(nk_str: list[str]) -> list[str]:
    """
    Возвращает развернутые комплементарные последовательности ДНК или РНК.

    Аргументы:
    nk_str -- список строк с последовательностями ДНК или РНК.

    Возвращает:
    Список строк с развернутыми комплементарными последовательностями.
    """
    if len(nk_str) == 1:
        for nk in nk_str:
            if "T" in nk or "t" in nk:
                comp_seq = "".join(dna_complenent_dict.get(n, n) for n in nk)
            elif "U" in nk or "u" in nk:
                comp_seq = "".join(rna_complenent_dict.get(n, n) for n in nk)
            return comp_seq[::-1]
    else:

        comp_seqs = []

        if 'T' in nk.upper() and 'U' in nk.upper():
            return "Некорректная последовательность: содержит как 'T'и 'U'"

        for nk in nk_str:
            if "T" in nk or "t" in nk:
                comp_seq = "".join(dna_complenent_dict.get(n, n) for n in nk)
                reverse_seq = comp_seq[::-1]
                comp_seqs.append(reverse_seq)
            elif "U" in nk or "u" in nk:
                comp_seq = "".join(rna_complenent_dict.get(n, n) for n in nk)
                reverse_seq = comp_seq[::-1]
                comp_seqs.append(reverse_seq)

        return comp_seqs
