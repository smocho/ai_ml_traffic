import math as m
import tensorflow as tf
import numpy as np
from tensorflow import keras
lh=[]
lv=[]
t=1
def Round(f):
    if f-m.floor(f)<0.5:
        return m.floor(f)
    elif f-m.floor(f)>0.5:
        return m.ceil(f)
    else:
        if m.floor(f)%2==0:
            return m.floor(f)
        else:
            return m.ceil(f)
def Predict(lh,lv,xs,ys,xd,yd):
    if xd>=xs and yd>=ys:
        lht=[]
        lvt=[]
        for i in range(11):
            lh1=[]
            for j in range(10):
                lh1.append([])
            lht.append(lh1)
        for i in range(11):
            lv1=[]
            for j in range(10):
                lv1.append([])
            lvt.append(lv1)
        for i in lh:
            for j in range(11):
                for k in range(10):
                    lht[j][k].append(i[j][k])
        for i in lv:
            for j in range(11):
                for k in range(10):
                    lvt[j][k].append(i[j][k])
        h1=[]
        v1=[]
        for i in range(len(lh)):
            h1.append(i)
        for i in range(len(lv)):
            v1.append(i)
        xc=xs
        yc=ys
        dr=[]
        tt=len(lh)+1
        while xc!=xd and yc!=yd:
            lhc=[]
            lvc=[]
            for i in lht:
                lhc.append(i)
            for i in lvt:
                lvc.append(i)
            hs=np.array(h1,dtype=float)
            vs=np.array(v1,dtype=float)
            r=xd-xc
            u=yd-yc
            for i in lhc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(hs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lht[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            for i in lvc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(vs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lvt[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            n=[]
            for i in range(int(m.pow(10,r+u-1)),int(m.pow(10,r+u))):
                j=i
                c1=0
                c2=0
                while j!=0:
                    d=j%10
                    if d==1:
                        c1+=1
                    if d==2:
                        c2+=1
                    j=int(j/10)
                if c1==r and c2==u:
                    n.append(i)
            for i in range(len(n)):
                n[i]=str(n[i])
            xct=xc
            yct=yc
            l=[]
            for i in n:
                s=0
                ct=len(lht[0][0])
                for j in i:
                    if j=='1':
                        s+=lhc[yc][xc][ct]
                        xc+=1
                    if j=='2':
                        s+=lvc[xc][yc][ct]
                        yc+=1
                    ct+=1
                xc=xct
                yc=yct
                l.append(s)
            mn=l[0]
            for i in l:
                if i<mn:
                    mn=i
            for i in range(len(l)):
                if l[i]==mn:
                    dr.append(n[i][0])
                    if len(dr)==1:
                        if n[i][0]=='1':
                            print('Drive straight to ('+str(xs+1)+','+str(ys)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs+1)+','+str(ys)+').')
                        if n[i][0]=='2':
                            print('Drive straight to ('+str(xs)+','+str(ys+1)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs)+','+str(ys+1)+').')
                    else:
                        if n[i][0]=='1':
                            if dr[len(dr)-2]=='1':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='2':
                                print('Turn right at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc+1)+','+str(yc)+').')
                        if n[i][0]=='2':
                            if dr[len(dr)-2]=='2':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='1':
                                print('Turn left at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc)+','+str(yc+1)+').')
                    if len(dr)==xd+yd-xs-ys:
                        print('You\'ve reached your destination.')
                    if n[i][0]=='1':
                        xc+=1
                    if n[i][0]=='2':
                        yc+=1
                    break
            for i in range(len(lhc)):
                for j in range(len(lhc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(j)+','+str(i)+') and ('+str(j+1)+','+str(i)+') in '+str(tt)+'th minute: '))
                    lht[i][j].append(no)
            for i in range(len(lvc)):
                for j in range(len(lvc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(i)+','+str(j)+') and ('+str(i)+','+str(j+1)+') in '+str(tt)+'th minute: '))
                    lvt[i][j].append(no)
            h1.append(tt-1)
            v1.append(tt-1)
            tt++
        lh=[]
        lv=[]
        for i in range(len(lht[0][0])):
            lh.append([])
        for i in range(len(lvt[0][0])):
            lv.append([])
        for i in lh:
            for j in range(11):
                i.append([])
        for i in lv:
            for j in range(11):
                i.append([])
        for i in range(len(lh)):
            for j in range(11):
                for k in range(10):
                    lh[i][j].append(lht[j][k][i])
        for i in range(len(lv)):
            for j in range(11):
                for k in range(10):
                    lv[i][j].append(lvt[j][k][i])
    elif xd<xs and yd>=ys:
        lht=[]
        lvt=[]
        for i in range(11):
            lh1=[]
            for j in range(10):
                lh1.append([])
            lht.append(lh1)
        for i in range(11):
            lv1=[]
            for j in range(10):
                lv1.append([])
            lvt.append(lv1)
        for i in lh:
            for j in range(11):
                for k in range(10):
                    lht[j][k].append(i[j][k])
        for i in lv:
            for j in range(11):
                for k in range(10):
                    lvt[j][k].append(i[j][k])
        h1=[]
        v1=[]
        for i in range(len(lh)):
            h1.append(i)
        for i in range(len(lv)):
            v1.append(i)
        xc=xs
        yc=ys
        dr=[]
        tt=len(lh)+1
        while xc!=xd and yc!=yd:
            lhc=[]
            lvc=[]
            for i in lht:
                lhc.append(i)
            for i in lvt:
                lvc.append(i)
            hs=np.array(h1,dtype=float)
            vs=np.array(v1,dtype=float)
            r=xc-xd
            u=yd-yc
            for i in lhc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(hs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lht[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            for i in lvc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(vs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lvt[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            n=[]
            for i in range(int(m.pow(10,r+u-1)),int(m.pow(10,r+u))):
                j=i
                c1=0
                c2=0
                while j!=0:
                    d=j%10
                    if d==1:
                        c1+=1
                    if d==2:
                        c2+=1
                    j=int(j/10)
                if c1==r and c2==u:
                    n.append(i)
            for i in range(len(n)):
                n[i]=str(n[i])
            xct=xc
            yct=yc
            l=[]
            for i in n:
                s=0
                ct=len(lht[0][0])
                for j in i:
                    if j=='1':
                        s+=lhc[yc][xc][ct]
                        xc-=1
                    if j=='2':
                        s+=lvc[xc][yc][ct]
                        yc+=1
                    ct+=1
                xc=xct
                yc=yct
                l.append(s)
            mn=l[0]
            for i in l:
                if i<mn:
                    mn=i
            for i in range(len(l)):
                if l[i]==mn:
                    dr.append(n[i][0])
                    if len(dr)==1:
                        if n[i][0]=='1':
                            print('Drive straight to ('+str(xs-1)+','+str(ys)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs-1)+','+str(ys)+').')
                        if n[i][0]=='2':
                            print('Drive straight to ('+str(xs)+','+str(ys+1)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs)+','+str(ys+1)+').')
                    else:
                        if n[i][0]=='1':
                            if dr[len(dr)-2]=='1':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='2':
                                print('Turn left at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc-1)+','+str(yc)+').')
                        if n[i][0]=='2':
                            if dr[len(dr)-2]=='2':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='1':
                                print('Turn right at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc)+','+str(yc+1)+').')
                    if len(dr)==xs+yd-xd-ys:
                        print('You\'ve reached your destination.')
                    if n[i][0]=='1':
                        xc-=1
                    if n[i][0]=='2':
                        yc+=1
                    break
            for i in range(len(lhc)):
                for j in range(len(lhc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(j)+','+str(i)+') and ('+str(j+1)+','+str(i)+') in '+str(tt)+'th minute: '))
                    lht[i][j].append(no)
            for i in range(len(lvc)):
                for j in range(len(lvc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(i)+','+str(j)+') and ('+str(i)+','+str(j+1)+') in '+str(tt)+'th minute: '))
                    lvt[i][j].append(no)
            h1.append(tt-1)
            v1.append(tt-1)
            tt++
        lh=[]
        lv=[]
        for i in range(len(lht[0][0])):
            lh.append([])
        for i in range(len(lvt[0][0])):
            lv.append([])
        for i in lh:
            for j in range(11):
                i.append([])
        for i in lv:
            for j in range(11):
                i.append([])
        for i in range(len(lh)):
            for j in range(11):
                for k in range(10):
                    lh[i][j].append(lht[j][k][i])
        for i in range(len(lv)):
            for j in range(11):
                for k in range(10):
                    lv[i][j].append(lvt[j][k][i])
    elif xd>=xs and yd<ys:
        lht=[]
        lvt=[]
        for i in range(11):
            lh1=[]
            for j in range(10):
                lh1.append([])
            lht.append(lh1)
        for i in range(11):
            lv1=[]
            for j in range(10):
                lv1.append([])
            lvt.append(lv1)
        for i in lh:
            for j in range(11):
                for k in range(10):
                    lht[j][k].append(i[j][k])
        for i in lv:
            for j in range(11):
                for k in range(10):
                    lvt[j][k].append(i[j][k])
        h1=[]
        v1=[]
        for i in range(len(lh)):
            h1.append(i)
        for i in range(len(lv)):
            v1.append(i)
        xc=xs
        yc=ys
        dr=[]
        tt=len(lh)+1
        while xc!=xd and yc!=yd:
            lhc=[]
            lvc=[]
            for i in lht:
                lhc.append(i)
            for i in lvt:
                lvc.append(i)
            hs=np.array(h1,dtype=float)
            vs=np.array(v1,dtype=float)
            r=xd-xc
            u=yc-yd
            for i in lhc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(hs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lht[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            for i in lvc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(vs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lvt[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            n=[]
            for i in range(int(m.pow(10,r+u-1)),int(m.pow(10,r+u))):
                j=i
                c1=0
                c2=0
                while j!=0:
                    d=j%10
                    if d==1:
                        c1+=1
                    if d==2:
                        c2+=1
                    j=int(j/10)
                if c1==r and c2==u:
                    n.append(i)
            for i in range(len(n)):
                n[i]=str(n[i])
            xct=xc
            yct=yc
            l=[]
            for i in n:
                s=0
                ct=len(lht[0][0])
                for j in i:
                    if j=='1':
                        s+=lhc[yc][xc][ct]
                        xc+=1
                    if j=='2':
                        s+=lvc[xc][yc][ct]
                        yc-=1
                    ct+=1
                xc=xct
                yc=yct
                l.append(s)
            mn=l[0]
            for i in l:
                if i<mn:
                    mn=i
            for i in range(len(l)):
                if l[i]==mn:
                    dr.append(n[i][0])
                    if len(dr)==1:
                        if n[i][0]=='1':
                            print('Drive straight to ('+str(xs+1)+','+str(ys)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs+1)+','+str(ys)+').')
                        if n[i][0]=='2':
                            print('Drive straight to ('+str(xs)+','+str(ys-1)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs)+','+str(ys-1)+').')
                    else:
                        if n[i][0]=='1':
                            if dr[len(dr)-2]=='1':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='2':
                                print('Turn left at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc+1)+','+str(yc)+').')
                        if n[i][0]=='2':
                            if dr[len(dr)-2]=='2':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='1':
                                print('Turn right at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc)+','+str(yc-1)+').')
                    if len(dr)==xd+ys-xs-yd:
                        print('You\'ve reached your destination.')
                    if n[i][0]=='1':
                        xc+=1
                    if n[i][0]=='2':
                        yc-=1
                    break
            for i in range(len(lhc)):
                for j in range(len(lhc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(j)+','+str(i)+') and ('+str(j+1)+','+str(i)+') in '+str(tt)+'th minute: '))
                    lht[i][j].append(no)
            for i in range(len(lvc)):
                for j in range(len(lvc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(i)+','+str(j)+') and ('+str(i)+','+str(j+1)+') in '+str(tt)+'th minute: '))
                    lvt[i][j].append(no)
            h1.append(tt-1)
            v1.append(tt-1)
            tt++
        lh=[]
        lv=[]
        for i in range(len(lht[0][0])):
            lh.append([])
        for i in range(len(lvt[0][0])):
            lv.append([])
        for i in lh:
            for j in range(11):
                i.append([])
        for i in lv:
            for j in range(11):
                i.append([])
        for i in range(len(lh)):
            for j in range(11):
                for k in range(10):
                    lh[i][j].append(lht[j][k][i])
        for i in range(len(lv)):
            for j in range(11):
                for k in range(10):
                    lv[i][j].append(lvt[j][k][i])
    else:
        lht=[]
        lvt=[]
        for i in range(11):
            lh1=[]
            for j in range(10):
                lh1.append([])
            lht.append(lh1)
        for i in range(11):
            lv1=[]
            for j in range(10):
                lv1.append([])
            lvt.append(lv1)
        for i in lh:
            for j in range(11):
                for k in range(10):
                    lht[j][k].append(i[j][k])
        for i in lv:
            for j in range(11):
                for k in range(10):
                    lvt[j][k].append(i[j][k])
        h1=[]
        v1=[]
        for i in range(len(lh)):
            h1.append(i)
        for i in range(len(lv)):
            v1.append(i)
        xc=xs
        yc=ys
        dr=[]
        tt=len(lh)+1
        while xc!=xd and yc!=yd:
            lhc=[]
            lvc=[]
            for i in lht:
                lhc.append(i)
            for i in lvt:
                lvc.append(i)
            hs=np.array(h1,dtype=float)
            vs=np.array(v1,dtype=float)
            r=xc-xd
            u=yc-yd
            for i in lhc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(hs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lht[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            for i in lvc:
                for j in i:
                    ys=np.array(j,dtype=float)
                    model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
                    model.compile(optimizer='sgd',loss='mean_squared_error')
                    model.fit(vs,ys,epochs=4000)
                    p=[]
                    for k in range(r+u):
                        p.append(float(len(lvt[0][0])+k))
                    exp=model.predict(x=np.array(p)).tolist()
                    q=[]
                    for k in exp:
                        q.append(Round(k[0]))
                    j+=q
            n=[]
            for i in range(int(m.pow(10,r+u-1)),int(m.pow(10,r+u))):
                j=i
                c1=0
                c2=0
                while j!=0:
                    d=j%10
                    if d==1:
                        c1+=1
                    if d==2:
                        c2+=1
                    j=int(j/10)
                if c1==r and c2==u:
                    n.append(i)
            for i in range(len(n)):
                n[i]=str(n[i])
            xct=xc
            yct=yc
            l=[]
            for i in n:
                s=0
                ct=len(lht[0][0])
                for j in i:
                    if j=='1':
                        s+=lhc[yc][xc][ct]
                        xc-=1
                    if j=='2':
                        s+=lvc[xc][yc][ct]
                        yc-=1
                    ct+=1
                xc=xct
                yc=yct
                l.append(s)
            mn=l[0]
            for i in l:
                if i<mn:
                    mn=i
            for i in range(len(l)):
                if l[i]==mn:
                    dr.append(n[i][0])
                    if len(dr)==1:
                        if n[i][0]=='1':
                            print('Drive straight to ('+str(xs-1)+','+str(ys)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs-1)+','+str(ys)+').')
                        if n[i][0]=='2':
                            print('Drive straight to ('+str(xs)+','+str(ys-1)+').')
                            print('You\'re now in rd. b/w ('+str(xs)+','+str(ys)+') and ('+str(xs)+','+str(ys-1)+').')
                    else:
                        if n[i][0]=='1':
                            if dr[len(dr)-2]=='1':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='2':
                                print('Turn right at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc-1)+','+str(yc)+').')
                        if n[i][0]=='2':
                            if dr[len(dr)-2]=='2':
                                print('Go straight at the next crossing.')
                            if dr[len(dr)-2]=='1':
                                print('Turn left at the next crossing.')
                            print('You\'re now in rd. b/w ('+str(xc)+','+str(yc)+') and ('+str(xc)+','+str(yc-1)+').')
                    if len(dr)==xs+ys-xd-yd:
                        print('You\'ve reached your destination.')
                    if n[i][0]=='1':
                        xc-=1
                    if n[i][0]=='2':
                        yc-=1
                    break
            for i in range(len(lhc)):
                for j in range(len(lhc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(j)+','+str(i)+') and ('+str(j+1)+','+str(i)+') in '+str(tt)+'th minute: '))
                    lht[i][j].append(no)
            for i in range(len(lvc)):
                for j in range(len(lvc[i])):
                    no=int(input('No. of cars passed in rd. b/w ('+str(i)+','+str(j)+') and ('+str(i)+','+str(j+1)+') in '+str(tt)+'th minute: '))
                    lvt[i][j].append(no)
            h1.append(tt-1)
            v1.append(tt-1)
            tt++
        lh=[]
        lv=[]
        for i in range(len(lht[0][0])):
            lh.append([])
        for i in range(len(lvt[0][0])):
            lv.append([])
        for i in lh:
            for j in range(11):
                i.append([])
        for i in lv:
            for j in range(11):
                i.append([])
        for i in range(len(lh)):
            for j in range(11):
                for k in range(10):
                    lh[i][j].append(lht[j][k][i])
        for i in range(len(lv)):
            for j in range(11):
                for k in range(10):
                    lv[i][j].append(lvt[j][k][i])
while True:
    h=[]
    v=[]
    for i in range(11):
        r=[]
        for j in range(9):
            no=int(input('No. of cars passed in rd. b/w ('+str(j)+','+str(i)+') and ('+str(j+1)+','+str(i)+') in '+str(t)+'th minute: '))
            r.append(no)
        h.append(r)
    for i in range(11):
        c=[]
        for j in range(9):
            no=int(input('No. of cars passed in rd. b/w ('+str(i)+','+str(j)+') and ('+str(i)+','+str(j+1)+') in '+str(t)+'th minute: '))
            c.append(no)
        v.append(c)
    lh.append(h)
    lv.append(v)
    b=input('Do you want to start your journey? (Y/N) ')
    if b=='Y' or b=='y':
        xs=int(input('Enter abscissa of starting point: '))
        ys=int(input('Enter ordinate of starting point: '))
        xd=int(input('Enter abscissa of destination point: '))
        yd=int(input('Enter ordinate of destination point: '))
        Predict(lh,lv,xs,ys,xd,yd)
        t+=int(m.fabs(xd-xs))+int(m.fabs(yd-ys))+1
    else:
        t++
    b=input('Do you want to terminate the system? (Y/N) ')
    if b=='Y' or b=='y':
        break
