import random as rd
NO_OF_PACKETS = 15
WINDOW_SIZE = 5

print(f'Transmitting begins..! No of Packets : {NO_OF_PACKETS}')
i = 1
while i <= NO_OF_PACKETS:
    print(f'Sending Packets from {i} to {WINDOW_SIZE + i - 1}')
    for packet in range(i, WINDOW_SIZE+i):
        print(f'Transmitting packet {packet}')
    
    nac = i + rd.randrange(0, WINDOW_SIZE)
    print(f'NACK : {nac + 1}')
    print(f'Sending Packet : {nac}')
    print(f'Ack : {nac + 1}')
    print(f'Ack : {i+WINDOW_SIZE}')
    i += WINDOW_SIZE
