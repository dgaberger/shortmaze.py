maze = [
	[ "[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]"],
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","  ","  ","[]"], 
	[ "[]","  ","[]","  ","  ","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","  ","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","  ","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]","  ","[]"], 
	[ "[]","  ","[]","  ","[]","  ","  ","  ","[]","  ","  ","  ","[]","  ","[]"], 
	[ "[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]","[]"]
]

lc = [1,1]
count = 0
move = "" 

while lc != [10, 13] and move != "quit" and count < 200:

	count += 1

	maze[lc[0]][lc[1]] = "@@"
	
	def print_board(board):
		for i in board:
			print("".join(str(x) for x in i))
	
	print_board(maze)	
	
	move = raw_input("enter up, down, left or right: ")
	
	if move == "down" and maze[lc[0]+1][lc[1]] == "  ":
		maze[lc[0]][lc[1]] = "  "
		lc = [lc[0]+1,lc[1]]

	elif move == "up" and maze[lc[0]-1][lc[1]] == "  ":
		maze[lc[0]][lc[1]] = "  "
		lc = [lc[0]-1,lc[1]]

	elif move == "left" and maze[lc[0]][lc[1]-1] == "  ":
		maze[lc[0]][lc[1]] = "  "

	elif move == "right" and maze[lc[0]][lc[1]+1] == "  ":
		maze[lc[0]][lc[1]] = "  "
		lc = [lc[0],lc[1]+1]
		
	elif move in ["down", "up", "right", "left"]:
		print("you cannot go there, there is a wall.")

	elif move == "quit":
		print("exiting the game")

	elif move not in ["down", "up", "right", "left", "quit"]:
		print("command not recognized")
