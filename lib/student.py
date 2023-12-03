#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
        #self.additional_knowledge = additional_knowledge
        
    def learn(self, extra):
        self.knowledge.append(extra)
        pass