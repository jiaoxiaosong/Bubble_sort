# -*- coding: utf-8 -*-
"""
冒泡排序
"""

def bubble_sort(input):
    n = len(input)
    for j in range(n):
        for i in range(n-1):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]


if __name__ == '__main__':
    input = [5, 2, 1, 9, 6, 3, 0]
    bubble_sort(input)
    print(input)
