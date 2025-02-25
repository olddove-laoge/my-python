import math

data = input().split()  # 从输入中读取数据并分割成列表
s = int(data[0])  # 路程（米）
v = int(data[1])  # 速度（米/分钟）

# 计算步行时间（分钟），包括额外的 10 分钟垃圾分类时间
time_walk = math.ceil(s / v) + 10

# 学校要求 8:00 到达，计算最晚出发时间
arrival_time = 8 * 60  # 8:00 对应的分钟数（从 0:00 开始）
latest_departure_time = arrival_time - time_walk

# 处理时间范围（确保在 0:00 到 23:59 之间）
if latest_departure_time < 0:
    latest_departure_time += 1440  # 如果时间小于 0，加上一天的分钟数

# 计算小时和分钟
hours = latest_departure_time // 60
minutes = latest_departure_time % 60

# 格式化输出
print(f"{hours:02d}:{minutes:02d}")
