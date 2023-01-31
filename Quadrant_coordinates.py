#Find out the quadrant in which the given coordinates lie
#Step 1:- Start.
#Step 2:- Take inputs for X and Y.
#Step 3:- Check if both X and y are positive Print First quadrant.
#Step 4:- Else if check X is negative and Y is positive print Second quadrant.
#Step 5:- Else if check X and Y both are negative print Third quadrant.
#Step 6:- Else if check X is positive and Y is negative print Fourth quadrant.
#Step 7:- Else print X and Y are at origin.
#Step 8:- End.
def quad(x,y):
    if x>0 and y>0:
        print(x, " and", y, "lie in Quadrant 1")
    elif x<0 and y>0:
        print(x, " and", y, "lie in Quadrant 2")
    elif x<0 and y<0:
        print(x," and", y,"lie in Quadrant 3")
    elif x>0 and y<0:
        print(x, " and", y, "lie in Quadrant 4")


if __name__=="__main__":
    quad(2,-4)
    quad(2,5)
    quad(-4,-7)
    quad(-3,9)