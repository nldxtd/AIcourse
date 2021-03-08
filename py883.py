'''883喝水问题：
设有三个没有刻度的杯子，分别可以装8两、8两和3两水。
两个8两的杯子装满了水，请问如何在不借助于其他器具的
情况下，让4个人每人喝到4两水。
用回溯方法求解883喝水问题              
说明:                                     
状态用列表表示[c8, c8, c3, p1, p2, p3, p4]  
capacity=[8, 8, 3, 4, 4, 4, 4]表示每个杯子的容量和人喝的水量 
规则[f, t]表示第f个杯子向第t个杯子或者人到水           
ruleset表示所有的规则      
结果为用规则表示的路径                        
本程序尽可能与课上描述的算法一致，没有讲究效率问题。'''

ruleset = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
           [1, 0], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
           [2, 0], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6]]

capacity = [8, 8, 3, 4, 4, 4, 4]

goal = [0, 0, 0, 4, 4, 4, 4]

def term(data):
    if data == goal:
        return True
    return False

def deadend(data):
    if data == False:
        return True
    return False

def apprules(data):
    return ruleset

def gen(r, data):
    f = r[0]
    t = r[1]
    f0 = data[f]
    t0 = data[t]
    c = capacity[t]
    data = list(data)
    if t < 3 and f0 + t0 > c and t0 != c:
        data[t] = c
        data[f] = f0 + t0 - c
        return data
    elif t < 3 and f0 + t0 <= c and f0 != 0:
        data[t] = f0 + t0
        data[f] = 0
        return data
    elif t > 2 and f0 > 0 and f0 + t0 <= c:
        data[f] = 0
        data[t] = f0 + t0
        return data
    return False

def member(data, datalist):
    for d in datalist:
        if d == data:
            return True
        elif d[0] == data[1] and d[1] == data[0] and d[2:] == data[2:]:
            return True
    return False

def DFS883(datalist, bound):
    data = datalist[0]
    if term(data):
        return []
    if len(datalist) > bound:
        return False
    rules = apprules(data)
    for r in rules:
        rdata = gen(r, data)
        if deadend(rdata):
            continue
        if member(rdata, datalist):
            continue
        rdatalist = [rdata, *datalist]
        path = DFS883(rdatalist, bound)
        if path == False:
            continue
        return [r, *path]
    return False

def printpath(data, path):
    if path == False:
        print('没有解！')
        return
    for r in path:
        print(data, '  ', r, '==>')
        data = gen(r, data)
    print(data)

#调用方式    
data = [8, 8, 0, 0, 0, 0, 0]
path = DFS883([data], 30)
printpath(data, path)






