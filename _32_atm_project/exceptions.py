class InvalidPinError(Exception):
    def __str__(self):
        return "Entered Pin is incorrect!"

class InvalidRangeError(Exception):
    def __str__(self):
        return "Entered Amount is beyond the range!"

class InvalidAmountError(Exception):
    def __str__(self):
        return "Entered Amount is invalid!"