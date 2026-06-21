import json
from pathlib import Path

from config import DATA_FOLDER


# ==========================================
# Lokasi Folder Data
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / DATA_FOLDER


# ==========================================
# Membaca File JSON
# ==========================================

def load_data(filename):

    file_path = DATA_DIR / filename

    if not file_path.exists():
        return []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:

        return []

    except Exception:

        return []


# ==========================================
# Menyimpan File JSON
# ==========================================

def save_data(filename, data):

    file_path = DATA_DIR / filename

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )