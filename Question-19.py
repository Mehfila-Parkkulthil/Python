#Question 19
#conditional statements

print("Please enter color: green  or red or yellow")
light=input().strip().lower()
#works for all cases

#light = input().lower() , also if condn has to be lowercase
#light =input().upper(), also if condition has to be in uppercase
if(light=="green"):
  print("Green signal")
elif(light=="yellow"):
  print("Yellow signal")
elif(light=="red"):
  print("Red signal")
else:
  print("Signal is broke")