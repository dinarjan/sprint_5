import random


def generate_email():
    names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Иван',
             'Александр', 'Сергей', 'Дмитрий', 'Андрей', 'Максим', 'Олег', 'Никита', 'Владимир', 'Евгений']
    domain = ['gmail.com', 'yahoo.com', 'outlook.com', 'mail.ru', 'yandex.ru', 'rambler.ru']
    return f'{random.choice(names)}_{random.randint(0, 100)}@{random.choice(domain)}'


def generate_incorrect_email():
    names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Иван',
             'Александр', 'Сергей', 'Дмитрий', 'Андрей', 'Максим', 'Олег', 'Никита', 'Владимир', 'Евгений']
    domain = ['gmail.com', 'yahoo.com', 'outlook.com', 'mail.ru', 'yandex.ru', 'rambler.ru']
    return f'{random.choice(names)}_{random.randint(0, 100)}{random.choice(domain)}'


def generate_password():
    return f'QWE{random.randint(0, 10000)}'


def generate_name():
    return f'Осциллограф{random.randint(100, 100000)}'


product_name = generate_name()
incorrect_login_name = generate_incorrect_email()
