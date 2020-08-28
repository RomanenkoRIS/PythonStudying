from sys import argv
script, filename = argv


print("Я собираюсь стереть файл {filename}.")
print("Если ві не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла")
target.truncate()

print("Запрос")

line1 = input("строка 1:")
line2 = input("строка 2:")
line3 = input("строка 3:")

print("Запись в файл")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Закрыть файл")
target.close()
