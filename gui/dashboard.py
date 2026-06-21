import tkinter as tk

from gui.components import (
    clear_frame,
    create_title,
    create_heading,
    create_button,
    create_card,
    create_label
)

from core.vehicle import (
    get_all_vehicles
)


# ==========================================
# Dashboard
# ==========================================

def create_dashboard(
    root,
    on_add_vehicle,
    on_open_vehicle,
    on_delete_vehicle
):

    clear_frame(root)

    root.columnconfigure(
        0,
        weight=1
    )

    root.rowconfigure(
        1,
        weight=1
    )

    # =========================
    # Header
    # =========================

    header = tk.Frame(root)

    header.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=20,
        pady=20
    )

    title = create_title(
        header,
        "MotoCare"
    )

    title.pack(
        anchor="w"
    )

    heading = create_heading(
        header,
        "My Motorcycles"
    )

    heading.pack(
        anchor="w"
    )

    # =========================
    # Body
    # =========================

    body = tk.Frame(root)

    body.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=20,
        pady=(0,20)
    )

    body.columnconfigure(
        0,
        weight=1
    )

    vehicles = get_all_vehicles()

    if len(vehicles) == 0:

        empty = tk.Frame(body)

        empty.pack(
            expand=True
        )

        label = create_label(
            empty,
            "No motorcycle found.\n\nClick 'Add Vehicle' to add your first motorcycle."
        )

        label.pack(
            pady=15
        )

    else:

        for vehicle in vehicles:

            create_vehicle_card(
                body,
                vehicle,
                on_open_vehicle,
                on_delete_vehicle
            )

    # =========================
    # Footer
    # =========================

    footer = tk.Frame(root)

    footer.grid(
        row=2,
        column=0,
        sticky="ew",
        padx=20,
        pady=(0,20)
    )

    button = create_button(
        footer,
        "Add Vehicle",
        on_add_vehicle
    )

    button.pack(
        anchor="e"
    )


# ==========================================
# Vehicle Card
# ==========================================

def create_vehicle_card(
    parent,
    vehicle,
    on_open_vehicle,
    on_delete_vehicle
):

    card = create_card(parent)

    card.pack(
        fill="x",
        pady=8
    )

    model = tk.Label(
        card,
        text=vehicle["model"],
        font=("Segoe UI",11,"bold"),
        bg="white"
    )

    model.grid(
        row=0,
        column=0,
        sticky="w"
    )

    plate = create_label(
        card,
        vehicle["plate_number"]
    )

    plate.grid(
        row=1,
        column=0,
        sticky="w"
    )

    odo = create_label(
        card,
        f'{vehicle["current_odometer"]:,} km'
    )

    odo.grid(
        row=2,
        column=0,
        sticky="w"
    )

    open_button = create_button(
        card,
        "Open",
        lambda:
        on_open_vehicle(
            vehicle["id"]
        )
    )

    open_button.grid(
        row=0,
        column=1,
        padx=10
    )

    delete_button = create_button(
        card,
        "Delete",
        lambda:
        on_delete_vehicle(
            vehicle["id"]
        )
    )

    delete_button.grid(
        row=1,
        column=1,
        padx=10
    )