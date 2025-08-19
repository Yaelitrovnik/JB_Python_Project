from src.machine import Machine
from input_handler import save_config, get_user_input
from src.service_installer import install_service
import logging

# Configure logging
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Starting infrastructure simulation")

    # Step 1: Get user input
    machines_data = get_user_input()
    logging.info(f"Received {len(machines_data)} machines from user input")

    # Step 2: Create machine objects
    machine_objects = []
    for machine_data in machines_data:
        machine = Machine(**machine_data)
        if machine.create():
            machine_objects.append(machine)
            logging.info(f"Created machine: {machine.name}")

    # Step 3: Save configuration
    save_config([m.to_dict() for m in machine_objects])
    logging.info("Saved machine configurations to configs/instances.json")

    # Step 4: Install services
    install_service()
    logging.info("Service installation completed")

if __name__ == "__main__":
    main()