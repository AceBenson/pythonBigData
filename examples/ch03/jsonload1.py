import json
class_str = """
{
  "一年甲班": [
    {
      "座號": 1,
      "姓名": "葉大雄",
      "國文": 65,
      "英文": 62,
      "數學": 40
    },
    {
      "座號": 2,
      "姓名": "陳靜香",
      "國文": 85,
      "英文": 90,
      "數學": 87
    },
    {
      "座號": 3,
      "姓名": "王聰明",
      "國文": 92,
      "英文": 90,
      "數學": 95
    }
  ]
}
"""
datas = json.loads(class_str)
print(type(datas))
for data in datas["一年甲班"]:
    print(data, data['姓名'])