# AI-BL-405-teamwork1
动物识别系统的python实现，详细题目见`实验要求.md`。  
## `Animal.py`
包含`class Animal`，用来存储动物类型。  
`Animal`类的`name` `features` `labels`分别表示名字、特征和所属类别。  
## `Identify.py`
包含`class Identify`用来根据规则识别动物。  
调用`Rules.py`，通过递归添加`features`和`labels`，进而进行动物识别。  
## `IdentifyRules.txt`
用来存储识别规则
例如：  
```IF (canine teeth) (paws) (binocular vision) THEN [carnivore]```  
中，IF后紧跟的内容是判断依据，其中小括号`(x)`代表特征`features == x`，中括号`[y]`代表类别标签`label == y`。  
## `AnimalIdentify.py`
主函数，调用`Animal.py`和`Identify.py`实现识别  
## `Rules.py`
读入`IdentifyRules.txt`的规则并进行判断。  
包含`class Rules`用来读取，修改规则。  
## `Database.py`
综合数据库
实现增删改查操作的同时，记录日志文件

---
