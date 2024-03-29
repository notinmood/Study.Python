"""
 * @file   : 11.特殊符号反斜线和星号在参数中的应用.py
 * @time   : 11:10
 * @date   : 2024/2/22
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""


# +--------------------------------------------------------------------------
# |::::TIPS::::| 函数参数中的 / 和 * 符号
# ---------------------------------------------------------------------------
# 在参数中可以使用 / 和 * 符号，来对参数进行特别的要求：如果你希望调用者使用函数时
# 1. 一定不能使用关键字参数传参，那么只需要把这些参数放在/前即可；
# 2. 一定要使用某些参数，且必须为关键字参数传参，那么只需要把这些参数放在*后面即可。
# +--------------------------------------------------------------------------

# 1. “/”参数的用法
# 如果你想要函数的调用者在某个参数位置只能使用位置参数而不能使用关键字参数传参，那么你只需要在所需位置后面放置一个/。
def func1(a, b, /):
    """

    :param a:
    :param b:
    :return:
    """
    c = a + b
    print("a+b=", c)
    return c


## 对于上面这个函数而言，调用f1时参数a，b只能是特定的值，而不能以关键字传参，即f1(2, 3)执行正确而f1(a=2, 3)和f1(2, b=3)将执行错误。
func1(2, 3)  # ok，


# func1(2, b=3)  # error
# func1(a=2, b=3)  # error


# 2. “*”参数的用法
# 如果你需要强迫调用者使用某些参数，且必须以关键字参数的形式传参，那么你只需要在所需位置的前一个位置放置一个*。
def func2(a, *, b):
    """

    :param a:
    :param b:
    :return:
    """
    c = a + b
    print("a+b=", c)
    return c


# 对于上面这个函数而言，调用时参数a可以任意值, 但b参数一定要以关键字参数的形式传参，如f1(1, b=4),否则将会报错。
func2(2, b=3)  # ok
func2(a=2, b=3)  # ok
# func2(2, 3) # error
