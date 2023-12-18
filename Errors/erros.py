class NotFilled(Exception):
    def __init__(self, value_error):
        self.value_error = value_error
    def __repr__(self) -> str:
        return self.value_error

class NoCheckboxesFilled(Exception):
    def __init__(self, value_error):
        self.value_error = value_error
    def __repr__(self) -> str:
        return self.value_error
    

class NoProductsSelected(Exception):
    def __init__(self, value_error):
        self.value_error = value_error
    def __repr__(self) -> str:
        return self.value_error
    
