import itertools
n = int(raw_input("Enter the dimension of the board. "))
print "For a chess board of size " + str(n) + "x" + str(n)

def onboard(x,y,n):
  if(x<=n and y<=n and x>0 and y>0):
    return True
  else :
    return False

def check(a,b,z,l):
  state = False
  for i in range(len(l)):
    if(i != z):
      if(a==l[i].x and b==l[i].y):
	state = True
  return state

class point(object):
  def __init__(self, x=None, y=None):
    self.x = x
    self.y = y

def configuration(positions):
  clash = False
  i = 0
  while(i<n and clash==False):
    for j in range(n):
      if(onboard(positions[i].x+j,positions[i].y+j,n)):
	if(check(positions[i].x+j,positions[i].y+j,i,positions) == True):
	  clash = True
      if(onboard(positions[i].x+j,positions[i].y-j,n)):
	if(check(positions[i].x+j,positions[i].y-j,i,positions) == True):
	  clash = True
      if(onboard(positions[i].x-j,positions[i].y+j,n)):
	if(check(positions[i].x-j,positions[i].y+j,i,positions) == True):
	  clash = True
      if(onboard(positions[i].x-j,positions[i].y-j,n)):
	if(check(positions[i].x-j,positions[i].y-j,i,positions) == True):
	  clash = True
    i = i+1
  return clash
count = 0
pos = []
permut = []
for i in range(n):
  pos.append(point(i+1,1))
for i in range(n):
  permut.append(1+i)
all_permut = list(itertools.permutations(permut, n))
for i in range(len(all_permut)):
  pos = []
  for j in range(n):
    pos.append(point(j+1,all_permut[i][j]))
  if(configuration(pos) == False):
    count = count +1
    print("Solution No. "+str(count))
    for k in range(n):
      print "Position of Queen No. " + str(k+1) + " : " + str(pos[k].x) + ", " + str(pos[k].y)
if(count == 0):
  print "No solutions exist."