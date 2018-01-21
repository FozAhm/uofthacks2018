import datetime, threading, time

next_call = time.time()

elbowData = []
headData = []

counter = 0

elbowPosition = [0,0,0,0]
headPosition = [0,0,0,0]
velocties = [0,0,0,0]

attemps = 0
success = 0

goingDown = True

def main():

  global next_call
  global attemps
  global success
  global data
  global counter

  print(datetime.datetime.now())

  elbowPosition.insert(0, elbowData[counter])
  elbowPosition.pop()

  headPosition.insert(0, headData[counter])
  headPosition.pop()

  velocties.insert(0, headPosition[0] - headPosition[1])
  velocties.pop()

  if(velocties[0] <= 0 and velocties[1] <=0):
      goingDown = True
  elif(velocties[0] >= 0 and velocties[1] >=0):
      goingDown = False
      attemps += 1

      if(headPosition[2] <= (elbowPosition[2] +20)):
          success +=1

  next_call = next_call+0.20
  counter +=1
  threading.Timer( next_call - time.time(), main ).start()

main()
