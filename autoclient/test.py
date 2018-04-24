# #!/usr/bin/env python
# #encoding:utf-8
# # class A():
# #     def __init__(self):
# #         return
# #
# # a=A()
# # print(a)
# #100任务
# #线程池ThreadPoolExecutor
# # from concurrent.futures import ProcessPoolExecutor
# # from concurrent.futures import ThreadPoolExecutor
# # import time
# #
# #
# # def task(i):
# #     time.sleep(1)
# #     print(i)
# #
# # if __name__ == '__main__':
# #     # p=ThreadPoolExecutor(10) #最多开10个线程
# #     p=ProcessPoolExecutor(10) #最多开10个进程
# #     for row in range(100):
# #         p.submit(task,row)
#
# # msg_list = [
# #         {'id': 1, 'content': '太好了', 'parent_id': None},
# #         {'id': 2, 'content': '你说得对', 'parent_id': None},
# #         {'id': 3, 'content': '顶楼上', 'parent_id': None},
# #         {'id': 4, 'content': '你眼瞎吗', 'parent_id': 1},
# #         {'id': 5, 'content': '我看是', 'parent_id': 4},
# #         {'id': 6, 'content': '嘿嘿', 'parent_id': 2},
# #         {'id': 7, 'content': '是你没呀', 'parent_id': 5},
# #         {'id': 8, 'content': 'xxxxxxx', 'parent_id': 3},
# #
# #     ]
# # result = []
# # msg_list_dict = {}
# # for i in msg_list:
# #
# #     i['child'] = []
# #     msg_list_dict[i['id']] = i
# #     pid = i['parent_id']
# #     if pid:
# #         msg_list_dict[pid]['child'].append(i)
# #     else:
# #         result.append(i)
# #
# #
# # for v in result:
# #     print(v)
#
# d = [(10,15),(16,23),(25,29),(30,35),(37,42),(50,60),(61,65),(70,80),(81,85),(90,100)]
#
#
#
# def search_inner(num, source_list):
#     if len(source_list) > 2:
#         if num < source_list[int(len(source_list)/2)][0]:
#             search_inner(num, source_list[:int(len(source_list)/2)])
#         elif num == source_list[int(len(source_list)/2)][0] or num == source_list[int(len(source_list)/2)][1]:
#             print("find it")
#             index_s = source_list_back.index(source_list[int(len(source_list)/2)])
#             print("the position of your number's index  is %s in source_list" % index_s)
#         elif num > source_list[int(len(source_list)/2)][1]:
#             search_inner(num, source_list[int(len(source_list)/2):])
#     else:
#         if source_list[0][0] == num or source_list[0][1] == num:
#             print("find it")
#             index_s = source_list_back.index(source_list[0])
#             print("the position of your number's index  is %s in source_list" % index_s)
#         elif source_list[1][0] == num or source_list[1][1] == num:
#             print("find it")
#             index_s = source_list_back.index(source_list[1])
#             print("the position of your number's index  is %s in source_list" % index_s)
#         else:
#             print("not exits")
#         return
#
#
# def search(source_list):
#     num = input("please input your number: ")
#     import copy
#     global source_list_back
#     source_list_back = copy.deepcopy(source_list)
#     if num.isdigit():
#         num = int(num)
#         search_inner(num, source_list)
#     else:
#         print("***---wrong word! please input number!!!---***")
#
#
# search(d)
from Crypto.Cipher import AES
def encrypt(message):
    key=b'dfjkerllesieskfd'  #由用户输入的16位或24位或32位长的初始密码字符串
    cipher=AES.new(key,AES.MODE_CBC,key)
    ba_data=bytearray(message,encoding='utf-8')  #ba_data必须是16字节或16字节的倍数
    v1=len(ba_data)
    v2=v1 % 16
    if v2==0:
        v3=16
    else:
        v3=16-v2
    for i in range(v3):  #填充相差的字节数，以满足16或者16的倍数
        ba_data.append(v3)
    final_data=ba_data.decode('utf-8')
    msg=cipher.encrypt(final_data)
    return msg


def decrypt(msg):
    key = b'dfjkerllesieskfd'
    cipher=AES.new(key,AES.MODE_CBC,key)
    result=cipher.decrypt(msg)
    data=result[0:-result[-1]]  #去除填充的数据
    return str(data,encoding='utf-8')
print(decrypt(encrypt('加密数据fdsafafs')))



def auth():
    import hashlib
    import time
    key='dfjiosajiofjewnenwoiewfndsslafdsa'

    ctime=time.time()
    m=hashlib.md5()
    new_key="%s|%s"%(key,ctime)
    m.update(new_key.encode("utf8"))
    md5_key=m.hexdigest()
    md5_time_key="%s|%s" %(md5_key,ctime)
    print(md5_time_key)
    import requests
    # response=requests.get('http://127.0.0.1:8000/api/asset.html',headers={'OpenKey':md5_time_key})
    response=requests.post('http://127.0.0.1:8000/api/asset.html',headers={'OpenKey':md5_time_key})
    print(response.text)