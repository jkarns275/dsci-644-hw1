"""
||========||
|| README ||
||========||
So the task for this homework assignment is to implement the methods I have written out here.
I have given a specific description on what each one should do, what exceptions it may raise,
and what values it should return.

To test things out, you can run the test.py script which will automatically grade your assignment.
It will tell you which things need to be fixed as well.


For those of you who arent familiar with what a LinkedList is or how it works, the following is for you:

A list is an ordered sequence of values of some kind.
A linked list is one way of representing this in memory, although they are seldom used in practice.

Below is a simple diagram of a linked list containing the first four
letters of the alphabet.

 INDEX       0        1        2        3
            ___      ___      ___      ___
           | A |--->| B |--->| C |--->| D |-->X (this X represents a null / no node)
            ```      ```      ```      ```
             ^      ^^^^^^^^^^^^^^^^^^^^^^^
             |                 |
             +-> head          +-> tail

Usually, the first element of a linked list is called the head of the list, and the remainder of
the list is the tail.

Linked lists are composed of linked nodes: each node contains an element of the list and a reference
to the tail of the list. If the end of the list has been reached, the reference to the tail
will be null / None. 


All of the essential list operations can be implemented on this data structure:
    - Fetching the head of the list

    - Fetching elements by their index
    
    - Calculating the length of the list 

    - Adding an element to the end of the list can be done by traveling to the end, and replacing
      the pointer to a null element with a new node containing the element.
    
    - Changing the element contained at a given index

    - Deletion can be done by changing a pointer to skip a node, with edge cases existing for the
      first element or the last element.

    - Insertion can be done by changing two pointers to place a node between two other nodes,
      e.g. to insert Z at index 1, make node A point to a new node containing Z and make that new node
      point to B. The start of the list is an edge case.

   - Empty the list (remove all elements from the list)

You will have to implement the methods described above in the following class
"""

class LinkedList:
    """
    The LinkedList class contains a single field, that field being 'list.'
    This field is a reference to the first node in the linked list, or if the list is empty,
    it is a None value.

    The Node class defined below is where the actual data structure of the linked list resides,
    but we are wrapping that because it makes some book keeping a little easier.
    """

    class Node:
        """
        Several of the methods described below rely on recursive traversal of the list. An example
        if this is given below, where the goal is to find the element at index 3. The node currently
        being examined is highlighted, and a counter is used to keep track of how deep we are in the list,.

        COUNTER                             +-------+
              0                             |  ___  |   ___      ___      ___
                                            | | A |--->| B |--->| C |--->| D |-->X
                                            |  ```  |   ```      ```      ```
                                            +-------+

                                            Counter is zero, so we are
                                            at index zero. 0 < 3, so go to the  
                                            next node and increment counter.

                                            +-------+
              1                       ___   |  ___  |   ___      ___      
                                     | A |--->| B |--->| C |--->| D |---X
                                      ```   |  ```  |   ```      ``` 
                                            +-------+

                                            Counter is 1, so we are at index 1.
                                            1 < 3, so go to the next node and increment the counter.

                                            +-------+
              2              ___      ___   |  ___  |   ___      
                            | A |--->| B |--->| C |--->| D |---X
                             ```      ```   |  ```  |   ``` 
                                            +-------+

                                            Counter is 2, so we are at index 2.
                                            2 < 3, so go to the next node and increment the counter.

                                            +-------+
              3     ___      ___      ___   |  ___  |    
                   | A |--->| B |--->| C |--->| D |---X
                    ```      ```      ```   |  ```  |
                                            +-------+

                                            Counter is 3, so we are at index 3.
                                            3 == 3, so we are at the correct index!
                                            We should return this element "D"
        """
        def __init__(self, element, tail):
            self.element = element
            self.tail = tail

        def get_tail(self):
            return self.tail
        
        def set_tail(self, tail):
            self.tail = tail

        def get_node_by_index(self, index, counter=0): # If you don't specify a value for counter, than it will default to zero
            """
            get_by_index - traverses the list to find a node. This method is similar to the one
                           described above. If the supplied index is not valid (i.e. it would
                           require going beyond the end of the list) then raise an exception.

            returns the node at the supplied index
            
            index: the index of the node we would like to return
            counter: the index we are currently at
            """
            raise Exception("Not implemented")

        def delete_by_index(self, index):
            """
            delete_by_index - deletes an element from the list at the specified index.
                              If index is zero, then this method will do nothing and will
                              rely on LinkedList to skip the first node. Otherwise, this 
                              method should fetch node index - 1 and set the 'tail' field to
                              the node at index + 1

            returns the element that got deleted

            index: the index we want to delete
            """
            raise Exception("Not implemented")

        def insert_by_index(self, index, element):
            """
            insert_by_index - insert an element at a given index. If the given index is equal
                              to the length of the list, the element should be placed at the end
                              of the list. If the specified index is greater than the length of
                              the list, than raise an exception.

            returns no value

            index: the index the element should be inserted at
            element: the element the node will contain
            """
            raise Exception("Not implemented")

        def get_length(self):
            """
            get_length - returns the length of the chain starting from this node.
                         The length of this sublist is 1 + the length of the tail,
                         if the tail is None than the length of it is zero.

            returns length of this "sublist"
            """
            raise Exception("Not implemented")

        def append(self, element):
            """
            append - add the supplied element to the end of the list. Traverses to the last element
                     in the list and changes the tail value to point to a new node containing the
                     supplied element.

            returns no value

            element: the element to append to the list
            """
            raise Exception("Not implemented")

    def __init__(self):
        self.list = None

    def head(self):
        """
        head - gets the first element in the list. If the list is empty,
               raise an exception.
        
        returns first element of the list
        """
        raise Exception("Not implemented")
    
    def get(self, index):
        """
        get - a methods that fetches the element at the specified index.
              raises an exception if the index is out of bounds.

        returns the item at the given index
        """
        raise Exception("Not implemented")

    def __getitem__(self, index):
        """
        __getitem__ - a method that, when implemented, will allow the use of the 
                      index operator on the list (e.g. instead of calling list.get(index), you
                      will be able to call list[index]). raises an exception if the index is
                      out of bounds.

        returns the item at the index

        index: the index of the element to be retrieved
        """
        raise Exception("Not implemented")

    def set(self, index, element):
        """
        set - sets the element at the given index to the supplied element.
              raises an exception if an invalid index is given.

        returns the old element

        index: the index of the element to replace
        element: the new element
        """
        raise Exception("Not implemented")

    def __setitem__(self, index, element):
        """
        __setitem__ - a method that, when implemented, will allow the use of index assignment.
                      i.e. instead of "list.set(index, element)" you can use "list[index] = element"

        returns nothing

        index: the index of the element to be replaced
        element: the new value to be placed at the given index
        """
        raise Exception("Not implemented")

    def get_length(self):
        """
        get_length - calculates and returns the length of the list

        returns the length of the list
        """
        raise Exception("Not implemented")

    def __len__(self):
        """
        __len__ - a method that allows one to write len(list) instead of list.get_length()

        returns the length of the list
        """
        return self.get_length()

    def append(self, element):
        """
        append - adds the supplied element to the end of the list.
                 if the list is empty, it simply sets self.list to a new node.

        returns no value

        element: the element to append to the list
        """
        raise Exception("Not implemented")
    
    def remove(self, index):
        """
        remove - removes the element at the given index from the list.
                 if the given index is out of bounds, raises an error.

        returns the removed element

        index: the index of the element to remove
        """
        raise Exception("Not implemented")

    def insert(self, index, element):
        """
        insert - inserts the element at the given index.
                 if the index is out of bounds, raises an error.

        returns nothing

        index: the index to insert the element
        element: the element to insert
        """
        raise Exception("Not implemented")

    def empty(self):
        """
        empty - the list is emptied.

        returns a LinkedList containing the elements of this list.
        """
        raise Exception("Not implemented")
