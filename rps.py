import random

while True:
	comp = random.choice(['rock','paper','scissor'])
	player = input("Choose rock, paper or scissor (or type Q to quit): ")

	if player == "Q":
		break

	if comp == player:
		print(f"Two {comp}! It's a draw.")
	if comp == "rock":
		if player == "paper":
			print("Player wins: Paper folds the rock")
		if player == "scissor":
			print("Computer wins: Rock breaks the scissor")
	if comp == "paper":
		if player == "rock":
			print("Computer wins: Paper folds the rock")
		if player == "scissor":
			print("Player wins: Scissor cuts the paper")
	if comp == "scissor":
		if player == "rock":
			print("Player wins: Rock breaks the scissor")
		if player == "paper":
			print("Computer wins: Scissor cuts the paper")