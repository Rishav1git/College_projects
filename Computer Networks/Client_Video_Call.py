import socket
import cv2
import pickle
import struct
import threading
import pyshine as ps
import ssl

CERT_FILE = 'server.crt'
SERVER_HOSTNAME = 'video_call' 

def handle_video_capture(socket_connection):
    try:
        vid = cv2.VideoCapture(0)  
        while True:
            ret, frame = vid.read()
            if not ret:
                print("Error capturing frame from webcam")
                break

            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            socket_connection.sendall(message)
    except ConnectionError as e:
        print(f"Connection error during video capture: {e}")
    finally:
        vid.release()  

def handle_received_video_data(socket_connection):
    try:
        data = b""
        payload_size = struct.calcsize("Q")

        while True:
            while len(data) < payload_size:
                packet = socket_connection.recv(1024)
                if not packet:
                    break  
                data += packet

            if not data:
                break  

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                packet = socket_connection.recv(1024)
                if not packet:
                    break  
                data += packet

            if not data:
                break 

            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data)
            cv2.imshow("RECEIVING VIDEO", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    except ConnectionError as e:
        print(f"Connection error while receiving data: {e}")

def handle_audio_capture(socket_connection):
    mode = 'send'
    name = 'TRANSMITTING AUDIO'
    audio, context = ps.audioCapture(mode=mode)
    while True:
        try:
            frame = audio.get()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            socket_connection.sendall(message)
        except Exception as e:
            print("Error sending audio:", e)
            break

def handle_received_audio_data(socket_connection):
    mode = 'get'
    name = ' RECEIVING AUDIO'
    audio, context = ps.audioCapture(mode=mode)
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        try:
            while len(data) < payload_size:
                packet = socket_connection.recv(1024)
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += socket_connection.recv(4*1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            audio.put(frame)
        except Exception as e:
            print("Error receiving audio:", e)
            break

def start_client():
    # audio_socket = None  
    try:
        video_host = '192.168.235.30'  
        video_port = 12345
        video_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CERT_FILE)
        ssl_context.verify_mode = ssl.CERT_REQUIRED
        ssl_context.check_hostname = True
        ssl_context.verify_callback = True
        video_socket = ssl_context.wrap_socket(video_socket, server_hostname=SERVER_HOSTNAME)

        video_socket.connect((video_host, video_port))

        audio_host = '192.168.235.30'  
        audio_port = 12346
        audio_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        audio_socket = ssl_context.wrap_socket(audio_socket, server_hostname=SERVER_HOSTNAME)

        audio_socket.connect((audio_host, audio_port))

        video_thread = threading.Thread(target=handle_video_capture, args=(video_socket,))
        receive_video_thread = threading.Thread(target=handle_received_video_data, args=(video_socket,))
        audio_thread = threading.Thread(target=handle_audio_capture, args=(audio_socket,))
        receive_audio_thread = threading.Thread(target=handle_received_audio_data, args=(audio_socket,))
        video_thread.start()
        receive_video_thread.start()
        audio_thread.start()
        receive_audio_thread.start()

        # Handle keyboard input for quitting
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        video_thread.join()
        receive_video_thread.join()
        audio_thread.join()
        receive_audio_thread.join()

    except ConnectionError as e:
        print(f"Connection error during client setup: {e}")
    finally:
        if audio_socket:
            audio_socket.close()  # Ensure audio socket is closed
        video_socket.close()  # Ensure video socket is closed
        cv2.destroyAllWindows()

if __name__ == "__main__":
    start_client()
