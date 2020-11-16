class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class LinkedQueue:
    def __init__(self):
        self.linked_list = []
        self.front = None
        self.rear = None
        self.sav = []

    def append_list(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = self.rear.link

    def compile_list(self):
        self.linked_list = []
        current_node = self.front
        while current_node is not None:
            self.linked_list.append(current_node.data)
            current_node = current_node.link

    def display_list(self):
        print(self.linked_list)

    def length_list(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.link
        return count

    def remove_node(self, data):
        curr = self.front
        if self.front.data == data:
            self.front = self.front.link
            curr = None
            del curr
        else:
            while curr.data != data:
                helper_node = curr
                if curr.link is not None:
                    curr = curr.link
                else:
                    print("Element is not present inside the list")
                    break
            else:
                helper_node.link = curr.link
                curr = None
                del curr

    def insert_node(self, position, data):
        new_node = Node(data)
        if position == 1:
            new_node.link = self.front
            self.front = new_node
        elif position > self.length_list()+1:
            print("Invalid index")
        else:
            curr = self.front
            ind = 1
            while ind != position-1:
                curr = curr.link
                ind += 1
            else:
                new_node.link = curr.link
                curr.link = new_node

    def clear(self):
        self.rear = self.front = None

    def save_list(self):
        self.sav = []
        self.sav = self.linked_list

    def function_call(self):
        dec = 'y'
        while dec == 'y':
            print('''
***Welcome to the linked list application***
Whenever prompted to enter a string answer with - (y/n) -> pro-tip''')
            choice = int(input('''
Enter your choice 
1-> To create/ append the linked list
2-> To display the content of the linked list
3-> To display the length of the current linked list
4-> To remove a particular element from the linked list
5-> To Insert at a particular position in the linked list
6-> To completely delete the data inside the linked list
    : '''))
            if choice == 1:
                n = int(input('Enter the number of nodes to be created: '))
                for i in range(n):
                    m = input('Data: ')
                    self.append_list(m)
                self.compile_list()
            elif choice == 2:
                self.compile_list()
                print('The current linked list contains:-')
                self.display_list()
            elif choice == 3:
                self.compile_list()
                count = self.length_list()
                print(f'The length of the current linked list is: {count}')
            elif choice == 4:
                element = input('Please enter the data to be deleted: ')
                self.remove_node(element)
                self.compile_list()
            elif choice == 5:
                pos = int(input('Please pass the position at which the new node is to be added: '))
                data = input("Please enter the data into the new node: ")
                self.insert_node(pos, data)
                self.compile_list()
            elif choice == 6:
                print('Deleting the data stored in the current linked list !!!')
                self.clear()
                self.compile_list()
            print('Saving your data now !!!')
            self.save_list()

            dec = input('Do you want to continue ... : ')

        else:
            print('\nOperation complete!')





