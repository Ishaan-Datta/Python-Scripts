# asyncio implemention separate module, test both splitting course modules, pages, files as async function or each course as own thread
# download queue begins here? or asyncio to start download queue after all files are collected for each course
# Timeit module for testing sync vs async implementations


import asyncio
import tqdm
import httpx

# https://canvas.ubc.ca/doc/api/file.graphql.html
# https://ubc.instructure.com/graphiql

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.get('http://127.0.0.1:9989/data.json') as resp:
        async with session.get("http://127.0.0.1:9989/with_bom.json") as resp:
            raw_text = await resp.text()
            text_without_bom = raw_text.encode().decode("utf-8-sig")
            work_items = json.loads(text_without_bom)
            print(type(work_items))
            print(work_items)


asyncio.run(main())
