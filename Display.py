from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display_info(self):
        pass
