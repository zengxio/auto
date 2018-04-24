#!/usr/bin/env python
#coding:utf-8
from Course_system.src import Teacher_class
from Course_system.src import Course_class
#admin 管理员接口程序
class admin_interface_class():
    msg = '1:创建课程,2:修改课程,3:创建老师信息,4:修改老师信息'
    @staticmethod
    def interface_func():

        flag = False
        while not flag:
            print(admin_interface_class.msg)

            #选择不同的序号，调用不同的类
            choice_msg = input('Selection options:').strip()
            if choice_msg == 'q': break
            #输入字典格式的数据
            inp = input('please input you want to create course infomation:').strip()
            if not inp: continue
            if inp == 'q': break

            #判断格式是否正确
            try:
                data = eval(inp)
            except Exception as e:
                print('error',e)

            #判断输入的数据是否是字典格式
            if isinstance(data, dict):
                #判断输入的数据为1或者2的时候，并且确定是根据课程为关键字，调用课程类的方法
                if choice_msg =='1'or choice_msg=='2' and data.get('course_name'):
                        res=Course_class.Course.Create_revision_course(choice_msg,data)

                #判断输入的数据为3或者4的时候，并且确定是根据老师为关键字，调用老师类的方法
                elif choice_msg=='3' or choice_msg=='4' and data.get('teacher_name'):
                    res=Teacher_class.Teacher.create_change_teacher_info(choice_msg,data)

                #如果返回的数据为真，就表示执行成功，并询问是否继续
                if res:
                    choice = input("Do you want to continue (y/n)?")
                    if choice != 'n':
                        continue
                    flag=True


                else:
                    print('Execution error,if you do not continue, press the q key')
                    continue

            else:
                print('''The format you entered is incorrect.
                                                            If you do not continue,press the q key,
                                                            Otherwise please re-enter it as follows :%s''' % (
                        {'teacher_name': 'halen', 'sex': 'female', 'age': '27', 'assets': 15000, 'course': [],
                         'identity': 'teacher'}))
                continue


if __name__ == '__main__':

    admin_interface_class.interface_func()

