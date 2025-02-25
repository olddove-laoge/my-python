s = ""
while True:  # 直接接收输入 E后面全部不要 就是下面截取就可以了
    s += input().strip()
    if "E" in s:
        s = s[:s.find("E") + 1]
        break
 
w, l = 0, 0  # 用两个计数
for i in s:
    if i == "W":
        w += 1
    if i == "L":
        l += 1
    if i == "E":
        print("%d:%d" % (w, l))
    if w - l >= 2 or l - w >= 2:  # 首先分差得大于等于2才可以哦
        if w >= 11 or l >= 11:
            # 其次就是w或者l必须要有一个大于11才可以 因为11盘为一把
            # 其实这个地方我觉得题目有问题 难道不是打到了11盘只要分差大于等于2不就可以了吗
            #  我用w+l>=11这样提交还出问题了 所以用11 下面21也是一样得
            print("%d:%d" % (w, l))
            w, l = 0, 0  # 每次输出比分之后 是不是就是清空计数啊 下一次继续比呗
 
w, l = 0, 0  # 11最后E之前还有一些计数 也要清空 
print()
for i in s:
    if i == "W":
        w += 1
    if i == "L":
        l += 1
    if i == "E":
        print("%d:%d" % (w, l))
    if w - l >= 2 or l - w >= 2:
        if w >= 21 or l >= 21:
            print("%d:%d" % (w, l))
            w, l = 0, 0
