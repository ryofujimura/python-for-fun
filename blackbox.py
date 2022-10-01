#python tic tac toe game with a blackbox AI?
'''
pro:
- it took 2sec to code all this
- basics are done
cons:
- no function
- no error output
- no overlap check
- random placement isnt good enough to win
- would be better with plays and win/loose count
'''
import random
row1=None
column1=None
row2 = None
column2 = None
print("Welcome to TIC-TAC-TOE!!")
tic=input("Enter O or X as your choice --> ")
if tic=='O':
    tac='X'
else:
    tac='O'
block=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
i=0
choice=int(input("Enter 1 for Head and 0 for Tail --> "))
x=random.randint(0,1)
if choice==x:
    print("You won the toss you get the first chance : ")
    print("## Enter the row and column you want to put your choice in ##")
    row1=int(input("Row --> "))
    column1=int(input("Column --> "))
    block[row1-1][column1-1]=tic
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])
    index1=0
    index2=0
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif i%2!=0:
            print("## A.I ##")
            if row2!=None and column2!=None:
                row2=random.randint(1,3)
                while block[row2-1][0]!=' ' and block[row2-1][1]!=' ' and block[row2-1][2]!=' ':
                    row2=random.randint(1,3)
                column2=random.randint(1,3)
                while block[row2-1][column2-1]!=' ':
                    column2=random.randint(1,3)
            else:
                row2=random.randint(1,3)
                column2=random.randint(1,3)
                while block[row2-1][column2-1]!=' ':
                    column2=random.randint(1,3)
            block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2==0:
            print('## Your Turn ##')
            row1=int(input("Row --> "))
            column1=int(input("Column --> "))
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        if block[0][0]!=' ' and block[0][1]!=' ' and block[0][2]!=' ' and block[1][0]!=' ' and block[1][1]!=' ' and block[1][2]!=' 'and block[2][0]!=' ' and block[2][1]!=' 'and block[2][2]!=' ':
            print("Draw!!")
            break
else:
    print("## A.I won the toss ##")
    print("## A.I ##")
    row2=random.randint(1,3)
    column2=random.randint(1,3)
    block[row2-1][column2-1]=tac
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif i%2==0:
            print("## A.I ##")
            row2=random.randint(1,3)
            while block[row2 - 1][0] != ' ' and block[row2 - 1][1] != ' ' and block[row2 - 1][2] != ' ':
                row2 = random.randint(1, 3)
            column2=random.randint(1,3)
            while block[row2-1][column2-1]!=' ':
                column2=random.randint(1,3)
            block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2!=0:
            print("## Your Turn ##")
            row1=int(input("Row --> "))
            column1=int(input("Column --> "))
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        if block[0][0]!=' ' and block[0][1]!=' ' and block[0][2]!=' ' and block[1][0]!=' ' and block[1][1]!=' ' and block[1][2]!=' 'and block[2][0]!=' ' and block[2][1]!=' 'and block[2][2]!=' ':
            print("Draw!!")
            break
print("Thanks for playing!!")


