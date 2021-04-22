import re
from Database import Database
RULESPATH = 'IdentifyRules.txt'


class Rules:

    def __init__(self, rulespath=RULESPATH):
        self._rulespath = RULESPATH
        self._rules = self.read_rules()
        self._DB = Database()

    def get_rules(self):
        return self._rules
        
    def read_rules(self):
        ''' 读取rulespath进行规则读取 '''
        with open(self._rulespath, 'r', encoding='utf-8') as lines:
            Rulelist = []

            for line in lines:
                split_by_THEN = re.split('THEN', string=line)
                IF_statement = split_by_THEN[0].strip()  # split_by_THEN的第一个元素是IF语句段
                THEN_statement = split_by_THEN[1].strip()   # split_by_THEN的第二个元素是THEN语句段

                dic = {}
                # IF_feature代表IF语句中的feature判断，其余同
                IF_feature = re.findall(re.compile(r'[(](.*?)[)]'), IF_statement)
                IF_label = re.findall(re.compile(r'[\[](.*?)[\]]'), IF_statement)

                THEN_feature = re.findall(re.compile(r'[(](.*?)[)]'), THEN_statement)
                THEN_label = re.findall(re.compile(r'[\[](.*?)[\]]'), THEN_statement)
                THEN_name = re.findall(re.compile(r'[\{](.*?)[\}]'), THEN_statement)
                dic['IF_feature'] = IF_feature
                dic['IF_label'] = IF_label
                dic['THEN_feature'] = THEN_feature
                dic['THEN_label'] = THEN_label
                dic['THEN_name'] = THEN_name

                Rulelist.append(dic)

        return(Rulelist)
    
    def add_rules(self, IF_feature, IF_label, THEN_feature, THEN_label, THEN_name):
        with open(self._rulespath, 'a+', encoding='utf-8') as lines:
            rule = "IF"
            for IF_feature in IF_feature:
                rule += f" ({IF_feature}) "
            for IF_label in IF_label:
                rule += f" ({IF_label}) "
            rule += "THEN"
            for THEN_feature in IF_feature:
                rule += f"({IF_feature})"
            for IF_feature in IF_feature:
                rule += f"({IF_feature})"
            for THEN_name in THEN_name:
                rule += " {" + THEN_name + "} "
            rule = rule[:-1] + '\n'
            lines.write(rule)
            self._DB.log(f"add rules : {rule}")

    def delete_rules(self):
        with open(self._rulespath, 'r', encoding='utf-8'):
            pass
