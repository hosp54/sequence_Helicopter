# GC-состав

def calculate_gc_content(sequence: str) -> float:
    """
    Calculates the GC content percentage in a sequence.

    Arguments:
    sequence -- a string representing a DNA or RNA sequence.

    Returns:
    The percentage of GC content in the sequence (float).
    """
    g_count = sequence.count("C")
    c_count = sequence.count("G")
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

# Подсчет среднего качества


def calculate_quality(quality_str: str) -> float:
    """
    Calculates the average quality score of a sequence based on a quality string.

    Arguments:
    quality_str -- a string representing quality scores (ASCII encoding).

    Returns:
    The average quality score of the sequence (float).
    """
    quality_scores = [ord(q_symbol) - 33 for q_symbol in quality_str]
    avg_quality = sum(quality_scores) / len(quality_scores)
    return avg_quality
