import asyncio


async def task_func():
    print("in task func")
    await asyncio.sleep(2)
    return "task result"


event_loop = asyncio.get_event_loop()
#asyncio.ensure_future()

try:
    print("Creating task")
    task = event_loop.create_task([task_func for _ in range(10)])
    print("task: {!r}".format(task))
    #task.cancel()

    print("Entering event loop")
    return_value = event_loop.
    print("task: {!r}".format(task))
    # print("return value: {!r}".format(return_value))
except asyncio.CancelledError as e:
    print("Got exception", end="")
    print(e)
finally:
    event_loop.close()

print("task result: {!r}".format(task.result()))
