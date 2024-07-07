print("You are in a dark room. You have to find a way to escape. You have to know that things may not be as they seem. At the end of the day survival is not guaranteed. You have to make the right choices.Monsters are everywhere.")
print("What do you do?")
choice1= input("Type 'Turn on the light' or 'Scream for help.'")
choice1l=choice1.lower()
if choice1l== "turn on the light":
          print("The torch lights up the room. You see a door. What do you do?")
          choice2= input("Type 'Walk further.' or 'Break the door'")
          choice2l= choice2.lower()
          if choice2l=='walk further':
                            print("The next room is open. You find a four-legged monster in the room. It wants to fight you.")
                            choice3= input('Type "Run" or "Fight"')
                            choice3l= choice3.lower()
                            if choice3l=="run":
                                      print("The monster chases you and eats you. Game over.")
                            elif choice3l=="fight":
                                        print("You defeat the monster and now you are the monster. You also find a key. At the edge of the room, you see a door but there's someone guarding it. What do you do?")
                                        choice4= input("Type 'Convince him you are not a monster' or 'Fight'")
                                        choice4l= choice4.lower()
                                        if choice4l=="convince him you are not a monster":
                                                     print("Your persuasion skills are very poor. He kills you. Game over.")
                                        elif choice4l=="fight":
                                                     print("You have escaped into the outer world. But you die due to a nuclear meltdown. Game over.")
                                        else:
                                                     print("Game over.")
                            else: 
                                      print("Game over.")
          elif  choice2l=='break the door':
                    print("You break the door and at the other side you find a man. There is a tunnel at the end of the door. But only one man can enter. What do you do?")
                    choice5=input("Type 'Talk to him' or 'Ignore him'")
                    choice5l= choice5.lower()
                    if choice5l=="talk to him":
                              print("He says he's hungry. He asks you for some food. What do you do?")
                              choice6=input("Type 'Give him something to eat.' or 'Run away' or 'Kill him'")
                              choice6l= choice6.lower()
                              if choice6l=='give him something to eat.':
                                        print("He kills you and eats you. Game over. Bro was just hungry.")
                              elif choice6l== 'run away':
                                        print("When you tried to run away he stopped from escaping and now you have killed each other. Game over.")
                              elif choice6l=='kill him':
                                        print('You are now free to escape. What do you do?')
                                        choice7= input("Type 'Run away' or 'Stay in the room forever.'")
                                        choice7l=choice7.lower()
                                        if choice7l== 'stay in the room forever':
                                                  print("Congratulations! You have narrowly escaped a nuclear meltdown by staying in the room forever. You win!")
                                        elif choice7l=='run away':
                                                      print("You escaped into the world but you died after a nuclear meltdown happened.Game over.") 
                                        else:
                                                      print("Game over.")
                              else:
                                        print("Game over.")
                    elif choice5l=='ignore him':
                              print("He has killed you. Game over.")
                    else:
                              print("Game over.")
          else:      print("Game over.")
if choice1l=='scream for help':
          print("You scream for help.But a monster hears you and eats you. Game over.")
else:
          print('Game over.')
          
                              
                    












