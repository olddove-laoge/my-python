#这个程序可以自动将你输入的学生成绩绘制成表格并排序
import openpyxl

lst=[['学生姓名','语文','数学','英语','物理','化学','地理','总分']]
while True:
    student_goal=input('请输入学生的名字及各科成绩，用逗号隔开，若想停止输出，请输入exit：')
    
    if student_goal == 'exit':
        break
    student_goal_str=student_goal.split('，')
    
    
    if len(student_goal_str)!=7:
        print('请正确输入6科成绩')  #判断是否输入7科成绩
        s=0
        continue



    sum_goal=0  #初始化总分
    
    

    for i in range(1,7):
        s=1
        if i in range (1,7):
            while True:
                try:
                    # global score
                    score = int(student_goal_str[i])
                    

                except ValueError:
                    print('各科分数应为整数！')
                    s=0
                
                break



        if i in range(1,4):#检验主科分数是否有误
            if score < 0  or  score > 150:
                print('主课成绩应为0-150分！')
                s=0
                break
       
     
        if i in range(4,7):#检验副科分数是否有误
            if score < 0 or  score > 100:
                print('副科成绩应为0-100分！')
                s=0
                break
      
        else:
            s=1
     
     
        if s==1:
            sum_goal+=score
    
    
    if s==1:    
        student_goal_str.append(sum_goal)
        lst.append(student_goal_str)
        print('当前已添加学生成绩：',lst)



# 计算排名并添加到列表
sorted_lst = sorted(lst[1:], key=lambda x: x[-1], reverse=True)  # 根据总分降序排序
lst[0].insert(0,'排名')
# 添加排名信息



ranked_lst = []
for index, student in enumerate(sorted_lst, start=1):
    new_student = [index] + student  # 创建一个包含排名的新列表
    ranked_lst.append(new_student)  # 将新列表添加到排名列表中


final_lst = [lst[0]] + ranked_lst


print("最终排名列表：")
for item in final_lst:
    print(item)


workbook=openpyxl.Workbook()
sheet=workbook.create_sheet('学生成绩')


for item in ranked_lst:
    sheet.append(item)
workbook.save('学生成绩.xlsx')
