print("\n08 de agosto de 2026. Sábado. Noite normal.")
print("\nPágina 161 - Usando a instrução continue")

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
