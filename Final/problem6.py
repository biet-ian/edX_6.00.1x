# Problem 1 and Problem 2 were objective type questions and therefore not listed
###############################################################################
# Problem 6

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

#Given
# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return 'It is obvious that ' + self.say(stuff)

# Corrected
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

    def lecture(self, stuff):         
        return 'It is obvious that ' + Person.say(self,stuff)

# Test
e = Person('eric1') 
le = Lecturer('eric2') 
pe = Professor('eric3') 
ap = ArrogantProfessor('eric4')

print(e.say("Hello"))

print(le.say("Hello"))
print(le.lecture("Hello"))

print(pe.say("Hello"))
print(pe.lecture("Hello"))

print(ap.say("Hello"))
print(ap.lecture("Hello"))
