# Дана строка-предложение на русском языке.
# Преобразовать строку так, чтобы каждое слово начиналось с заглавной буквы.
# Словом считать набор символов, не содержащий пробелов и ограниченный пробелами или началом/концом строки.
# Слова, не начинающиеся с буквы, не изменять.

# -> Влада любит кушать корольки и инжир
# <- Влада Любит Кушать Корольки И Инжир

Str = input("Enter string: ")
print(Str.title())