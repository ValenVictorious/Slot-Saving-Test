import stuff
import trace_goto
loop = 1
name = input("Name? ")
content = input("content? ")
place = input("place? ")
while(loop < 2):
  Next = input("next? ")
  if Next == "commands":
    print("""commands:
    New Save: Create a new save
    Veiw Save: Veiw saves
    end: end the program""")
  if name != "" and content != "" and place != "":
    stuff.assignStuff(name, content, place)
    Next = input("next? ")
  if Next == "veiw save":
    veiwplace = input("which file? ")
    stuff.getStuff(veiwplace)
    Next = input("next? ")
  if Next == "new save":
    name = input("name? ")
    content = input("content? ")
    place = input("place? ")
    if name != "" and content != "" and place != "":
      stuff.assignStuff(name,content,place)
    Next = input("next? ")
  if Next == "end":
    loop = 2
    print("""ended
    to continue type "continue"
    to end type "terminate"
    """)
    Next = input("next? ")
if Next == "continue" and loop == 2:
  loop = 1
  trace_goto.goto(7)
if Next == "terminate" and loop == 2:
  print("termenated", end="-" )