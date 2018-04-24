#!/usr/bin/env python
#coding:utf-8
from Course_system.lib import Open_file

class Course:
    def __init__(self,course_name,class_time,class_fee,class_teacher):
        self.course_name=course_name
        self.class_time=class_time
        self.class_fee=class_fee
        self.class_teacher=class_teacher

    @staticmethod
    #创建课程的类
    def Create_revision_course(choice_msg,data):
        flag=False
        while not flag:
            #如果传入的数据为1时，就代表创建课程，如课程存在就打印课程存在，如不存在就写入程序
            if choice_msg=='1':
                res_data=Open_file.Open_file_class(Open_file.course_info_file).read()
                if data['course_name'] in res_data:
                    print('The curriculum already exists,if you do not continue, press the q key')
                    break

                res_course=Course(data['course_name'],data['class_time'],data['class_fee'],data['class_teacher'])
                print('create course successfully!')

                #拼接成字典
                new_course_dict={data['course_name']:data}
                res_data.update(new_course_dict)
                file_name=Open_file.course_info_file
                f=Open_file.Open_file_class(file_name,model='wb')

                #print(res_data.update(new_course_dict))
                f.write(res_data)
               # print(res_data)
                return res_course

            #如果传入的值为2，就是修改课程，判断数据是否存在，存在则修改，不存在就打印不存在
            elif choice_msg=='2':
                read_data = Open_file.Open_file_class(Open_file.course_info_file).read()
                if data['course_name'] in read_data:
                    new_course={data['course_name']:data}
                    read_data.update(new_course)

                    Res=Open_file.Open_file_class(Open_file.course_info_file,model='wb')
                    Res.write(read_data)
                    print('change successfully')
                    return True
                else:
                    print('course not exists')
                    break
            else:
                return False





