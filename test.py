import itertools
import random


class Board:
    def __init__(self, board_array):
        # 後々使いそうな変数はself.の形にして保存しておく
        self.array = board_array
        self.height_list = self.make_height_list()
        self.box_list = self.make_box_list()

    # 縦区切りの全体リスト(height_list)を作成する。return: [ [要素*9], ... *9]
    def make_height_list(self):
        height_list = []
        for a in range(9):
            temp = []
            for b in range(9):
                temp.append(self.array[b][a])
            height_list.append(temp)
        return height_list

    # 3*3ブロック区切りのリストを作成する。return: [ [要素*9], ... *9]
    def make_box_list(self):
        block_list = []
        temp = []
        # 3*3ボックスの中心の座標は(1,1), (1,4), (1,7), (4,1), ... , (7,7)
        for center_x_y in itertools.product([1,4,7],[1,4,7]):
            temp = []
            """
            中心の座標から(-1,-1), (-1,0), (-1,1), (0,-1), ... , (1,1)だけ
            移動した９つの場所（3*3ボックス）を配列にappendする。これを中心の座標の数(9)だけ繰り返す。
            """
            for dx_dy in itertools.product([-1,0,1],[-1,0,1]):
                temp.append(self.array[center_x_y[0] + dx_dy[0]][center_x_y[1] + dx_dy[1]])
            block_list.append(temp)
        return block_list

    def printArray(self):
        for i in self.array:
            print(i)





final_Board = [
    [0, 4, 0, 6, 0, 7, 0, 1, 0],
    [1, 0, 5, 0, 4, 0, 9, 0, 6],
    [6, 0, 7, 0, 3, 0, 5, 0, 2],
    [0, 9, 0, 7, 0, 2, 0, 3, 0],
    [8, 0, 1, 0, 6, 0, 4, 0, 9],
    [3, 0, 2, 0, 9, 0, 8, 0, 7],
    [0, 5, 0, 9, 0, 3, 0, 8, 0],
    [0, 1, 0, 8, 0, 4, 0, 6, 0],
    [4, 0, 8, 0, 1, 0, 7, 0, 3]]

Board_Overall = []
# 初期の盤面の状況を入力して保存する
def load(message):
    initial_condition = input(message)
    # inputされた値が九桁の数字である（int型に置き換えられる）ことを確かめる
    try:
        x = int(initial_condition) 
    except ValueError:
        return 0
    if len(initial_condition) == 9:
        return initial_condition
    else:
        return 0

# 入力された横列ごとの情報を一つのリストにまとめる
def combine(information):
    all_condition = [int(x) for x in list(str(information))]
    Board_Overall.append(all_condition)
    return Board_Overall

# 縦区切りの全体リスト(combine)を作成する
def height_list(information):
    combine = []
    for a in range(9):
        height_list = []
        for b in range(9):
            height_list.append(information[b][a])
        combine.append(height_list)
    return combine

# 3*3 のリストを作成する
def box_list(information):
    combine = []
    count =[[0,1,2],[3,4,5],[6,7,8]]
    for a in range(3):
        for b in range(3):
            box_list  = []
            for c in count[a]:
                for i in count[b]:
                    box_list.append(information[c][i])
            combine.append(box_list)
    return combine


# 横の判定をする
def judge_width(information):
    final = []
    for h in range(9):
        line = []
        for i in range(9):
            if not h+1 in information[i]:
                x = [i]
                y = [a for a, b in enumerate(information[i]) if b == 0]
                # (縦,横)で情報をまとめる
                v = list(itertools.product(x,y))
            else:
                v = []
            line.append(v)
        final.append(line)
    return final

# 縦の判定をする（横の判定とまとめたい）
def judge_height(information):
    final = []
    for h in range(9):
        line = []
        for i in range(9):
            if not h+1 in information[i]:
                x = [i]
                
                y = [a for a, b in enumerate(information[i]) if b == 0]
                #　(縦,横)で情報をまとめる
                v = list(itertools.product(y,x))
            else:
                v = []
            line.append(v)
        final.append(line)
    return final

# 3*3の判定をする
def judge_box(information):
    final = []
    for h in range(9):
        box = []
        for i in range(9):
            if not h+1 in information[i]:
                if i == 0 or i == 1 or i == 2:
                    x = [0,1,2]
                elif i == 3 or i == 4 or i == 5:
                    x = [3,4,5]
                else:
                    x = [6,7,8]
                if i % 3 == 0:
                    y = [0,1,2]
                elif i % 3 == 1:
                    y = [3,4,5]
                else:
                    y = [6,7,8]
                # (縦,横)で情報をまとめる
                v = list(itertools.product(x,y))
            else:
                v = [tuple([])]
            box.append(v)
        final.append(box)
    return final

# できればこの中身をまとめたい
def set_able(x,y,z):
    set_all = []
    for h in range(9):
        list_x = []
        list_y = []
        list_z = []
        for i in range(9):
            list_x.append(x[h][i])
            list_y.append(y[h][i])
            list_z.append(z[h][i])
        #　特にここらへん　↓
        new_list1 = list_x[0] + list_x[1] +list_x[2] + list_x[3] + list_x[4] + list_x[5] + list_x[6] + list_x[7] + list_x[8]
        new_list2 = list_y[0] + list_y[1] +list_y[2] + list_y[3] + list_y[4] + list_y[5] + list_y[6] + list_y[7] + list_y[8]
        new_list3 = list_z[0] + list_z[1] +list_z[2] + list_z[3] + list_z[4] + list_z[5] + list_z[6] + list_z[7] + list_z[8]
        set_x = set(new_list1)
        set_y = set(new_list2)
        set_z = set(new_list3)
        set_all.append(list(set_x & set_y & set_z))
    return set_all

# 確定した数字を代入する
def assign(x,y):
    for n in [0,3,6]:
        new_list = y[n] + y[n + 1] +y[n + 2]
        for i in range(9):
            num = new_list.count(i + 1)
            a = [n,n+1,n+2]
            b = [0,1,2,3,4,5,6,7,8]
            but = list(itertools.product(a,b))
            if len(set(x[i]) & set(but)) == 3 - num and not num == 3:
                print(list(set(x[i]) & set(but)))
                print(i + 1)
        print("________")


def main():
    # for i in range(9):
    #     condition = load(str(i+1) + "行目の盤面の状況を入力してください")
    #     while condition == 0:
    #         condition = load("入力にミスがあります。再入力してください")
    #     final_Board = combine(condition)
    # print(final_Board)
    list_of_height = height_list(final_Board)
    list_of_boxes = box_list(final_Board)
    for a in range(9):
        print (final_Board[a])
    able_width = judge_width(final_Board)
    able_height = judge_height(list_of_height)
    able_boxes = judge_box(list_of_boxes)
    set_all = set_able(able_width,able_height,able_boxes)
    assign(set_all,final_Board)

# main()

def main2():
    """
    Boardクラス

    変数:
    .array: 盤面の配列情報
    .height_list: 縦区切りの盤面の配列情報
    .box_list: 3*3ボックス区切りの盤面の配列情報

    メソッド:
    .printArray(): 現在の盤面の配列情報を出力する。

    """
    board = Board(final_Board)
    board.printArray()

main2()