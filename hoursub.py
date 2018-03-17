time1 = float(input("Input time in seconds: "))
hour1 = time1// 3600
min1 = time1 // 60
print(hour1,"hour1",min1,"min1")
time2 = float(input("Input time in seconds: "))
hour2 = time2// 3600
min2 = time2 // 60
print(hour2,"hour2",min2,"min2")
hour=hour1-hour2
min=min1-min2
print(hour,"hour",min,"min")
