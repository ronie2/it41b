import asyncio


def callback():
    print("callback")


def stopper(loop):
    print("stoper")
    loop.stop()


event_loop = asyncio.get_event_loop()

try:
    print("registering callback")
    event_loop.call_soon(callback)
    event_loop.call_soon(stopper, event_loop)

    print("Entering event loop")
    event_loop.run_forever()
except KeyboardInterrupt as e:
    event_loop.stop()
    event_loop.close()
    print(e)
finally:
    pass
    print("closing event loop")
    event_loop.close()
