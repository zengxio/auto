#! /usr/bin/evn python
# -*- coding:utf-8 -*-

import os
import copy
import time

current_user = []   # 当前登录用户
count = {}          # 用于临时存放新创建的用户的信息


def create_count():
    c_id = input("please input ID number:")
    c_name = input("please input user name:")
    c_login_password = input("please input login password:")
    i = 0
    while i < 3:     # 重新确认登陆密码，最多确认三次
        i += 1
        c_login_password1 = input("please input login password again:")
        if c_login_password1 == c_login_password:
            break
        if i == 3:
            print("You have input the wrong password 3 times.please restart to create count")
            exit()
    c_count_money = input("please input count money:")
    c_pay_password = input("please input pay password:")
    j = 0
    while j < 3:   # 重新确认交易密码，最多确认三次
        j += 1
        c_pay_password1 = input("please input login password again:")
        if c_pay_password1 == c_pay_password:
            break
        if j == 3:
            print("You have input the wrong password 3 times.please restart to create count")
            exit()
    count["ID"] = c_id
    count["name"] = c_name
    count["login_password"] = c_login_password
    count["count_money"] = [c_count_money, 0]    # c_count_money为指定的最大额度，0为已使用额度，默认为0
    count["pay_password"] = c_pay_password
    count_show = copy.deepcopy(count)
    count_show["login_password"] = "********"
    count_show["pay_password"] = "********"
    print("The user has been created!\n%s" % count_show)
    with open("count_table", "a", encoding="utf-8") as f:    # 将用户信息存入文件
        f.write("%s\n" % str(count))


def login():
    flag = False
    name = input("please input your name: ")
    ff = os.path.exists("block_list")
    if ff:
        f = open("block_list")
        if name in f:  # 检验账户是否已冻结
            print("This count has been blocked")
            while True:
                name = input("please input other name: ")
                if name not in f:
                    break
    login_password = input("please input your login password: ")
    f = open("count_table", encoding="utf-8")
    for line in f:
        line = eval(line)
        if name == line["name"] and login_password == line["login_password"]:
            current_user.append(line["name"])
            print("login \033[32;1m Successful\033[0m")
            flag = True
            break
    if not flag:
        print("login \033[32;1m Failure:\033[0m user name not exists or password is wrong."
              "please login again")


def get_cash():
    if current_user:
        import os
        with open("count_table", "r", encoding="utf-8") as f_r, open("count_table_new", "w", encoding="utf-8") as f_w:
            for line in f_r:
                line = eval(line)
                if line["name"] == current_user[-1]:
                    print("the money you can get most is %s" % line["count_money"][0])
                    while True:
                        cash = int(input("please input the money you want:"))
                        if cash < int(line["count_money"][0]):
                            break
                        else:
                            print("account shows a negative balance")   # 余额不足
                    line["count_money"][0] = int(line["count_money"][0]) - cash
                    line["count_money"][1] = int(line["count_money"][1]) + cash
                    with open("%s_list" % line["name"], "a", encoding="utf-8") as f:     # 账单
                        act_time = time.strftime('%Y-%m-%d %X')
                        f.write("%s\n =========>>You get money %s\n" % (act_time, cash))
                        f.flush()
                    print("your account balance is \033[32;0m%s\033[1m" % line["count_money"][0])
                f_w.write("%s\n" % str(line))
        os.rename("count_table", "count_table_bak")
        os.rename("count_table_new", "count_table")
        os.remove("count_table_bak")     # 删除旧文件（下次再存钱时就不会因为文件名已存在或者相同而报错）
    else:
        print("please login first")


def save_cash():
    if current_user:
        import os
        with open("count_table", "r", encoding="utf-8") as f_r, open("count_table_save", "w", encoding="utf-8") as f_w:
            for line in f_r:
                line = eval(line)
                if line["name"] == current_user[-1]:
                    print("the money of your debt is %s" % line["count_money"][1])
                    cash = int(input("please input the money you save:"))
                    with open("%s_list" % line["name"], "a", encoding="utf-8") as f:  # 账单
                        act_time = time.strftime('%Y-%m-%d %X')
                        f.write("%s\n =========>>You save money %s\n" % (act_time, cash))
                        f.flush()
                    if cash == int(line["count_money"][1]):      # 存款等于欠款
                            print("you have no debts")
                            line["count_money"][0] = int(line["count_money"][0]) + cash    # 恢复额度
                            line["count_money"][1] = 0
                    elif cash < int(line["count_money"][1]):     # 存款小于欠款
                        line["count_money"][0] = int(line["count_money"][0]) + cash
                        line["count_money"][1] = int(line["count_money"][1]) - cash
                        print("you have back %s,current debt is %s" % (cash, line["count_money"][1]))
                    else:                                        # 存款大于欠款
                        line["count_money"][0] = int(line["count_money"][0]) + int(line["count_money"][1])
                        line["count_money"][1] = int(line["count_money"][1]) - cash
                        print("you have no debts,current debt is %s" % (line["count_money"][1]))
                f_w.write("%s\n" % str(line))
        os.rename("count_table", "count_table_bak2")
        os.rename("count_table_save", "count_table")
        # os.remove("count_table_save")
        os.remove("count_table_bak2")     # 删除旧文件（下次再存钱时就不会因为文件名已存在或者相同而报错）
    else:
        print("please login first")


def bill():                    # 没有存取款时账单不存在，先用try判断一下
    if current_user:
        try:
            with open("%s_list" % current_user[-1], "r", encoding="utf-8") as f:  # 查看账单
                t = time.strftime('%Y-%m-%d')
                if t[-2:] == str(1):    # 为指定出账单日，验证时可改为当日日期，就可以看到账单
                    for m in f:
                        print(m)
        except FileNotFoundError:
            print("no trade,no bill")
    else:
        print("please login first")


def transfer_cash():
    if current_user:
        transfer = []
        with open("count_table", "r", encoding="utf-8") as f_r, open("count_table_save", "w", encoding="utf-8") as f_w:
            for line in f_r:
                line = eval(line)
                if line["name"] == current_user[-1]:
                    print("You have %s to transfer" % line["count_money"][0])
                    transfer_name = input("please input the name you transfer money to: ")
                    transfer.append(transfer_name)
                    cash_trans = int(input("please input the money you transfer:"))
                    transfer.append(cash_trans)
                    line["count_money"][0] = int(line["count_money"][0]) - cash_trans
                    line["count_money"][1] = int(line["count_money"][1]) + cash_trans
                    with open("%s_list" % line["name"], "a", encoding="utf-8") as f:  # 账单
                        act_time = time.strftime('%Y-%m-%d %X')
                        f.write("%s\n =========>>You transfer money %s\n" % (act_time, cash_trans))
                        f.flush()
                f_w.write("%s\n" % str(line))
                f_w.flush()
        with open("count_table_save", "r", encoding="utf-8") as f_r1, open("count_table_save1", "w", encoding="utf-8") \
                as f_w1:
            for line in f_r1:
                line = eval(line)
                if line["name"] == transfer[0]:
                    line["count_money"][0] = int(line["count_money"][0]) + transfer[1]
                    with open("%s_list" % line["name"], "a", encoding="utf-8") as f:  # 账单
                        act_time = time.strftime('%Y-%m-%d %X')
                        f.write("%s\n =========>>You  get transfer_money %s\n" % (act_time, transfer[1]))
                        f.flush()
                f_w1.write("%s\n" % str(line))
                f_w1.flush()

        os.rename("count_table", "count_table_back")
        os.rename("count_table_save1", "count_table")
        os.remove("count_table_back")  # 删除旧文件（下次再存钱时就不会因为文件名已存在或者相同而报错
        os.remove("count_table_save")
    else:
        print("please login first")


def back_cash():
    if current_user:
        with open("count_table", "r", encoding="utf-8") as f, open("count_table_back", "w", encoding="utf-8") as f_w:
            t = time.strftime('%Y-%m-%d')
            if t[-2:] == str(1):    # 20号为指定的还款日，验证时可改为当日日期，以便测试
                for line in f:
                    line = eval(line)
                    if line["name"] == current_user[-1]:
                        if line["count_money"][1] == 0 or line["count_money"][1] < 0:
                            print("the account is balance,no debt to back")
                        else:
                            print("your debt is %s" % (line["count_money"][1]))
                            cash = int(input("please input the money you back:"))
                            print("current debt left is %s" % (line["count_money"][1] - cash))
                            line["count_money"][1] = line["count_money"][1] - cash
                            line["count_money"][0] = line["count_money"][0] + cash
                    f_w.write("%s\n" % str(line))
                    f_w.flush()
        os.rename("count_table", "count_table_bak2")
        os.rename("count_table_back", "count_table")
        os.remove("count_table_bak2")  # 删除旧文件（下次再存钱时就不会因为文件名已存在或者相同而报错）
    else:
        print("please login first")


def block_user():
    name = input("please input the user name you want to block: ")
    with open("block_list", "a", encoding="utf-8") as f:
        f.write(name)


def out_atm():
    exit()


cmd_dic = {
                "create_count": create_count,
                "login": login,
                "get_cash": get_cash,
                "save_cash": save_cash,
                "bill": bill,
                "transfer_cash": transfer_cash,
                "back_cash": back_cash,
                "block_user": block_user,
                "out_atm": out_atm
            }


def tell_msg():
    global msg
    msg = "\033[32;1m" \
         "create_count  ------创建账户\n" \
          "login  ------------登陆\n" \
          "get_cash  ---------取现\n" \
          "save_cash  --------存款\n" \
          "transfer_cash -----转账\n" \
          "back_cash  --------还款\n" \
          "bill  -------------出账单\n" \
          "block_user  -------冻结账户\n" \
          "out_atm  ----------退出\n\033[0m"
    print(msg)


def atm():
    while True:
        tell_msg()
        choice = input("please input your choice: ").strip()
        if choice not in msg:
            print("please input right choice")
        else:
            cmd_dic[choice]()


atm()
