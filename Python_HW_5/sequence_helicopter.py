
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

from fastq_reader import (fastq_to_dict, write_fastq)


    
def filter_fastq(input_fastq: str, output_fastq: str,
                 gc_bounds: tuple[float, float] = (0, 100),
                 length_bounds: tuple[int, int] = (0, 2**32),
                 quality_threshold: float = 0) -> None:
    """
    Filters sequences from an input FASTQ file based on GC content, length, and quality threshold
    and writes the filtered sequences to an output FASTQ file.

    Arguments:
    input_fastq -- the path to the input FASTQ file (str).
    output_fastq -- the path to the output FASTQ file (str).
    gc_bounds -- a tuple with the minimum and maximum GC content values (default is (0, 100)).
    length_bounds -- a tuple with the minimum and maximum sequence length (default is (0, 2**32)).
    quality_threshold -- the threshold for the average quality score (default is 0).

    Returns:
    None
    """
    seqs = fastq_to_dict(input_fastq)
    good_filtered_seqs = {}  # Пустой словарь для запист отфильтрованных посл.

    # Цикл, который будет вынимать из словаря каждую пару ключ-значение
    # и пропускать через фильтр sequence_str и quality_str из значений,
    # присваивая одной из 3-х переменных для фильтрации значение True/False
    # key in seqs - строка с имем последовательнсти
    # value in seqs - кортеж с двумя строками - (последовательность, качество)

    for seq_name, (seq_str, quality_str, plus_str) in seqs.items():
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
            good_filtered_seqs[seq_name] = (seq_str, quality_str, plus_str)



        # Фильтрация данных
    good_filtered_seqs = filter_fastq(seqs)

    if not good_filtered_seqs:
        print("No sequences match the filtering criteria.")
    else:
        print(f"Sequences filtered: {len(good_filtered_seqs)}")

    # Шаг 3: Запись отфильтрованных последовательностей в файл
    write_fastq(good_filtered_seqs, output_fastq)

    

def run_dna_rna_tools(*args: str) -> list[str]:

    """
    Performs the selected operation on DNA or RNA sequences.

    Arguments:
    *args -- strings with sequences and the last string as the command to execute.
             Available commands: "transcribe", "reverse", "complement", "reverse_complement".

    Returns:
    A list of strings with the result of applying the command to the given sequences.
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

