# 读取行数和列数（在同一行输入，用空格分隔）
people, actions = map(int, input().split())
matrix_people = []
matrix_actions = []

# 读取人物特征
for _ in range(people):
    person_features = list(input().split())
    matrix_people.append(person_features)

# 读取动作指令
for _ in range(actions):
    direction, number = map(int, input().split())
    matrix_actions.append((direction, number))

start_index = 0

# 处理动作指令
for row in matrix_actions:
    direction, number = row
    if direction == 1:  # 向前移动
        if matrix_people[start_index][0] == '0':  # 如果当前状态是 '0'
            start_index = (start_index + number) % people  # 循环向前移动
        else:  # 如果当前状态不是 '0'
            start_index = (start_index - number) % people  # 循环向后移动
    elif direction == 0:  # 向后移动
        if matrix_people[start_index][0] == '0':  # 如果当前状态是 '0'
            start_index = (start_index - number) % people  # 循环向后移动
        else:  # 如果当前状态不是 '0'
            start_index = (start_index + number) % people  # 循环向前移动

# 输出结果
print(matrix_people[start_index][1])
