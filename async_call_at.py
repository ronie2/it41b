import asyncio, time


def callback(n, loop):
    print("callback {} invoked at {}".format(n, loop.time()))


def stopper(loop):
    print("stoper invoked at {}".format(loop.time()))
    loop.stop()


event_loop = asyncio.get_event_loop()

try:
    now = event_loop.time()
    wall_clack = time.time()
    print("wall clock: {}".format(wall_clack))
    print("loop clock: {}".format(now))
    print("registering callback")
    # event_loop.call_later(0.5, callback, 1)
    # event_loop.call_later(1, callback, 2)
    # event_loop.call_later(2, stopper, event_loop)
    event_loop.call_at(now + 0.5, callback, 1, event_loop)
    event_loop.call_at(now + 0.1, callback, 2, event_loop)
    event_loop.call_at(now + 0.1, stopper, event_loop)
    event_loop.call_soon(callback, 3, event_loop)

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
