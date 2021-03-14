class Animal:
    ''' 用来存储动物类型 '''
    def __init__(self, name, features=[], labels=[]):
        self._name = name
        self._features = features
        self._labels = labels

    def get_name(self):
        return self._name

    def get_features(self):
        return self._features
    
    def get_labels(self):
        return self._labels
    
    def update_name(self, name):
        self._name = name

    def update_features(self, features):
        self._features = features

    def update_labels(self, label):
        self._labels = label
    
    def append_feature(self, feature):
        self._features.append(feature)
    
    def append_label(self, label):
        self._labels.append(label)
    
    def remove_feature(self, feature):
        if feature in self._features:
            self._features.remove(feature)
        else:
            print(f"feature {feature} does not exist.")
    
    def remove_label(self, label):
        if label in self._labels:
            self._features.remove(label)
        else:
            print(f"label {label} does not exist.")
    
    def has_feature(self, feature):
        return feature in self._features
    
    def has_label(self, label):
        return label in self._labels
