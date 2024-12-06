from typing import List

"""
    vvvv      YOUR SOLUTION      vvvv
"""


class Person:

    def __init__(self, name: str, surname: str, age: int) -> None:
        """
        initialize person object with name, surname, age and count of owned vehicles
        """
        self.name = name
        self.surname = surname
        self.age = age
        self._vehicle_count = 0

    def __eq__(self, other: 'Person') -> bool:
        """
        change magic method to get exact object from memory
        """
        return self.name == other.name and self.surname == other.surname and self.age == other.age

    def get_vehicle_count(self) -> int:
        """
        method for getting vehicle count, resets its value and counts owned vehicle
        returns number
        """
        self._vehicle_count = 0
        for car in register.car_register:
            if self == car.owner:
                self._vehicle_count += 1
        return self._vehicle_count


class Vehicle:

    def __init__(self, registration_plate: str, creation_date: str, owner: Person) -> None:
        """
        initialize Vehicle object with registration_plate,
        creation_date and owner
        """
        self.registration_plate = registration_plate
        self.creation_date = creation_date
        self.owner = owner

    def __eq__(self, other: 'Vehicle') -> bool:
        """
        change magic method to get exact object from memory
        """
        return self.registration_plate == other.registration_plate


class Register:

    def __init__(self) -> None:
        """
        initialized a Register object as a list and owners list
        """
        self.car_register = []
        self.owners = []

    def insert_vehicle(self, vehicle: Vehicle) -> bool:
        """
        method for adding original vehicles
        ignores existing vehicles
        if adding, adding original owners too
        """
        if vehicle in self.car_register:
            return False

        self.car_register.append(vehicle)
        if vehicle.owner not in self.owners:
            self.owners.append(vehicle.owner)
        return True

    def update_vehicle_owner(self, registration_plate: str, new_owner: Person) -> bool:
        """
        update owner by plate, returns False if no update, True if updated
        deletes owners without vehicle
        """
        for car in self.car_register:
            if car.registration_plate == registration_plate and car.owner is not new_owner:
                car.owner = new_owner
                self.delete_owners()
                return True

        self.delete_owners()
        return False

    def delete_owners(self):
        """
        if owner has no cars, remove them
        """
        for owner in self.owners:
            if owner.get_vehicle_count() == 0:
                self.owners.remove(owner)

    def delete_vehicle(self, registration_plate: str) -> bool:
        """
        find vehicle by plate, remove it, delete superfluous owners
        """
        for registered_vehicle in self.car_register:
            if registered_vehicle.registration_plate == registration_plate:
                self.car_register.remove(registered_vehicle)
                self.delete_owners()
                return True
            
        self.delete_owners()
        return False

    def list_vehicles(self) -> List[Vehicle]:
        """
        returns vehicle register as list
        """
        return self.car_register

    def list_owners(self) -> List[Person]:
        """
        return list of owners
        """
        return self.owners

    def list_vehicle_by_owner(self, owner: Person) -> List[Vehicle]:
        """
        for given car owner, return list of cars
        """
        vehicles_by_owner = []
        for vehicle in self.car_register:
            if vehicle.owner == owner:
                vehicles_by_owner.append(vehicle)
        return vehicles_by_owner


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


register = Register()

person1 = Person("John", "Doe", 20)
person2 = Person("Alice", "Doe", 22)

car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)

# print(person2.get_vehicle_count())
# car1 = Vehicle("abc", "20221122", person1)

# test insertion
assert register.insert_vehicle(car1) == 1
assert register.insert_vehicle(car2) == 1
assert register.insert_vehicle(car3) == 0
assert register.insert_vehicle(car4) == 1
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
print("Vehicles listed")
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 2 and register.list_owners()[1].get_vehicle_count() == 1
print("Owners listed")
# test update

assert register.update_vehicle_owner("abc1", person1) == 0
print("1st update")
assert register.update_vehicle_owner("not in register", person1) == 0
print("2st update")
assert register.update_vehicle_owner("abc1", person2) == 1
print("3rd update")
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
print("vehicles listed")

assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 1 and register.list_owners()[1].get_vehicle_count() == 2
print("register 1st")
assert register.update_vehicle_owner("abc0", person2) == 1

assert register.list_vehicles() == [Vehicle("abc0", "20221122", person2), Vehicle("abc1", "20221123", person2), Vehicle("xyz", "20221124", person2)]
print("second listing")
assert register.list_owners() == [Person("Alice", "Doe", 22)] and register.list_owners()[0].get_vehicle_count() == 3

# test delete
assert register.delete_vehicle("not in register") == 0
assert register.delete_vehicle("abc0") == 1
assert register.delete_vehicle("abc1") == 1
assert register.delete_vehicle("xyz") == 1
assert register.list_vehicles() == []
assert register.list_owners() == []
#
# # test lists
car1 = Vehicle("abc0", "20221122", person1)
car2 = Vehicle("abc1", "20221123", person1)
car3 = Vehicle("abc0", "20221122", person1)
car4 = Vehicle("xyz", "20221124", person2)
#
register.insert_vehicle(car1)
register.insert_vehicle(car2)
register.insert_vehicle(car3)
register.insert_vehicle(car4)
#
assert register.list_vehicles() == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1), Vehicle("xyz", "20221124", person2)]
assert register.list_owners() == [Person("John", "Doe", 20), Person("Alice", "Doe", 22)]
assert register.list_vehicle_by_owner(person1) == [Vehicle("abc0", "20221122", person1), Vehicle("abc1", "20221123", person1)]
