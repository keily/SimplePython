#coding=UTF-8
from CycleQueue import CycleQueue
from LinkStack import LinkStack
from LinkList import SingleLinkList
if __name__ == "__main__":
    #single linknode
    sinLList=SingleLinkList()
    sinLList.Insert(element=6)
    sinLList.Insert(element=13)
    sinLList.Insert(element=6)
    sinLList.Insert(element=0)
    print sinLList.Display()
    print '%s position %s in linklist'%(sinLList.Find(element=13),13)
    sinLList.Update(1, 15)
    print '%s position %s in linklist'%(1,sinLList.GetData(1))
    sinLList.Sort()
    print 'after sort:%s'%sinLList.Display()
    sinLList.Delete(6)
    print sinLList.Display()
    
    #cycle queue
    q=CycleQueue(4)
    q.Append('a')
    q.Append('b')
    q.Append('c')
    q.Append('d')
    try:
        q.Append('e')
    except Exception,e:
        print 'insert to queue error:',e
    print 'queue\s front element:%s'%q.Front()
    print 'queue\s length:%s',q.Length()
    while not q.IsEmpty():
        print 'In queue %s delete %s'%(q.Display(),q.Delete())
    print 'queue\s length:',q.Length()
    
    #link stack
    stack=LinkStack()
    print '%s a is pushed to stack'% stack.Push('a')
    print '%s b is pushed to stack'% stack.Push('b')
    print '%s c is pushed to stack'% stack.Push('c')
    print 'link stack:%s ,length:%s'% (stack.Display(),stack.Length())
    while(not stack.IsEmpty()):
        print '%s pop'%stack.Pop()