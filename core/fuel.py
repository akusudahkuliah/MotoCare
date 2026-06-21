from config import (
    FUELS_FILE
)

from core.storage import (
    load_data,
    save_data
)


# ==========================================
# Fuel CRUD
# ==========================================

def get_all_fuels():

    return load_data(
        FUELS_FILE
    )


def generate_fuel_id():

    fuels = get_all_fuels()

    if len(fuels) == 0:

        return 1

    return max(

        fuel["id"]

        for fuel in fuels

    ) + 1


def get_vehicle_fuels(
    vehicle_id
):

    fuels = get_all_fuels()

    result = []

    for fuel in fuels:

        if fuel["vehicle_id"] == vehicle_id:

            result.append(
                fuel
            )

    result.sort(

        key=lambda x:
        x["odometer"]

    )

    return result


def create_empty_fuel():

    return {

        "id":0,

        "vehicle_id":0,

        "date":"",

        "odometer":0,

        "liter":0,

        "price_per_liter":0,

        "total":0

    }


def save_fuel(
    fuel
):

    fuels = get_all_fuels()

    fuel["id"] = generate_fuel_id()

    fuels.append(
        fuel
    )

    save_data(

        FUELS_FILE,

        fuels

    )


def delete_fuel(
    fuel_id
):

    fuels = get_all_fuels()

    result = []

    for fuel in fuels:

        if fuel["id"] != fuel_id:

            result.append(
                fuel
            )

    save_data(

        FUELS_FILE,

        result

    )


# ==========================================
# Calculation
# ==========================================

def calculate_history(
    vehicle_id
):

    fuels = get_vehicle_fuels(
        vehicle_id
    )

    history = []

    previous = None

    for fuel in fuels:

        item = fuel.copy()

        item["km_per_liter"] = None

        item["cost_per_km"] = None

        if previous is not None:

            distance = (

                fuel["odometer"]

                -

                previous["odometer"]

            )

            if fuel["liter"] > 0:

                item["km_per_liter"] = round(

                    distance /

                    fuel["liter"],

                    2

                )

            if distance > 0:

                item["cost_per_km"] = round(

                    fuel["total"]

                    /

                    distance,

                    2

                )

        history.append(
            item
        )

        previous = fuel

    return history