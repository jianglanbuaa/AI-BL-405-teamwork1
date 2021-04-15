from Animal import Animal
from Identify import Identify


def AnimalIdentify(features=[], labels=[]):
    '''调用Animal、Identify进行识别'''
    animal = Animal(name="", features=features, labels=labels)
    Identify(animal)
    print(animal)


class TestCases:
    def test():
        features = ["canine teeth", "paws", "binocular vision", "yellowish brown", "black stripe"]
        labels = ["mammal"]
        
        AnimalIdentify(features, labels)
        AnimalIdentify(features, [])


if __name__ == "__main__":
    TestCases.test()
