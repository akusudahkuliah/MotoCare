import tkinter as tk

from gui.components import (
    create_label
)

from core.vehicle import (
    get_service_interval
)

from core.service import (
    engine_oil_status,
    cvt_oil_status,
    cvt_clean_status,
    chain_status,
    chain_lube_status
)


# ==========================================
# Service Tab
# ==========================================

def create_service_tab(
    parent,
    vehicle
):

    frame = tk.Frame(parent)

    frame.pack(

        fill="both",

        expand=True,

        padx=20,

        pady=20

    )

    if vehicle is None:

        create_label(

            frame,

            "Please save vehicle first."

        ).pack()

        return

    interval = get_service_interval(

        vehicle["model"]

    )

    engine = engine_oil_status(

        vehicle,

        interval["engine_oil"]

    )

    cvt = cvt_oil_status(

        vehicle,

        interval["cvt_oil"]

    )

    clean = cvt_clean_status(

        vehicle,

        interval["cvt_clean"]

    )

    chain = chain_status(

        vehicle,

        interval["chain"]

    )

    lube = chain_lube_status(

        vehicle,

        interval["chain_lube"]

    )

    create_item(

        frame,

        "Engine Oil",

        engine

    )

    create_item(

        frame,

        "CVT Oil",

        cvt

    )

    create_item(

        frame,

        "CVT Cleaning",

        clean

    )

    if chain is not None:

        create_item(

            frame,

            "Chain",

            chain

        )

    if lube is not None:

        create_item(

            frame,

            "Chain Lube",

            lube

        )


# ==========================================
# Item
# ==========================================

def create_item(
    parent,
    title,
    data
):

    frame = tk.Frame(

        parent,

        bd=1,

        relief="solid",

        padx=10,

        pady=10

    )

    frame.pack(

        fill="x",

        pady=5

    )

    create_label(

        frame,

        title

    ).grid(

        row=0,

        column=0,

        sticky="w"

    )

    create_label(

        frame,

        f'Remaining : {data["remaining"]} km'

    ).grid(

        row=1,

        column=0,

        sticky="w"

    )

    status = create_label(

        frame,

        f'Status : {data["status"]}'

    )

    status.grid(

        row=0,

        column=1,

        padx=30

    )

    if data["status"] == "GOOD":

        status.config(

            fg="green"

        )

    elif data["status"] == "SOON":

        status.config(

            fg="orange"

        )

    else:

        status.config(

            fg="red"
        )