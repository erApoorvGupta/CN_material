import random
import time

class NoisyChannelSimulation:
    def __init__(self, packet_loss_prob):
        self.packet_loss_prob = packet_loss_prob
        self.sender_data = list(range(1, 11))
        self.receiver_data = []
        self.window_size = 4
        self.base = 0
        self.next_seq_num = 0

    def simulate_stop_and_wait(self):
        time_unit = 1  # Time unit
        time_elapsed = 0
        
        for packet in self.sender_data:
            while True:
                print(f"\n --> Sending packet: {packet}")
                time.sleep(0.5)
                time_elapsed += time_unit
                
                if random.random() > self.packet_loss_prob:
                    print(f"✅ Packet {packet} sent successfully")
                    received_ack = False
                    ack_wait_time = 0
                    while not received_ack:
                        print("Waiting for ACK...")
                        time.sleep(time_unit)  # Time for waiting ACK
                        time_elapsed += time_unit
                        if random.random() > self.packet_loss_prob:
                            print(f"✅ ACK received for packet: {packet}")
                            received_ack = True
                        else:
                            print("❌ ACK lost, resending packet")
                            ack_wait_time += time_unit
                            time_elapsed += time_unit
                    print(f"Time elapsed: {ack_wait_time + 2 * time_unit} units")  # Sending + waiting time
                    break
                else:
                    print(f"❌ Packet {packet} lost")
                    
        print(f"\n\n🕔 Total time taken: {time_elapsed} seconds")

    def simulate_go_back_n(self):
            time_unit = 1  # Time unit
            time_elapsed = 0
            number_of_packets = 7;
            window_size = 3;
            current_send = 0;
            current_ack = 0;
            while current_send <= number_of_packets:
                for i in range(window_size):
                    if (current_send <= number_of_packets):
                        print(f" --> Sending packet: {current_send}")
                        time.sleep(0.2)
                        time_elapsed += time_unit
                        current_send += 1
                    else:
                        break;
                print("\n")
                
                for i in range(window_size):
                    
                    if (current_ack <= number_of_packets):
                        if (random.random() > self.packet_loss_prob):
                            print(f"✅ ACK received for packet: {current_ack}")
                            time.sleep(0.2)
                            time_elapsed += time_unit
                            current_ack += 1
                        else:
                            print(f"❌ ACK lost for packet: {current_ack}")
                            if(current_send > current_ack):
                                current_send = current_ack 
                            current_ack += 1
                    else:
                        break;
                current_ack = current_send
                print("\n")
            print(f"\n🕔 Total time taken: {time_elapsed} seconds") 


    def simulate_selective_repeat(self):
        time_unit = 1
        time_elapsed = 0
        number_of_packets = 10

        n = 3  # number of packets <= 2^(n - 1)
        window_size = 2**(n - 1)
        sent_buffer = [False] * (number_of_packets + 1)  # Initialize a buffer to track sent packets
        received_buffer = [False] * (number_of_packets + 1)  # Initialize a buffer to track 
        order_received = []

        current_sent = 0;
        current_ack = 0;


        while not all(received_buffer):
            for i in range(window_size):
                if current_sent <= number_of_packets:
                    print(f" --> Sending packet: {current_sent}")
                    time.sleep(0.2)
                    time_elapsed += time_unit
                    # set sent_buffer[current_sent] to True
                    sent_buffer[current_sent] = True
                    current_sent += 1
                else:
                    break;
            
            print("\n")
            for i in range(window_size):
                if current_ack <= number_of_packets:
                    if random.random() > self.packet_loss_prob:
                        print(f"✅ ACK received for packet: {current_ack}")
                        time.sleep(0.2)
                        time_elapsed += time_unit
                        received_buffer[current_ack] = True
                        order_received.append(current_ack)
                        received_buffer[current_ack] = True
                        order_received.append(current_ack)
                    else:
                        print(f"❌ ACK lost for packet: {current_ack}")
                        time.sleep(0.2)
                        time_elapsed += time_unit
                    current_ack += 1
                else:
                    break;
            
            sent_buffer = received_buffer

            # check array sent_buffer till current_sent and resend lost packets
            for i in range(current_sent):
                if not sent_buffer[i]:
                    print(f" --> Resending packet: {i}")
                    time.sleep(0.2)
                    time_elapsed += time_unit
                    print(f"✅ ACK received for packet: {i}")
                    order_received.append(i)
                    sent_buffer[i] = True
                    received_buffer[i] = True

        print("\n🕔 Total time taken: ", time_elapsed)



    def menu(self):
        while True:
            print("\nSelect a protocol:")
            print("1. Stop-and-Wait ARQ")
            print("2. Go-Back-N ARQ")
            print("3. Selective Repeat ARQ")
            print("4. Quit")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                self.simulate_stop_and_wait()
            elif choice == 2:
                self.simulate_go_back_n()
            elif choice == 3:
                self.simulate_selective_repeat()
            elif choice == 4:
                break
            else:
                print("Invalid choice, please try again")

if __name__ == "__main__":
    packet_loss_prob = 0.2
    simulator = NoisyChannelSimulation(packet_loss_prob)
    simulator.menu()
