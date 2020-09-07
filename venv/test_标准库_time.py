import time

print(time.asctime())
print(time.time())
print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S"))

now_timestamp = time.time()
lastday_time_timestamp = now_timestamp - 60*60*24*2
time_tuple = time.localtime(lastday_time_timestamp)
print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple))