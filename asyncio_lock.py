import asyncio
import functools

event_loop = asyncio.get_event_loop()


def unlock(lock):
    print("callback releasing lock")
    lock.release()


async def coro1(lock):
    print('coro1 waiting for the lock')
    with await lock:
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coro2(lock):
    print('coro2 waiting for the lock')
    await lock
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


try:
    lock = asyncio.Lock()
    print("acquiring the lock before starting coroutines")
    event_loop.run_until_complete(lock.acquire())
    print("lock acquired: {} - {!r}".format(lock.locked(), lock))

    event_loop.call_later(1, functools.partial(unlock, lock))
    print("lock acquired: {} - {!r}".format(lock.locked(), lock))

    print("entering event loop")
    event_loop.run_until_complete(
        asyncio.wait([coro1(lock),
                      coro2(lock)]),
    )

    print("exited event loop")

    print("lock status: {} - {!r}".format(lock.locked(), lock))
finally:
    event_loop.close()
