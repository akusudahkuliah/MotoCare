from datetime import datetime


# ==========================================
# Date
# ==========================================

def today():

    return datetime.today()


# ==========================================
# Remaining Distance
# ==========================================

def remaining_distance(
    current_km,
    last_km,
    interval
):

    return (

        last_km +

        interval -

        current_km

    )


# ==========================================
# Service Status
# ==========================================

def get_status(
    remaining
):

    if remaining <= 0:

        return "OVERDUE"

    if remaining <= 500:

        return "SOON"

    return "GOOD"


# ==========================================
# Engine Oil
# ==========================================

def engine_oil_status(
    vehicle,
    interval
):

    remaining = remaining_distance(

        vehicle["current_odometer"],

        vehicle["last_engine_oil"],

        interval

    )

    return {

        "remaining": remaining,

        "status": get_status(
            remaining
        )

    }


# ==========================================
# CVT Oil
# ==========================================

def cvt_oil_status(
    vehicle,
    interval
):

    remaining = remaining_distance(

        vehicle["current_odometer"],

        vehicle["last_cvt_oil"],

        interval

    )

    return {

        "remaining": remaining,

        "status": get_status(
            remaining
        )

    }


# ==========================================
# CVT Cleaning
# ==========================================

def cvt_clean_status(
    vehicle,
    interval
):

    remaining = remaining_distance(

        vehicle["current_odometer"],

        vehicle["last_cvt_cleaning"],

        interval

    )

    return {

        "remaining": remaining,

        "status": get_status(
            remaining
        )

    }


# ==========================================
# Chain
# ==========================================

def chain_status(
    vehicle,
    interval
):

    if interval == 0:

        return None

    remaining = remaining_distance(

        vehicle["current_odometer"],

        vehicle["last_chain"],

        interval

    )

    return {

        "remaining": remaining,

        "status": get_status(
            remaining
        )

    }


# ==========================================
# Chain Lube
# ==========================================

def chain_lube_status(
    vehicle,
    interval
):

    if interval == 0:

        return None

    remaining = remaining_distance(

        vehicle["current_odometer"],

        vehicle["last_chain_lube"],

        interval

    )

    return {

        "remaining": remaining,

        "status": get_status(
            remaining
        )

    }