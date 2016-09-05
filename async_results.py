import asyncio


def mark_done(future, result):
    print("setting future result to: {!r}".format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()

try:
    all_done = asyncio.Future()
    print("Scheduling mark_done")
    event_loop.call_soon(mark_done, all_done, "My Own Result")

    print("Entering event loop")
    result = event_loop.run_until_complete(all_done)

    print("returned result: {!r}".format(result))
finally:
    print("Closing event loop")
    event_loop.close()
