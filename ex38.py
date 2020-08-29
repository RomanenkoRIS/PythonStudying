ten_things = "Яблоки Апельсин Ворона Телефон Свет Сахар"
stuff = ten_things.split(' ')
more_stuf = ["День", "Ночь","Песня","Мишка"]

while len(stuff)!=10:
    next_one = more_stuf.pop()
    print("Добавляем:",next_one)
    stuff.append(next_one)
    print(f"Теперь у нас {len(stuff)} объектов")
    
print("Итак:", stuff)
print("Колическто сделем объектами")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))

