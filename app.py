from tkinter import messagebox

from gui.dashboard import create_dashboard
from gui.vehicle import create_vehicle_page

from core.vehicle import (
    create_empty_vehicle,
    save_vehicle,
    get_vehicle,
    update_vehicle,
    delete_vehicle
)


class MotoCareApp:

    def __init__(self, root):

        self.root = root

        self.show_dashboard()

    # ==========================================
    # Dashboard
    # ==========================================

    def show_dashboard(self):

        create_dashboard(

            root=self.root,

            on_add_vehicle=self.add_vehicle,

            on_open_vehicle=self.open_vehicle,

            on_delete_vehicle=self.delete_vehicle

        )

    # ==========================================
    # Add Vehicle
    # ==========================================

    def add_vehicle(self):

        create_vehicle_page(

            root=self.root,

            on_back=self.show_dashboard,

            on_save=self.save_new_vehicle

        )

    # ==========================================
    # Open Vehicle
    # ==========================================

    def open_vehicle(
        self,
        vehicle_id
    ):

        vehicle = get_vehicle(
            vehicle_id
        )

        if vehicle is None:

            return

        create_vehicle_page(

            root=self.root,

            on_back=self.show_dashboard,

            on_save=self.update_existing_vehicle,

            vehicle=vehicle

        )

    # ==========================================
    # Save New Vehicle
    # ==========================================

    def save_new_vehicle(
        self,
        data
    ):

        vehicle = create_empty_vehicle()

        self.fill_vehicle_data(
            vehicle,
            data
        )

        save_vehicle(
            vehicle
        )

        messagebox.showinfo(

            "MotoCare",

            "Vehicle added successfully."

        )

        self.show_dashboard()

    # ==========================================
    # Update Vehicle
    # ==========================================

    def update_existing_vehicle(
        self,
        data
    ):

        vehicle = create_empty_vehicle()

        self.fill_vehicle_data(
            vehicle,
            data
        )

        vehicle["id"] = data["id"]

        update_vehicle(
            vehicle
        )

        messagebox.showinfo(

            "MotoCare",

            "Vehicle updated successfully."

        )

        self.show_dashboard()

    # ==========================================
    # Delete Vehicle
    # ==========================================

    def delete_vehicle(
        self,
        vehicle_id
    ):

        answer = messagebox.askyesno(

            "Delete Vehicle",

            "Delete this vehicle?"

        )

        if not answer:

            return

        delete_vehicle(
            vehicle_id
        )

        self.show_dashboard()

    # ==========================================
    # Fill Dictionary
    # ==========================================

    def fill_vehicle_data(
        self,
        vehicle,
        data
    ):

        vehicle["model"] = data["model"]

        vehicle["plate_number"] = data["plate_number"]

        vehicle["current_odometer"] = int(
            data["current_odometer"] or 0
        )

        vehicle["fuel_type"] = data["fuel_type"]

        vehicle["daily_distance"] = int(
            data["daily_distance"] or 0
        )

        vehicle["pkb"] = int(
            data["pkb"] or 0
        )

        vehicle["swdkllj"] = int(
            data["swdkllj"] or 0
        )

        vehicle["due_date"] = data["due_date"]

        vehicle["last_engine_oil"] = int(
            data["last_engine_oil"] or 0
        )

        vehicle["last_cvt_oil"] = int(
            data["last_cvt_oil"] or 0
        )

        vehicle["last_cvt_cleaning"] = int(
            data["last_cvt_cleaning"] or 0
        )

        vehicle["last_chain"] = int(
            data["last_chain"] or 0
        )

        vehicle["last_chain_lube"] = int(
            data["last_chain_lube"] or 0
        )

    # ==========================================
    # Run
    # ==========================================

    def run(self):

        self.root.mainloop()