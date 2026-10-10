def read_file(file_path):
    """
    Читает файл и возвращает список его строк.
    """
    with open(file_path, encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def combine_files(file_paths, output_path):
    """
    Объединяет несколько файлов в один с сортировкой по количеству строк.
    """
    files_data = []

    # 1. Читаем все файлы и считаем строки
    for path in file_paths:
        lines = read_file(path)
        files_data.append({
            'name': path,
            'lines_count': len(lines),
            'lines': lines,
        })

    # 2. Сортируем по количеству строк (по возрастанию)
    files_data.sort(key=lambda item: item['lines_count'])

    # 3. Записываем в итоговый файл
    with open(output_path, 'w', encoding='utf-8') as f:
        for file_info in files_data:
            f.write(f"{file_info['name']}\n")
            f.write(f"{file_info['lines_count']}\n")
            for line in file_info['lines']:
                f.write(f"{line}\n")


def main():
    file_paths = ['1.txt', '2.txt']
    combine_files(file_paths, 'result.txt')
    print("Готово! Результат в result.txt")


if __name__ == '__main__':
    main()