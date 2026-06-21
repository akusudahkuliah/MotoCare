import tkinter as tk
from tkinter import ttk

from gui.components import (
    clear_frame,
    create_title,
    create_label,
    create_entry,
    create_combobox,
    create_button,
    create_notebook
)

from core.vehicle import (
    get_motorcycle_names,
    get_default_fuel
)


# ==========================================
# Vehicle Editor
# ==========================================

def create_vehicle_page(
    root,
    on_back,
    on_save,
    vehicle=None
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

    create_header(
        root,
        on_back
    )

    notebook = create_notebook(
        root
    )

    notebook.grid(
        row=1,
        column=0,
        sticky="nsew",
        padx=20,
        pady=(0,20)
    )

    vehicle_tab = ttk.Frame(notebook)
    service_tab = ttk.Frame(notebook)
    fuel_tab = ttk.Frame(notebook)
    summary_tab = ttk.Frame(notebook)
    calendar_tab = ttk.Frame(notebook)
    about_tab = ttk.Frame(notebook)

    notebook.add(
        vehicle_tab,
        text="Vehicle"
    )

    notebook.add(
        service_tab,
        text="Service"
    )

    notebook.add(
        fuel_tab,
        text="Fuel"
    )

    notebook.add(
        summary_tab,
        text="Summary"
    )

    notebook.add(
        calendar_tab,
        text="Calendar"
    )

    notebook.add(
        about_tab,
        text="About"
    )

    create_vehicle_tab(
        vehicle_tab,
        on_save,
        vehicle
    )

    create_placeholder_tab(
        service_tab,
        "Service Module\nComing Soon"
    )

    create_placeholder_tab(
        fuel_tab,
        "Fuel Module\nComing Soon"
    )

    create_placeholder_tab(
        summary_tab,
        "Summary Module\nComing Soon"
    )

    create_placeholder_tab(
        calendar_tab,
        "Calendar Module\nComing Soon"
    )

    create_placeholder_tab(
        about_tab,
        "About MotoCare\nComing Soon"
    )


# ==========================================
# Header
# ==========================================

def create_header(
    parent,
    on_back
):

    frame = tk.Frame(parent)

    frame.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=20,
        pady=20
    )

    button = create_button(
        frame,
        "← Back",
        on_back
    )

    button.pack(
        side="left"
    )

    title = create_title(
        frame,
        "Vehicle Editor"
    )

    title.pack(
        side="left",
        padx=15
    )


# ==========================================
# Vehicle Tab
# ==========================================

def create_vehicle_tab(
    parent,
    on_save,
    vehicle=None
):

    frame = tk.Frame(parent)

    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ==========================
    # Variable
    # ==========================

    model_var = tk.StringVar()
    plate_var = tk.StringVar()
    odometer_var = tk.StringVar()

    fuel_var = tk.StringVar()
    daily_var = tk.StringVar()

    pkb_var = tk.StringVar()
    swdkllj_var = tk.StringVar()
    due_var = tk.StringVar()

    engine_oil_var = tk.StringVar()
    cvt_oil_var = tk.StringVar()
    cvt_clean_var = tk.StringVar()

    chain_var = tk.StringVar()
    chain_lube_var = tk.StringVar()

    if vehicle is not None:

        model_var.set(
            vehicle["model"]
        )

        plate_var.set(
            vehicle["plate_number"]
        )

        odometer_var.set(
            vehicle["current_odometer"]
        )

        fuel_var.set(
            vehicle["fuel_type"]
        )

        daily_var.set(
            vehicle["daily_distance"]
        )

        pkb_var.set(
            vehicle["pkb"]
        )

        swdkllj_var.set(
            vehicle["swdkllj"]
        )

        due_var.set(
            vehicle["due_date"]
        )

        engine_oil_var.set(
            vehicle["last_engine_oil"]
        )

        cvt_oil_var.set(
            vehicle["last_cvt_oil"]
        )

        cvt_clean_var.set(
            vehicle["last_cvt_cleaning"]
        )

        chain_var.set(
            vehicle["last_chain"]
        )

        chain_lube_var.set(
            vehicle["last_chain_lube"]
        )

    # ==========================
    # Left Frame
    # ==========================

    left = tk.Frame(frame)

    left.grid(
        row=0,
        column=0,
        sticky="nw",
        padx=(0,40)
    )

    create_label(
        left,
        "Motorcycle"
    ).grid(
        row=0,
        column=0,
        sticky="w"
    )

    motorcycle = create_combobox(
        left,
        get_motorcycle_names(),
        model_var
    )

    motorcycle.grid(
        row=1,
        column=0,
        pady=(0,10)
    )

    def update_motorcycle(event=None):

        fuel = get_default_fuel(
            model_var.get()
        )

        fuel_var.set(fuel)

    motorcycle.bind(
        "<<ComboboxSelected>>",
        update_motorcycle
    )

    create_label(
        left,
        "Plate Number"
    ).grid(
        row=2,
        column=0,
        sticky="w"
    )

    create_entry(
        left,
        plate_var
    ).grid(
        row=3,
        column=0,
        pady=(0,10)
    )

    create_label(
        left,
        "Current Odometer"
    ).grid(
        row=4,
        column=0,
        sticky="w"
    )

    create_entry(
        left,
        odometer_var
    ).grid(
        row=5,
        column=0,
        pady=(0,10)
    )

    create_label(
        left,
        "Fuel Type"
    ).grid(
        row=6,
        column=0,
        sticky="w"
    )

    fuel = create_combobox(
        left,
        [
            "Pertalite",
            "Pertamax",
            "Pertamax Turbo",
            "Shell Super",
            "Shell V-Power"
        ],
        fuel_var
    )

    fuel.grid(
        row=7,
        column=0,
        pady=(0,10)
    )

    create_label(
        left,
        "Daily Distance (km)"
    ).grid(
        row=8,
        column=0,
        sticky="w"
    )

    create_entry(
        left,
        daily_var
    ).grid(
        row=9,
        column=0,
        pady=(0,10)
    )


    # ==========================
    # Right Frame
    # ==========================

    right = tk.Frame(frame)

    right.grid(
        row=0,
        column=1,
        sticky="nw"
    )

    create_label(
        right,
        "PKB"
    ).grid(row=0,column=0,sticky="w")

    create_entry(
        right,
        pkb_var
    ).grid(
        row=1,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "SWDKLLJ"
    ).grid(row=2,column=0,sticky="w")

    create_entry(
        right,
        swdkllj_var
    ).grid(
        row=3,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Due Date"
    ).grid(row=4,column=0,sticky="w")

    create_entry(
        right,
        due_var
    ).grid(
        row=5,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Last Engine Oil (km)"
    ).grid(row=6,column=0,sticky="w")

    create_entry(
        right,
        engine_oil_var
    ).grid(
        row=7,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Last CVT Oil (km)"
    ).grid(row=8,column=0,sticky="w")

    create_entry(
        right,
        cvt_oil_var
    ).grid(
        row=9,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Last CVT Cleaning (km)"
    ).grid(row=10,column=0,sticky="w")

    create_entry(
        right,
        cvt_clean_var
    ).grid(
        row=11,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Last Chain (km)"
    ).grid(row=12,column=0,sticky="w")

    create_entry(
        right,
        chain_var
    ).grid(
        row=13,
        column=0,
        pady=(0,10)
    )

    create_label(
        right,
        "Last Chain Lube (km)"
    ).grid(row=14,column=0,sticky="w")

    create_entry(
        right,
        chain_lube_var
    ).grid(
        row=15,
        column=0,
        pady=(0,20)
    )

    # ==========================
    # Save
    # ==========================

    def save():

        vehicle_id = 0

        if vehicle is not None:

            vehicle_id = vehicle["id"]

        data = {

            "id": vehicle_id,

            "model": model_var.get(),

            "plate_number": plate_var.get(),

            "current_odometer": odometer_var.get(),

            "fuel_type": fuel_var.get(),

            "daily_distance": daily_var.get(),

            "pkb": pkb_var.get(),

            "swdkllj": swdkllj_var.get(),

            "due_date": due_var.get(),

            "last_engine_oil": engine_oil_var.get(),

            "last_cvt_oil": cvt_oil_var.get(),

            "last_cvt_cleaning": cvt_clean_var.get(),

            "last_chain": chain_var.get(),

            "last_chain_lube": chain_lube_var.get()

        }

        on_save(data)

    button = create_button(
        frame,
        "Save",
        save
    )

    button.grid(
        row=1,
        column=1,
        sticky="e",
        pady=20
    )


# ==========================================
# Placeholder Tab
# ==========================================

def create_placeholder_tab(
    parent,
    text
):

    label = create_label(
        parent,
        text
    )

    label.pack(
        expand=True
    )