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
    Transcribes DNA sequences into RNA.

    Arguments:
    nk_str -- a list of strings containing DNA or RNA sequences.

    Returns:
    A list of strings containing RNA sequences.
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
    Returns the reversed sequences of DNA or RNA.

    Arguments:
    nk_str -- a list of strings containing DNA or RNA sequences.

    Returns:
    A list of strings containing the reversed DNA or RNA sequences.
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
    Returns the complementary sequences of DNA or RNA.

    Arguments:
    nk_str -- a list of strings containing DNA or RNA sequences.

    Returns:
    A list of strings containing the complementary sequences.
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
                return "Invalid sequence: contains 'T' and 'U'"

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
    Returns the reversed complementary sequences of DNA or RNA.

    Arguments:
    nk_str -- a list of strings containing DNA or RNA sequences.

    Returns:
    A list of strings containing the reversed complementary sequences.
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
            return "Invalid sequence: contains both 'T' and 'U'"

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
