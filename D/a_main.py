# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

file_path = __file__.rsplit('/',1)[0]
f=open(file_path + '/input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import collections
S = input()
Q = int(input())

query_list = [input().split() for _ in range(Q)]

T_cnt_list = collections.deque([0])
left = ''
right = ''

for i, query in enumerate(query_list):
    if query[0] == '1':
        T_cnt_list.append(1+T_cnt_list[-1])

    else:
        T_cnt_list.append(T_cnt_list[-1])

        if query[1] == '1' and T_cnt_list[i+1]%2 == 0:
            left = query[2] + left

        elif query[1] == '1' and T_cnt_list[i+1]%2 == 1:
            right = right + query[2]

        elif query[1] == '2' and T_cnt_list[i+1]%2 == 0:
            right = right + query[2]

        elif query[1] == '2' and T_cnt_list[i+1]%2 == 1:
            left = query[2] + left

if T_cnt_list[-1]%2 == 0:
    print(left + S + right)
else:
    print(right[::-1] + S[::-1] + left[::-1])



