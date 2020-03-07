# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
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
A, B = [int(item) for item in input().split()]
is_found = False

for i in range(10001):
    A_cal = int(i * 0.08)
    B_cal = int(i * 0.10)

    if A_cal == A and B_cal == B:
        print(i)
        is_found = True
        break
    
if not is_found:
    print(-1)


        