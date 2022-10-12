import re

data_str = "00.123"
data_str_2 = "9999"
data_str_3 = ".123"
data_str_4 = "12."
data_str_5 = "0.b"

re_filter = r'(?P<count>\d+\.\d+)'
# r'\d+(\.\d*)?'

result = re.search(re_filter, data_str)
print(result.group("count"))
print(bool(result))
result = re.match(re_filter, data_str_2)
print(result)
print(bool(result))
result = re.match(re_filter, data_str_3)
print(result)
print(bool(result))
result = re.match(re_filter, data_str_4)
print(result)
print(bool(result))
result = re.match(re_filter, data_str_5)
print(result)
print(bool(result))

# likes = 0
# reposts = 0
# messages = ['Лайков: 3, Репостов: 5', 'Лайков: 3, Репостов: 5','Лайков: 3, Репостов: 5']
#
# like_pattern = r'Лайков:\s*\d+'
# repost_pattern = r'Репостов:\s*\d+'
#
# for msg in messages:
#     if re.findall(like_pattern, msg):
#         print(re.findall(like_pattern, msg))
#         likes += int(re.findall(r'\d+', re.findall(like_pattern, msg)[0])[0])
#     if re.findall(repost_pattern, msg):
#         print(re.findall(repost_pattern, msg))
#         reposts += int(re.findall(r'\d+', re.findall(repost_pattern, msg)[0])[0])
#
# print(likes)
# print(reposts)

# r"[.?!]\s"