"""
Centralized logging for services
"""
from datetime import datetime

class Logger:
    @staticmethod
    def log(service_name, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level} - {service_name}: {message}")