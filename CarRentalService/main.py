from datetime import timedelta
from .CarRental import *



system_address = Address("500","Winchester","UK","TQPY7U")


## Defining Parkin space

slot1 = Slot(SlotSize.MEDIUM)
floor1 = Floor(1,[slot1])
parking_space = ParkingSpace(system_address)


## Defining Users

member_account = Member("Jake","jaky@proton.com","jaky@1","****")
admin_account = Admin("Peralta","perakta@proton.com","pery@3","$$$$")


## Defining Vehicles

audi = Car("DF34T","WVSC3499","Audi A6",slot1)
audi.generate_scan_code(CodeType.BAR)


## Defining Car rental system

car_rental = CarRentalSystem(system_address,parking_space,100)
car_rental.add_admins(admin_account)


## Search Vehicle
audi = member_account.search_vehicles("audi a6",SearchType.CAR_NAME)


## Requesting Reservation

reservation: Reservation = member_account.request_reservation(audi,datetime.date(),datetime.date.today() + timedelta(days=10))
reservation.add_equipments(Trolley)
reservation.add_services(WiFi)
fare = reservation.get_price()


## Make the payment

if car_rental.make_payment(CreditCardPayment(fare)):  # internally will take care of the payment process
    print("Reservation made")
    car_rental.reservations.append(reservation)
else:
    print("Reservation failed")


## Return vehicle

car_rental.return_vehicle(reservation)


