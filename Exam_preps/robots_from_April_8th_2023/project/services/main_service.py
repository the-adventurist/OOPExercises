from project.services.base_service import BaseService


class MainService(BaseService):
    __CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, capacity=self.__CAPACITY)

    def details(self):
        info = f"{self.name} Main Service:" + "\n" + "Robots: "
        if self.robots:
            info += " ".join(r.name for r in self.robots)
        else:
            info += "none"

