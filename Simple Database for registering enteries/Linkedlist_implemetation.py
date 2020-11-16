from Linked import Node, LinkedQueue

try:
    def database_edit():
        store = []
        database = []
        n = int(input('Enter the no of lists you want to edit and store: '))
        for i in range(n):
            obj_n = LinkedQueue()
            database.append(obj_n)

        count = 0
        for i in database:
            count += 1
            print(f'Iterating for {count} time')
            i.function_call()
            if i.sav is not None:
                store.append(i.sav)
        else:
            print('Check the 2d list now')
        return store


    a = []
    a = database_edit()

    for j in a:
        print(j)

except ValueError:
    print('There was a Value Error please recheck your inputs')