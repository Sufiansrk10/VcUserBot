import asyncio



from pytgcalls import idle

from confing import call_py


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | VcUserBot Started! |
    ------------------
"""
    )
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
