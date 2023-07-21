class Node:
    def __init__(self,weight,quantity,price,pname,key):
        self.weight=weight
        self.quantity=quantity
        self.price=price
        self.pname=pname
        self.key=key
        self.next=None
        self.child=None
        #print(weight,quantity,price,pname,key)
    def set_next(self,next):
        self.next=next

class LinkedList():
    def __init__(self):
        self.head=None
        self.count=0

    def insert(self,weight,quantity,price,pname,key):
        new_node=Node(weight,quantity,price,pname,key)
        Node.temp=Node(0,0,0,'',0)
        #print(weight,quantity,price,pname,key)
        if self.head is None:
            new_node.set_next(self.head)
            self.head=new_node
            self.count += 1
        else:
            Node.temp=self.head
            while temp.next != None:
                if temp.key/1000==new_node.key/1000:
                    while temp.child !=None:
                        temp=temp.child
                    temp.child=new_node
                    return
                else:
                    temp=temp.next
            if temp.key/1000==new_node.key/1000:
                while temp.child !=None:
                    temp=temp.child
                temp.child=new_node
                return
            else:
                temp=new_node
                return

    def search(self,key):
        item=self.head
        while item!=None:
            if item.get_data()== key :
                return item
            else:
                item=item.get_next()
        return None
        
    def delete(key):
        Node.temp= LinkedList.Node_traversal(key)
        temp=temp.child
    def Node_traversal(self,key):
        if self.head is None:
            ("The list is empty")
            return None
        else:
            Node.temp =self.head
            while temp.next !=None:
                if temp.key/1000==key/1000:
                    if temp.key==key:
                        if temp.next is None:
                            return temp
                else:
                    temp=temp.next
            if temp.key/1000==key/1000:
                while temp.child !=None:
                    temp=temp.child
                return temp
            else:
                ("No such key exists")
                return None

    def update(weight,quantity,price,pname,key):
        Node.temp=Node(None,None,None,None,key)
        Node.temp=LinkedList.Node_traversal(key)
        if weight!=None:
            Node.temp.weight=weight
        elif quantity!=None:
            Node.temp.quantity=quantity
        elif price!=None:
            Node.temp.price=price
        elif pname!=None:
            Node.temp.pname=pname

    def display(self):
        if self.head is None:
            ("The list is empty")
            return None
        else:
            pk =self.head
            sk=Node
            
            while pk.next !=None:
                sk=pk.child
                print (pk.weight, pk.quantity,pk.price,pk.pname, end="-->")
                result=""+pk.weight+pk.quantity+pk.price+pk.pname+"\n"
                while sk.child !=None:
                    print (sk.weight, sk.quantity,sk.price,sk.pname, end=" ")
                    sk=sk.child
                print(" ")
                pk=pk.next

    def initialize(self):
        with open('randomnum.txt') as f:
            for line in f.readlines():
                x=line.split()
                #print("iweadifasdi",x[4:len(x)])
                x1=x[4:len(x)]
                pname = ' '.join([str(elem) for elem in x1])
                
                self.insert(x[1],x[3],x[2],pname,x[0])
        self.display()
