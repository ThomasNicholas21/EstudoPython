"""
Exemplo prático para entender o padrão de projeto Factory Method.

Componentes principais:
- Builder <<interface>>
- ConcreteBuilder
- Product
- Director
- Client
"""
from abc import ABC, abstractmethod


class StringClassMixin:
    def __str__(self):
        params = ', '.join(
            [
                f'{k}={v}'
                for k, v in self.__dict__.items()
            ]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class User(StringClassMixin):
    def __init__(self):
        self.full_name = None
        self.birthday = None
        self.address = []
        self.email = None
        self.password = None
        self.is_admin = None


class UserBuilderInterface(ABC):
    @property
    @abstractmethod
    def create(self): pass

    @abstractmethod
    def add_full_name(self): pass

    @abstractmethod
    def add_birthday(self): pass

    @abstractmethod
    def add_address(self): pass

    @abstractmethod
    def add_email(self): pass

    @abstractmethod
    def add_password(self): pass

    @abstractmethod
    def add_is_admin(self): pass


class UserBuilder(UserBuilderInterface):
    def __init__(self):
        self.reset()

    def reset(self):
        self._create = User()

    @property
    def create(self):
        data = self._create
        self.reset()
        return data

    def add_full_name(self, full_name):
        self._create.full_name = full_name
        return self

    def add_birthday(self, birthday):
        self._create.birthday = birthday
        return self

    def add_address(self, address):
        self._create.address = address
        return self

    def add_email(self, email):
        self._create.email = email
        return self

    def add_password(self, password):
        self._create.password = password
        return self

    def add_is_admin(self):
        self._create.is_admin = True
        return self


class DirectorBuilder:
    def __init__(self):
        self._builder = None

    @property
    def get_builder(self):
        return self._builder

    @get_builder.setter
    def set_builder(self, builder: UserBuilder):
        self._builder = builder

    def create_user_default(
        self,
        *,
        full_name,
        password
    ):
        self._builder.add_full_name(
            full_name
        ).add_password(password)
        return self._builder.create

    def create_user_admin(
        self,
        *,
        full_name,
        birthday,
        address,
        email,
        password,
    ):
        self._builder.add_full_name(
            full_name
        ).add_birthday(
            birthday
        ).add_address(
            address
        ).add_email(
            email
        ).add_password(
            password
        ).add_is_admin()
        return self._builder.create


if __name__ == "__main__":
    director = DirectorBuilder()
    userbuilder = UserBuilder()
    director.set_builder = userbuilder

    user1 = director.create_user_default(
        full_name='Thomas Nicholas',
        password='123456'
    )
    print(user1)

    user2 = director.create_user_admin(
        full_name='Thomas Nicholas',
        birthday='31/07/2000',
        address='Rua X Bairro Y',
        email='thomas@thomas.com',
        password='123456'
    )
    print(user2)
