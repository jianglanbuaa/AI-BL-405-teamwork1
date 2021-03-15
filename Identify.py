import re


class Identify:
    ''' 根据规则识别动物 '''
    def __init__(self, Animal):
        self._Animal = Animal
        self._rulespath = 'IdentifyRules.txt'
        self._Rulelist = self.rules_translate()
        ''' Rulelist中的元素为 dic，其中包含一条规则的信息
        键包括：'IF_feature'，'IF_label'，'THEN_feature'，'THEN_label'
        值为相对应的信息列表
        '''
    
    def rules_translate(self):
        ''' 读取IdentifyRules.txt进行规则读取 '''
        with open(self._rulespath, 'r', encoding='utf-8') as lines:
            Rulelist = []

            for line in lines:
                split_by_THEN = re.split(line, stirng='THEN')
                IF_statement = split_by_THEN.pop(0).strip()  # split_by_THEN的第一个元素是IF语句段
                split_by_IF = re.split(IF_statement, stirng='IF')

                dic = {}
                # IF_feature代表IF语句中的feature判断，其余同
                for statement in split_by_IF:
                    IF_feature = re.findall(re.compile(r'[(](.*?)[)]'), statement)
                    IF_label = re.findall(re.compile(r'[\[](.*?)[\]]'), statement)
                for statement in split_by_THEN:
                    THEN_feature = re.findall(re.compile(r'[(](.*?)[)]'), statement)
                    THEN_label = re.findall(re.compile(r'[\[](.*?)[\]]'), statement)
                dic['IF_feature'] = IF_feature
                dic['IF_label'] = IF_label
                dic['THEN_feature'] = THEN_feature
                dic['THEN_label'] = THEN_label

                Rulelist.append(dic)

        return(Rulelist)


