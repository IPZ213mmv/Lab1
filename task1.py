def xor(x1, x2):
    or_result = x1 or x2
    and_result = x1 and x2
    xor_result = or_result and not and_result
    return xor_result

# Приклад використання
print(xor(0, 0))  # Виведе: False
print(xor(0, 1))  # Виведе: True
print(xor(1, 0))  # Виведе: True
print(xor(1, 1))  # Виведе: False
