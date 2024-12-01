
import os


def fastq_to_dict(input_fastq: str) -> dict[str, tuple[str, str, str]]:
    """
    Converts a FASTQ file into a dictionary.

    Arguments:
    input_fastq (str): The path to the input FASTQ file.

    Returns:
    dict[str, tuple[str, str, str]]: A dictionary where the key is the sequence name, 
    and the value is a tuple containing the sequence string, quality string, and the '+' string.
    """
    # Создадим пустой словарь для записи
    seqs = {}

    # Откроем файл
    with open(input_fastq, "r") as fastq:

        # Цикл обработки нужных строк и записи в словарь
        # Будем идти по всем строкам и сохранять все в 4 переменные
        # Кол-во строк должно быть кратно 4, поэтому если 1 строка не будет найдена, то файл закончился
        while True:
            seq_name = fastq.readline().strip() # читаем строку и сразу убираем разделители
            if not seq_name:
                break # Выход из цикла, если файл закончился
            seq_str = fastq.readline().strip()
            plus_str = fastq.readline().strip()
            quality_str = fastq.readline().strip()

            # Записываем каждую итерацию в элемент словаря
            seqs[seq_name] = (seq_str, quality_str, plus_str)
        
    return seqs





def write_fastq(good_filtered_seqs: dict[str, tuple[str, str, str]], output_fastq: str) -> None:
    """
    Writes filtered sequences to a FASTQ file.

    Arguments:
    good_filtered_seqs (dict[str, tuple[str, str, str]]): A dictionary where the key is the sequence name,
    and the value is a tuple containing the sequence string, quality string, and the '+' string.
    
    output_fastq (str): The name of the output FASTQ file.

    Returns:
    None
    """
    # Проверим наличие папки по заданному пути
    out_dir = "filtered"

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    # Создадим путь для записи файла
    out_path = os.path.join(out_dir, output_fastq)

    with open(out_path, "w"):
    # Цикл, который каждый элемент в словаре запишет
    # в виде FASTQ через метод f-строки
        for seq_name, (seq_str, quality_str, plus_str) in seqs.items():
            file.write(f"{seq_name}\n{seq_str}\n{plus_str}\n{quality_str}\n")