n = 10
while n == 10:
  import string
  import random
  print("""
                            ____    ___ ____  ____ 
                           |    \  /  _|    \|    |
                           |  o  )/  [_|  _  ||   | 
                           |     |    _|  |  ||   | 
                           |  O  |   [_|  |  ||   | 
                           |     |     |  |  ||   | 
                           |_____|_____|__|__|____|
  """)
  decoding = input("Are you decoding? (T/F)") #true to reverse, false to create
  if decoding == "T":
      decoding = True
      putmessagehere = input("Add your coded message here.") #add message here
  elif decoding == "F":
      decoding = False
      putmessagehere = input("Add your needed-to-be-coded message here.") #add message here
  else:
      print("Invalid input")
      exit()
  incode = ""
  coded = ""
  something = ""
  msglength3 = round(len(putmessagehere)/2) - 1
  msglength1 = range(len(putmessagehere))
  msglength2 = len(putmessagehere) - 1
  codedmessage = "" #dont touch
  for index in msglength1:
      if putmessagehere == "":
          break
      if decoding == False:
          char = putmessagehere[msglength2]
          msglength2 += -1
          coded += char
          coded += random.choice(string.ascii_lowercase)
      if decoding == True:
          for index in msglength1:
              if index % 2 != 1:
                  char = putmessagehere[index]
                  incode += char
          char = incode[msglength3]
          msglength3 += -1
          coded += char
  if decoding == False:
      print("Here is your coded message. Try our decoder!")
      print(coded)
  if decoding == True:
      print("Here is your decoded message. Try our coder!")
      print(coded[:round(len(coded)/2)])















