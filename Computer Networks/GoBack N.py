n_frames = int(input('Enter the number of packets to send : '))

sent = 0
while True:
    for packet in range(n_frames):
        print(f'Frame {sent} has been transmitted')
        sent += 1
        if sent >= n_frames:
            break
    ack = int(input('Enter the last acknowledgement received : '))
    if ack >= n_frames:
        break
    else:
        sent = ack
    