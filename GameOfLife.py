"""Game of Life
This code runs the Game of Life for a given grid.
"1"s denote living cells and "0"s denote dead cells.
Author: Stephanie Cook"""



def flatten_grid(grid):
      "Flattens a given grid to a list."
      flat=[]
      for row in grid:
            for item in row:
                  flat.append(item)
      return flat



def print_grid(grid):
      "Makes outputted grids print neatly."
      
      grid_width=len(grid[0])
      grid_height=len(grid)
      flat_grid=flatten_grid(grid)

      #Convert each element in the list to a string.
      string_grid=[]
      for i in flat_grid:
            string_grid.append(str(i))

      #Put the rows back in to the new string.
      final_grid=[]
      x=0
      while x < grid_height:
            final_grid.append(string_grid[x*grid_width:(x+1)*grid_width])
            x+=1

      #Hide the excess formatting to make the results more user friendly.
      for row in final_grid:
          print " ".join(row)
          
          

def total_neighbours(cell_index,grid):
      "Finds the number of living neighbouring cells." 
      grid_width=len(grid[0])
      grid_height=len(grid)
      grid=flatten_grid(grid)


      #Defins the indexes of neighbouring cells.
      top_left_index=cell_index-grid_width-1
      top_index=cell_index-grid_width
      top_right_index=cell_index-grid_width+1
      left_index=cell_index-1
      right_index=cell_index+1
      bottom_left_index=cell_index+grid_width-1
      bottom_index=cell_index+grid_width
      bottom_right_index=cell_index+grid_width+1

     
    #If the cell is in the corners...
      #top left
      if cell_index==0:
            #This adds up all the values in the surrounding cells.
            return grid[right_index]+grid[bottom_right_index]+grid[bottom_index]
            
      #top right
      elif cell_index==grid_width-1:
            return grid[left_index]+grid[bottom_left_index]+grid[bottom_index]
      #bottom left
      elif cell_index==grid_width*grid_height-grid_width:
            return grid[top_index]+grid[top_right_index]+grid[right_index]
      #bottom right
      elif cell_index==grid_height*grid_width-1:
            return grid[top_left_index]+grid[top_index]+grid[left_index]

    #If the cell is on the outer rows/columns...
      #top
      elif cell_index<grid_width:
            return grid[left_index]+grid[right_index]+grid[bottom_left_index]+grid[bottom_index]+grid[bottom_right_index]
      #bottom
      elif cell_index>grid_width*grid_height-grid_width:
            return grid[top_left_index]+grid[top_index]+grid[top_right_index]+grid[left_index]+grid[right_index]
      #left
      elif cell_index%grid_width==0:
            return grid[top_index]+grid[top_right_index]+grid[right_index]+grid[bottom_index]+grid[bottom_right_index]
      #right
      elif cell_index%grid_width==grid_width-1:
            return grid[top_left_index]+grid[top_index]+grid[left_index]+grid[bottom_left_index]+grid[bottom_index]

    #If the cell is in the centre...
      elif cell_index > grid_width or (cell_index <= grid_height*grid_width-1 and cell_index >= grid_height*grid_width-grid_width)or cell_index%grid_width==0 or cell_index%grid_width==grid_width-1:
            return grid[top_left_index]+grid[top_index]+grid[top_right_index]+grid[left_index]+grid[right_index]+grid[bottom_left_index]+grid[bottom_index]+grid[bottom_right_index]



def total_neighbours_test(cell_index,grid):
      "Checks whether the cell should die or remain alive by applying the Game of Life rules."
      grid_flat=flatten_grid(grid)
      
      #If the cell has exactly 2 neighbours and the cell is alive.
      if total_neighbours(cell_index,grid)==2 and grid_flat[cell_index]==1:
            #The cell lives due to Scenario 3:Survival.
            grid_flat[cell_index]=1
        
      #If the cell has exactly 3 neighbours.
      elif total_neighbours(cell_index,grid)==3:
            #The cell lives
               #If the cell was alive this is due to Scenario 3:Survival.
               #If the cell was not alive this is Scenario 4:Creation of life.
            grid_flat[cell_index]=1
        
      else:
            #The cell dies
               #If the cell had less than 2 neighbours this is due to Scenario 1:Underpopulation.
               #If the cell had more than 3 neighbours this is due to Scenario 2:Overcrowding.
               #If the grid contains no living cells, then the cell has no neighbours and Scenario 0:No interactions occurs.
            grid_flat[cell_index]=0
        
      return grid_flat[cell_index]


    
def game_of_life_single(grid):
      "Runs the Game of Life rules on every cell in the grid."

      grid_width=len(grid[0])
      grid_height=len(grid)
      
      results_list=[]
      cell_index=0

      #Makes a list of the new states of each cell after applying the Game of Life rules.
      while cell_index < grid_width*grid_height:
            results_list.append(total_neighbours_test(cell_index,grid))
            cell_index +=1

      #Turns this list back into a grid.
      results_grid=[]
      x=0
      while x < grid_height:
            results_grid.append(results_list[x*grid_width:(x+1)*grid_width])
            x+=1

      #Prints the resulting grid in an easy to read format.
      print_grid(results_grid)
      return results_grid
      

def game_of_life(grid,iterations):
      "Runs the Game of Life rules for every cell in a given grid for a given number of iterations."

      #Prints the initial grid.
      print "Initial Grid State: "
      print_grid(grid)

      #Prints the grid for each iteration requested.
      game_grid=grid
      iteration=1
      while iteration<= iterations:
           print "Iteration "+str(iteration)+": "
           game_grid=game_of_life_single(game_grid)
           iteration+=1
           



print "Game of Life for Scenario 5: Grid with no live cells."
scenario5=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
game_of_life(scenario5,1)


print "\nGame of Life for Scenario 6: Expected game outcome for seeded grid."
scenario6=[[0,0,0],[1,1,1],[0,0,0]]
game_of_life(scenario6,2)
