import time

def simple_protocol(sender_data, receiver_data):
    for i, frame in enumerate(sender_data):
        print(f"--> Sending frame {i}")
        receiver_data.append(frame)
        time.sleep(0.5)

def stop_and_wait_protocol(sender_data, receiver_data):
    for i, frame in enumerate(sender_data):
        print(f"\n --> Sending frame {i}")
        print(f"✅ Frame {i} received")
        receiver_data.append(frame)
        time.sleep(0.5)
        print("<-- Acknowledgment sent")

def main():
    sender_data = ["Frame1", "Frame2", "Frame3", "Frame4", "Frame5"]
    receiver_data = []

    while True:
        print("\nSelect a protocol:")
        print("1. Simple Protocol")
        print("2. Stop and Wait Protocol")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            simple_protocol(sender_data, receiver_data)
        elif choice == 2:
            stop_and_wait_protocol(sender_data, receiver_data)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
