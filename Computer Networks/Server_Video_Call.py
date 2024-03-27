import socket
import ssl
import struct
import threading

CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

def handle_client_video(client_socket, client_address, target_socket):
    try:
        print(f"Connection established with {client_address}")
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = client_socket.recv(1024)  
                if not packet:
                    break
                data += packet
            if not data:
                break
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            target_socket.sendall(packed_msg_size + frame_data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def handle_client_audio(client_socket, client_address, target_socket):
    try:
        print(f"Connection established with {client_address}")
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            while len(data) < payload_size:
                packet = client_socket.recv(1024) 
                if not packet:
                    break
                data += packet
            if not data:
                break
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            target_socket.sendall(packed_msg_size + frame_data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server_video():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

    # Wrap the socket with SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

    # Bind the socket to a specific address and port
    host = '192.168.235.30'  # Listen on all available network interfaces
    port = 12345
    server_socket.bind((host, port))

    server_socket.listen(5)  # Listen for incoming connections

    print(f"Video server listening on {host}:{port}")

    try:
        while True:
            client_socket1, client_address1 = server_socket.accept()
            print(f"Video connection established with {client_address1}")

            client_socket2, client_address2 = server_socket.accept()
            print(f"Video connection established with {client_address2}")

            # Create threads to handle each client separately
            thread1 = threading.Thread(target=handle_client_video, args=(client_socket1, client_address1, client_socket2))
            thread2 = threading.Thread(target=handle_client_video, args=(client_socket2, client_address2, client_socket1))

            # Start the threads
            thread1.start()
            thread2.start()

    except KeyboardInterrupt:
        print("Video server shutting down.")
    finally:
        server_socket.close()

def start_server_audio():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
    server_socket = ssl_context.wrap_socket(server_socket, server_side=True)

    host = '192.168.235.30'  
    port = 12346
    server_socket.bind((host, port))

    server_socket.listen(5)  

    print(f"Audio server listening on {host}:{port}")

    try:
        while True:
            client_socket1, client_address1 = server_socket.accept()
            print(f"Audio connection established with {client_address1}")

            client_socket2, client_address2 = server_socket.accept()
            print(f"Audio connection established with {client_address2}")

            thread1 = threading.Thread(target=handle_client_audio, args=(client_socket1, client_address1, client_socket2))
            thread2 = threading.Thread(target=handle_client_audio, args=(client_socket2, client_address2, client_socket1))

            thread1.start()
            thread2.start()

    except KeyboardInterrupt:
        print("Audio server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    video_thread = threading.Thread(target=start_server_video)
    audio_thread = threading.Thread(target=start_server_audio)

    video_thread.start()
    audio_thread.start()
    
    video_thread.join()
    audio_thread.join()
