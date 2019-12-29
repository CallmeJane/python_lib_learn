import numpy as np


def print_ret(ret, oper):
    print(oper+":")
    print(ret)
    print()


def numpy_specical_array():
    #numpy特殊数组
    #初始化全为0
    spe = np.zeros((2, 2))
    print_ret(spe, "zores")
    #初始化全为1
    spe = np.ones((3, 3))
    print_ret(spe, "ones")
    #初始化接近为0
    spe = np.empty((2, 2))
    print_ret(spe, "empty")


def numpy_compute():
    #numpy数组
    #a = np.array([1,2],[3,4],dtype=int)
    a = np.array([[1, 2], [3, 4]], dtype=int)
    #numpy数组运算
    b = np.array([[11, 12], [13, 14]], dtype=int)
    ret = a/b
    print_ret(ret, "除法")
    #2次幂
    ret = a**2
    print_ret(ret, "2次幂")
    print("a.min:{},a.max:{},a.sum:{}".format(a.min(), a.max(), a.sum()))


def numpy_arange():
    #numpy差值数组
    a = np.arange(1, 120, 10)  # 起始，结束，步长
    print_ret(a, "arange")


def numpy_index():
    #numpy的索引
    a = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
    print_ret(a, "索引")
    print("第一行：{}".format(a[0]))
    print("第二行，第二列：{}".format(a[1][1]))


def numpy_light_deep_copy():
    #numpy的深拷贝与浅拷贝
    a = np.array([[1, 2], [3, 4]], dtype=int)
    #浅拷贝,复制的是引用
    b = a
    b[0][0] = 100
    print_ret(a, "a")
    print_ret(b, "b")
    #深拷贝，重新开辟一块儿内存，将数据copy过去
    c = a.copy()
    c[0][0] = 1
    print_ret(a, "a")
    print_ret(c, "c")


def numpy_matrix():
    #numpy矩阵，可以进行转置（T），求逆操作（I）
    a = np.matrix([[1, 2], [3, 4]], dtype=int)
    b = a.T
    print_ret(b, "转置")
    b = a.I
    print_ret(b, "逆")
    b = a*b
    print_ret(b, "与自己逆矩阵相乘")


def numpy_dot():
    #点乘
    a = np.array([[1, 2], [3, 4]], dtype=int)
    b = np.array([[11, 12], [13, 14]], dtype=int)
    ret = a.dot(b)
    print_ret(ret, "点乘")


def numpy_det():
    a = np.array([[1, 2], [3, 4]], dtype=int)
    #行列式
    print_ret(np.linalg.det(a), "行列式")


def numpy_file_operation():
    #文件读取
    a = np.array([1, 2, 3, 4], dtype=int)
    np.save("a", a)
    b = np.load("a.npy")  # .npy文件是二进制文件
    print_ret(b, "b")

    np.savetxt("a.txt", a)
    c = np.loadtxt("a.txt")
    print_ret(c, "c")


if __name__ == "__main__":
    print("end")
