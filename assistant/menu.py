""""Menu"""
from addressbook import run_addressbook as a_main
from notes import run_notes as b_main
from sort_directory import run_sort as c_main


def menu():
    work_loop = True
    while True:
        user_input = input("Menu press button:\n1-AddressBook\n2-Notes\n3-Sort_Files\n0-Exit\nChoose 0 - 3\n>>> ")
        if user_input == '1':
            print('AddressBook Started!')
            a_main()
        elif user_input == '2':
            print('Notes Started!')
            b_main()
        elif user_input == '3':
            print('Sort_Files Started!')
            c_main()
        elif user_input == '0':
            work_loop = False
            print('Goodbye!')
            break


