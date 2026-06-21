from config import (
    VEHICLES_FILE,
    MOTORCYCLES_FILE
)

from core.storage import (
    load_data,
    save_data
)


# ==========================================
# Vehicle
# ==========================================

def get_all_vehicles():

    return load_data(VEHICLES_FILE)


def get_vehicle(vehicle_id):

    vehicles = get_all_vehicles()

    for vehicle in vehicles:

        if vehicle["id"] == vehicle_id:

            return vehicle

    return None


# ==========================================
# Motorcycle Master
# ==========================================

def get_all_motorcycles():

    return load_data(MOTORCYCLES_FILE)


def get_motorcycle_names():

    motorcycles = get_all_motorcycles()

    names = []

    for motorcycle in motorcycles:

        names.append(
            motorcycle["model"]
        )

    return names


def get_motorcycle(model):

    motorcycles = get_all_motorcycles()

    for motorcycle in motorcycles:

        if motorcycle["model"] == model:

            return motorcycle

    return None


# ==========================================
# Default Fuel
# ==========================================

def get_default_fuel(model):

    motorcycle = get_motorcycle(model)

    if motorcycle is None:

        return ""

    return motorcycle["fuel"]


# ==========================================
# ID Generator
# ==========================================

def generate_vehicle_id():

    vehicles = get_all_vehicles()

    if len(vehicles) == 0:

        return 1

    max_id = 0

    for vehicle in vehicles:

        if vehicle["id"] > max_id:

            max_id = vehicle["id"]

    return max_id + 1


# ==========================================
# Template
# ==========================================

def create_empty_vehicle():

    return {

        "id": 0,

        "model": "",

        "plate_number": "",

        "current_odometer": 0,

        "pkb": 0,

        "swdkllj": 0,

        "due_date": "",

        "fuel_type": "",

        "daily_distance": 20,

        "last_engine_oil": 0,

        "last_cvt_oil": 0,

        "last_cvt_cleaning": 0,

        "last_chain": 0,

        "last_chain_lube": 0

    }


# ==========================================
# Save
# ==========================================

def save_vehicle(vehicle):

    vehicles = get_all_vehicles()

    if vehicle["id"] == 0:

        vehicle["id"] = generate_vehicle_id()

        vehicles.append(vehicle)

    else:

        for index in range(len(vehicles)):

            if vehicles[index]["id"] == vehicle["id"]:

                vehicles[index] = vehicle

                break

    save_data(
        VEHICLES_FILE,
        vehicles
    )

    return vehicle["id"]


# ==========================================
# Delete
# ==========================================

def delete_vehicle(vehicle_id):

    vehicles = get_all_vehicles()

    new_data = []

    for vehicle in vehicles:

        if vehicle["id"] != vehicle_id:

            new_data.append(vehicle)

    save_data(
        VEHICLES_FILE,
        new_data
    )


# ==========================================
# Update
# ==========================================

def update_vehicle(vehicle):

    vehicles = get_all_vehicles()

    for i in range(len(vehicles)):

        if vehicles[i]["id"] == vehicle["id"]:

            vehicles[i] = vehicle

            break

    save_data(
        VEHICLES_FILE,
        vehicles
    )