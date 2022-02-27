#To_Make_A_Square:-
    
#def  turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#def turn_around():
#    turn_right()
#    move()    
#turn_left()
#move()
#turn_around()
#turn_around()
#turn_around()

                 #Hurdle Challange(1):-

def turn_right():
 turn_left()
 turn_left()
 turn_left()

def pass_one_hurdle():
# move()
 turn_left()
 while wall_on_right():
       move()

 turn_right()
 move()
 turn_left()
 turn_left()
 turn_left()
 while front_is_clear():
        move()
 turn_left()       
 
# move()
# turn_left()

              #By_using_for_loop:-
#for p in range(0,6):
#    pass_one_hurdle()

             #By_Using_while_loop:-
#number_of_hurdle = 6
#while number_of_hurdle > 0:
#   pass_one_hurdle()
#   number_of_hurdle -= 1
    
                #Hurdle_Race_2:-
                   #Method(1):-
#while at_goal() != True:
#  pass_one_hurdle()
                  #Method(2):-
#while not at_goal():
#  pass_one_hurdle()
    
                  #Hurdle_3:- 
while not at_goal():
   if wall_in_front():
    pass_one_hurdle()
   else:
    move()
      
