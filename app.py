import mongo_db.controller as mongo_controller
import mysql_db.controller as mysql_controller


def init():
    while True:
        db_choice = input('Choose database:\n\t'
                          '1.MongoDB\n\t'
                          '2.MySQL\n\t'
                          '3.Quit program:\nYour choice: ')

        if db_choice == '3':
            exit(0)
        elif db_choice not in ['1', '2']:
            continue

        action_choice = input('Choose action to perform:\n\t'
                              '1.Insert data from CSV\n\t'
                              '2.Get all data\n\t'
                              '3.Update all data\n\t'
                              '4.Delete all data:\nYour choice: ')
        mongo_controller.dispatch(db_choice, action_choice)
        mysql_controller.dispatch(db_choice, action_choice)


if __name__ == '__main__':
    init()
