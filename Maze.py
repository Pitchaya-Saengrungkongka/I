from readchar import readchar
import random,os,time

def editWalls(rand_wall):
	sc = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		sc += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		sc += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		sc += 1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		sc += 1
	if (sc < 2):
		maze[rand_wall[0]][rand_wall[1]] = 'c'
		# Upper
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
				maze[rand_wall[0]-1][rand_wall[1]] = 'w'
			if ([rand_wall[0]-1, rand_wall[1]] not in walls):
				walls.append([rand_wall[0]-1, rand_wall[1]])
		# Bottom 
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
				maze[rand_wall[0]+1][rand_wall[1]] = 'w'
			if ([rand_wall[0]+1, rand_wall[1]] not in walls):
				walls.append([rand_wall[0]+1, rand_wall[1]])
		# Left
		if (rand_wall[1] != 0):	
			if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
				maze[rand_wall[0]][rand_wall[1]-1] = 'w'
			if ([rand_wall[0], rand_wall[1]-1] not in walls):
				walls.append([rand_wall[0], rand_wall[1]-1])
    # Right
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
				maze[rand_wall[0]][rand_wall[1]+1] = 'w'
			if ([rand_wall[0], rand_wall[1]+1] not in walls):
				walls.append([rand_wall[0], rand_wall[1]+1])

def genmap():
    while (walls):
      x = random.randint(1, 6)
  	  # Random wall
      rand_wall = walls[int(random.random()*len(walls))-1]
      # Check left 
      if (rand_wall[1] != 0):
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
          editWalls(rand_wall)
    	# Check upper 
      if (rand_wall[0] != 0):
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
          editWalls(rand_wall)
    	# Check bottom 
      if (rand_wall[0] != height-1):
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
          editWalls(rand_wall)
    	# Check right 
      if (rand_wall[1] != width-1):
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
          editWalls(rand_wall)
    	# Delete wall from list
      for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
          walls.remove(wall)
      if (x==1 and rand_wall[0]!=2 and rand_wall[1]!=2 and rand_wall[0]!=height-3 and rand_wall[1]!=width-3 ):
        maze[rand_wall[0]][rand_wall[1]]='c'
    return maze

def printmaze(x):
    for i in range(height):
      for j in range(width):
        if cha[0] == i and cha[1] == j:
          if cha[2] == 1:
            print('⏫', end = "")
          if cha[2] == 2:
            print('⏩', end = "")
          if cha[2] == 3:
            print('⏬', end = "")
          if cha[2] == 0:
            print('⏪', end = "")
        else:
          if (maze[i][j] == 'c'):
            print("⬛", end="")
          else:
            print("🟥", end="")
      print("")
        
def read(maze):
  read = readchar()
  ch1=cha[0]
  ch2=cha[1]
  chd=cha[2]
  if read == 'w' and cha[2] == 1 and maze[ch1-1][ch2] == 'c':
    cha[0]=cha[0]-1
  elif read == 's' and cha[2] == 1 and maze[ch1+1][ch2] == 'c':
    cha[0]=cha[0]+1
    
  elif read == 'w' and cha[2] == 2 and maze[ch1][ch2+1] == 'c':
    cha[1]=cha[1]+1
  elif read == 's' and cha[2] == 2 and maze[ch1][ch2-1] == 'c':
    cha[1]=cha[1]-1
    
  elif read == 'w' and cha[2] == 3 and maze[ch1+1][ch2] == 'c':
    cha[0]=cha[0]+1
  elif read == 's' and cha[2] == 3 and maze[ch1-1][ch2] == 'c':
    cha[0]=cha[0]-1
    
  elif read == 'w' and cha[2] == 0 and maze[ch1][ch2-1] == 'c':
    cha[1]=cha[1]-1
  elif read == 's' and cha[2] == 0 and maze[ch1][ch2+1] == 'c':
    cha[1]=cha[1]+1
  elif read == 'd':
    cha[2]=(cha[2]+1)%4
  elif read == 'a':
    cha[2]=(cha[2]-1)%4    
  os.system('clear')
  printmaze(maze)

height = 50 #include +6 walls
width = 50 #include +6 walls
maze = [['u' for i in range(width)] for j in range(height)]
st_height = int(random.random()*height)
st_width = int(random.random()*width)
for i in range(height):
  maze[i][0] = 'w'
  maze[i][1] = 'w'
  maze[i][width-1] = 'w'
  maze[i][width-2] = 'w'
for j in range(width):
  maze[0][j] = 'w'
  maze[1][j] = 'w'
  maze[height-1][j] = 'w'
  maze[height-2][j] = 'w'
if (st_height >= height-3):
	st_height -= 3
if (st_height <= 2):
	st_height += 3
if (st_width >= width-3):
	st_width -= 3
if (st_width <= 2):
	st_width += 3  
cha=[st_height, st_width,1]
maze[st_height][st_width] = 'c'
walls = []
maze[st_height-1][st_width] = 'w'
maze[st_height][st_width-1] = 'w'
maze[st_height][st_width+1] = 'w'
maze[st_height+1][st_width] = 'w'
walls.append([st_height-1, st_width])
walls.append([st_height, st_width-1])
walls.append([st_height, st_width+1])
walls.append([st_height+1, st_width])
maze = genmap()

while True:
  read(maze)
  print("🟩🟩🟩🟩🟩🟩🟩🟩")
