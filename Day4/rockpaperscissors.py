import random

scissors ='''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

'''

paper = '''

                     _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
              jgs    |    |
'''

rock = '''
        _____
    /\| | | |
    / /|_|_|_|
    \        |
     \_______/
    /______/
'''
options = [rock,paper,scissors]
comp_choices = [0,1,2]

user_selection = int(input("Choose between rock as 0, paper as 1, or scissor as 2: "))

comp_selection = random.choice(comp_choices)

#print(comp_selection)
result = "Draw"
print(f"\nYou: {options[user_selection]}, Computer: {options[comp_selection]}")

if(user_selection == comp_selection):
    print(result)
elif (user_selection == 0 and comp_selection == 2) or \
         (user_selection == 1 and comp_selection == 0) or \
         (user_selection == 2 and comp_selection == 1):
        print("You win!")
else:
    print("You lose.")