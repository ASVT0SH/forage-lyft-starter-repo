from abc import ABC
class Battery(ABC):
    """Battery class, which is imported by
    Spindler and Nubbin"""
    def needs_service(self)->bool:
        pass