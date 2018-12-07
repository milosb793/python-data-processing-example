from threading import Thread

inserted_index = 0
thread_pool = []
chunk_index = 0

def chunk(array, packet_size):
    if not isinstance(array, list):
        raise Exception('Only lists could be chunked!')
    for i in range(0, len(array), packet_size):
        yield array[i: i + packet_size]


def insert_chunk(chunk):
    from scripts.parsing_singlethread import insert_record
    global chunk_index
    global inserted_index

    for item in chunk:
        insert_record(inserted_index, item)
        inserted_index += 1

    print(f'Chunk: {chunk_index} has been processed!', '\n')
    chunk_index += 1


def insert_chunk_thread(chunk):
    global thread_pool

    t = Thread(target=insert_chunk, args=(chunk,))
    thread_pool.append(t)
    t.run()
