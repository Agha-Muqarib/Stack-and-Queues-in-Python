#!/usr/bin/env python
# coding: utf-8

# In[7]:


class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.List=[0 for i in range(size)]
        self.top=0
    def Push(self,value):
        if self.top!=self.size:
            self.List[self.top]=value
            self.top=self.top+1
            print(self.List)
        else:
            print("Stack Overflow")
    def Pop(self):
        if self.IsEmpty():
            print("Stack Underflow")
        self.top=self.top-1
        x=self.List[self.top]
        return x
        
    def IsEmpty(self):
        if self.top==0:
            print("Stack Underflow")
    def Peek(self):
        return (self.List[self.top - 1])
    def Count(self):
        print ("The number of elements in stack is",self.size,"!!!")
    def strExp(self,String):
        s=ArrayStack(len(String))
        for i in String:
            if i == "(" or i== "{" or i == "[":
                s.Push(i)
            
            elif i == ")" or i== "}" or i== "]":
                s.Pop()
            
        if s.IsEmpty() == True:
            print("True")
    def Print(self):
        print(self.List)

        
# Driver Code 

size=4
ob=ArrayStack(size)

print("Pushing elements into stack: ")

ob.Push(7)
ob.Push(2)
ob.Push(8)
ob.Push(9)
print("\n")
ob.Push(2)
ob.Print()

print("\nPopping element from stack: ")

ob.Pop()
ob.Print()

print("\nPeek in stack: ")


ob.Peek()
ob.Print()

print("\nCounting elements in stack: ")
ob.Count()

print("\nString expression in stack: ")
String = "{}()["
ob.strExp(String)


# In[11]:


class ArrayQueue:
    def __init__(self,size):
        self.size=size
        self.List=[0 for i in range(size)]
        self.front=0
        self.rear=0
        self.count=0
    def Enqueue(self,value):
        self.List[self.rear]=value
        self.rear=(self.rear+1)%self.size
        self.count+=1
        print(self.List)
    def Dequeue(self):
        self.front=(self.front+1)%self.size
        return (self.List[self.front])

    def IsEmpty(self):
        if self.top==0:
            print("Stack Underflow")



size=3
ob=ArrayQueue(size)

print("\nEnqueing: \n")
ob.Enqueue(5)
ob.Enqueue(2)

print("\nDequeuing:")
ob.Dequeue()


# In[ ]:




