nameDB = ['leopard', 'tiger', 'giraffe', 'zebra', 'ostrich', 'penguin', 'albatross']
featureDB = ['hair', 'breast milk', 'feather', 'capable of flying', 'incapable of flying', 'skilled in flying', 'lay eggs', 'carnivorous', 'canine teeth', 'paws', 'binocular vision', 'hoof', 'yellowish brown', 'dark spots', 'black stripe', 'long neck', 'black stripe', 'long legs', 'swim', 'black and white']
labelDB = ['mammal', 'bird', 'carnivore', 'ungulate']

DB = dict(nameDB=nameDB, featureDB=featureDB, labelDB=labelDB)


class Database:
    '''综合数据库，实现增删改查'''
    def __init__(self, DB=DB):
        self._DB = DB
    
    def add(self, item, DBname='nameDB'):
        if item in self._DB[DBname]:
            print('item has existed!')
        else:
            self._DB[DBname].append(item)
    
    def delete(self, item, DBname='nameDB'):
        if item in self._DB[DBname]:
            self._DB[DBname].remove(item)
        else:
            print('item does not exist!')
    
    def amend(self, item1, item2, DBname='nameDB'):
        '''将item1改成item2'''
        DB = self._DB[DBname]
        if item1 in DB:
            DB[DB.index(item1)] = item2
        else:
            print('item does not exist!')
    
        
