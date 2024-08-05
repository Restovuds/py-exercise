# lecture code #

# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except ValueError as error:
#         print('Oops! Try again...', error, sep='\n')

########################################################################################################################

# f = open('test.txt', 'r')
# int_lines = []
# i = 0
# try:                                                                 # run this code
#     for line in f:
#         int_lines.append(int(line))
#         i += 1
# except ValueError as error:                                          # Execute this code when there is an exception
#     print(f'{i+1}-th line in file is not integer number: {error}')
# else:                                                                # No exceptions& Run this code
#     print(f'File has {len(int_lines)} integer numbers')
# finally:                                                             # Always run this code
#     f.close()

########################################################################################################################

# import sys
#
# try:
#     f = open('file.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print(f'OS error: {err}')
# except ValueError:
#     print("Could not convert data to an integer")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
# &&&&&&&&&&&&&&&&&&&
# try:
#     f = open('file.txt')
#     s = f.readline()
#     i = int(s.strip())
# except (OSError, ValueError, RuntimeError) as err:
#     print(f'Error: {err}')

########################################################################################################################

# raise statement
# def test(height):
#     if height < 5:
#         raise ValueError('Height must be greater than or equal to 5.')
#     return True
#
#
# try:
#     data = test(3)
# except ValueError as err:
#     print(err)

########################################################################################################################

# https://docs.python.org/3/library/exceptions.html - Built-in Exceptions

########################################################################################################################

# user-defined Exceptions
# class InputError(Exception):
#     """
#     Exception raised for errors in the input.
#     """
#
#     def __init__(self, expression, message):
#         """
#         :param expression: input expression in which the error occurred.
#         :param message: explanation of the error.
#         """
#         self.expression = expression
#         self.message = message
#
#
# x = int(input("Enter a number between 1 to 10: "))
# try:
#     if x not in range(1,11):
#         raise InputError(x, "Invalid input entered")
# except InputError as err:
#     print(err)

########################################################################################################################

# # logging
#
# import logging
#
# # create logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formater
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
#
# # an 'application' code
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")

##############################################################

# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s')
#
# console = logging.StreamHandler()
# console.setLevel(logging.WARNING)
# console.setFormatter(formatter)
#
# file_handler = logging.FileHandler('log.log')
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(console)
# logger.addHandler(file_handler)
#
# if __name__ == '__main__':
#     logger.info('Hello World!')
#     logger.warning("Hello world warning")
#     logger.critical("fffffff")
#     logger.info("finish logging")
