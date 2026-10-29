
def separate_even_odd(numbers):
  even = []
  odd = []

  for number in numbers:
    if number % 2 == 0:
      even.append(number)
    else:
      odd.append(number)

  return even, odd
even,odd=separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("even:", even)
print("odd:", odd)
