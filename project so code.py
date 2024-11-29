import random

done= False
wins, losses, ties=0 , 0 , 0
P='Yes'

names= {'R': 'Rock' , 'P': 'Paper' , 'S': 'Scissors' }

while not done :
    
   
   
    if P == 'Yes' :
        
        choice = input('Please chose your next move (R , P , S) (Q to Quit)')
        cpu_choice= random.choice([ 'R' , 'P' , 'S'])
        if choice == cpu_choice :
          print(f"it is a tie You both chose {names [choice]}")
          ties += 1
        elif choice == 'R':
           if cpu_choice == 'P':
              print(f'computer wind ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
              losses += 1
           else:
               print(f'You wind  ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
               wins += 1 
        elif choice == 'P':
            if cpu_choice == 'S':
               print(f'computer wind ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
               losses += 1
            else:
               print(f'You wind ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
               wins += 1  
        elif choice == 'S':
           if cpu_choice == 'R':
            print(f'computer wind ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
            losses += 1
           else:
            print(f'You wind ! You chose {names[choice]}, The computer chose {names[cpu_choice]}.')
            wins += 1 
        elif  choice == 'Q':  
           done = True
        else:
          print ('Inviled Comand')
    
        print(f'Curant States : {wins} Wins , {losses} losses , {ties} Ties')
        P = input('Do You Want Play Game Again (Yes Or No)')
 
    else :
       print('Thanks for playing! Goodbye!')
       done = True

      