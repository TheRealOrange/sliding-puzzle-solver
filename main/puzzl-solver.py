#this is basic idea
# - identify locations of the first two pieces
# - move to center (e.g. is on side, spin 2x2 until in, if already in position, dont touch)
# - shift up, spin into position
# - continue until solved

# #We should create like a Tkinter GUI for this
#like for entering the current position
#change
print "welcome to a collabaration between an orange and a bat."
print "..."
print """
this is how you input the puzzle:
if the puzzle is in this state:
+-+-+-+
|1|2|3|
+-+-+-+
|4|5|6|
+-+-+-+
|7|8| |
+-+-+-+
type 123456780 below.
"""
print "..."
valid=True
while valid:
  try:
    raw_puzzle=int(raw_input("Input your puzzle here!"))
    print "..."
    if len(str(raw_puzzle))==9:
      valid=False
    else:
      print " please enter the correct number of digits"
      print "..."
  except ValueError:
    print "..."
    print "Input the puzzle again."
    print "..."
array=(str(raw_puzzle))
array=" ".join(array)
array=array.split()
array=[int(x) for x in array]
