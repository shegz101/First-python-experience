#class object
class Employees(object):
    def __init__(self, name, rate, hours) :
        self.name = name
        self.rate = rate
        self.hours = hours

staff = Employees(“Wayne”, 20, 8)
supervisor = Employees(“Dwight”, 35, 8)
manager = Employees(“Melinda”, 100, 8)

print(staff.name, staff.rate, staff.hours)
print(supervisor.name, supervisor.rate, supervisor.hours)
print(manager.name, manager.rate, manager.hours)



 