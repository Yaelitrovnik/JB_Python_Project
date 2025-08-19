from src.machine import Machine
from input_handler import save_config 
from input_handler import get_user_input

def main():
      machines = get_user_input()
      for machine_data in machines:
          machine = Machine(**machine_data)
          if machine.create():
              save_config(machines)
