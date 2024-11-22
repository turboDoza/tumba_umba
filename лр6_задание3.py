n = int(input("Введите количество элементов в списке: "))
elements = []

for i in range(n):
    element = int(input(f"Введите элемент {i + 1}: "))
    elements.append(element)

C = int(input("Введите значение C: "))

count_less_than_C = 0
max_element = elements[0] if elements else None

for element in elements:
    if element < C:
        count_less_than_C += 1
    if element > max_element:
        max_element = element

print("Количество элементов списка, меньших C:", count_less_than_C)
if max_element is not None:
    print("Максимальный элемент списка:", max_element)
else:
    print("Список пуст.")