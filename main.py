#TODO: Create a letter using starting_letter.txt 
with open("./Input/Letters/starting_letter.txt") as starting_letter:
  letter = starting_letter.read()
  
with open("./Input/Names/invited_names.txt") as names:
  invited_names = []
  for line in names:
    invited_names.append(line.strip())
#Replace the [name] placeholder with the actual name.
letters = []
for name in invited_names:
  # create file name
  file_name = "Letter_for_" + name + ".txt"
  letters.append(file_name)

  # save data in file
  # replace [name] in letter with actual name
  # Save the letters in the folder "ReadyToSend".
  temp_letter = letter.replace('[name]', name)
  with open(f"./Output/ReadyToSend/{file_name}", "w") as file:
    file.write(f"{temp_letter}")