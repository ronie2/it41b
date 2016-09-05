import asyncio


def callback(n):
    print("callback {} invoker".format(n))


def stopper(loop):
    print("stoper invoked")
    loop.stop()


event_loop = asyncio.get_event_loop()

try:
    print("registering callback")
    event_loop.call_later(0.5, callback, 1)
    event_loop.call_later(1, callback, 2)
    event_loop.call_later(2, stopper, event_loop)
    event_loop.call_soon(callback, 3)

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
