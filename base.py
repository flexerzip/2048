#!/usr/bin/python
#coding=utf-8

import random

#横向排序，把数字紧凑
def sorting(arr):
	new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(4):
		count=0
		for j in range(4):
			if arr[i][j]!=0:
				new[i][count]=arr[i][j]
				count+=1
	return new

#合并相邻两个相同的数据
def merge(arr):
	for i in range(4):
		for j in range(3):
			if arr[i][j]==arr[i][j+1] and arr[i][j]!=0:
				arr[i][j]*=2
				arr[i][j+1]=0
	return arr

#横向旋转
def ytranslate(arr):
	new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(4):
		for j in range(4):
			new[i][j]=arr[i][4-j-1]
	
	return new

#关于y=-x函数旋转
def xytraslate(arr):
	new=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(4):
		for j in range(4):
			new[i][j]=arr[j][i]

	return new



#创建一个新的游戏
def new_game():
	game=[]
	for i in range(4):
		game.append([0]*4)

	return game

#填充一个2
def add_two(arr):
	status=game_status(arr)
	if status!='need_add':
		return arr, status

	a=random.randint(0,3)
	b=random.randint(0,3)
	while(arr[a][b]!=0):
		a=random.randint(0,3)
		b=random.randint(0,3)
	arr[a][b]=2

	return arr,status


#游戏状态
def game_status(arr):
	#存在2048就获胜
	#存在0则游戏尚未结束
	#arr[i][j]右边和下面存在相等，游戏尚未结束
	for i in range(4):
		for j in range(4):
			if arr[i][j]==2048:
				return 'win'
			if arr[i][j]==0:
				return 'need_add'
			
	for i in range(3):
		for j in range(3):
			if arr[i][j]==arr[i][j+1] or arr[i][j]==arr[i+1][j]:
				return 'no_add'
	
	for k in range(3):
		if arr[3][k]==arr[3][k+1]:
			return 'no_add'
		if arr[k][3]==arr[k+1][3]:
			return 'no_add'

	return 'lose'

def game_operator(arr):
	try:
		str=input("请选择(上:w/下:s/左:a/右:d/退出:q): ")
		if str == 'w':
			arr = xytraslate(arr)
			arr = sorting(arr)
			arr = merge(arr)
			arr = sorting(arr)
			arr = xytraslate(arr)
			result = True
		elif str == 's':
			arr = xytraslate(arr)
			arr = ytranslate(arr)
			arr = sorting(arr)
			arr = merge(arr)
			arr = sorting(arr)
			arr = ytranslate(arr)
			arr = xytraslate(arr)
			result = True
		elif str == 'a':
			arr = sorting(arr)
			arr = merge(arr)
			arr = sorting(arr)
			result = True
		elif str == 'd':
			arr = ytranslate(arr)
			arr = sorting(arr)
			arr = merge(arr)
			arr = sorting(arr)
			arr = ytranslate(arr)
			result = True
		elif str == 'q':
			result = False
		else:
			print("输入错误!!!")
			arr, result = game_operator(arr)
	except Exception:
		result=False

	return arr, result

#开始游戏
game=new_game()
game,status=add_two(game)

while(1):
	game,status = add_two(game)
	if status=='win':
		print("恭喜你赢了！")
		break
	elif status=='lose':
		print("你输了，再接再厉~")
		break
	else:
		for i in game:
			for j in i:
				print(j,end="	")
			print()
		game,err=game_operator(game)
		if err==False:
			print ("======游戏结束~=======")
			break
