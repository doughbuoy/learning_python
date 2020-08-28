""" Model for aircraft flights"""

class Flight:

    def __init__(self,number, Aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No Airline Code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Airline Code is not caps '{number}'")
        self._number = number
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Flight Number is not numeric '{number}'")
        self._number = number
        self._Aircraft = Aircraft

    def aircraft_model(self):
        return self._Aircraft.model()


    def number(self):
        return self._number


    def airline(self):
        return(self._number[:2])

class Aircraft:
    def __init__(self,reg, model, num_rows, num_seats_per_row):
        self._reg = reg
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def reg(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows +1),
                "ABCDEFGHJK"[:self._num_seats_per_row])



