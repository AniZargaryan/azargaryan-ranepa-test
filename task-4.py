def my_factorial(n):

  if type(n) != int:
    raise TypeError("Ошибка: Число должно быть целым")
    
  if n < 0:
    raise ValueError("Ошибка: Отрицательное число")

  if n == 0 or n == 1:
    return 1
    
  res = 1
  for i in range(2, n + 1):
    result *= i
    return result
