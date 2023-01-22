import asyncio

import aiohttp

from env import api1, api2


async def api(session):
    res = await session.get('https://api.open-meteo.com/v1/forecast?latitude=40.6971494&'
                            'longitude=-74.2598655&hourly=temperature_2m&start_date=2023-01-17&end_date=2023-01-17')
    res = await res.json()
    res = res['current_weather']['temperature']
    res_average = int(sum(res) // len(res))
    return res_average


async def api_2(session):
    r = await session.get('https://api.weatherbit.io/v2.0/current?lat=40.6971494&lon=-74.2598655&key='+api1)
    res = await r.json()
    responce = res['data'][0]['temp']
    return responce


async def api3(session):
    r = await session.get('http://api.weatherstack.com/current?access_key='+api2+'&query=Kiev')
    res = await r.json()
    responce = res['current']['temperature']
    return responce


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(api(session), api_2(session), api3(session))
    answer = sum(result) / len(result)
    print(answer)


asyncio.run(main())
