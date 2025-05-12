class Counter:
    object_Counter = 0

    def __init__(self):
        Counter.object_Counter += 1

    @classmethod
    def display_count(cls):
        print("Total Objects Created" , cls.object_Counter)

Obj1 = Counter()
Obj2 = Counter()
Obj3 = Counter()
Obj4 = Counter()

Counter.display_count()
