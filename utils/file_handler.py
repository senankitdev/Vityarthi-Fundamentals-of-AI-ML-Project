import json
import os


# Load data from JSON file
def load_data(filepath):
    # If file does not exist, return empty dictionary
    if not os.path.exists(filepath):
        return {}

    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data
    except:
        return {}


# Save data to JSON file
def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)