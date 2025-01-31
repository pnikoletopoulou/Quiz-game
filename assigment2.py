
from time import sleep
import csv 

# Function to load existing accounts from the csv file 
def load_accounts():
    accountsfile = open( 'accounts.csv', 'r')
    lines = accountsfile.readlines() 

    accounts = {}
    
    for line in lines:
        parts = line.strip().split(',') 
        if len(parts) < 2: 
            continue
        if parts[0] != 'username':
            account = {'username': parts[0], 'password': parts[1]}   
            accounts[parts[0]] = account
    return accounts

# Function to check if the login 
def check_login(username, password, accounts):
    if username in accounts:
        account = accounts[username]
        if account['password'] == password:
            return account
        
# Open the csv file in append to add new accounts 
accountsfile = open( 'accounts.csv', 'a')
w = csv.writer(accountsfile)

# Load accounts
accounts = load_accounts()

# Welcome message 
print("Welcome to the Quiz game!")
sleep(1)

# Loop for login and register 
while True:
    
    s = input("Do you have an account?(yes/no)")
    s = s.lower()

    # Option to register 
    if s == "no":
        r = input("Do you want to register?(yes/no)").strip().lower()
        if r == "no":
            exit()
        if r == "yes":
            
            # Loop to register 
            while True:
               username = input("Username: ")
               # Check if the username exists
               if username in accounts:
                    print("This username already exists.")
                    sleep(1)
                    print("Please choose another one!")
                    sleep(1)
               elif username  not in accounts :
                    password = input("Pin:")
                    # Write new account to csv file
                    w.writerow([username, password])
                    print("You are ready!")     
                    break
    elif s == "yes":
       # Loop for login
       while True:
       
        def login_prompt():
           # Login in an existing account 
           username = input("Username: ")
           password = input("Pin:")
           return username,password
        username, password = login_prompt()
        # Check if the username and password are correct
        if username in accounts and accounts[username]['password'] == password:
            print("Welcome", username)
            break
        else:
           print("Invalid username or password!")
           sleep(1)
           print("Try again")
        
    else:
      print("You need to answer with 'yes' or 'no'!")
      sleep(2) 
      # Restart the loop to answer yes or no
      continue
    break

# Starting the quiz 
sleep(1)
print("Lets start!") 

import requests 
import html
import random 
from datetime import datetime

# Open the score file 
score = open('score.csv', 'a')
write = csv.writer(score)

url = 'https://opentdb.com/api.php?amount=5&type=multiple'

# Function for new questions
def new_q():
  response = requests.get(url)
  data = response.json()
  return data['results']

# Loop for the quiz
while True:

  results = new_q()
  counter = 0
  round_score = 0
  
  # Loop to ask 5 questions are asked per round
  while counter < 5:
      
      item = random.choice(results)
      results.remove(item) 
      q = html.unescape(item['question'])
      sleep(1)
      print("Q: ", q)
      counter += 1 
      sleep(1)

      ca = html.unescape(item['correct_answer'])
      answers = [ca]
      
      # Add the incorrect answers 
      for enrty in item['incorrect_answers']:
            ia = html.unescape(enrty)
            answers.append(ia)
      
      # shuffle the answers
      random.shuffle(answers)

      s = ['a)', 'b)', 'c)', 'd)']
      for i in range(len(s)):
        print(s[i], answers[i])

      answer = input("type your answer(a,b,c or d):").lower()

      # Loop to make sure the answer is valid
      while True:

        if answer not in ['a', 'b', 'c', 'd']:
          print("Your answer is not valid!")
          sleep(1)
          print("Choose one of the following:")
          sleep(1)
          for i in range(len(s)):
            print(s[i], answers[i])
          answer = input("type your answer(a,b,c or d):").lower()

        a = s.index(answer + ')')
        sel_answer = answers[a]

        if sel_answer == ca:
           # if guess the asnwer increase score
           round_score += 1
           print("Your answer is correct!")
        else:
           print("Your answer is incorrect. The correct answer was:", ca)
             
        sleep(1)
        # Informing the user about their current score 
        print("Your current round score is", round_score, "/5")
        break

  # End of the round 
  sleep(1)
  print("Round over!")
  sleep(1)
  print("Final score for this round:", round_score, "/5")

  # save on the csv file the information of the user
  write.writerow([username, password, datetime.now(), round_score])

  # Loop to ask if the user wants to play again
  while True:
           
    sleep(1)
    play_again = input("Do you want to play again?(yes/no)").lower()
      
    if play_again == 'yes':
       print("Let's continue!")  
       break
    elif play_again == 'no':      
       print("Thanks for playing!")
       exit()
    else:
       print("Please answer with 'yes' or 'no'!")