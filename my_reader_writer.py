import asyncio


async def writer_coro(writer_id, write_semaphore, read_semaphore):
    print("Writer {} acquiring write semaphore".format(writer_id))
    await write_semaphore.acquire()

    print("Writer {} writing".format(writer_id))
    await asyncio.sleep(.2)

    print("Writer {} releasing write semaphore".format(writer_id))
    write_semaphore.release()
    return


async def reader_coro(reader_id, write_semaphore, read_semaphore):
    #print("Reader {} acquiring read semaphore".format(reader_id))
    await read_semaphore.acquire()

    if read_semaphore.locked():
        print("Reader {} acquiring write semaphore".format(reader_id))
        await write_semaphore.acquire()

    print("Reader {} releasing read semaphore".format(reader_id))
    read_semaphore.release()

    print("Reader {} reading".format(reader_id))
    await asyncio.sleep(.1)

    print("Reader {} releasing write semaphore".format(reader_id))
    write_semaphore.release()
    return


num_of_writers = 8
num_of_readers = 20

event_loop = asyncio.get_event_loop()
write_semaphore = asyncio.Semaphore()
read_semaphore = asyncio.Semaphore()

tasks = [writer_coro(writer_id, write_semaphore, read_semaphore)
         for writer_id in range(num_of_writers)] + \
        [reader_coro(reader_id, write_semaphore, read_semaphore)
         for reader_id in range(num_of_readers)]

event_loop.run_until_complete(asyncio.wait(tasks))
event_loop.close()
