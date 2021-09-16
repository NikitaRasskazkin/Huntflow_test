import sys

from services.repository import DataBase


def main():
    args = sys.argv
    if len(args) != 3:
        print('Неверно введены параметры\nmain.py <токен> <путь к папке с базой>')
        input()
        return 0
    token = args[1]
    path = args[2]
    db = DataBase(path)
    ws = db.get_database()
    if type(ws) == str:
        print(f'Error when opening the database: {ws}')
        input()
        return 0


if __name__ == '__main__':
    main()
