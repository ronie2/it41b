import asyncio
import functools


async def phase(i):
    print("in pahse {}".format(i))
    #await asyncio.sleep(1 * i)
    print("done with phase {}".format(i))
    return "phase {} result".format(i)


async def main(num_phases):
    print("starting main")
    phases = [phase(i) for i in range(num_phases)]
    print("waiting for phases to complete")
    completed, pending = await asyncio.wait(phases)
    print(pending)
    result = [t.result() for t in completed]
    print("result: {!r}".format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
