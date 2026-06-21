from config import (
    VEHICLES_FILE,
    MOTORCYCLES_FILE
)

from core.storage import (
    load_data,
    save_data
)


# ==================================================
# Vehicle CRUD
# ==================================================

def get_all_vehicles():

    return load_data(
        VEHICLES_FILE
    )


def get_vehicle(
    vehicle_id
):

    vehicles = get_all_vehicles()

    for vehicle in vehicles:

        if vehicle["id"] == vehicle_id:

            return vehicle

    return None


def generate_vehicle_id():

    vehicles = get_all_vehicles()

    if len(vehicles) == 0:

        return 1

    return max(

        vehicle["id"]

        for vehicle in vehicles

    ) + 1


def create_empty_vehicle():

    return {

        "id":0,

        "model":"",

        "plate_number":"",

        "current_odometer":0,

        "fuel_type":"",

        "daily_distance":20,

        "pkb":0,

        "swdkllj":0,

        "due_date":"",

        "last_engine_oil":0,

        "last_cvt_oil":0,

        "last_cvt_cleaning":0,

        "last_chain":0,

        "last_chain_lube":0

    }


def save_vehicle(
    vehicle
):

    vehicles = get_all_vehicles()

    vehicle["id"] = generate_vehicle_id()

    vehicles.append(
        vehicle
    )

    save_data(

        VEHICLES_FILE,

        vehicles

    )

    return vehicle["id"]


def update_vehicle(
    vehicle
):

    vehicles = get_all_vehicles()

    for index in range(
        len(vehicles)
    ):

        if vehicles[index]["id"] == vehicle["id"]:

            vehicles[index] = vehicle

            break

    save_data(

        VEHICLES_FILE,

        vehicles

    )


def delete_vehicle(
    vehicle_id
):

    vehicles = get_all_vehicles()

    result = []

    for vehicle in vehicles:

        if vehicle["id"] != vehicle_id:

            result.append(
                vehicle
            )

    save_data(

        VEHICLES_FILE,

        result

    )


# ==================================================
# Motorcycle Master
# ==================================================

def get_all_motorcycles():

    return load_data(
        MOTORCYCLES_FILE
    )


def get_motorcycle_names():

    motorcycles = get_all_motorcycles()

    names = []

    for motorcycle in motorcycles:

        names.append(
            motorcycle["model"]
        )

    return names


def get_motorcycle(
    model
):

    motorcycles = get_all_motorcycles()

    for motorcycle in motorcycles:

        if motorcycle["model"] == model:

            return motorcycle

    return None


# ==================================================
# Default Data
# ==================================================

def get_default_fuel(
    model
):

    motorcycle = get_motorcycle(
        model
    )

    if motorcycle is None:

        return ""

    return motorcycle[
        "fuel_type"
    ]


def get_service_interval(
    model
):

    motorcycle = get_motorcycle(
        model
    )

    if motorcycle is None:

        return {

            "engine_oil": 0,

            "cvt_oil": 0,

            "cvt_clean": 0,

            "chain": 0,

            "chain_lube": 0

        }

    return {

        "engine_oil":
            motorcycle["engine_oil_interval"],

        "cvt_oil":
            motorcycle["cvt_oil_interval"],

        "cvt_clean":
            motorcycle["cvt_clean_interval"],

        "chain":
            motorcycle["chain_interval"],

        "chain_lube":
            motorcycle["chain_lube_interval"]

    }