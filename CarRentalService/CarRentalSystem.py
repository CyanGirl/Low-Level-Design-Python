from abc import ABC, abstractmethod
import datetime
from enum import Enum






#### System Structure

class RentalSystem(ABC):
    def __init__(self,name,address,late_fine) -> None:
        self.name = name
        self.address= address # Address Object
        self.late_fine = late_fine


class CarRentalSystem(RentalSystem):
    def __init__(self, address, parking_space, late_fine) -> None:
        super().__init__(address, late_fine)
        self.parking_space = parking_space
        self.vehicles = [] # Vehicle[]
        self.admins = [] # Admin[]
        self.reservations = [] # Reservation[]
        self.equiments_available = []
        self.services_available = []

    def add_admins(self,person): pass
    def make_reservation(self,vehicle): pass
    def return_vehicle(self,reservation): pass # accept vehicle from member
    def scan_code(self,vehicle): pass # scan codes from vehicles
    def calculate_fine(self,reservation): pass
    def notify_member(self,msg,notificationObj,member): pass
    def make_payment(self,amount) -> bool: pass






#### Address

class Address:
    def __init__(self,street,city,country,zipcode) -> None:
        self.street = street
        self.city = city
        self.country = country
        self.zipcode = zipcode





#### Scan Code

class CodeType(Enum):
    BAR = "BAR"
    QR = "QR"

class Code(ABC):
    id = 0
    def __init__(self,encoded_details) -> None:
        self.id = id
        id+=1
        self.encoded_details = encoded_details

    @abstractmethod
    def get_code(self): pass
    @abstractmethod
    def update_code(self,updated_details): pass

class BarCode(Code):
    def get_code(self): pass

class QRCode(Code):
    pass





###### Reservation of Vehicle

class Reservation:
    id = 0
    def __init__(self,vehicle, start_time, end_time, member,equipments = [], services  =[]) -> None:
        self.id = id
        id+=1
        self.vehicle = vehicle
        self.start_time = start_time
        self.end_time = end_time
        self.member = member
        self.equipments = equipments
        self.services = services
        self.reservation_date = datetime.date()

    def get_details(self): pass
    def add_services(self,service): pass
    def add_equipments(self,equiment): pass
    def get_price(self) -> float: pass
    def cancel(self): pass  # cancel the reservation
    def close(self): pass # close the reservation of the vehicle




####### Extra Equipments and Services

class Equipment:
    id = 0
    def __init__(self,name,details) -> None:
        self.id = id
        id+=1
        self.name = name

class Trolley(Equipment):
    def __init__(self, name,price) -> None:
        super().__init__(name)
        self.price = price


class Service:
    id = 0
    def __init__(self,name,details,start_time,end_time) -> None:
        self.id = id
        id+=1
        self.name = name
        self.details = details
        self.start_time = start_time
        self.end_time = end_time


class WiFi(Service):
    def __init__(self, name, details, start_time, end_time,price) -> None:
        super().__init__(name, details, start_time, end_time)
        self.price = price






###### Payment for a Reservation

class Payment(ABC):
    id = 0
    def __init__(self,amount) -> None:
        self.id =id
        id+=1
        self.amount = amount

    @abstractmethod
    def make_payment(self): pass
    @abstractmethod
    def cancel_payment(self): pass



class CreditCardPayment(Payment):
    def __init__(self, id, amount, reservation,credit_card) -> None:
        super().__init__(id, amount, reservation)
        self.credit_card = credit_card

    def make_payment(self): pass
    def cancel_payment(self): pass


class UpiPayment(Payment):
    pass






##### Parking Spots

class ParkingSpace:
    def __init__(self,id,address,floors=[]) -> None:
        self.id = id
        self.address = address
        self.floors = floors

class Floor:
    def __init__(self,id,slots=[]) -> None:
        self.id = id
        self.slots = slots
    def add_slot(self,slot): pass
    def remove_slot(self,slot): pass
        

class Slot:
    id = 0
    def __init__(self,size,vehicle=None) -> None:
        self.id = id
        id +=1
        self.vehicle = vehicle
        self.size = size



###### Slot Sizes
class SlotSize(Enum):
    SMALL = "small"
    MEDIUM  = "medium"
    LARGE = "large"






##### Vehicles

class VehicleType(Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"
    SUVS = "SUVS"


class Vehicle(ABC):
    def __init__(self,id,name,mileage,number_plate,company) -> None:
        self.id = id
        self.number_plate = number_plate
        self.company = company
        self.name = name
        self.mileage = mileage


class RentVehicle(Vehicle):
    def __init__(self, id, number_plate, company, parking_spot) -> None:
        super().__init__(id, number_plate, company)
        self.parking_spot = parking_spot
        self.__reservation = None
        self.scan_code = None
    
    def reservation(self): pass
    def set_reservation(self,reservation): pass
    def generate_scan_code(self,code_type): pass # generate scan code based on type

    
class Car(RentVehicle):
    def __init__(self, id, number_plate, company, parking_spot) -> None:
        super().__init__(id, number_plate, company,parking_spot)
        self.vehicle_type = VehicleType.CAR
    





######  Notifications

class Notification(ABC):
    def __init__(self,id,content) -> None:
        self.id = id
        self.content = content

    @abstractmethod
    def send_notification(): pass


class EmailNotification(Notification):
    def __init__(self, id, content,email) -> None:
        super().__init__(id, content)
        self.email = email

    def send_notification(): pass






###### Search Index

class SearchType(Enum):
    CAR_NAME = "CAR NAME"
    CAR_TYPE = "CAR_TYPE"

class SearchIndex:
    def __init__(self) -> None:
        self.car_names = {}
        self.car_types = {}

    def update_car_names(self,obj): pass
    def update_car_types(self,obj): pass
    def search_by_car_name(self,car_name): pass
    def search_by_car_type(self,car_type): pass

    
class Search:
    def search(self,query,queryType):
        if queryType == SearchType.CAR_NAME:
            SearchIndex.search_by_car_name(query)

    




###### Users

class User(ABC):
    def __init__(self, name,contact) -> None:
        self.name = name
        self.contact = contact


class Account(User):
    def __init__(self, name, contact, username, password) -> None:
        super().__init__(name, contact)
        self.username = username
        self.password = password
        self.createdAt = datetime.date()


class Admin(Account):
    
    def add_car(self): pass
    def remove_car(self): pass
    def receive_car(self,vehicle): pass
    def reserve_car(self,vehicle): pass
    def add_new_equiment(self,equipment): pass
    def add_new_service(self,service): pass


class Member(Account):
    def __init__(self, name, contact, username, password) -> None:
        super().__init__(name, contact, username, password)
        self.active_reservation = None
        self.reservation_history = []

    def search_vehicles(self,query,queryType:SearchType): pass
    def request_reservation(self,vehicle, start_time, end_time): pass
    def request_return(self,reservation): pass
    def cancel_reservation(self): pass
    def add_insurance(self): pass


