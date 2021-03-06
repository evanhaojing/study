'''Evas'''
import pygame

# 1、游戏初始化
pygame.init()

# 2、创建游戏窗口
'''
set_mode(窗口大小) - 窗口大笑是一个元组，有两个元素：width，height
set_mode(（宽度，高度）)
宽度和高度的单位是像素
'''

window = pygame.display.set_mode((400,600))
# 将窗口填充指定的颜色
'''
fill(颜色)
计算机颜色：计算机三颜色 - 红，绿，蓝（rgb）
            颜色值就是有三个数字组成，分别代表红，绿，蓝，数字范围是0-255
        
Python中的颜色是一个元组，元组是有三个颜色，分为是r，g，b
（255,255,255）  - 白色
（0,0,0）  - 黑色
（255,0,0）  - 红色
'''
window.fill((100,250,250))

# 将窗口展示到设备上
pygame.display.flip()

# 3、创建游戏循环
while True:
    # 4、检测事件
    for event in pygame.event.get():
        # ===区分不同的事件，做出不一样的反应===
        # 判断关闭按钮点击事件是否发生
        if event.type == pygame.QUIT:
            exit()