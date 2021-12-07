class Student:
    pass
    def __init__(self, id:int, name:str):
        self.id:int = id
        self.name:str = name

    def __repr__(self):
        return f"Student(id='{self.id}', name='{self.name}')"



if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/student.md')
