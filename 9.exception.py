# 自定义error对我一开始是难点，第一我不知道自定义的是在父object Exception下面弄，其次raise XXXXError(这里可以写文字) 后面except XXXXError as e 后面print(e)我也不理解为什么e打出来的优势上面的raise XXXXError 括号里面的问题 其实就按照分工来理解，写error 的人把这个话传递下去而已，下面写try的不需要理解e是啥，直接用就可以了。当然自己写Error就更清楚了，作为object的error把message传递下去而已。这是我一开始学的时候觉得很难理解的地方


try:
    a = 5/0
except Exception as e:
    print(e)


# own exception class
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def testvalue(x):
    if x > 10:
        raise ValueTooHighError("too high")  # 这里用的exception父亲object的argument
    if x < 2:
        raise ValueTooSmallError("Too small", x)  # 这里自己定义的子object


try:
    testvalue(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(f"{e.value} is {e.message}")
else:
    print("all good")
