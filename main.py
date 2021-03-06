# Author: Shang Yuan Lim szl6038@psu.edu
# Collaborator: Shiquan Zhang spz5202@psu.edu
# Collaborator: Christian Davis ckd5367@psu.edu
# Collaborator: Mitchell Feyl mmf5871@psu.edu 
# Section: 010R
# Breakout: 14

def sum_n(n):
  if n<=1:
    return n
  else: 
    return n + sum_n(n-1)

def print_n(string, int):
  if int>0:
    print(string)
    print_n(string, int-1)



def run():
  number = input("Enter an int: ")

  number = int(number)

  added = sum_n(number)

  print("sum is " + str(added) + ".")

  string = input("Enter a string: "
  )

  print_n(string, number)


if __name__ == "__main__":
  run()