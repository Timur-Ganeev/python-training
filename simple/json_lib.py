import json

l = "[1, 2, 'g', 'w2', -1, 0.02]"
l_nums = "[1, 2, 3]"
l_nums_2 = "[0.1, 2, 00.030]"
l_alpha = '["a1", "a2", "a-0"]'
# n = '["a", 0.1, -1, "bhj76ghguyrty9y9u"]'
n = '[0.1, 2, 0.0010]'
result = json.loads(n)
#
print(result)
# print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))