R, O, C = map(int, input().split())

runs_needed_for_victory = (R - C + 1)
no_of_overs_left = (20 - O)
no_of_balls_left = (no_of_overs_left)*6
max_runs_that_can_be_made = (no_of_balls_left)*6

if ((max_runs_that_can_be_made) >= (runs_needed_for_victory)):
    print("YES")
else:
    print("NO")
    
    
    
    
