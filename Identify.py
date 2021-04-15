from Rules import Rules


class Identify:
    ''' 根据规则识别动物 '''

    def __init__(self, Animal):
        self._Animal = Animal
        rules = Rules()
        self._Rulelist = rules.get_rules()
        ''' Rulelist中的元素为 dic，其中包含一条规则的信息
        键包括：'IF_feature'，'IF_label', 'THEN_feature'，'THEN_label', 'THEN_name'
        值为相对应的信息列表
        '''
        self.judge()  # 根据规则对 Animal 的 feature 和 label 进行更新
        self.identify()  # 识别动物

    def judge(self):
        '''根据规则对 Animal 的 feature 和 label 进行递归更新'''
        features = self._Animal.get_features()
        labels = self._Animal.get_labels()

        RECURSE = False
        for Rule in self._Rulelist:
            if Rule['THEN_name'] != []:  # 如果是识别语句，则跳过
                continue

            MATCH = True
            for IF_feature in Rule['IF_feature']:
                if IF_feature not in features:
                    MATCH = False
            for IF_label in Rule['IF_label']:
                if IF_label not in labels:
                    MATCH = False
            if MATCH:
                for THEN_feature in Rule['THEN_feature']:
                    if THEN_feature not in self._Animal.get_features():
                        self._Animal.append_feature(THEN_feature)
                        IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                        self._Animal.record(f'{IF_statement} -> {THEN_feature}\n')
                        RECURSE = True
                for THEN_label in Rule['THEN_label']:
                    if THEN_label not in self._Animal.get_labels():
                        self._Animal.append_label(THEN_label)
                        IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                        self._Animal.record(f'{IF_statement} -> {THEN_label}\n')
                        RECURSE = True
        if RECURSE:  # 如果Animal的状态有更新，则递归
            self.judge()

    def identify(self):
        '''根据规则识别 Animal '''
        features = self._Animal.get_features()
        labels = self._Animal.get_labels()

        for Rule in self._Rulelist:
            if Rule['THEN_name'] == []:
                continue

            MATCH = True
            for IF_feature in Rule['IF_feature']:
                if IF_feature not in features:
                    MATCH = False
            for IF_label in Rule['IF_label']:
                if IF_label not in labels:
                    MATCH = False
            if MATCH:
                name = Rule['THEN_name'][0]
                self._Animal.update_name(name)
                IF_statement = [feature for feature in Rule['IF_feature']] + [label for label in Rule['IF_label']]
                self._Animal.record(f'{IF_statement} -> {name}\n')
                break

