def singleton(arg):
    d = {}
    def inner():
        if (arg not in d):
            d[arg] = arg()
        return d[arg]
    return inner

@singleton
class jailer():
    def __init__(self):
        self.tt = 100
    def booking(self,n):
        if (self.tt>=n):
            print('Tickets booked successfully.')
            self.tt-=n
            print(f'Available tickets {self.tt}.')
        else:
            print(f'{n} no.of tickets not available.')
@singleton
class baby():
    def __init__(self):
        self.tt = 100
    def booking(self,n):
        if (self.tt>n):
            print("Tickets booked successfully.")
            self.tt-=n
            print(f'Available tickets {n}.')
        else:
            print(f'{n} no.of tickets not available.')
def bms():
    print("1.jailer/n2.baby")
    choice = int(input("Select the movie: "))
    if choice==1:
        n = int(input("Enter the no.of tickets: "))
        ob = jailer()
        ob.booking(n)
    elif choice==2:
        n = int(input("Enter the no.of tickets: "))
        ob = baby()
        ob.booking(n)


bms()