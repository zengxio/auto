#!/usr/bin/env python
#coding:utf-8
from Course_system.src import  Course_class
class Admin:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def create_teache(self):
        pass

    def create_course(self,course_name,class_time,class_fee,class_teacher):
        course_obj=Course_class.Cource(course_name,class_time,class_fee,class_teacher)
        pass


