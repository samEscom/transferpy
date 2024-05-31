from dataclasses import dataclass


@dataclass
class UserTest:
    email: str = "sam@prueba.com"
    password: str = "1234"
    name: str = "Samuel"
    fullname: str = "John Doe"
    address: str = "calle 1"
    phone_number: str = "12345678"
