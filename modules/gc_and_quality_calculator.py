# GC-состав

def calculate_gc_content(sequence: str) -> float:
    """
    Вычисляет процент содержания GC в последовательности.

    Аргументы:
    sequence -- строка с последовательностью ДНК или РНК.

    Возвращает:
    Процент содержания GC в последовательности (float).
    """
    g_count = sequence.count("C")
    c_count = sequence.count("G")
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

# Подсчет среднего качества


def calculate_quality(quality_str: str) -> float:
    """
    Вычисляет среднее качество последовательности по строке качеств.

    Аргументы:
    quality_str -- строка с символами качества (ASCII-кодировка).

    Возвращает:
    Среднее качество последовательности (float).
    """
    quality_scores = [ord(q_symbol) - 33 for q_symbol in quality_str]
    avg_quality = sum(quality_scores) / len(quality_scores)
    return avg_quality
