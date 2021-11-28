#!/usr/bin/env python3

class Student:
    def __init__(self, id, height):
        self.id = id
        self.height = height
        self.friends = []
        
    def add_friend(self, friend_id):
        self.friends.append(friend_id)

def parse(instance_path):
    global students
    
    students = []

    with open(instance_path, "r") as instance_file:
        number_students = instance_file.readline()
        number_friends = instance_file.readline()
        
        for i in range(int(number_students)):
            height = instance_file.readline()
            students.append(Student(i+1, int(height))) #Ids start at 1
        
        for i in range(int(number_friends)):
            friends = instance_file.readline().split(" ")
            friend1 = int(friends[0])
            friend2 = int(friends[1])
            #Index of student is id-1
            students[friend1-1].add_friend(friend2)
            students[friend2-1].add_friend(friend1)
        
        # for i in range(len(students)):
        #     student = students[i]
        #     print("id: " + str(student.id) + " heigh: " + str(student.height) + " friends: " + str(student.friends))
    



