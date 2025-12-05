from math import floor, log10

fn is_invalid_number(number: Float64) -> Bool:
  # num_digits = floor(log10(number)) + 1
  # ensure num_digits is even
  # d = num_digits / 2
  # n = number / (10 ^ d + 1)
  # if n is int, it's invalid

  num_digits = floor(log10(number)) + 1
  if num_digits % 2 != 0:
    return False

  d = num_digits / 2
  
  n_first = floor(number / (10 ** d))
  n_last = number % (10 ** d)

  if n_first != n_last:
    return False

  return True

  

fn part1[origin: Origin](ids: List[StringSlice[origin]]) raises -> Int:
  var result = 0

  for id_range in ids:
    split_id_range = id_range.split("-")
    start, end = atol(split_id_range[0]), atol(split_id_range[1])
    for number in range(start, end+1):
      if is_invalid_number(Float64(number)):
        result += number

  return result



fn main() raises:
  
  var f = open("input.txt", "r")

  var data = f.read().split(",")
  
  f.close()

  print(part1(data))


  
