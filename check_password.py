from sys import argv
email = argv[1].casefold()
password = argv[2]

users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"},
    {"email": "user7@domain.com", "password": "123456"},
    {"email": "user8@domain.com", "password": "123456"},
    {"email": "user9@mail.com.ru", "password": "password9"}
]

for i in range(len(users)):
    if email == users[i]['email']:
        print('Доступ открыт' if password == users[i]['password'] else 'Доступ закрыт')
        break
else:
    print('Пользователь не найден')


# ver 2
print('Доступ открыт' if any(d['email'] == argv[1].casefold() and d['password'] == argv[2] for d in users) else 'Доступ закрыт' if any(d['email'] == argv[1].casefold() for d in users) else 'Пользователь не найден')
