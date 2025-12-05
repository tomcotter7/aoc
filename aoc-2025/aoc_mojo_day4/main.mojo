
fn part1[origin: Origin](grid: List[StringSlice[origin]]) raises -> Int:

  var check_sum = 0

  height = len(grid)
  width = len(grid[0])

  total_pos = height * width

  for idx in range(total_pos):
    x = idx // width
    y = idx % width

    if grid[x][y] == "@":
      n_tp = 0
      for idx_x in range(max(x - 1, 0), min(x + 2, height)):
        for idx_y in range(max(y - 1, 0), min(y + 2, width)):
          elem = grid[idx_x][idx_y]
          if elem == "@":
            n_tp += 1

      if n_tp < 5:
        check_sum += 1


  return check_sum

fn main() raises:
  var f = open("input.txt", "r")
  var data = f.read().split("\n")
  f.close()



  print(part1(data))
