fn part2[origin: Origin](rotations: List[StringSlice[origin]]) raises -> Int:
  
  var position = 50
  var result: Int = 0


  for rotation in rotations:
    direction = rotation[0]
    value = atol(rotation[1:].strip())

    if direction == "L":
      value *= -1

    var unnormalised_pos = position + value
    var laps = unnormalised_pos // 100
    if position == 0 and direction == "L":
      laps += 1
    if (unnormalised_pos % 100 == 0) and direction == "R":
      laps -= 1

    result += abs(laps)

    position = (unnormalised_pos % 100)

    if position == 0:
      result += 1


  return result

fn part1[origin: Origin](rotations: List[StringSlice[origin]]) raises -> Int:
  
  var position = 50
  var result = 0
  
  for rotation in rotations:
    direction = rotation[0]
    value = atol(rotation[1:].strip())

    if direction == "L":
      value *= -1
  
    position = (position + value) % 100

    if position == 0:
      result += 1

  return result

fn main() raises:
  
  var f = open("input.txt", "r")
  var rotations = f.read().strip().splitlines()

  f.close()

  print(part1(rotations))
  print(part2(rotations))


