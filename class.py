class Students:
    def __init__(self, student={}, name=None, score=None):
        self.student = student
        self.student['name'] = name
        self.student['score'] = score

    def __repr__(self):
        try:
            return f"The student with name: {self.student['name']} has a score of: {self.student['score']}"
        except KeyError:
            return f"This is a student of name: {self.student['name']}"

    def add_score(self, score):
        if score < 0 or score > 100:
            return "score must be between 0 and 100 "
        else:
            self.student['score'] = score

    def retrieve_score(self, name):
        if name not in self.student['name']:
            return "Name not found"
        else:
            return f"{name} has a score of {self.student['score']}"
        
    def update_score(self, name, score):
        if name in self.student['name']:
            if score < 0 or score > 100:
                return "Please enter a score between 0 and 100 "
            else:
                self.student['score'] = score
        else:
            return f"{name} is not a student."
        
    def delete_score(self, name):
        if name not in self.student['name']:
            return "Name not found"
        else:
           del self.student['score']
mack = Students(name= 'mack')
mack.add_score(87)
print(mack)
mack.retrieve_score('mack')
print(mack)
mack.update_score('mack', 94)
print(mack)
mack.delete_score('mack')
print(mack)