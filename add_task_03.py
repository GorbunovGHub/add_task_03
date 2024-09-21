data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    total_sum = 0

    if isinstance(data_structure, str):
        total_sum += len(data_structure)
    if isinstance(data_structure, int):
        total_sum += data_structure
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item)

    return total_sum


result = calculate_structure_sum(data_structure)
print(result)
