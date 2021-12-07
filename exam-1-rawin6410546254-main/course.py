class Course:
    pass
    def __init__(self, id:str, name:str, credits:str):
        self.id:str = id
        self.name:str = name
        self.credits:str = credits

    def __repr__(self):
        return f"Course(id='{self.id}', name='{self.name}', credits={self.credits})"



if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/course.md')
