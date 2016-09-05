import asyncio
import functools

event_loop = asyncio.get_event_loop()


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


try:
    event = asyncio.Event()
    print("event state: {}".format(event.is_set()))

    event_loop.call_later(5, functools.partial(set_event, event))

    print("Entering event loop")
    result = event_loop.run_until_complete(
        asyncio.wait([coro1(event), coro2(event)]), )
    print("Exited event loop")

    print("event state: {}".format(event.is_set()))
finally:
    event_loop.close()
