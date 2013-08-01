#coding=gbk
'''
kmp 算法，在给定字符串中查找匹配串
'''

def makenext(pat,dicts):
    i=1
    j=0
    dicts[0]=0
    while(i<len(pat)):
        while(j>0 and pat[i]<>pat[j]): j=dicts[j-1]
        if pat[i]==pat[j]:
            j+=1
        dicts[i]=j
        i=i+1

def kmp(source,pat,dicts):
    i=0
    j=0
    len_s=len(source)
    len_p=len(pat)
    makenext(pat,dicts)
    while i<len_s:
        while j>0 and source[i]<>pat[j]:
            j=dicts[j-1]
        if source[i]==pat[j]:j=j+1
        if j==len_p:
            print 'at index %s-%s find "%s" in "%s"'%(i-len_p+2,i,pat,source)
            return 0
        i=i+1
pat='abcdeabd'
source='abc abcdeabcdeabdabc'
dicts=[]
for x in pat:dicts.append(None)
kmp(source,pat,dicts)
