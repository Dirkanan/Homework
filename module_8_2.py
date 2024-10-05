def personal_sum(numbers):
    result = 0
    incorrect_data_count = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data_count += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return (result, incorrect_data_count)


def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            numbers = numbers.split(',')  # Преобразуем строку в список
        elif not isinstance(numbers, list):
            raise TypeError('В numbers записан некорректный тип данных')

        result, incorrect_count = personal_sum(numbers)

        valid_count = len(numbers) - incorrect_count

        return result / valid_count
    except ZeroDivisionError as zde:
        return 0
    except TypeError as te:
        print(str(te))
        return None

print(f'Результат 1: {calculate_average("1, 2, 3, 123, ghfyr")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 15])}')
