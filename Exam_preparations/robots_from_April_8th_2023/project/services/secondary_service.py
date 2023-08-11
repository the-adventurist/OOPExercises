from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"""{self.name} Secondary Service
Robots: {self._get_names()}"""

