import subprocess
import logging

# Make sure logging is configured
logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_service():
    try:
        subprocess.run(['bash', 'scripts/install_nginx.sh'], check=True)
        logging.info("Service installation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred during service installation: {e}")
