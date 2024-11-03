def todolist():
    question = input('would you like to Add a Task?: ')
    my_inputs: list[str] = []
    if question == "yes".lower():
        print("Enter Your Tasks(when done, type stop!): ")
        user_task = input('Task: ')
        while user_task != 'stop'.lower():
            my_inputs.append(user_task)
            user_task = input('Task: ')
        else:
            print('your tasks have been saved!')
        ask = input('would you like to remove a task?: ')
        if ask == 'yes'.lower():
            while my_inputs:
                print(f'remaining tasks are{my_inputs}')
                ask = input('which task would you like to remove?: ')
                if ask in my_inputs:
                    my_inputs.remove(ask)
                    print(f'task "{ask}" is removed!')
                if not my_inputs:
                    print("no more tasks remaining!")
        elif ask == 'no'.lower():
            print('okay, goodbye!')
        else:
            print('goodbye.')
    elif question == "no".lower():
        print('no worries, have a good day!')
    else:
        print('invalid')

todolist()
