# serialisation/encoding
from json import JSONEncoder
import json
from typing import Any


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Louis", 22)  # type is a custom object of the class User.


def encode_user(o):  # customise a encoder
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError('i wrote this errror')


# 方法2
class UserEncoder(JSONEncoder):  # 把JSONEncoder替换成自己的
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)  # 原来的


# 如果这里还想用dump string的话 对于object操作的话 先要变成dictionary，这就是encode_user function做的事情
# userJSON = json.dumps(user, default=encode_user) #方法1
# userJSON = json.dumps(user, cls=UserEncoder)  # 方法2 用自己的encoder
userJSON = UserEncoder().encode(user)  # 方法3 最直接


# 这里用的是JSONEncoder
print(userJSON)

# 从dictionary变成object 所以这里要加一个method


def decode_user(dict):
    if User.__name__ in dict:  # 之前encode的时候加了一个class name，这里User.__name__就是User的意思
        # This checks if the key corresponding to the class name (User.__name__) is present in the dictionary. The reason for using __name__ is that it returns the name of the class as a string. Using User.__name__ is a common practice when dealing with class names dynamically, and it makes the code more maintainable if the class name changes in the future.
        # In Python, the __name__ attribute is a special attribute associated with classes and modules. Specifically:

        # For Classes:

        # In the context of a class, __name__ represents the name of the class as a string.
        # When you access SomeClass.__name__, you get the name of the class SomeClass.
        # It's often used when you need the class name as a string, for example, for dynamic type checking or logging.
        # create an User object
        return User(name=dict['name'], age=dict['age'])
    return dict


# decode from JSON to object
user = json.loads(userJSON, object_hook=decode_user)
# 这里是dictionary 不是object 因为不能写成user.name 所以这里要加一个customer decode method
print(user.name)
