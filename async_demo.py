import asyncio
import time


async def down(name, seconds):
    print(f"start {name}")
    await asyncio.sleep(seconds)
    print(f"done {name}")
    return f"{name} finished"

async def main():
    
    start=time.perf_counter()
    results= await asyncio.gather(
        down("a", 5),
        down("b",2)
    )
    print (results)
    print(f"tot : {time.perf_counter()- start:.1f} sec")
asyncio.run(main())