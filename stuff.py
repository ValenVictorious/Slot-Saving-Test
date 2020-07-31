stf1 = ""
stf2 = ""
stf3 = ""
stf4 = ""

#create data  
def assignStuff (name, content, place):
  global stf1
  global stf2
  global stf3
  global stf4
  if place == "stf1":
    stf1 = name + content
    print ("assigned to stf1")
  if place == "stf2":
    stf2 = name + content
    print ("assigned to stf2")
  if place == "stf3":
    stf1 = name + content
    print ("assigned to stf3")
  if place == "stf4":
    stf4 = name + content
    print ("assigned to stf4")

#display data
def getStuff (place):
  if place == "stf1" and stf1 != "":
    print (stf1)
  if place == "stf1" and stf1 == "":
    print ("there is nothing in stf1")
  if place == "stf2" and stf2 != "":
    print (stf2)
  if place == "stf2" and stf2 == "":
    print ("there is nothing in stf2")
  if place == "stf3" and stf3 != "":
    print (stf3)
  if place == "stf3" and stf3 == "":
    print ("there is nothing in stf3")
  if place == "stf4" and stf4 != "":
    print (stf4)
  if place == "stf4" and stf4 == "":
    print ("there is nothing in stf1")

#remove data    
def resetStuff (place):
  global stf1
  global stf2
  global stf3
  global stf4
  if place == "stf1":
    stf1 = ""
    print("stf1 has been reset")
  if place == "stf2":
    stf2 = ""
    print("stf2 has been reset")
  if place == "stf3":
    stf3 = ""
    print("stf3 has been reset")
  if place == "stf4":
    stf4 = ""
    print("stf4 has been reset")
