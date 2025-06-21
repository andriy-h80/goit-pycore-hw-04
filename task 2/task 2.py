
'''
У вас є текстовий файл, який містить інформацію про котів.
Кожен рядок файлу містить унікальний ідентифікатор кота,
його ім'я та вік, розділені комою. 
Завдання - розробити функцію get_cats_info(path),
яка читає цей файл та повертає список словників з інформацією про кожного кота.
'''

# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5

with open("cats_file.txt", "w", encoding='utf-8') as fh:
    fh.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    fh.write("0b90c2413067a15887e1ae2,Vika,1\n")
    fh.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    fh.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    fh.write("060b90c4613067a15887e1ae5,Tessi,5\n")

def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding='utf-8') as fh:
            for line in fh:
                cat_id, name, age = line.strip().split(',')
                cat = {"id": cat_id, "name": name, "age": int(age)}        
                cats.append(cat)
            return cats

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' відсутній.")
        return []
            
cats_info = get_cats_info("cats_file.txt")
print(cats_info)

# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
