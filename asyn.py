import asyncio


async def one():
    print("In 'one'")
    return "Result 'one'"


async def two(args):
    print("In 'two' with args: {!r}".format(args))


async def coroutine():
    print("In coroutine")
    print("Awaiting 'one'")
    result_one = await one()
    print("Awaiting 'two'")
    result_two = await two(result_one)
    return result_one, result_two


event_loop = asyncio.get_event_loop()
try:
    print("entering event loop")
    return_value = event_loop.run_until_complete(coroutine())
    print("it returned: {!r}".format(return_value))
finally:
    print("closing event loop")
    event_loop.close()
