#coding:gbk
acct=1000
print('��ǰ��'+str(float(acct)))
amt=float(input('������۳�������'))
while acct>0: #bool(acct)==True or bool(acct)==False:
    if amt<0:
        amt = float(input('��������ȷ������������۳�������'))
    elif acct-amt<0 or acct<=0:
        amt = float(input('��ǰ���㣬����������۳�������'))
    #elif acct<=0:
        #print('��ǰ���Ϊ�㣬��лʹ��')
        #break
    else:
        acct=acct-amt
        print('��ǰ��'+str(acct))
        if acct<=0:
            print('��ǰ����Ѳ��㣬��лʹ�ã�')
            break
        else:
            cmmd=input('�Ƿ�����۳�����/��')
            if cmmd=='��' or cmmd=='y' or cmmd=='Y':
                amt = float(input('���������۳�������'))
                continue
            #elif cmmd!='��' and cmmd!='��':
                #print('����������ָ�')
                #continue
            else:
                print('��лʹ�ã�')
            break
#print('��ǰ����Ѳ��㣬��лʹ�ã�')
