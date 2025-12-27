def combine_files(file_list):
    """
    Объединяет текстовые файлы в один, соблюдая правила задачи.

    Args:
      file_list: Список имен файлов.

    Returns:
      Строка с объединенным содержимым файлов.
    """

    file_data = []
    for filename in file_list:
        with open(filename, 'r') as f:
            lines = f.readlines()
            file_data.append((filename, len(lines), lines))

    # Сортируем файлы по количеству строк
    file_data.sort(key=lambda x: x[1])

    output = ""
    for filename, line_count, lines in file_data:
        output += filename + "\n"
        output += str(line_count) + "\n"
        output += "".join(lines)

    return output

# Пример использования:
files_to_combine = ["2.txt", "1.txt", "3.txt"]  # Порядок важен только если кол-во строк одинаковое.
result = combine_files(files_to_combine)
print(result)

# Чтобы записать результат в файл:
with open("output.txt", "w") as f:
    f.write(result)