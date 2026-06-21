import tkinter as tk
from tkinter import ttk

from config import (
    TITLE_FONT,
    HEADING_FONT,
    LABEL_FONT,
    BUTTON_FONT,
    ENTRY_WIDTH,
    COMBOBOX_WIDTH,
    BUTTON_WIDTH,
    PAD_X,
    PAD_Y,
    CARD_COLOR
)


# ==========================================
# Label
# ==========================================

def create_title(parent, text):

    return tk.Label(
        parent,
        text=text,
        font=TITLE_FONT
    )


def create_heading(parent, text):

    return tk.Label(
        parent,
        text=text,
        font=HEADING_FONT
    )


def create_label(parent, text):

    return tk.Label(
        parent,
        text=text,
        font=LABEL_FONT,
        anchor="w"
    )


# ==========================================
# Entry
# ==========================================

def create_entry(parent, textvariable=None):

    return tk.Entry(
        parent,
        width=ENTRY_WIDTH,
        font=LABEL_FONT,
        textvariable=textvariable
    )


# ==========================================
# Combobox
# ==========================================

def create_combobox(parent, values, textvariable=None):

    combobox = ttk.Combobox(
        parent,
        values=values,
        width=COMBOBOX_WIDTH,
        state="readonly",
        textvariable=textvariable
    )

    return combobox


# ==========================================
# Button
# ==========================================

def create_button(parent, text, command):

    return tk.Button(
        parent,
        text=text,
        width=BUTTON_WIDTH,
        font=BUTTON_FONT,
        command=command
    )


# ==========================================
# Card
# ==========================================

def create_card(parent):

    return tk.Frame(
        parent,
        bg=CARD_COLOR,
        relief="solid",
        bd=1,
        padx=PAD_X,
        pady=PAD_Y
    )


# ==========================================
# Notebook
# ==========================================

def create_notebook(parent):

    return ttk.Notebook(parent)


# ==========================================
# Separator
# ==========================================

def create_separator(parent):

    return ttk.Separator(
        parent,
        orient="horizontal"
    )


# ==========================================
# Clear Frame
# ==========================================

def clear_frame(parent):

    for widget in parent.winfo_children():

        widget.destroy()