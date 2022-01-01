#This kind of function should seem familiar...
def f(x):
  return 3*x + 2

def g(x):
  #In order to indicate that this function isn't defined yet, and that we need to define it later,
  #We put pass as its only line of code

  #Change the code in this function so that it returns the squared value of x (would graph as a parabola)
  pass

def main():
  print("Let's see what f(x) gives us for different values of x")
  print(f(3))
  print(f(4))

  print("What about g(x)?")
  print(g(0))
  print(g(1))
  print(g(2))
  print(g(3))


#The line below is a call to the function we defined above
main()