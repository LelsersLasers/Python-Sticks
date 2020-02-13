oneLeft = 1
oneRight = 1
twoLeft = 1
twoRight = 1
gameOn = True

while gameOn:

	#one turn

	turnOne = True
	while turnOne:
		turnOne = False
		print("playerOne Left Hand: " + str(oneLeft))
		print("playerOne Right Hand: " + str(oneRight))
		print("playerTwo Left Hand: " + str(twoLeft))
		print("playerTwo Right Hand: " + str(twoRight))

		move = input("Move options (playerOne): [A]ttack or [S]plit. ")
		if move[0].lower() == 's':
			totalFingers = oneLeft + oneRight
			if totalFingers <= 1:
				print("You cannot split!")
				print("Try again...")
				turnOne = True
				print("")
			else:
				howManyOnRight = -1
				while howManyOnRight > totalFingers or howManyOnRight < 0 or howManyOnRight == oneRight:
					howManyOnRight = int(
					    input(
					        "How many Fingers do you want on your right hand? How have a total of "
					        + str(totalFingers) + " Fingers to split. "))

				oneRight = howManyOnRight
				oneLeft = totalFingers - howManyOnRight

		elif move[0].lower() == 'a':
			#big stuff
			if oneRight > 0 and oneLeft > 0:
				whichHand = input(
				    "Do you want to attack with your [r]ight or [l]eft hand: ")
				if whichHand[0].lower() == 'r':
					theirHands = input(
					    "Which hand do you want to attack? (r/l) ")
					if theirHands[0].lower() == 'r':
						if twoRight > 0:
							twoRight = oneRight + twoRight
						else:
							print("You cannot attack that hand!")
							print("Try again...")
							turnOne = True
							print("")
					else:
						if twoLeft > 0:
							twoLeft = oneRight + twoLeft
						else:
							print("You connot attack that hand!")
							print("Try again...")
							turnOne = True
							print("")
				else:
					theirHands = input(
					    "Which hand do you want to attack? (r/l) ")
					if theirHands[0].lower() == 'r':
						if twoRight > 0:
							twoRight = oneLeft + twoRight
						else:
							print("You cannot attack that hand!")
							print("Try again...")
							turnOne = True
							print("")
					else:
						if twoLeft > 0:
							twoLeft = oneLeft + twoLeft
						else:
							print("You cannot attack that hand")
							print("Try again...")
							turnOne = True
							print("")

			elif oneRight <= 0:  #force left handed attack
				theirHands = input(
				    "Which hand do you want to attack? (r/l) (Note: you are attacking with your left hand!) "
				)
				if theirHands[0].lower() == 'r':
					if twoRight > 0:
						twoRight = oneLeft + twoRight
					else:
						print("You cannot attack that hand!")
						print("Try again...")
						turnOne = True
						print("")
				else:
					if twoLeft > 0:
						twoLeft = oneLeft + twoLeft
					else:
						print("You cannot attack that hand")
						print("Try again...")
						turnOne = True
						print("")
			else:  # force right
				theirHands = input(
				    "Which hand do you want to attack? (r/l) (Note: you are attacking with your right hand!) "
				)
				if theirHands[0].lower() == 'r':
					if twoRight > 0:
						twoRight = oneRight + twoRight
					else:
						print("You cannot attack that hand!")
						print("Try again...")
						turnOne = True
						print("")
				else:
					if twoLeft > 0:
						twoLeft = oneRight + twoLeft
					else:
						print("You connot attack that hand!")
						print("Try again...")
						turnOne = True
						print("")

	print("")
	#two turn

	if oneRight > 4 or oneRight < 0:
		oneRight = 0
	if oneLeft > 4 or oneLeft < 0:
		oneLeft = 0
	if twoRight > 4 or twoRight < 0:
		twoRight = 0
	if twoLeft > 4 or twoLeft < 0:
		twoLeft = 0

	print("playerOne Left Hand: " + str(oneLeft))
	print("playerOne Right Hand: " + str(oneRight))
	print("playertwo Left Hand: " + str(twoLeft))
	print("playerTwo Right Hand: " + str(twoRight))

	if oneRight == 0 and oneLeft == 0:
		print("playerTwo wins!")
		gameOn = False
	elif twoRight == 0 and twoLeft == 0:
		print("playerOne wins!")
		gameOn = False

	turnTwo = True
	while turnTwo:
		turnTwo = False
		move = input("Move options (playerTwo): [A]ttack or [S]plit. ")

		if move[0].lower() == 's':
			totalFingers = twoLeft + twoRight
			if totalFingers <= 1:
				print("You cannot split!")
				print("Try again...")
				turnTwo = True
				print("")
			else:
				howManyOnRight = -1
				while howManyOnRight > totalFingers or howManyOnRight < 0:
					howManyOnRight = int(
					    input(
					        "How many Fingers do you want on your right hand? How have a total of "
					        + str(totalFingers) + " Fingers to split. "))

					twoRight = howManyOnRight
					twoLeft = totalFingers - howManyOnRight

		elif move[0].lower() == 'a':
			#stuff
			if twoRight > 0 and twoLeft > 0:
				whichHand = input(
				    "Do you want to attack with your [r]ight or [l]eft hand: ")
				if whichHand[0].lower() == 'r':
					theirHands = input(
					    "Which hand do you want to attack? (r/l) ")
					if theirHands[0].lower() == 'r':
						if oneRight > 0:
							oneRight = twoRight + oneRight
						else:
							print("You cannot attack that hand!")
							print("Try again...")
							turnTwo = True
							print("")
					else:
						if oneLeft > 0:
							oneLeft = twoRight + oneLeft
						else:
							print("You connot attack that hand!")
							print("Try again...")
							turnTwo = True
							print("")
				else:
					theirHands = input(
					    "Which hand do you want to attack? (r/l) ")
					if theirHands[0].lower() == 'r':
						if oneRight > 0:
							oneRight = twoLeft + oneRight
						else:
							print("You cannot attack that hand!")
							print("Try again...")
							turnTwo = True
							print("")
					else:
						if oneLeft > 0:
							oneLeft = twoLeft + oneLeft
						else:
							print("You cannot attack that hand")
							print("Try again...")
							turnTwo = True
							print("")

			elif twoRight <= 0:  #force left handed attack
				theirHands = input(
				    "Which hand do you want to attack? (r/l) (Note: you are attacking with your left hand!) "
				)
				if theirHands[0].lower() == 'r':
					if oneRight > 0:
						oneRight = twoLeft + oneRight
					else:
						print("You cannot attack that hand!")
						print("Try again...")
						turnTwo = True
						print("")
				else:
					if oneLeft > 0:
						oneLeft = twoLeft + oneLeft
					else:
						print("You cannot attack that hand")
						print("Try again...")
						turnTwo = True
						print("")
			else:  # force right
				theirHands = input(
				    "Which hand do you want to attack? (r/l) (Note: you are attacking with your right hand!) "
				)
				if theirHands[0].lower() == 'r':
					if oneRight > 0:
						oneRight = twoRight + oneRight
					else:
						print("You cannot attack that hand!")
						print("Try again...")
						turnTwo = True
						print("")
				else:
					if oneLeft > 0:
						oneLeft = twoRight + oneLeft
					else:
						print("You connot attack that hand!")
						print("Try again...")
						turnTwo = True
						print("")

	print("")
	if oneRight > 4 or oneRight < 0:
		oneRight = 0
	if oneLeft > 4 or oneLeft < 0:
		oneLeft = 0
	if twoRight > 4 or twoRight < 0:
		twoRight = 0
	if twoLeft > 4 or twoLeft < 0:
		twoLeft = 0

	if oneRight == 0 and oneLeft == 0:
		print("playerTwo wins!")
		gameOn = False
	elif twoRight == 0 and twoLeft == 0:
		print("playerOne wins!")
		gameOn = False
