
def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:

    """
    Converts a multi-line FASTA file into a single-line format for each sequence.

    Arguments:
    input_fasta -- the path to the input FASTA file (str).
    output_fasta -- the path to the output FASTA file (str). If not provided, a new filename
                    will be created by appending '_oneline' to the input file's name (default is None).

    Returns:
    None
    """
     oneline_seqs = {}

    with open(input_fasta, "r") as fasta:

        seq_name =  None
        seq_list = []

        while True:
            line = fasta.readline().strip()
            if not line: # Если строка пустая, значит файл прочитан до конца
                if seq_name: # Сохраняем последнюю последовательность
                    oneline_seqs[seq_name] = "".join(seq_list)
                break

            # Если строка начинается с ">" - это название последовательности
            if line.startswith(">"):
                # Если уже есть предыдущая последовательность
                if seq_name is not None:
                    oneline_seqs[seq_name] = "".join(seq_list)
                
                seq_name = line  # Обновляем название последовательности
                seq_list = []  # Очищаем список для новой последовательности

            else: # иначе - записываем нашу строку в список
                seq_list.append(line) # Добавляем фрагмент последовательности в список
            
    # Охабка дров - словарь готов, но ретерна тут не будет - возвращаем мы файл   
   
    # Запишем наш словарь в файл

    # Если при вызове функции output_fasta не был указан (то есть его значение — None), то
    # автоматически создается имя выходного файла на основе имени входного файла (input_fasta)
    #  Метод .replace() используется для создания нового имени файла
    if output_fasta is None:
        output_fasta = input_fasta.replace(".fasta", "_oneline.fasta") # добавили к файлу по пути input.fasta окончание _oneline (внимание на расширения)
    
    # Открыли файл в режиме чтения
    with open(output_fasta, "w") as output_fasta:
        for seq_name, seq in oneline_seqs.items(): # Цикл проходил по всем парам ключ-значение в словаре

            # Запишем в наш выходной файл последовательность в 2 строки (методом f-строки)
            output_fasta.write(f"{seq_name}\n{seq}\n")


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Parses a BLAST output file to extract the first matching description for each query and
    sorts these descriptions alphabetically.

    Arguments:
    input_file -- the path to the input BLAST output file (str).
    output_file -- the path to the output file where sorted descriptions will be written (str).

    Returns:
    None
    """


    # Кортеж для записи первых строк Description
    first_description_lines = []

    # Читаем файл
    with open(input_file, "r") as blast:
        # Идем по каждой строке файла
        for blast_line in blast:
            blast_line = blast_line.strip()

            # Ищем начало Query
            if blast_line.startswith("Query #"): # Дошли до нужной строки с Query #
                for query_line in blast:
                    query_line = query_line.strip()

                     # Если находим строку с Description
                    if query_line.startswith("Description"):
                         # Считываем первую строку после Description
                        description = query_line
                        first_description_line = blast.readline().strip().split("  ")[0]
                        # Добавляем её в список
                        first_description_lines.append(first_description_line)
                        break # Прекращаем обработку этого Query и ищем следующий
            
     # Сортируем все собранные строки с Description по алфавиту
    sorted_description_lines = sorted(first_description_lines, key=str.lower)

   # Запишем результат в новый файл
    with open(output_file, "w") as output: # теперь наш файл - output
        # У нас есть список (или кортеж) и нам надо записать его элементы в каждую линию
        # Сделаем это через цикл for и дозапись в файл с \n в конце

        for description_line in sorted_description_lines:
            output.write(f"{description_line}\n") # Дозапись каждой линии

