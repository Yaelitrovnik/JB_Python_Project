import json
from jsonschema import validate, ValidationError

def get_user_input():
      machines = []
      while True:
          name = input("Enter machine name (or 'done' to finish): ")
          if name.lower() == 'done':
              break
          os = input("Enter OS (Ubuntu/CentOS): ")
          cpu = input("Enter CPU (e.g., 2vCPU): ")
          ram = input("Enter RAM (e.g., 4GB): ")
          instance_data = {"name": name, "os": os, "cpu": cpu, "ram": ram}
          # Validate input
          try:
              validate(instance=instance_data, schema=machine_schema)
              machines.append(instance_data)
          except ValidationError as e:
              print(f"Invalid input: {e.message}")
      return machines

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

def save_config(machines):
    with open('configs/instances.json', 'w') as f:
        json.dump(machines, f, indent=4)