"""
main
"""
import asyncio


async def main(secs: int):
    """
    prints hello and world, with an asynch delay imbetween
    """
    print("hello")
    await asyncio.sleep(secs)
    print("world")
