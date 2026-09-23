import random
count_rock = 0
count_paper = 0
count_scissors = 0
rock = 0
paper = 1
scissors = 2
#update_counts() function.
def update_count(user_input):
  global count_rock, count_paper, count_scissors
  if user_input == 0:
    count_rock+=1
  elif user_input == 1:
    count_paper+=1
  elif user_input == 2:
    count_scissors+=1

#predict() function.
def predict():
  if count_rock > count_paper and count_rock > count_scissors :
    pred1 = 0
  elif count_paper > count_rock and count_paper > count_scissors :
    pred1 = 1
  elif count_scissors > count_rock and count_scissors > count_paper :
    pred1 = 2
  else:
    pred1 = random.randint(0,2)
  return pred1

#player_score and comp_score variables.
player_score = 0
comp_score = 0
def update_score(user_input) :
  global player_score, comp_score
  pred = predict()
  if user_input == 0:
    if pred == 0:
      print("\nYOU PLAYED ROCK, COMPUTER PLAYED ROCK.")
      print("\nCOMPUTER SCORE :", comp_score,"\nYOUR SCORE:",player_score)
    elif pred == 1 :
      print("\nYOU PLAYED ROCK, COMPUTER PLAYED PAPER.")
      comp_score+=1
      print("\nCOMPUTER SCORE:",comp_score,"\nYOUR SCORE:",player_score)
    elif pred == 2:
      print("\nYOU PLAYED ROCK, COMPUTER PLAYRD SCISSORS.")
      player_score+=1
      print("\nCOMPUTER SCORE :",comp_score,"\nYOUR SCORE:",player_score)
  elif user_input == 1 :
    if pred == 0 :
      print("\nYOU PLAYED PAPER, COMPUTER PLAYED ROCK")
      player_score+=1
      print("\nCOMPUTER SCORE :",comp_score,"YOUR SCORE :",player_score)
    elif pred == 1 :
      print("\nYOU PLAYED PAPER, COMPUTER PLAYED PAPER")
      print("\nCOMPUTER SCORE:",comp_score,"\nYOUR SCORE :",player_score)
    elif pred == 2 :
      print("\nYOU PLAYED PAPER, COMPUTER PLAYED SCISSORS")
      comp_score+=1
      print("\nCOMPUTER SCORE :", comp_score,"YOUR SCORE :",player_score)
  elif user_input == 2:
    if pred == 0 :
      print("\nYOU PLAYED SCISSORS, COMPUTER PLAYED ROCK")
      comp_score+=1
      print("\nCOMPUTER SCOREW:",comp_score, "YOUR SCORE",player_score)
    elif pred == 1 :
      print("\nYOU PLAYER SCISSORS, COMPUTER PLAYED PAPER")
      player_score+=1
      print("\nCOMPUTER SCORE :",comp_score, "\nYOUR SCORE :",player_score)
    elif pred == 2 :
      print("\nYOU PLAYED SCISSORS, COMPUTER PLAYED SCISSORS")
      print("\nCOMPUTER SCORE :",comp_score,"\nYOUR SCORE :",player_score)


valid_entries = ['0', '1', '2']
# Main loop
while True:
  user_input = input("enter 0 for rock, 1 for paper and 2 for scissors")
  if user_input not in valid_entries :
    print("INVALID ENTRY")
    user_input = input("enter 0 for rock, 1 for paper and 2 for scissors")
  user_input = int(user_input)
  update_score(user_input)
  update_count(user_input)
  
  if comp_score == 10 :
    print("COMPUTER WON")
    break



  elif player_score == 10:
    print("YOU WON")
    break


