
import zmq
import os


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def valid_directory(filepath: str) -> bool:
    """Checks if the directory of a provided filepath exists"""
    directory = os.path.dirname(filepath)
    if not directory:
        directory = "." # Current directory

    return os.path.exists(directory) and os.path.isdir(directory)


def valid_filepath(filepath: str)->bool:
    """Checks if a filepath exists"""
    if not valid_directory(filepath):
        print("Error: The directory does not exist.")
        return False
    try:
        with open(filepath, 'r'):
            print("Valid filepath")
            return True
    except IOError as e:
        print("Error:", e)
        return False

# --------------------------- Server Loop --------------------------- #

while True:
    #  Wait for next request from client
    message = socket.recv()
    filepath = message.decode('utf-8')
    print(f"Received request: {filepath}")

    if valid_filepath(filepath):
        socket.send_string(filepath)
    else:
        socket.send_string("False")
    print()

# --------------------------- Local Tests --------------------------- #

# # Relative path
# print(valid_filepath(r"file.txt"))
# print(valid_filepath(r"./file.txt"))
# print(valid_filepath(r"invalid_file.txt"))
# # Absolute path
# print(valid_filepath(r"C:\Users\cfrit\source\OSU\CS361\Assignment 8\file.txt"))
# print(valid_filepath(r"C:\Users\cfrit\source\OSU\CS361\Assignment 8\invalid_file.txt"))

