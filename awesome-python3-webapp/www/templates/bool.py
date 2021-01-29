#coding:gbk
acct=1000
print('当前余额：'+str(float(acct)))
amt=float(input('请输入扣除数量：'))
while acct>0: #bool(acct)==True or bool(acct)==False:
    if amt<0:
        amt = float(input('数量不正确，请重新输入扣除数量：'))
    elif acct-amt<0 or acct<=0:
        amt = float(input('当前余额不足，请重新输入扣除数量：'))
    #elif acct<=0:
        #print('当前余额为零，感谢使用')
        #break
    else:
        acct=acct-amt
        print('当前余额：'+str(acct))
        if acct<=0:
            print('当前余额已不足，感谢使用！')
            break
        else:
            cmmd=input('是否继续扣除？是/否')
            if cmmd=='是' or cmmd=='y' or cmmd=='Y':
                amt = float(input('请继续输入扣除数量：'))
                continue
            #elif cmmd!='否' and cmmd!='是':
                #print('请重新输入指令。')
                #continue
            else:
                print('感谢使用！')
            break
#print('当前余额已不足，感谢使用！')
