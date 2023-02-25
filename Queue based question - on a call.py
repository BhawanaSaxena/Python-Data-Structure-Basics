'''You are making a call center application, which should handle customers in a queue.
The CallCenter class is implemented as a Queue. Each element of the queue has the topic of the call as its value. The two possible values are 'general' and 'technical'. A 'general' call takes on average 5 minutes to handle, while a 'technical' call requires 10 minutes.
The given code adds multiple customers to the Queue from user input.
You need to dequeue all added customers, calculate and output the total time required to handle all calls.'''


#Lets understand this code

#We have defined a class Callcenter which has an empty list of self.calls

class Callcenter:
    def __init__(self):
        self.calls = []

#this method will return an empty list
    def is_empty(self):
        return self.calls == []

#this method will add calls at the end of the list -- enqueue
    def add_call(self,item):
        self.calls.insert(0,item)

#this method will remove calls one by one starting from the first call (first element of list self.calls)
    def next_call(self):
        return self.calls.pop()


#c is an object of Callcenter()
c =Callcenter()

#while condition is true , it will take input from user : either general/technical , else end the input
while True:
    n= input("Enter your call type: general/technical")
    if n=="end":
        break
#using add_call method to add each call inpu by user to the list at the end
    c.add_call(n)

#a variable as a time counter ,set to 0
time_call =0

#while loop to dequeue customers and calculate the time taken for each type of call
while True:
    if c.is_empty():
        break

    #dequeue_call is a variable assigned to our object "c" with its method of removing calls from first index of list
    dequeue_call = c.next_call()

    #if else condition to cal. time if general ,5 min  and if technical, 10min
    if dequeue_call=="general":
        time_call+=5
    elif dequeue_call=="technical":
        time_call+=10

#o/p is total time taken
print("Total time",time_call)


#Try this code and let me know if it works
