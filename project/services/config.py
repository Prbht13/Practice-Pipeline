"""
Configuration settings for services
"""

class Config:
    DEBUG = True
    USER_SERVICE_NAME = "user-service"
    AUTH_SERVICE_NAME = "auth-service"
    
    @classmethod
    def get_service_config(cls, service_name):
        return {
            "name": service_name,
            "debug": cls.DEBUG,
            "version": "1.0.0"
        }