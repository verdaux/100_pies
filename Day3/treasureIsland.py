print(
'''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|

      Welcome to treasure island
'''
)

show = "Game over"

first_step = input("Left or right? ")

if(first_step == "left" or first_step == "Left"):
    second_step = input("Swim or wait? ")
    if(second_step == "Wait" or second_step == "wait"):
        third_step = input("Which door? Red, Blue, or Yellow : ")
        if(third_step == "Red" or third_step == "red"):
            show = "Burned by fire"
        elif(third_step == "Blue" or third_step == "blue"):
            show = "Eaten by beasts"
        elif(third_step == "Yellow" or third_step == "yellow"):
            show = "You win"
    else:
        show = "Attacked by trout"
print(show)