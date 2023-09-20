import random as rd

n_packets = int(input('Enter the number of packets to Send : '))
packet = 1
while packet <= n_packets:
    print(f'The Packet Sent is {packet}')
    flag = rd.choice([True, False])
    if flag:
        boolean = rd.choice([True, False])
        if boolean:
            print(f'[ACK] : {packet + 1}')
        else:
            print(f'[NACK] : {packet}')
            packet -= 1
    else:
        print('Time Out..! Resend Packet')
        packet -= 1
    packet += 1
