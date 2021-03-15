# AI-BL-405-teamwork1
动物识别系统的python实现，详细题目见`实验要求.md`。
## `Animal.py`
包含`class Animal`，用来存储动物类型。
`Animal`类的`name``features``labels`分别表示名字、特征和所属类别
## `Identify.py`
包含`class Identify`用来根据规则识别动物
## `IdentifyRules.txt`
用来存储识别规则
例如：
`IF (canine teeth) IF (paws) IF (binocular vision) THEN [carnivore]`
中，IF后紧跟的内容是判断依据，其中小括号`(x)`代表特征`x`，中括号`[y]`代表特征`y`
## `AnimalIdentify.py`
主函数，实现识别

---

## `database`(未实现)
