from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def conv2d(im, kernel, stride=1):           # 第一种代码实现
    # 翻转卷积核
    kernel_reversed = [row[::-1] for row in reversed(kernel)]
    h, w = len(kernel_reversed), len(kernel_reversed[0])
    H, W = len(im), len(im[0])

    # 计算输出维度
    H_out = (H - h) // stride + 1
    W_out = (W - w) // stride + 1

    # 响应值计算函数
    def cal(x, y):
        return sum(
            im[x + i][y + j] * kernel_reversed[i][j]
            for i in range(h)
            for j in range(w)
        )

    # 重构循环结构
    im_out = []
    for i in range(H_out):
        row = []
        start_row = i * stride  # 计算实际起始行
        for j in range(W_out):
            start_col = j * stride  # 计算实际起始列
            row.append(cal(start_row, start_col))
        im_out.append(row)

    return im_out


def conv2d_1(im, kernel, stride=1):             # 第二种代码实现
    # 翻转卷积核（垂直+水平翻转）
    kernel = [row[::-1] for row in reversed(kernel)]
    h, w = len(kernel), len(kernel[0])
    H, W = len(im), len(im[0])

    # 计算输出尺寸
    out_h = (H - h) // stride + 1
    out_w = (W - w) // stride + 1

    # 生成输出矩阵（列表推导式优化）
    return [
        [
            # 计算单个窗口的卷积值
            sum(
                im[i * stride + di][j * stride + dj] * kernel[di][dj]
                for di in range(h)
                for dj in range(w)
            )
            for j in range(out_w)  # 列方向滑动
        ]
        for i in range(out_h)  # 行方向滑动
    ]

def conv2d_2(im, kernel, stride =1):            # 第三种代码实现
    # 翻转核矩阵
    kernel_reversed = []
    for i in range(0,len(kernel)):
        kernel_reversed.append(kernel[len(kernel)-i-1][::-1])
    # print(len(kernel_reversed),len(kernel_reversed[0]))
    # print(kernel_reversed)
    # 计算响应值
    def cal(x,y):
        out = 0
        for i in range(0,len(kernel_reversed)):
            for j in range(0,len(kernel_reversed[i])):
                out += im[x+i][y+j] * kernel_reversed[i][j]
        return out

    im_out = []
    # H_out = (len(im) - h) // stride + 1
    # W_out = (len(im[0]) - w) // stride + 1
    for j in range(0,len(im)-len(kernel_reversed)+1,stride):
        im_out.append([])
        for k in range(0,len(im[0])-len(kernel_reversed[0])+1,stride):
            im_out[j // stride].append(cal(j,k))
    # print(len(im_out),len(im_out[0]))
    return im_out


im =  [[ 8, -1, -8,  2,  3, -9, -2,  5,  5,  5, -8],
       [ 8,  2, -8, -4,  1,  7,  6, -7,  8, -4, -6],
       [ 5,  7, -1,  2,  1, -7, -4,  1, -1,  1,  0],
       [-3,  0, -2, -2, -5, -4, -7,  5,  0, -3, -1],
       [-5,  0,  3,  1, -1,  4,  8, -2, -3, -8,  5],
       [-2, -7, -6, -3, -3, -3,  2,  5, -7,  7,  3],
       [ 8, -9, -3,  3,  0, -4, -6, -8,  6, -8, -7],
       [-6,  0,  0,  8,  3, -6,  1,  8, -2,  2,  7],
       [-4, -8,  6, -3, -9,  2, -5, -4, -9,  0, -5],
       [-6,  4, -1,  0, -4,  7,  4,  5,  0, -4, -6],
       [ 6,  4,  2, -4,  7,  4,  8, -5, -1, -7, -5]]

K =   [[ 5, -3,  3,  5,  7],
       [ 0, -9,  8, -8, -8],
       [ 6,  6,  1, -5,  3],
       [-3, -9,  5,  0,  1],
       [ 1, -9, -6,  0,  8]]

stride = 2


#输入图像

plt.imshow(im)
plt.show()

im_out = conv2d_1(im, K, stride)
print(im_out)
# print(type(im_out))

im_out = np.array(im_out)
im1 = Image.fromarray(im_out.astype('uint8'))
plt.imshow(im1)
plt.show()

# print(im_out)
# print(type(im_out))