def q1():
  bool = True
  print (bool)

def q2():
  let = input ("Input an integer: ")
  bool = ("5" < let)
  print(bool)
 


def q3():
  wordinput = input ("Input the letter a: ")
  boolinput = (wordinput == "a")
  print (boolinput)


def q4():
  googleinput = input ("Input a word earlier in the dictionary than google: ")
  boolinput = (googleinput < "google")
  print (boolinput)

def q5():
integer1 = int(input("Input an integer: "))
integer2 = int(input("Input another integer: "))
number = integer1 * integer2
bool = (number > 40)
sentence = (f"Your numbers multiplied together are greater than 40: {bool}")
print(sentence)

#Do edit the code below
#Comment the lines below when running your tests

# q1()
# q2()
# q3()
# q4()
# q5()
