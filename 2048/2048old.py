import random

def set_both_lists():
  global data_grid
  global full_cells_coords
  global full_cells
  full_cells_coords = []
  full_cells = []
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      if data_grid[y][x] != 0:
        full_cells.append([y, x, data_grid[y][x]])
        full_cells_coords.append([y, x])

def create_object():
  global data_grid
  empty_cells = []
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      if data_grid[y][x] == 0:
        empty_cells.append([y, x])
  print("EMPTY_CELLS = ", empty_cells , "LEN: ", len(empty_cells))
  grid_to_add = random.choice(empty_cells)
  empty_cells.remove(grid_to_add)
  print("GRID ADDED", grid_to_add)
  y_num, x_num = grid_to_add[0], grid_to_add[1]
  data_grid[y_num][x_num] = 2
  for i in data_grid:
    print(i)
  print("EMPTY_CELLS = ", empty_cells , "LEN: ", len(empty_cells))
  if len(empty_cells) == 0:
    print("NO EMPTY CELLS TO ADD TO > CALLING CHECKLOSE()")
    print("________________________________")
    return check_lose()

print("________________________________")




print("____________________")
def check_lose():
  global lose
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      data_grid_num = data_grid[y][x]
      if y - 1 != -1:
        if data_grid[y - 1][x] == data_grid_num:
          print("CHECKLOSE RETURNED FALSE")
          return False
      if y + 1 != 4:
        if data_grid[y + 1][x] == data_grid_num:
          print("CHECKLOSE RETURNED FALSE")
          return False
      if x - 1 != -1:
        if data_grid[y][x - 1] == data_grid_num:
          print("CHECKLOSE RETURNED FALSE")
          return False
      if x + 1 != 4:
        if data_grid[y][x + 1] == data_grid_num:
          print("CHECKLOSE RETURNED FALSE")
          return False
  lose = True
  print("CHECKLOSE RETURNED TRUE")
  return True


def move(direction):
  global data_grid
  global win
  global moved
  global full_cells
  full_cells = []
  full_cells_coords = []
  x_deviation = 0
  y_deviation = 0
  loop_variables = [] #this ensure numbers move according to closest to direction eg. rightmost box moves first when direction is right
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      if data_grid[y][x] != 0:
        full_cells.append([y, x, data_grid[y][x]])
        full_cells_coords.append([y, x])
  print("FULL_CELLS:", full_cells)
  if len(full_cells) == 16:
    if check_lose():
      return
    else:
      print("CHECKLOSE RETURNED FALSE, STILL POSSIBLE TO MAKE MOVE")
  if direction == "r":
    x_deviation = 1
    axis_and_number = [1, 3]
    loop_variables = [len(full_cells) -1, -1, -1]
  elif direction == "l":
    x_deviation = -1
    axis_and_number = [1, 0]
    loop_variables = [0, len(full_cells) , 1]
  elif direction == "u":
    y_deviation = -1
    axis_and_number = [0, 0]
    loop_variables = [0, len(full_cells), 1]
  elif direction == "d":
    y_deviation = 1
    axis_and_number = [0, 3]
    loop_variables = [len(full_cells) -1, -1, -1]
  for i in range(loop_variables[0], loop_variables[1], loop_variables[2]):
    while True:
      set_both_lists()
      print("SET LISTS")
      print(i)
      print(full_cells)
      print(full_cells_coords)
      if full_cells[i][axis_and_number[0]] == axis_and_number[1]:
        print(f"object{i} ({full_cells[i]})stopped because axis_and_number")
        break
      if [full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation] in full_cells_coords and full_cells[full_cells_coords.index([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation])][2] != 0:
        print([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation] , "in fulL_cells_coords")
        print("full_cells[i]: ", full_cells[i])
        print("full_cells: ", full_cells)
        print("full_cells_coords: ", full_cells_coords)
        print("COMBO: ", [full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation])
        print(full_cells_coords.index([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation]))
        print(full_cells[full_cells_coords.index([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation])])
        print("IF STATEMENT NOW:")
        if full_cells[i][2] == full_cells[full_cells_coords.index([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation])][2]:
          print("NUMBERS ARE THE SAME, MERGING")
          #MERGE NUMBERS
          full_cells[full_cells_coords.index([full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation])][2] *= 2
          full_cells[i][2] = 0
          data_grid[full_cells[i][0] + y_deviation][full_cells[i][1] + x_deviation] *= 2
          data_grid[full_cells[i][0]][full_cells[i][1]] = 0
          moved = True
          if data_grid[full_cells[i][0] + y_deviation][full_cells[i][1] + x_deviation] == 2048:
            win = True
            break
          break
        else:
          print("NOT SAME")
          break
      else:
        set_both_lists()
        print(f"moving {full_cells[i]} to here:  {[full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation]}")
        data_grid[full_cells[i][0] + y_deviation][full_cells[i][1] + x_deviation] = full_cells[i][2]
        print(data_grid[full_cells[i][0] + y_deviation][full_cells[i][1] + x_deviation])
        for data_grid_row in data_grid:
          print(data_grid_row)
        data_grid[full_cells[i][0]][full_cells[i][1]] = 0
        print(full_cells, full_cells_coords)
        full_cells_coords[i][0], full_cells_coords[i][1] = full_cells_coords[i][0] + y_deviation, full_cells_coords[i][1] + x_deviation
        full_cells[i][0], full_cells[i][1] = full_cells[i][0] + y_deviation, full_cells[i][1] + x_deviation
        moved = True
      for bbbb in data_grid:
        print(bbbb)



data_grid = []
for i in range(4):
  data_grid.append([])
  for j in range(4):
    data_grid[i].append(0)

for i in data_grid:
  print(i)

create_object()
lose = False
win = False
moved = False
full_cells = []
while True:
  while True:
    if len(full_cells) == 16:
      if check_lose():
        print("CALLED CHECKLOSE AS len(FULL_CELLS) == 16")
        break
    if lose or win:
      break
    input1 = input("Direction (u, d, l , r) : ")
    if input1.lower() in ['u', 'd', 'l', 'r', 'x']:
      moved = False
      move(input1)
      if moved:
        create_object()
      for i in data_grid:
        print(i)
    else:
      print("INPUT MUST BE 'u' (UP) , 'd' (DOWN) , 'l' (LEFT) , 'r' (RIGHT)")
  if win:
    print("YOU WIN")
  elif lose:
    print("YOU LOSE")
  while True:
    choice = input("Play again? (y/n): ")
    if choice.lower() == 'y' or choice.lower() == 'n':
      break
    else:
      print("INPUT MUST BE 'Y' OR 'N'")
  if choice == 'n':
    break
print("Thank you for playing!")



