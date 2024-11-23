import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        attempts = 10 / power
        await asyncio.sleep(attempts)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman_1 = asyncio.create_task(start_strongman("Hercules", 8))
    strongman_2 = asyncio.create_task(start_strongman("Samson", 4))
    strongman_3 = asyncio.create_task(start_strongman("Poddubny", 12))
    await strongman_1
    await strongman_2
    await strongman_3
    print('The end')


# просто повторить охото было :-Р
start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f'Затрачено времени: {finish - start} ')
