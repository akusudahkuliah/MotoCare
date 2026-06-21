import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from gui.components import (
    create_label,
    create_entry,
    create_button
)

from core.fuel import (
    create_empty_fuel,
    save_fuel,
    calculate_history
)


# ==========================================
# Fuel Tab
# ==========================================

def create_fuel_tab(
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

    create_input_section(

        frame,

        vehicle

    )

    ttk.Separator(

        frame,

        orient="horizontal"

    ).pack(

        fill="x",

        pady=15

    )

    create_history_section(

        frame,

        vehicle

    )


# ==========================================
# Input
# ==========================================

def create_input_section(
    parent,
    vehicle
):

    form = tk.Frame(parent)

    form.pack(

        anchor="w"

    )

    date_var = tk.StringVar()

    odo_var = tk.StringVar()

    liter_var = tk.StringVar()

    price_var = tk.StringVar()

    total_var = tk.StringVar()

    create_label(

        form,

        "Date"

    ).grid(

        row=0,

        column=0,

        sticky="w"

    )

    create_entry(

        form,

        date_var

    ).grid(

        row=1,

        column=0,

        padx=5,

        pady=5

    )

    create_label(

        form,

        "Odometer"

    ).grid(

        row=0,

        column=1,

        sticky="w"

    )

    create_entry(

        form,

        odo_var

    ).grid(

        row=1,

        column=1,

        padx=5,

        pady=5

    )

    create_label(

        form,

        "Liter"

    ).grid(

        row=0,

        column=2,

        sticky="w"

    )

    create_entry(

        form,

        liter_var

    ).grid(

        row=1,

        column=2,

        padx=5,

        pady=5

    )

    create_label(

        form,

        "Price / Liter"

    ).grid(

        row=0,

        column=3,

        sticky="w"

    )

    create_entry(

        form,

        price_var

    ).grid(

        row=1,

        column=3,

        padx=5,

        pady=5

    )

    create_label(

        form,

        "Total"

    ).grid(

        row=0,

        column=4,

        sticky="w"

    )

    create_entry(

        form,

        total_var

    ).grid(

        row=1,

        column=4,

        padx=5,

        pady=5

    )

    def add_fuel():

        fuel = create_empty_fuel()

        fuel["vehicle_id"] = vehicle["id"]

        fuel["date"] = date_var.get()

        fuel["odometer"] = int(
            odo_var.get()
        )

        fuel["liter"] = float(
            liter_var.get()
        )

        fuel["price_per_liter"] = int(
            price_var.get()
        )

        fuel["total"] = int(
            total_var.get()
        )

        save_fuel(
            fuel
        )

        messagebox.showinfo(

            "MotoCare",

            "Fuel data saved."

        )

    create_button(

        form,

        "Add Fuel",

        add_fuel

    ).grid(

        row=2,

        column=4,

        pady=15

    )


# ==========================================
# History
# ==========================================

def create_history_section(
    parent,
    vehicle
):

    history = calculate_history(
        vehicle["id"]
    )

    title = create_label(
        parent,
        "Fuel History"
    )

    title.pack(
        anchor="w",
        pady=(0,10)
    )

    columns = (

        "Date",
        "Odometer",
        "Liter",
        "Total",
        "Km/L",
        "Rp/Km"

    )

    tree = ttk.Treeview(

        parent,

        columns=columns,

        show="headings",

        height=8

    )

    for column in columns:

        tree.heading(

            column,

            text=column

        )

        tree.column(

            column,

            width=110,

            anchor="center"

        )

    total_kmpl = 0

    total_cost = 0

    count = 0

    for item in history:

        kmpl = item["km_per_liter"]

        cost = item["cost_per_km"]

        if kmpl is None:

            kmpl_text = "-"

        else:

            kmpl_text = f"{kmpl:.2f}"

            total_kmpl += kmpl

            count += 1

        if cost is None:

            cost_text = "-"

        else:

            cost_text = f"{cost:.2f}"

            total_cost += cost

        tree.insert(

            "",

            "end",

            values=(

                item["date"],

                item["odometer"],

                item["liter"],

                f'Rp {item["total"]:,}',

                kmpl_text,

                cost_text

            )

        )

    tree.pack(

        fill="x",

        pady=10

    )

    average = tk.Frame(parent)

    average.pack(

        anchor="w",

        pady=10

    )

    if count > 0:

        avg_kmpl = round(

            total_kmpl /

            count,

            2

        )

        avg_cost = round(

            total_cost /

            count,

            2

        )

    else:

        avg_kmpl = 0

        avg_cost = 0

    create_label(

        average,

        f"Average Fuel Consumption : {avg_kmpl} km/L"

    ).pack(

        anchor="w"

    )

    create_label(

        average,

        f"Average Cost : Rp {avg_cost:,.2f} / km"

    ).pack(

        anchor="w"

    )