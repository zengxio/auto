#!/usr/bin/env python
#coding:utf-8
#{'teacher_name':'halen','sex':'female','age':'27','assets':15000,'course':[],'identity':'teacher'}
from Course_system.lib import Open_file
class Teacher():
    def __init__(self,teacher_name,sex,age,assets):
        self.teacher_name=teacher_name
        self.sex=sex
        self.age=age
        self.assets=assets
        #self.course=[]

    def teach_fee(self):
        pass

    @staticmethod
    def create_change_teacher_info(choice_msg,data):
        flag=False
        while not flag:
            #传入的choice_msg为3时，为创建老师，判断原数据是否存在，不存在就创建并写入数据，存在就打印已经存在
            if choice_msg=='3':
                res_data = Open_file.Open_file_class(Open_file.teacher_info_file).read()
                if data['teacher_name'] in res_data:
                    print('The curriculum already exists,if you do not continue, press the q key')
                    break
                res_course = Teacher(data['teacher_name'], data['sex'],
                                    data['age'],data['assets'])
                print('create teacher information successfully!')

                #拼接成字典
                new_course_dict = {data['teacher_name']: data}
                file_name=Open_file.teacher_info_file
                f = Open_file.Open_file_class(file_name, model='wb')
                res_data.update(new_course_dict)

                # print(res_data.update(new_course_dict))
                f.write(res_data)
                # print(res_data)
                return res_course

            #当choice_msg为4的时候，就判断数据是否存在，如不存在就打印不存在，存在则update并写入
            elif choice_msg == '4':
                read_data = Open_file.Open_file_class(Open_file.teacher_info_file).read()
                if data['teacher_name'] in read_data:
                    new_course = {data['teacher_name']: data}
                    read_data.update(new_course)
                    Res = Open_file.Open_file_class(Open_file.teacher_info_file, model='wb')
                    Res.write(read_data)
                    print('change teacher information successfully')
                    return True
                else:
                    print('teacher is not exists')
                    break
            else:
                return False


    @staticmethod
    def choice_tercher_func():
        f=Open_file.Open_file_class(Open_file.teacher_info_file)
        userdata=f.read()
        for i in userdata:
            print(i)
            #print(userdata[i])






if __name__ == '__main__':
   Teacher.choice_tercher_func()