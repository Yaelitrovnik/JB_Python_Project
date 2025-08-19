import subprocess
import logging

# Make sure logging is configured
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_service(vm_name):
    try:
        subprocess.run(['bash', 'scripts/install_nginx.sh', vm_name], check=True)
        logging.info("Service installation completed successfully on {vm_name} .")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred during service installation on {vm_name}: {e}")
