#
# Name : Austin Whittaker
#
# Date : 4/25/2021
#
# Purpose: This program showcases the uses of the Binary search tree with help of the BST_driver
#
# Algorithm: Use of insert by using a random number generator. Search with input from the user.
#            Delete with input from the user. Traversals, and a visual of a binary search
#            using turtle graphics.
#
#
# Resources: Dr. Pence csc 231 class, notes, lectures, books and powerpoints
#                - 4/12 - 4-25
#
##################################################################

from BST_Driver import *
import turtle
import random


def main():
    '''
        This function is to showcase the binary search tree
    :return: None
    '''


    print('Welcome back for another lab!')
    print()
    print()
    print('Quick Note: I used inputs to be able to progress, If you hit enter and nothing happens')
    print('press backspace and then enter again')
    print()
    myBST = BinarySearchTree()

    print()
    print('Generating a random list...')
    print()

    randomList = []
    for i in range(0,15):
        n = random.randint(1,200)
        if n not in randomList:
            randomList.append(n)


    print('Here is the list of numbers:',randomList)
    print()
    input('Now adding list to binary search tree. Press enter to continue:')

    for num in randomList:
        myBST.insert(num)
    print('-----------------------------------------------------------------------------')

    print()
    print()
    print('-'*15,'Tree','-'*15)
    print()
    print()
    myBST.printTree(myBST.root,0)

    print()
    print()

    print('Traverse In-order:')
    myBST.traverse_inorder(myBST.root)

    print()
    print()
    print('Traverse Pre-order:')
    myBST.traverse_preorder(myBST.root)
    print()
    print()
    print('Traverse Post-order:')
    myBST.traverse_postorder(myBST.root)

    print()
    input('Here is the tree created and the traversals. Press enter to continue:')
    print('-----------------------------------------------------------------------------')


    print('Number of leaves: ', myBST.leaf)
    for num in myBST.leaflist:
        myBST.__contains__(num)
    print('-----------------------------------------------------------------------------')
    print()
    print(' Data Collected')
    print("''''''''''''''''")
    print()
    print('Maxheight: ',myBST.max_height())

    print('Max height on left: ', myBST.maxLeftHeight)

    print('Max height on right: ', myBST.maxRightHeight)
    print()
    print('Number of leaves: ', myBST.leaf)
    print(myBST.leaflist)
    print()
    print('All leaves on the left:')
    print(myBST.leaflistLeft)
    print()
    print('All leaves on the right:')
    print(myBST.leftlistRight)
    print()
    print('The highest leaf: ')
    print(myBST.biggestLeaf)
    print()
    print('The size of the BST is:',len(myBST))
    print()
    print('-----------------------------------------------------------------------------')
    print()
    input('Press enter to continue:')
    print('-----------------------------------------------------------------------------')




    print()
    print('  Searching  ')
    print("'''''''''''''")
    print()
    print()
    print('-'*15,'Tree','-'*15)
    print()
    print()
    myBST.printTree(myBST.root,0)
    print()
    print()
    print(randomList)

    searchNum = input('From the numbers above, enter a number you would like to search for:')
    if searchNum != type(int):
        try:
            searchNum = int(searchNum)
        except:
                searchNum = input('From the numbers above, enter a number you would like to search for:')


    print('is',searchNum,'in tree', (int(searchNum) in myBST))


    print()


    input('Press enter to continue:')
    print()
    print('-----------------------------------------------------------------------------')
    print()





    print('  Delete  ')
    print("''''''''''")
    print()
    print()
    print('-'*15,'Tree','-'*15)
    print()
    print()
    myBST.printTree(myBST.root,0)
    print()
    print()
    print(randomList)
    deleteNum = input('From the numbers above, enter a number you would like to delete:')
    if deleteNum != type(int):
        try:
            deleteNum = int(searchNum)
        except:
            deleteNum = input('From the numbers above, enter a number you would like to delete:')




    myBST.delete(int(deleteNum))

    print('-----------------------------------------------------------------------------')


    print()

    print()
    myBST.printTree(myBST.root,0)
    print()



    print('Traverse In-order:')
    myBST.traverse_inorder(myBST.root)

    print()
    print()
    print('Traverse Pre-order:')
    myBST.traverse_preorder(myBST.root)
    print()
    print()
    print('Traverse Post-order:')
    myBST.traverse_postorder(myBST.root)
    print()


    print('The size of the BST is:',len(myBST))
    print()

    answer = 'a'
    answer = input('Do you want to see the visual of a tree using turtle graphics? (y/n):')
    answer = answer.upper()
    while answer != 'Y' and answer !='N':
        try:
            answer = input('Do you want to see the visual of a tree using turtle graphics? (y/n):')
            answer = answer.upper()
        except:
            print('whoops lets try that again: ')
            answer = input('Do you want to see the visual of a tree using turtle graphics? (y/n):')
            answer = answer.upper()

    if answer == 'Y':
        turtle_graphics()

    else:
        return






    return


def turtle_graphics():
    turtle.penup()
    turtle.goto(-300, -25)
    turtle.pendown()
    #turtle.color("yellow")
    #turtle.begin_fill()
    turtle.circle(25)
    #turtle.end_fill()
    turtle.penup()
    turtle.goto(-300,-5)

    turtle.write('25', True, 'center',('Arial',20,'normal'))
    turtle.penup()
    turtle.goto(-275,0)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(200)
    turtle.right(45)
    turtle.circle(25,540)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)




    turtle.write('17', True, 'center',('Arial',20,'normal'))
    turtle.goto(-275,0)
    turtle.pendown()
    turtle.right(45)


    turtle.forward(200)
    turtle.right(45)
    turtle.circle(25,540)
    turtle.penup()
    turtle.left(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.write('36', True, 'center',('Arial',20,'normal'))
    turtle.right(180)
    turtle.goto(-275,0)
    turtle.pendown()
    turtle.right(45)


    turtle.forward(200)
    turtle.right(45)
    turtle.circle(25,180)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)

    turtle.circle(25,360)
    turtle.left(90)
    turtle.penup()
    turtle.forward(25)
    turtle.right(135)
    turtle.forward(10)
    turtle.write('20', True, 'center',('Arial',20,'normal'))
    turtle.penup()
    turtle.goto(-275,0)
    turtle.left(90)

    turtle.pendown()
    turtle.right(45)


    turtle.forward(200)
    turtle.right(45)
    turtle.circle(25,180)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(90)

    turtle.circle(25,360)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(45)
    turtle.forward(10)
    turtle.write('2', True, 'center',('Arial',20,'normal'))
    turtle.hideturtle()




    turtle.done()





main()
