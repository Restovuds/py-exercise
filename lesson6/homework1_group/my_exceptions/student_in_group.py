
class StudentInGroupException(Exception):
    """
    Exception raised for errors related to the number of students in the group.
    """
    def __init__(self, expression, message):
        """
        :param expression:
        :param message:
        """
        self.expression = expression
        self.message = message

    def __str__(self):
        return f'{self.message}: {self.expression}'