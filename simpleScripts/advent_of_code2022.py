
loop_flag = True
current_move = 0
counter = 0
increased = 0
level_track = []

while(loop_flag):
  print("What's your next move?")
  current_move = int(input())
  print("Your current input is: "+str(current_move))
  level_track.append(current_move)
  if(counter != 0 and level_track[counter]-level_track[counter-1] > 0 ):
    print("Increase!")
    increased+=1
  if(current_move == 0):
    loop_flag = False
  counter+=1

for i in range(len(level_track)):
  print(level_track[i])
print("Total increased: "+str(increased))

