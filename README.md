# Filepath-Validation-Microservice

A microservice that validates whether a given file path is accessible by server and thereby valid. It listens for incoming requests using a ZeroMQ REP socket on port 5555 by default. When a valid file path is provided, the service sends back the file path as confirmation. Otherwise, it returns the string `"False"`.

## Dependencies
Python3\
pyzmq

Requirements can be installed via ```pip install -r requirements.txt``` or manually.

## Requesting Data

Create a REQ Socket using ZeroMQ's REQ socket to send requests. Connect to the correct address (e.g., `tcp://localhost:5555`). Next, prepare the file path as a string and send it using the `send_string` method. Be sure to use the string prefix 'r' to treat backslashes as literal characters rather than escape characters, and 'b' to represent the string as a sequence of bytes.

### Example Request Code

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# absolute or relative path as a string with the prefix 'rb'
file_path = rb"C:/Users/yourname/yourproject/file.txt" 

socket.send_string(file_path)
```

## Receiving Data

ZeroMQ REQ/REP pattern requires the client to recieve a reply from the microservice after sending a request. This reply can be recieved using the `recv_string()` method. The reply from the filepath validation microservice will either be the filepath initially sent in the request, indicating a valid filepath, or the string `"False"`, indicating an invalid filepath.

### Example Receiving Code

```python
response = socket.recv_string()
print("Received response:", response)
```

## UML Diagram

![UML-Diagram](https://github.com/user-attachments/assets/03d5c550-ab30-4fd1-b6fb-ceacb92da2ad)
