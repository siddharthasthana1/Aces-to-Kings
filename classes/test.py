import inquirer
hand = [5,8,3,34,6,9,3]
question1 = [inquirer.Checkbox('CreateNewSet', message = "Choose cards to create a new set", choices=['yes','no'])]
answer1 = inquirer.prompt(question1)
