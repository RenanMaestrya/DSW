class Elevator:
    def __init__(self, amountOfFloors: int, capacity: int):
        self.__amountOfFloors = amountOfFloors;
        self.__capacity = capacity;
        self.__currentFloor = 0;
        self.__presentPeople = 0;

    def __str__(self):
            return (
                f"Informações do Elevador:\n"
                f"Andar Atual: {self.__currentFloor}\n"
                f"Número de Pessoas: {self.__presentPeople}\n"
                f"Capacidade: {self.__capacity}\n"
                f"Total de Andares: {self.__amountOfFloors}"
            )

    def get_amountOfFloors(self):
        return self.__amountOfFloors

    def get_capacity(self):
        return self.__capacity

    def get_currentFloor(self):
        return self.__currentFloor

    def get_presentPeople(self):
        return self.__presentPeople

    def set_amountOfFloors(self, new_amount):
        if new_amount > 0:
            self.__amountOfFloors = new_amount
        else:
            print("Número inválido para andares.")

    def set_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__capacity = new_capacity
        else:
            print("Número inválido para capacidade de pessoas.")
    
    def set_currentFloor(self, new_floor):
        if 0 <= new_floor <= self.__amountOfFloors:
            self.__currentFloor = new_floor
        else:
            print("Andar inválido.")

    def set_presentPeople(self, new_people):
        if 0 <= new_people <= self.__capacity:
            self.__presentPeople = new_people
        else:
            print("Número de pessoas inválido.")

    def personEntered(self):
        if self.__presentPeople < self.__capacity:
            self.__presentPeople += 1;
        else:
            raise Exception("Elevador lotado! A capacidade de {self.__capacity} foi atingida.")


    def personLeft(self):
        if self.__presentPeople > 0:
            self.__presentPeople -= 1;
        else:
            raise Exception("Elevador vazio! Não tem mais ninguém aqui.")
    
    def upFloor(self):
        if self.__currentFloor < self.__amountOfFloors :
            self.__currentFloor += 1;
        else:
            raise Exception("Andar mais alto! Não há mais andares acima.")
    
    def downFloor(self):
        if self.__currentFloor > 0 :
            self.__currentFloor -= 1;
        else:
            raise Exception("Já estamos no térreo! Não há mais andares abaixo.")
    
         


