import random, json, os
from datetime import datetime
# import boto3

# session = boto3.Session(aws_access_key_id='YOUR_ACCESS_KEY',
#                         aws_secret_access_key='YOUR_SECRET_KEY')
# s3_client = session.client('s3')

class Parking_lot:

    def __init__(self, square_footage, spot_sizes="8x12"):
        
        self.square_footage = square_footage
        spot_sizes = spot_sizes.split('x')
        width, height = int(spot_sizes[0]), int(spot_sizes[1])
        self.parking_spot_size = int(square_footage) // (width * height)
        self.parking_lot = [None] *  self.parking_spot_size
        self.mapped_vehicles = {}

    def map_parked_vehicles(self):
        now = datetime.now()
        date_time = now.strftime("%d_%m_%Y_%H_%M")
        file_name = f"mapped_vehicles_{date_time}.json"

        with open(file_name, "w") as f:
            f.write(json.dumps(self.mapped_vehicles, indent=2))

        # bucket_name = f"Parking_lot_{self.square_footage}_{self.parking_spot_size}"
        # path = os.getcwd() + rf'{file_name}'
        # s3_client.upload_file(path, bucket_name, file_name)
        return json.dumps(self.mapped_vehicles, indent=2)


class Car:

    def __init__(self, licence_plate):
        self.licence_plate = licence_plate

    def park(self, parking):
        lots = parking.parking_lot
        while None in lots:
            self.spot = random.choice(range(len(lots)))
            print(lots,self.spot)
            print(random.choice(range(len(lots))))
            if lots[self.spot] == None:
                lots[self.spot] = '#'
                print(f"Car with license plate {self.licence_plate} parked successfully in spot {self.spot}")
                break
            else:
                print(f"Car with license plate {self.licence_plate} was not parked successfully.")
    
    def __str__(self):
        return f"License Plate number --> {self.licence_plate}"

def main():
    parking = Parking_lot("2000")
    car_licenses = [random.choice(range(1000000,9999999)) for c in range(parking.parking_spot_size)]
    print(car_licenses)
    for license in car_licenses:
        parking_car = Car(license)
        parking_car.park(parking)
        parking.mapped_vehicles[parking_car.licence_plate] = parking_car.spot
    print(parking.map_parked_vehicles())


if __name__ == '__main__':
    main()