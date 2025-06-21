
'''
Є текстовий файл, який містить інформацію
про місячні заробітні плати розробників у вашій компанії.
Кожен рядок у файлі містить прізвище розробника та його заробітну плату,
які розділені комою без пробілів.
'''

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

with open("salary_file.txt", "w", encoding='utf-8') as fh:
    fh.write("Alex Korp,3000\n")
    fh.write("Nikita Borisenko,2000\n")
    fh.write("Sitarama Raju,1000\n")

def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as fh:
            total = 0
            quantity = 0
            for line in fh:
                name, salary = line.strip().split(',')
                total += int(salary)
                quantity += 1
        
            if quantity == 0:
                return (0, 0)
        
            average = total / quantity
            return (total, average)
        
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' відсутній.")
        return (0, 0)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
