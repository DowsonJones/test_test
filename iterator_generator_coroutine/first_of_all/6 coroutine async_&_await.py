import asyncio


async def do_some_work(x):
    print('waiting: ', x)
    await asyncio.sleep(x)
    return f'Done after {x}s'


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(do_some_work(1)),
    asyncio.ensure_future(do_some_work(2)),
]
loop.run_until_complete(asyncio.wait(tasks))

# result
for task in tasks:
    print('Task ret: ', task.result())
