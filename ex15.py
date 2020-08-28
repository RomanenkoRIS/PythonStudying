from sys import argv
script, filename = argv
#name = "ех15data.txt"
txt = open(filename) #mode='r', encoding = 'ascii')
print(f"Содержимое файла {filename}:")
print(txt.read())
txt.close()
# print("Снова введите имя файла")
# file_again = input("Имя файла:")
# txt_again = open(file_again)# mode='r', encoding = 'ascii')
# # #
# print(txt_again.read())

#python ex15.py ех15data.txt