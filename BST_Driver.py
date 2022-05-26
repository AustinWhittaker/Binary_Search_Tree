#
# Name : Austin Whittaker
#
# Date : 4/25/2021
#
# Purpose: The purpose of this Program is to work with Binary Search Trees and become
#           well acquainted with how they work
#
# Algorithm : This program has 2 classes Node and BinarySearchTree. Node is responsible for
#             for creating a node with data, left and right and also the ability to print
#             out its contents. BinarySearchTree is responsible for inserting new nodes.
#             deleting nodes, determining if an item is within the tree by searching. Keeping
#             track of the size of the tree, the height of the tree, as well as left and right
#             of the tree. Traversals in 3 orders such as sorted(inorder), preorder and postorder.
#             Print a visual of tree. Return the height at O(1) time. Find all of the leaves (AT FIRST)
#             As well as the biggest leaf(AT FIRST)
#
# Resources : Dr. Pence csc 231 class, notes, lectures, books and powerpoints
#               - 4/12 - 4-25
#
##################################################################

class Node(object):
    '''
        This class is responsible for creating a node containing data, a left pointer,
        a right pointer and estabilishing a string method
    '''

    def __init__(self, data=None):
        '''
            This function is for building a new node.
        :param data: integer
        '''
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        '''
            this function provides a way to print the contents of the Binary search tree on
            the screen.
        :return:
        '''
        leftData = None
        rightData = None
        if self.left:
            leftData = str(self.left.data)
        if self.right:
            rightData = str(self.right.data)
        return "{}, left: {}, right:{}.".format(self.data, leftData, rightData)


class BinarySearchTree():
    '''
        In this class we have multiple methods such as __init__ to initialize variables such as
        the root, size, maxheight of left, max height of right, and the overall max height.
        Insert method to place any new items within the list in the correct order.
        Delete method to remove an item and replace its position in the correct manner.
        __Contains__ which determines if an integer that is inputed from the user, is within
        the binary search tree.
        __len__ which returns the size of the Binary search tree at O(1) time.
        Traverse in order which will return the binary search tree in sorted order.
        Traverse pre order which will print in the order starting with the top item.
        traverse post order which will print in the order starting with the last
        item in the left side.
        Print tree which will print out a visual of what the tree looks like horizontally.
        max height which will return the height of the tree at O(1) time.
        Max left right which is an operation to determine the size of the tree going to the
        left and the right of the tree.
    '''

    def __init__(self):
        '''
            Initialize the following variables such as root, size of the tree, size of the tree
            going left, size of the tree going right, and the overall size of the tree.
        '''
        self.root = None
        self.size = 0
        self.leaf = 0
        self.leaflist =[]
        self.leaflistLeft = []
        self.leftlistRight = []
        self.biggestLeaf = []
        self.maxLeftHeight = 0
        self.maxRightHeight = 0
        self.maxheight = -1

    def insert(self, item):
        '''
            This method will insert an item into the binary search tree in the correct order
            by determining if what is being put in is greater, lesser, or equal too the node
            within the tree already.
        :param item: an integer
        :return:
        '''
        newNode = Node(item)
        lookCount = 0
        maxLookCount =0
        startingLeft = False                                    # Set some variables to keep track of what is going on
        startingRight = False


        print()

        if self.root == None:
            self.root = newNode
            self.size += 1                                      # if there is nothing in the tree yet
            self.maxheight += 1

            print('Current Max Height:', self.maxheight)

########################################################################################################################

        else:
            inserted = False                                    # If the is already a root node within the tree
            current = self.root

            while not inserted:                                 # Establish a flag to stop once an item is inserted

                print("current node is", current)

##########################################
#           Going  Left                  #
##########################################

                if item < current.data:                         # If item is less then the root go right
                    if current.data == self.root.data:
                        startingLeft = True                     # For maintaining the height of the left


                    print('looking left')
                    lookCount += 1
                    if current.left == None:
                        if lookCount > self.maxheight:          # Kept track of the amount of times we looked in a
                            self.maxheight = lookCount          # certain direction to set the max height
                            maxLookCount = self.maxheight
                            print('Current Max Height:', self.maxheight)

                            print()

                            lookCount= 0

                        current.left = newNode
                        self.size += 1

                        self.max_leftRight(startingRight, startingLeft, None, None) # Call to obtain the true height of left or

                        inserted = True                                 # Right
                    else:
                        current = current.left

##########################################
#             Going Right                #
##########################################

                elif item > current.data:                       # if item if greater then the root go right
                    if current.data == self.root.data:
                        startingRight = True                    # For maintaining the height of the right
                        print('beginning')
                    print('looking right')
                    lookCount += 1

                    if current.right == None:
                        if lookCount > self.maxheight:          # Kept track of the amount of times we looked in a
                            self.maxheight = lookCount          # certain direction to set the max height
                            maxLookCount = self.maxheight
                            print('Current Max Height:', self.maxheight)
                            print()
                            lookCount = 0


                        current.right = newNode
                        self.size += 1
                        self.max_leftRight(startingRight, startingLeft, None, None) # Call to obtain the true height of left or
                        inserted = True                                 # certain direction to set the max height
                    else:
                        current = current.right


        return

    def delete(self, item):
        '''
            This method is resposible for removing an item that is inputed from the user by taking the right most
            node from the left side of the tree.
        :param item: An Integer
        :return:
        '''

        found = False
        lookCount = 0
        deleteRight = False                                     # Set variables to use later
        deleteLeft = False


        current = self.root
        previous = current

##########################################
#             First One                  #
##########################################

        if self.__contains__(item) == False:
            print("Cant delete it isn't here")                   # To insure that we dont waste any time
            return                                               # check if the number exists already.

        if item == self.root.data:                              # This is the first Node in the tree

            print()
            if current.left == None and current.right == None:  # If the Node is alone remove it
                self.root = None
                self.maxheight -=1

            nextCurrent = current.left
            if current.left == None:                            # If there no nodes on the left side of the tree

                self.root = current.right
                self.size -= 1

                return

            elif current.right == None:                         # If there are no nodes on the right side of the tree

                self.root = current.left
                self.size -= 1



            elif nextCurrent.left != None and nextCurrent.right == None:  # If the first Node on the left side
                                                                          # has nothing on the right of that but
                                                                          # has something on the on the left
                                                                          # of that node.
                self.root = current.left
                nextCurrent.right = current.right
                self.size -= 1

            elif nextCurrent.left != None and nextCurrent.right!=None: # If there are 2 nodes attached to the first left
                                                                       # node of the tree
                while nextCurrent.right != None :
                                                                       # loop until we find that right most node
                                                                       # on the left side of the tree
                    nextCurrent = nextCurrent.right
                    print(nextCurrent)

                if nextCurrent.left == None and nextCurrent.right == None: # If the right most node has nothing on the
                                                                           # left or the right.

                    self.root.data= nextCurrent.data                       #flip the nodes we want to change
                    nextCurrent.data = previous.data
                    self.root.left = current.left
                    self.root.right = current.right
                    future = self.root.left

                    while future.right != None:                            # look to find the node that we flipped
                        theEnd = future
                        future = future.right
                    theEnd.right = None                                     # remove it
                    self.size-=1
                    return


                elif nextCurrent.left != None:                              # If the right most Node has nothing on
                                                                            # on the left side
                    self.root.data = nextCurrent.data
                    print(self.root)
                    print()
                    passage = self.root.left
                    while passage.right != None:
                        beforePassage = passage
                        passage = passage.right
                    beforePassage.right = passage.left
                    return


            elif nextCurrent.left == None and nextCurrent.right == None: # If the first node on the left has nothing
                                                                         # on its left and right side

                previous = current
                print()
                print(previous)
                print(current)
                print(nextCurrent)
                self.root = current.left
                nextCurrent.right = current.right

            elif nextCurrent.left == None and nextCurrent.right != None: # If the first node on the left has nothing
                                                                         # on its left but does have something on its
                                                                         # right side
                previous = current
                print()

                while nextCurrent.right != None :                         # loop to find the right most node
                    nextCurrent = nextCurrent.right

                if nextCurrent.left == None:                              # If that right most node has nothing on its
                                                                          # left side
                    self.root.data = nextCurrent.data
                    nextCurrent.data = previous.data                      # flip in place
                    self.root.left = current.left
                    self.root.right = current.right
                    future = self.root.left

                    while future.right != None:                           # back through to find what we flipped
                        theEnd = future
                        future = future.right
                    theEnd.right = None                                   # remove it





                else:                                                     # If the right most node does have something
                                                                          # on the left side of it

                    self.root.data = nextCurrent.data
                    nextCurrent.data = previous.data                      # Flip in place
                    self.root.right = current.right
                    newCurrent= self.root.left

                    while newCurrent.right != None:                       # Loop through to find what we flipped
                        prev = newCurrent
                        newCurrent= newCurrent.right
                    prev.right = newCurrent.left                          # remove it and change pointers

                    return

##########################################
#             Going Right                #
##########################################

        while not found:                                      # Since our first Node isnt what we are trying to delete
                                                              # we are going to compare if it is grater then what we are
                                                              # looking for.
            print("current node is", current)


            if item > current.data:                           # Going right
                if current.data == self.root.data:
                    deleteRight = True                        # Keep track of which way we went first
                print('looking right')
                lookCount+=1
                previous = current
                current = current.right


                if current.data == item:                      # Found what we were looking for
                    print('found it')
                    print(previous)
                    print(current)



                    if current.left != None and current.right != None: # if there is something on the left and right

                        nextCurrent = current.left


                        if nextCurrent.left == None and nextCurrent.right == None: # If the node has
                                                                                   # nothing on the left or the right
                                                                                   # it

                            previous.right = nextCurrent
                            nextCurrent.right = current.right
                            self.size-=1


                        elif nextCurrent.left!= None and nextCurrent.right == None: # if what is on the left contains

                            previous.right = nextCurrent                            # something on the left but not
                            nextCurrent.right = current.right                       # on the right
                            self.size-=1


                        elif nextCurrent.left == None and nextCurrent.right != None: # if what is on the left contains
                                                                                     # Nothing on the left, but
                                                                                     # something on the right

                            previous.right = nextCurrent
                            nextCurrent = nextCurrent.right
                            nextCurrent.right = current.right
                            self.size-=1



                        else:

                            previous.right = nextCurrent
                            nextCurrent = nextCurrent.right
                            nextCurrent.right = current.right
                            self.size-=1




                    elif current.left != None and current.right == None: # if there is something only on the left
                        nextCurrent = current.left

                        if nextCurrent.left == None and nextCurrent.right == None: # if what is on the left has nothing
                            previous.right = nextCurrent                           # on left or right
                            print()
                            print(self.root)
                            print(self.root.left)
                            print(self.root.left.left)
                            print(self.root.left.left.right)

                            self.size-=1


                        elif nextCurrent.left != None and nextCurrent.right != None: # if what is on the left has
                                                                                     # something on the left and right

                            previous.right = nextCurrent
                            self.size-=1


                        elif nextCurrent.left == None and nextCurrent.right != None:# if what is on the left has
                                                                                    # something on the right but not the
                                                                                    # left

                            previous.right = nextCurrent
                            self.size-=1

                        else:
                            previous.right = nextCurrent
                            self.size-=1

                    elif current.left == None and current.right != None: # if there is something only on the right
                        nextCurrent = current.right

                        if nextCurrent.left == None and nextCurrent.right == None: # if there is nothing on the left or
                            print(nextCurrent)                                     # right
                            previous.right = nextCurrent

                            self.size-=1

                        elif nextCurrent.left == None and nextCurrent.right != None: # if there is nothing on the left
                            print(nextCurrent)

                            previous.right = current.right
                            self.size-=1

                        elif nextCurrent.left != None and nextCurrent.right == None: # if there is nothing on the right
                            print(nextCurrent)

                            previous.right = nextCurrent
                            self.size-=1
                        else:
                            print(nextCurrent)

                            previous.right = nextCurrent
                            self.size-=1

                    else:                                           # LEAF
                        print(previous)
                        print(current)
                        nextCurrent = current.right
                        print(nextCurrent)

                        previous.right = None
                        self.size-=1
                        for num in self.leaflist:                # this is something I was working on but it didnt
                                                                 # work for the most part
                            if num == item:
                                self.leaflist.remove(item)
                                self.leaf -= 1


                        if len(self.biggestLeaf) == 1:
                            if item == self.biggestLeaf:
                                self.maxheight -=1
                                self.max_leftRight(None, None, deleteRight, deleteLeft)





                    found = True




##########################################
#           going  Left                  #
##########################################


            elif item < current.data:                           # going left
                print('looking left')
                previous = current
                current = current.left
                if self.root.data == current.data:
                    deleteLeft = True


                if current.data == item:                        # found
                    print()
                    print('found it')
                    print(previous)
                    print(current)
                    if current.left != None and current.right != None: # if there is something on the left and right

                        nextCurrent = current.left


                        if nextCurrent.left == None and nextCurrent.right == None: # if what is on the left has nothing
                            print(nextCurrent)

                            previous.left = nextCurrent                           # on the left or right
                            nextCurrent.right = current.right
                            self.size-=1


                        elif nextCurrent.left!= None and nextCurrent.right == None: # if what is on the left contains

                            previous.left = nextCurrent                            # something on the left but not
                            nextCurrent.right = current.right                       # on the right
                            self.size-=1


                        elif nextCurrent.left == None and nextCurrent.right != None: # if what is on the left contains
                                                                                     # something on the right but not
                                                                                     # the left
                            print(nextCurrent)

                            while nextCurrent.right != None:
                                prev = nextCurrent
                                nextCurrent = nextCurrent.right

                            prev.right =nextCurrent.right
                            previous.left = nextCurrent


                            nextCurrent.left = current.left
                            nextCurrent.right = current.right


                            self.size-=1


                        else:                                   # if all else fails

                            future = nextCurrent.right
                            previous.left = future.data
                            nextcurrent.right = future.left
                            self.size-=1


                    elif current.left != None and current.right == None: # if there is something only on the left
                        nextCurrent = current.left

                        if nextCurrent.left == None and nextCurrent.right == None: # if what is on the left has nothing
                            print(nextCurrent)
                            previous.left = nextCurrent                           # on left or right
                            print()


                            self.size-=1

                        elif nextCurrent.left != None and nextCurrent.right == None:   #  if what is on the left
                                                                                       # has nothing on the right but
                                                                                       # there is something on the left
                            print(nextCurrent)
                            previous.left =nextCurrent

                            self.size-=1

                        elif nextCurrent.left == None and nextCurrent.right != None:    # if what is on the left has
                                                                                        # nothing on the left but
                                                                                        # there is something on the right
                            print(nextCurrent)

                            print()
                            previous.left= nextCurrent
                            self.size-=1

                        else:                                                           # everything else

                            previous.left = nextCurrent
                            self.size-=1

                    elif current.left == None and current.right != None: # if there is something only on the right
                        nextCurrent = current.right

                        if nextCurrent.left == None and nextCurrent.right == None:  # if there is nothing on either side
                            print(nextCurrent)
                            previous.left = nextCurrent



                            self.size-=1

                        elif nextCurrent.left == None and nextCurrent.right != None:  # only somethin on the right
                            print(nextCurrent)

                            previous.left = current.right
                            self.size-=1

                        elif nextCurrent.left != None and nextCurrent.right == None:   # only something on the left
                            print(nextCurrent)

                            previous.left = nextCurrent
                            self.size-=1

                        else:                                                   # everything else
                            print(nextCurrent)

                            previous.left = nextCurrent
                            self.size-=1

                    else:                                   # LEAF

                        print(previous)
                        print(current)
                        previous.left = None
                        for num in self.leaflist:               # <--This is something I was working on but didnt work
                                                                # 100%
                            if num == item:
                                self.leaflist.remove(item)
                                self.leaf -=1
                        self.size-=1
                    found = True

        return

    def __contains__(self, item):
        '''
            This program returns a true or false value whether an item that is being searched
            by the user is within the tree.
        :param item: an integer
        :return: True -integer in tree
        :return: False - integer not in tree
        '''
        found = False
        startLeft = False
        startRight = False                                  # set variables
        lookCount = 0

        current = self.root
        while found == False and current != None:           # loop until we find
            print('Looking at:', current.data)
            if current.data == item:
                print('Found it')
                self.leafSide(item, startLeft,startRight)

                if lookCount == self.maxheight:             # found the biggest leaf but it doesnt matter
                    self.biggestLeaf.append(item)

                lookCount = 0
                found = True
            elif item < current.data:                       # item is less then what we want. Go left
                lookCount+=1

                print('Going left')
                if self.root.data == current.data:
                    startLeft = True
                current = current.left
            elif item > current.data:                       # item is more than what we want go right
                lookCount+=1
                if self.root.data == current.data:
                    startRight = True
                print('Going right')
                current = current.right

        return found

    def __len__(self):
        '''
            This method sends back the length of this list at O(1) time
        :return: size of tree
        '''
        return self.size

    def traverse_inorder(self, node = None):
        '''
            This method prints out a traversal of the tree and also finds the leaf nodes but I didnt get to use them
        :param: Node used for traversal
        :return: sorted list
        '''


        if node.left == None and node.right == None:    # So i was trying to use these to update max height at all
                                                        # times like if I found one, how many there were and if I should
                                                        # remove one from max height if one went missing but I didnt get
                                                        # that far. Just playing with it.

            if node.data not in self.leaflist:
                self.leaf +=1
                self.leaflist.append(node.data)

        if node.left != None:                           # Hit the left
            self.traverse_inorder(node.left)


        print(node.data, end=' ')                       # print the node

        if node.right != None:                          # hit the right
            self.traverse_inorder(node.right)

        return


    def traverse_preorder(self, node=None):
        '''
            This method will traverse the tree in pre order
        :param node: node used for traversal
        :return: preordered version of the tree
        '''

        print(node.data, end=' ')                   # print

        if node.left != None:
            self.traverse_preorder(node.left)       # hit left


        if node.right != None:
            self.traverse_preorder(node.right)      # hit right



    def traverse_postorder(self, node=None):
        '''
            This method will traverse the tree in post order
        :param node: node used for traversal
        :return: post ordered version of the tree
        '''

        if node.left != None:                        # hit left
            self.traverse_postorder(node.left)


        if node.right != None:
            self.traverse_postorder(node.right)      # Hit right


        print(node.data, end=' ')                    # print


    def printTree(self, node, level=0):
        '''
            This Method prints out visual of the tree in the terminal to have an idea of what it looks like
        :param node: Node of tree
        :param level: level to print the tree
        :return: tree horizontally
        '''

        if node != None:
            self.printTree(node.right, level + 1)           # print the right side node on Level
            print('  ' * 4 * level+'>', node.data,' ')      # print the data of the node
            self.printTree(node.left, level + 1)            # print the left side of node on left

    def max_height(self):
        '''
            returns the max height at its highest. I did alot of finding and altering in insert.

        :return: height of the tree
        '''

        return self.maxheight

    def max_leftRight(self, startingRight, startingLeft, deleteRight, deleteLeft):
        '''
            In this method I was working on altering the height of the tree on the right side and
            on the left side dealing with leafs and so forth. It works for the most part
            but i never got to delete right or left but starting works. This is passed down
            from insert.
        :param startingRight: If we went to the left for the very first time when inserting
        :param startingLeft: If we went right for the very first time when inserting
        :param deleteRight: This would but if we went left for the very first time when deleting
        :param deleteLeft: This would be if we went to the right for the ery first time when deleting
        :return: False to start the loop over again in insert if not finished
        '''

        if startingRight == True:                       # if we started to the right max right height +1
            if self.maxheight > self.maxRightHeight:
                self.maxRightHeight+=1
                return startingRight == False

        if startingLeft == True:                        # if we started to the left max left height +1
            if self.maxheight > self.maxLeftHeight:
                self.maxLeftHeight+=1
                return startingLeft == False

        if deleteRight == True:                         # didnt use it
            if self.maxRightHeight > 0:
                self.maxRightHeight -= 1
            return deleteRight == False


        if deleteLeft == True:                          # didnt use it
            if self.maxLeftHeight > 0:
                self.maxLeftHeight -= 1
            return deleteLeft == False

    def leafSide(self, item, startLeft, startRight):
        '''
            This determines what side the leaves are on.
        :param item: item in tree
        :param startLeft: If we went to the left while searching first leaf is on the left
        :param startRight: If we went to the right while searching first leaf is on the right
        :return: False to restart loop within contains
        '''

        if startLeft == True:                 # started left, leaf on left
            self.leaflistLeft.append(item)
            return startLeft == False
        elif startRight == True:              # started right, leaf on right
            self.leftlistRight.append(item)
            return startRight == False

    def biggest_Leaf(self):
        '''
            In this method we determine what the highest leaf is. We set the leaf to a list
            that we can search from by using contains. It works at first but i didnt get around
            to using it due to time. I was going to use it to update max height. for example say that if we
            are deleting and we hit one of those numbers. Well if there's 2 it wouldn't really matter
            but if there is only 1 then we should decrease the max height and then find the new
            biggest leaves or leaf but oh well I spent 2 days working on just that, but oh well.
            Honestly with the time that I put in it I should've worked on the Extra credit but
            I just got so into it I couldn't stop. I wonder if you read this message lol

        :return:
        '''
        for num in self.leaflist:    # With the numbers that are within the leaf list search to find the highest height.
            self.__contains__(num)

