import random

from faker import Faker

fake_data = Faker()


def get_random_number(min_num=0, max_num=9999):
    return random.randint(min_num, max_num)


def get_random_element(options):
    return random.choice(options)


def get_random_name():
    return random.choice([fake_data.first_name(), fake_data.name()])


def get_random_list_of_names(quantity=get_random_number()):
    list_of_names = [random.choice([fake_data.first_name(), fake_data.name()]) for _ in range(quantity)]
    return list_of_names


def get_random_list_of_strings(quantity=get_random_number()):
    list_of_strings = [fake_data.pystr() for _ in range(quantity)]
    return list_of_strings
