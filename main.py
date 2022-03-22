import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
def exercise():
  mylist = []
  for x in range(4):
    mylist.append(int(input("Please enter a number: ")))
  for i in range(4):
    print(mylist[i])
  mylist[0], mylist[-1] = mylist[-1], mylist[0]
  for j in range(4):
    print(mylist[j])

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
    exercise()
