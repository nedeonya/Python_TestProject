
class User:
    def __init__(self, first_name, last_name, email_address, age=None, phone_number=None, address=None):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._phone_number = phone_number
        self._address = address
        self._email_address = email_address

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    def get_email_address(self):
        return self._email_address

    def get_info(self):
        info = f"First name: {self._first_name}\n"
        info += f"Last name: {self._last_name}\n"
        if self._age is not None:
            info += f"Age: {self._age}\n"
        if self._phone_number is not None:
            info += f"Phone number: {self._phone_number}\n"
        if self._address is not None:
            info += f"Address: {self._address}\n"
        info += f"Email address: {self._email_address}\n"
        return info


class UserBuilder():
    def __init__(self, first_name, last_name, email_address):
        self.user = User(first_name, last_name, email_address)

    def add_age(self, age):
        self.user._age = age
        return self

    def add_phone_number(self, phone_number):
        self.user._phone_number = phone_number
        return self

    def add_address(self, address):
        self.user._address = address
        return self

    def build(self):
        return self.user


#Testing
if __name__ == "__main__":
    user1 = UserBuilder("Biba", "Boba", "bb@gmail.com").add_age(25).add_phone_number("123-45-67").build()
    print(user1.get_info())
