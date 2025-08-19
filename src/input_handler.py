import json
from jsonschema import validate, ValidationError
import logging
import os

# Ensure logs folder exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

machine_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string", "enum": ["Ubuntu", "CentOS"]},
        "cpu": {"type": "string"},
        "ram": {"type": "string"}
    },
    "required": ["name", "os", "cpu", "ram"]
}

def get_user_input():
    machines = []
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        os_input = input("Enter OS (Ubuntu/CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        instance_data = {"name": name, "os": os_input, "cpu": cpu, "ram": ram}
        try:
            validate(instance=instance_data, schema=machine_schema)
            machines.append(instance_data)
            logging.info(f"Added machine: {name} ({os_input}, {cpu}, {ram})")
        except ValidationError as e:
            logging.error(f"Invalid input for {name}: {e.message}")
    return machines

def save_config(machines):
    try:
        os.makedirs('configs', exist_ok=True)  # Ensure configs folder exists
        with open('configs/instances.json', 'w') as f:
            json.dump(machines, f, indent=4)
        logging.info(f"Saved {len(machines)} machines to configs/instances.json")
    except Exception as e:
        logging.error(f"Failed to save configuration: {e}")
