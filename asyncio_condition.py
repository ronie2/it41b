import asyncio
import functools

async def consumer(condition, i):
    with await condition:
        print("consumer {} is waiting".format(i))
        await condition.wait()
        print("consumer {} triggered".format(i))
    print("Ending consumer {}".format(i))

async def manipulate(condition):
    print("Starting Manipulate")

    await asyncio.sleep(1)

    for i in range(1, 3):
        with await condition:
            print("Nitify {}".format(i))
            condition.notify(n=i)
        await asyncio.sleep(1)

    with await condition:
        print("Notify remaining")
        condition.notify_all()

    print("Ending manipulate")

event_loop = asyncio.get_event_loop()

try:
    condition = asyncio.Condition()

    consumers = [consumer(condition, i) for i in range(5)]
    event_loop.create_task(manipulate(condition))
    print("Entering event loop")
    result = event_loop.run_until_complete(asyncio.wait(consumers),)
    print("exited event loop")
finally:
    print("Closing event loop")
    event_loop.close()