"""
 * @file   : A01.三个点的使用2.数值中的使用.py
 * @time   : 10:04
 * @date   : 2024/2/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

#  数值中不再适用三个点？

d = [
    [[0, 1, 2],
     [2, 3, 4],
     [4, 5, 6]],

    [[8, 9, 10],
     [10, 11, 12],
     [12, 13, 14]],

    [[16, 17, 18],
     [18, 19, 20],
     [20, 21, 22]]
]

if __name__ == '__main__':
    print(d[1])
    # print(d[1, ...])
    # print(d[..., 1])
    # print(d[1, ..., 1])
    print(d[1][1])

# >>> d[1,...]
# array([[ 8,  9, 10],
#        [10, 11, 12],
#        [12, 13, 14]])
# >>> d[...,1]
# array([[ 1,  3,  5],
#        [ 9, 11, 13],
#        [17, 19, 21]])
# >>> d[1,...,1]
# array([ 9, 11, 13])

# 参考：https://zhuanlan.zhihu.com/p/264896206
