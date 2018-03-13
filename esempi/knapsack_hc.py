#!/usr/bin/env python3

import random

class knapsack:
    def __init__ (self,max_weight):
        self.weight = max_weight
        self.itemos=list()

    def add(self,item):
        if item.weight>self.weight:
            return False
        self.weight-=item.weight
        self.itemos.append(item)
        return True

    def get(self,index):
        return self.itemos[index]

    def notfull(self):
        return self.weight!=0

    def remove(self,item_index):
        self.itemos = self.itemos[:item_index]+self.itemos[item_index+1:]
        return True

    def dcopy(self):
        newsack = knapsack(self.weight)
        newsack.itemos=self.itemos[:]
        return newsack

    def __eq__(self,other):
        return self.weight==other.weight and all(i==j for i,j in zip(self.items,other.items))

    @property
    def value(self):
        total=0
        for i in self.items:
            total += i.value
        return total

    @property
    def random_item(self):
        return random.randint(0,len(self.itemos)-1)

    @property
    def items(self):
        return self.itemos

class item:
    def __init__ (self,weight,value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "("+str(self.weight)+","+str(self.value)+")"

    def dcopy(self):
        return item(self.weight,self.value)

    def __eq__(self,other):
        return self.weight==other.weight and self.value==other.value


def randomitem(max_weight=5,max_value=1000):
    return item(random.randint(1,max_weight),random.randint(1,max_value))


def fillsack(sack,inventory):
    working_inventory = inventory[:]
    while(sack.notfull() and working_inventory):
        itemtoadd = random.choice(working_inventory)
        working_inventory.remove(itemtoadd)
        if not sack.add(itemtoadd):
            continue
        inventory.remove(itemtoadd)


def remitem(item,listname):
    listname.remove(item)
    return True

    
def list_sub(one,two):
    return [i for i in one.items if i not in two.items and remitem(i,two)]


def main():
    #create a sack with random starting elements
    starting_sack = knapsack(random.randint(1,50))
    inventory = [randomitem() for i in range(random.randint(1,50))]
    fillsack(starting_sack,inventory)
    count =0
    stepnumber=10000
    out=False
    while count < stepnumber:
        #create a new sack by removing a random element from the initial sack
        central_sack = starting_sack.dcopy()
        random_item_index = central_sack.random_item
        toaddlater = central_sack.get(random_item_index)
        central_sack.remove(random_item_index)
        #create a list of new sacks each being randomly filled 
        possible_sacks = list()
        working_inventory = inventory[:]
        while working_inventory:
            step_sack = central_sack.dcopy()
            fillsack(step_sack,working_inventory)
            if step_sack == central_sack:
                out=True
                break
            if step_sack.value>central_sack.value:
                print("added")
                possible_sacks.append(step_sack)
        if out:
            out =False
            count+=1
            continue
        #calculate the value of all the sacks in the list and migrate to the maximum
        total_improvements = [i.value for i in possible_sacks]
        import operator
        max_index,max_value = max(enumerate(total_improvements),key=operator.itemgetter(1))
        inventory.append(toaddlater)
        starting_sack = possible_sack[max_index]
        count +=1


if __name__=="__main__":
    main()
