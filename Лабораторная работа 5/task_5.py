import random


def get_random_password() -> str:
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    connector = ''
    return connector.join(random.sample(sample, 8))


print(get_random_password())
