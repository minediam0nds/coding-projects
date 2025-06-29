import random



data_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
data_grid_coords = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]


def save_prev_grid(): #FUNCTION IS ONLY FOR DEBUGGING: TO COMPARE PREVIOUS TO CURRENT AFTER MOVE()
  global data_grid
  global prev_data_grid
  #prev_data_grid = data_grid.copy() heres where i needed help. i learnt that there are 'shallow copies' and 'deep copies', and doing what i did would create a shallow one, which was still affected when i modified the lists inside data_grid
  #below is how i made a 'deep copy'
  prev_data_grid = []
  for y in range(len(data_grid)):
    prev_data_grid.append([])
    for x in range(len(data_grid[y])):
      prev_data_grid[y].append(data_grid[y][x])


def print_prev_grid():#FUNCTION IS ONLY FOR DEBUGGING: TO COMPARE PREVIOUS TO CURRENT AFTER MOVE()
  global prev_data_grid
  for i in prev_data_grid:
    print(i)



def print_grid():
  global data_grid
  for i in data_grid:
    print(i)

def create_two():
  zero_cells = []
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      if data_grid[y][x] == 0:
        zero_cells.append([y , x])
  if len(zero_cells) == 0:
    return
  selected_cell = zero_cells[random.randint(0, len(zero_cells)-1)]
  data_grid[selected_cell[0]][selected_cell[1]] = 2

def move(dir):
  global win #winning in 2048 is merging a number to 2048, so this variable changes to True when 2048 is detected when merging
  global data_grid
  global moved
  already_merged_cells_coords = [] #this variable is too make sure the code is consistent with the original; a merged number cannot merge with another number in the same movex
  if dir == 'u':
    x_dev = 0
    y_dev = -1
    next_cell_i_change = -4
    axis_and_axis_limit = [0, 0]
  elif dir == 'd':
    x_dev = 0
    y_dev = 1
    next_cell_i_change = 4
    axis_and_axis_limit = [0, 3]
  elif dir == 'l':
    x_dev = -1
    y_dev = 0
    next_cell_i_change = -1
    axis_and_axis_limit = [1, 0]
  elif dir == 'r':
    x_dev = 1
    y_dev = 0
    next_cell_i_change = 1
    axis_and_axis_limit = [1, 3]

  if dir in ['u', 'l']:  # i had to do this to be consistent with the original game, basically just iterates through data_grid in opp direction (for 'd' and 'r')
    i = 0
    while i < 16:
      if data_grid[data_grid_coords[i][0]][data_grid_coords[i][1]] == 0:
        i += 1
        continue
      current_cell_coords = data_grid_coords[i]
      current_cell_num = data_grid[current_cell_coords[0]][current_cell_coords[1]]
      #check if adjacent cell in 'dir' of current cell exists
      try:
        data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev]
      except IndexError:
        i += 1
        continue #cell doesnt exist, hence continue to the next cell
      if -1 in [current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev]:
        i += 1
        continue #cells shouldnt move to the other side of the box (-1), hence continue to next cell

      #cell exists as it passed the test, now move or merge

      nested_i = i
      while nested_i <= 15:
        current_cell_coords = data_grid_coords[nested_i]
        current_cell_num = data_grid[current_cell_coords[0]][current_cell_coords[1]]

        #same check
        try:
          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev]

        except IndexError:

          i += 1
          break #cell doesnt exist, hence continue to the next cell
        if -1 in [current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev]:

          i += 1
          break #cell doesnt exist, hence continue to the next cell
  
        if data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == 0:#next cell empty, move cell to there

          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] = current_cell_num #changed next cell to current cell num
          data_grid[current_cell_coords[0]][current_cell_coords[1]] = 0 #changed current cell to 0
          #current cell moved in to next cell, so change i to nextcells index in data_grid_coords
          moved = True
          nested_i += next_cell_i_change
        elif data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == current_cell_num and [current_cell_coords[0] + y_dev , current_cell_coords[1] + x_dev] not in already_merged_cells_coords : #numbers are the same, merge
          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] = current_cell_num*2
          already_merged_cells_coords.append([current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev])
          data_grid[current_cell_coords[0]][current_cell_coords[1]] = 0
          nested_i += next_cell_i_change
          i+= 1
          if data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == 2048:
            win = True
            return
          moved = True
          break #reason for breaking is because this num becomes a merged cell, hence it has no more possible moves
        else: 
          i += 1
          break #num in next cell is different, so now this num is finished with all its moves , move on to next



  else: #--------------------------------------for opp directions
    i = 15
    while i >= 0:
      if data_grid[data_grid_coords[i][0]][data_grid_coords[i][1]] == 0:
        i -= 1
        continue
      current_cell_coords = data_grid_coords[i]
      current_cell_num = data_grid[current_cell_coords[0]][current_cell_coords[1]]
      #check if adjacent cell in 'dir' of current cell exists
      try:
        data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev]
      except IndexError:
        i -= 1
        continue #cell doesnt exist, hence continue to the next cell
      if -1 in [current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev]:
        i -= 1
        continue #cells shouldnt move to the other side of the box (-1), hence continue to next cell

      #cell exists as it passed the test, now move or merge

      nested_i = i
      while nested_i <= 15:
        current_cell_coords = data_grid_coords[nested_i]
        current_cell_num = data_grid[current_cell_coords[0]][current_cell_coords[1]]


        #same check
        try:
          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev]
        except IndexError:
          i -= 1
          break #cell doesnt exist, hence continue to the next cell
        if -1 in [current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev]:

          i -= 1
          break #cell doesnt exist, hence continue to the next cell
  
        if data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == 0:#next cell empty, move cell to there

          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] = current_cell_num #changed next cell to current cell num
          data_grid[current_cell_coords[0]][current_cell_coords[1]] = 0 #changed current cell to 0

          #current cell moved in to next cell, so change i to nextcells index in data_grid_coords
          moved = True

          nested_i += next_cell_i_change
        elif data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == current_cell_num and [current_cell_coords[0] + y_dev , current_cell_coords[1] + x_dev] not in already_merged_cells_coords : #numbers are the same, merge
          data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] = current_cell_num*2
          already_merged_cells_coords.append([current_cell_coords[0] + y_dev, current_cell_coords[1] + x_dev])
          data_grid[current_cell_coords[0]][current_cell_coords[1]] = 0
          nested_i += next_cell_i_change
          i -= 1

          if data_grid[current_cell_coords[0] + y_dev][current_cell_coords[1] + x_dev] == 2048:

            win = True
            return
          moved = True

          break #reason for breaking is because this num becomes a merged cell, hence it has no more possible moves
        else:  
          i -= 1
          break #num in next cell is different, so now this num is finished with all its moves , move on to next




    #check for next cell == current cell


def check_lose(): #checking for loss, conditions for loss are no moves are possible
  for y in range(len(data_grid)):
    for x in range(len(data_grid[y])):
      data_grid_num = data_grid[y][x]
      if y - 1 != -1: #these lines before are just to prevent a IndexError
        if data_grid[y - 1][x] == data_grid_num or data_grid[y - 1][x] == 0: #compare above cell

          return False
      if y + 1 != 4:
        if data_grid[y + 1][x] == data_grid_num or data_grid[y + 1][x] == 0: #compare below cell

          return False
      if x - 1 != -1:
        if data_grid[y][x - 1] == data_grid_num or data_grid[y][x - 1] == 0: #compare left cell
 
          return False
      if x + 1 != 4:
        if data_grid[y][x + 1] == data_grid_num or data_grid[y][x - 1] == 0: #compare right cell

          return False
  return True








create_two()
print_grid()
win = False
while True:
  moved = False #in 2048, if you input a direction, but no num moves, a two will not be created    
  save_prev_grid()
  while True:         
    x = input("MOVE: ")
    if x not in ['u', 'd', 'l', 'r']:
      print("INPUT MUST BE 'u', 'd', 'l' ,'r'")
    else:
      break
  move(x)
  if moved:
    create_two()
  if check_lose():
    break
  print_grid()
  if win:
    break

if win:
  print("YOU WON !!!!!!!!!")
else:
  print("YOU LOST!!!!!!!!")


