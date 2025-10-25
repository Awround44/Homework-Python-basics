# Task 2
def filter_strings(filter_func, strings: list[str]) -> list[str]:
    """Фильтрует список строк на основе предоставленной лямбда-функции."""
    return list(filter(filter_func, strings))

string_array = ["ago", "egg", "cherry", "rule", " launcher ", "fig", "grape", "a car"]

no_spaces = filter_strings(lambda x: ' ' not in x, string_array)
print("No spaces:", no_spaces)

no_start_a = filter_strings(lambda x: not x.lower().startswith('a'), string_array)
print("No start with 'a':", no_start_a)

longer_than_4 = filter_strings(lambda x: len(x) >= 5, string_array)
print("Length >= 5:", longer_than_4)