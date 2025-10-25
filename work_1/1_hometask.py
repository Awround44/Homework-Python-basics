# Task 1
def is_palindrom(s: str) -> bool:
    """Проверяет является ли строка палиндромом."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrom("1Madam, I m Adam1"))
print(is_palindrom("ladno"))