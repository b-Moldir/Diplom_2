import random
import string


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "yandex.ru", "outlook.com"]
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(domains)
    return f"{name}@{domain}"


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def create_user_payload():
    email = generate_random_email(),
    password = generate_random_string(8),
    name = generate_random_string(10)

    return {
            "email": email,
            "password": password,
            "name": name
        }


