#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Wed Oct 21 13:00:18 CEST 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

def testString():
    print("")
    print("testString()")
    print("2*3 =",2*3)
    vatstr='qwklwe {} wer {}'
    print(vatstr)
    print(vatstr.format("wwwww","wwww"))
    vatstr2='qwklwe {aa} wer {bb}'
    print(vatstr2)
    print(vatstr2.format(bb="bbbb",aa="aaaa"))
    vatstr3='HELLO'
    print(vatstr3[0])
    print(vatstr3[1])
    print(vatstr3[-1])
    vatstr4="123456789"
    print(vatstr4[3:-1])
    print(vatstr4[0:3])
    print(vatstr4[:3])

def testList():
    print("")
    print("testList()")
    l=[1,2,3]
    print(l)
    ls=['a','b','c']
    print(ls)
    ls.append('w')
    print(ls)
    print(ls[0])
    print(ls[1:3])
    print(ls[-1])
    lnest=['1',1,'c',[1,2,3]]
    print(lnest)
    print(lnest[0])
    print(lnest[3])
    print(lnest[3][2])
    print(lnest[3][-1])
    print(lnest[3][:])
    lnest2=['1',1,'c',[1,2,3,['1',1,'c','qwerty']]]
    print(lnest2[3][0])
    print(lnest2[3][3][-1])
    print(lnest2[3][3][-1][2:4])
    ll1=[1,2,3]
    ll2=['a','b','c']
    ll3=['aa','bb','cv',ll1,ll2]
    print(ll3)
    ll4=['aa','bb','cv',ll1[-1],ll2[0:2]]
    print(ll4)
    print(ll2)
    ll2=['d','e','f']
    print(ll4)
    print(ll2)

def dictionaries():
    print("")
    print("dictionaries()")
    d = {'key1':'val','key2':123}
    print(d)
    d2 = {'key1':'val','key2':123,44:55}
    print(d2)
    print(d2['key1'])
    print(d2[44])
    d3 = {'key1':[1,2,3],'key2':{33:77,'key1':[4,5,6]},44:55}
    print(d3['key1'][0])
    print(d3['key2'][33])
    print(d3['key2']['key1'][0])
    print(d3['key2']['key1'][-1])
    print(type(d3))

def testBool():
    print(True)
    print(False)

def testTuples():
    tnest=('1',1,'c',[1,2,3])
    print(tnest)
    print(tnest[3])
    print(tnest[3][0])
    tnest[3][0] = 44
    print(tnest[3][0])
    print(tnest[1])
    #error
    #tnest[1] = 55
    #print(tnest[1])

def testSets():
    s={1,2,3,4,4,4,55,55,5}
    print(s)
    s.add(6)
    print(s)
    s.add(6)
    print(s)
    print(set([1,1,2,2,3,3,4,4,5,5]))

def testLogicOperations():
    print(1<2)
    print(1>2)
    print(True or False)
    print(False and False)
    print(True and True)
    print((1<2) and (2<3))

def testIfElse():
    if 1 < 2:
        print("1 < 2")
    else:
        print("1>=2")

    if 1 > 2:
        print("1 < 2")
    elif 3 == 3:
        print("3 == 3")
    else:
        print("1>=2")

def testLoops():
    seq=[1,4,44,66,2,2,2,1,[1,2,3,4,5],{1:1,2:3,'2':[1,2,3]}]
    print(len(seq))
    for oo in seq:
        print(oo)
    #
    rr=range(0,5)
    rrl=list(range(0,5))
    print(type(rr))
    print(type(rrl))
    for x in rr:
        print(x)
    for x in rrl:
        print(x)
    i = 1
    while i < 5 :
        print('i = {}'.format(i))
        i = i + 1

def testListComprehension():
    x = [1,2,3,4]
    out = []
    for num in x:
        out.append(num**2)
    #
    print(x)
    print(out)
    #ListComprehension
    out2=[num*2 for num in x]
    print(out)

def testListComprehensionBis():
    print('[for for]')
    [ print('i = {}, j = {}'.format(i,j)) for i in range(3) for j in range(3)]
    print('[[for]for]')
    [ [print('i = {}, j = {}'.format(i,j)) for i in range(3)] for j in range(3)]
    
def testRange():
    rr=range(0,5)
    rrl=list(range(0,5))
    print(type(rr))
    print(type(rrl))
    print(rr)
    print(rrl)

def times2(var):
    return var*2
    
def testMap():
    seq = [1,2,3,4]
    m = map(times2,seq)
    ml = list(m)
    ms = map(str,ml)
    msl = list(ms)
    print(type(m))
    print(m)
    print(type(ml))
    print(ml)
    print(ml[0])
    print(type(ml[0]))
    print(msl[0])
    print(type(msl[0]))
    print('\n'.join(map(str,ml)))

def testLambda():
    seq = [1,2,3,4]
    out = list(map(lambda v:v*2,seq))
    print(seq)
    print(out)

def testLambdaListComprehension():
    [(lambda i: [print('i = {}, j = {}'.format(i,j)) for j in range(i)])(i+1) for i in range(3)]
    
def testFilter():
    seq = [1,2,3,4]
    out = list(filter(lambda v:v%2==0,seq))
    print(seq)
    print(out)

def testBis():
    s = 'qwert yyy # UUuuu'
    print(type(s))
    print(s.upper())
    print(s.lower())
    print(s.split())
    print(s.split('#'))
    print(s.split(' # '))
    vv = ('x' in [1,2,3,4])
    print(vv)
    vv = ('x' in ['x','y',3,4])
    print(vv)
    vv = ('x' in ['xx','y',3,4])
    print(vv)
    
def testTupleUnpacking():
    x = [(1,2),(3,4),(5,6)]
    for item in x:
        print (item)
    for a,b in x:
        print (b)
    
def main():
    #testString()
    #testList()
    #dictionaries()
    #testBool()
    #testTuples()
    #testSets()
    #testLogicOperations()
    #testIfElse()
    #testLoops()
    #testListComprehension()
    #testListComprehensionBis()
    #testRange()
    #testMap()
    #testLambda()
    testLambdaListComprehension()
    #testFilter()
    #testBis()
    #testTupleUnpacking()
    
if __name__ == "__main__":
    main()
