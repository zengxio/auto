# # # from concurrent.futures import ProcessPoolExecutor
# # # import  time
# # # def task(name):
# # #     print("name",name)
# # #     time.sleep(1)
# # #
# # # if __name__ == "__main__":
# # #     # start = time.time()
# # #     p = ProcessPoolExecutor(2)
# # #
# # #     for i in range(100):
# # #         p.submit(task,"safly%d"%i)
# # #     # p.shutdown(wait=True)
# # #     #
# # #     # print("main")
# # #     # end = time.time()
# # #     # print(end - start)
# # from Crypto.Cipher import AES
# # def encrypt(message):
# #     key=settings.DATA_KEY  #由用户输入的16位或24位或32位长的初始密码字符串
# #     cipher=AES.new(key,AES.MODE_CBC,key)
# #     ba_data=bytearray(message,encoding='utf-8')  #ba_data必须是16字节或16字节的倍数
# #     v1=len(ba_data)
# #     v2=v1 % 16
# #     if v2==0:
# #         v3=16
# #     else:
# #         v3=16-v2
# #     for i in range(v3):  #填充相差的字节数，以满足16或者16的倍数
# #         ba_data.append(v3)
# #     final_data=ba_data.decode('utf-8')
# #     msg=cipher.encrypt(final_data)
# #     return msg
# #
# #
# # def decrypt(msg):
# #     key = settings.DATA_KEY
# #     cipher=AES.new(key,AES.MODE_CBC,key)
# #     result=cipher.decrypt(msg)
# #     data=result[0:-result[-1]]  #去除填充的数据
# #     return str(data,encoding='utf-8')
# #
# # print(decrypt(encrypt('加密数据fdsafafs')))
#
# L=[(10,15),(16,23),(25,29),(30,35),(37,42),(50,60),(61,65),(70,80),(81,85),(90,100)]
#
# n=5
# select=int(input('>>'))
# while True:
#     try:
#         n-=1
#         L1=L[:5][n]
#         L2=L[5:][n]
#
#         if select in L1:
#             print('1 %d'%select)
#         elif select in L2:
#             print('2 %d'%select)
#     except Exception:
#         break
a={
    'k1':'v1',
    'k2':'v2',
    'k3':'v3',
   }
for i in list(a.keys()):
    if a[i]=='v2':
        del a[i]
print(
    a
)