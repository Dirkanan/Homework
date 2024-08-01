data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_all_sum(data_structure):
    all_sum = 0
    if isinstance(data_structure, (int, float)):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for object in data_structure:
            all_sum += calculate_structure_all_sum(object)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            all_sum += calculate_structure_all_sum(key)
            all_sum += calculate_structure_all_sum(value)
    return all_sum

result = calculate_structure_all_sum(data_structure)
print(result)
