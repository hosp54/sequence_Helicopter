
from dna_rna_operations import (
    complement,
    transcribe,
    reverse,
    reverse_complement
)

from gc_and_quality_calculator import (
    calculate_gc_content,
    calculate_quality
)


def filter_fastq(seqs: dict[str, tuple[str, str]],
                 gc_bounds: tuple[float, float] = (0, 100),
                 length_bounds: tuple[int, int] = (0, 2**32),
                 quality_threshold: float = 0) -> dict[str, tuple[str, str]]:
    
    """
    Фильтрует FASTQ-последовательности по параметрам GC-состава, длины и порогу качества.

    Аргументы:
    seqs -- словарь, где ключи это имена последовательностей (str),
    а значения кортежи с двумя строками: (последовательность, качество).
    gc_bounds -- кортеж с минимальным и максимальным значениями для GC-состава.
    length_bounds -- кортеж с минимальной и максимальной длиной последовательности.
    quality_threshold -- порог среднего качества последовательности.

    Возвращает:
    Словарь с отфильтрованными последовательностями, которые соответствуют условиям фильтрации.
    """

    good_filtered_seqs = {}  # Пустой словарь для запист отфильтрованных посл.

    # Цикл, который будет вынимать из словаря каждую пару ключ-значение
    # и пропускать через фильтр sequence_str и quality_str из значений,
    # присваивая одной из 3-х переменных для фильтрации значение True/False
    # key in seqs - строка с имем последовательнсти
    # value in seqs - кортеж с двумя строками - (последовательность, качество)

    for seq_name, (seq_str, quality_str) in seqs.items():
        gc_content = calculate_gc_content(seq_str)  # Считаем GC-состав
        avg_quality = calculate_quality(quality_str)  # Считаем ср. качество
        length_seq = len(seq_str)                   # Длина последовательности

    # Переменные, которые хранят булевы значения о состоянии каждого этапа
        gc_status = False
        length_status = False
        quality_status = False

        # Проверяем GC состав

        if isinstance(gc_bounds, (int, float)):
            if gc_content <= gc_bounds:
                gc_status = True

        elif isinstance(gc_bounds, tuple):
            if gc_bounds[0] <= gc_content <= gc_bounds[1]:
                gc_status = True

        # Проверяем длину последовательности
        if isinstance(length_bounds, (int, float)):
            if length_seq <= length_bounds:
                length_status = True

        elif isinstance(length_bounds, tuple):
            if length_bounds[0] <= length_seq <= length_bounds[1]:
                length_status = True

        # Проверяем среднее качество
        if avg_quality >= quality_threshold:
            quality_status = True

        # Проверяем все 3 условия на True/False

        if gc_status and length_status and quality_status:
            # Записываем элемент словаря seqs через ключ в новый словарь
            good_filtered_seqs[seq_name] = (seq_str, quality_str)

    return good_filtered_seqs


def run_dna_rna_tools(*args: str) -> list[str]:

    """
    Выполняет выбранную операцию над последовательностями ДНК или РНК.

    Аргументы:
    *args -- строки с последовательностями и последней строкой — командой для выполнения.
             Доступные команды: "transcribe", "reverse", "complement", "reverse_complement".

    Возвращает:
    Список строк с результатом выполнения команды над переданными последовательностями.
    """
    *seqs, command = args
    if command == "transcribe":
        return transcribe(seqs)
    elif command == "reverse":
        return reverse(seqs)
    elif command == "complement":
        return complement(seqs)
    elif command == "reverse_complement":
        return reverse_complement(seqs)
