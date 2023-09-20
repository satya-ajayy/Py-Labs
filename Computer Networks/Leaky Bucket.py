STORAGE = 0
NO_OF_QUERIES = 4
BUCKET_SIZE = 10
INPUT_PACKET_SIZE = 4
OUTPUT_PACKET_SIZE = 1


for query in range(NO_OF_QUERIES):
    size_left = BUCKET_SIZE - STORAGE
    if INPUT_PACKET_SIZE < size_left:
        STORAGE += INPUT_PACKET_SIZE
        print(f'Buffer size / Bucket size : {STORAGE:02} / {BUCKET_SIZE}')
    else:
        print(f'Packet loss : {INPUT_PACKET_SIZE-size_left}')
        STORAGE = BUCKET_SIZE
        print(f'Buffer size / Bucket size : {STORAGE} / {BUCKET_SIZE}')
    STORAGE -= OUTPUT_PACKET_SIZE
