#!/usr/bin/env python
#coding:utf-8
import os
import pickle
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
student_info_file=os.path.join(BASE_DIR,"db","Student_info_file")
teacher_info_file=os.path.join(BASE_DIR,"db","Teacher_info_file")
course_info_file=os.path.join(BASE_DIR,"db","Course_info_file")
admin_info_file=os.path.join(BASE_DIR,"db","Admin_info_file")
# userdb=os.path.join(BASE_DIR,'db','userdb')

student_data={"zxy":{"username":"zxy","password":"123",'age':'20',"sex":"female","course_list":[],"class_record":[],'login':False},"yanzi":{"username":"yanzi","password":"123",'age':'20',"sex":"female","course_list":[],"class_record":[],'login':False}}
teacher_data={'halen':{'teacher_name':'halen','sex':'female','age':'27','assets':15000,'course':[]},'aric':{'teacher_name':'aric','sex':'female','age':'27','assets':15000,'course':[]}}
admin_data={'admin':{'username':'admin','password':'123','login':False}}
course_data={'python':{'course_name':'python','class_time':'7m','class_fee':'19800','class_teacher':'aric'},'linux':{'course_name':'linux','class_time':'5m','class_fee':'23000','class_teacher':'halen'}}


#打开文件的类
class Open_file_class():
    def __init__(self,file_path,model='rb'):
        self.x=open(file_path,mode=model)

    #如果是写模式，就用pickle先进行序列化写入
    def write(self,line):
        print('正在写入...')
        pickle_line=pickle.dumps(line)
        self.x.write(pickle_line)

    #如果是读模式，就用pickle先进行序列化读取数据并返回
    def read(self):
        read_line=self.x.read()
        pickle_read_line=pickle.loads(read_line)
        return pickle_read_line


    def __del__(self):
        self.x.close()

if __name__ == '__main__':
#     f_read=Open_file_class()
#     print(f_read.read())
# else:
#     write_f=Open_file_class(student_info_file,model='wb')
#     write_f.write(student_data)
#     write_f = Open_file_class(teacher_info_file, model='wb')
#     write_f.write(teacher_data)
#     write_f = Open_file_class(admin_info_file, model='wb')
#     write_f.write(admin_data)
#     write_f = Open_file_class(course_info_file, model='wb')
#     write_f.write(course_data)
    f=Open_file_class(course_info_file)
    print(f.read())
