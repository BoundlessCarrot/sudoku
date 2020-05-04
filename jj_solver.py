# completely unfinished, gonna take a min to think. don't know how to select numbers to try. 

def msquare_solver(grid, free_nums = list(range(1, 10))):
    if len(free_nums) == 0:
        return grid
    
    for row in grid:
        for x in free_nums:
            if row.count(x) != 0:
                free_nums.remove(x)
        
    for row in grid:
        for box in row:
            if box != 0:
                for n in free_nums:
                    

