def is_palindrome(s):
    # Преобразование строки: убираем пробелы, приводим к нижнему регистру
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Сравниваем строку с её перевёрнутой версией
    return s == s[::-1]

print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("Привет, мир!"))  # False

