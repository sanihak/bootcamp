x = input("Enter number 1 : ")
y = input("Enter number 2 : ")
d = 0
try :
    d = int(x)/int(y)
    a = "baby doll" + 123
# except ZeroDivisionError as ze:
#     print("exception occured : " , ze)
# except TypeError as te:
#     print("exception occurred : " , te)
except Exception as e:
    print("Generic Exception : ",e)
print("Division is: " , d)

balance =0
def deposit(amount):
    global balance
    if amount <=0:
        raise ValueError("Amount should not be less than 0")
    balance += amount

deposit(-1)
print(balance)