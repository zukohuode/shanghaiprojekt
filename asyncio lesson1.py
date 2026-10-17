import time
import asyncio

#async def umbrella():
#   print('start')
#    await asyncio.sleep(2)
#    print('end')

#asyncio.run(umbrella())
async def task():
    await asyncio.sleep(2)

async def main():
    print('start')
    asyncio.create_task(task())
    print('end')



asyncio.run(main())