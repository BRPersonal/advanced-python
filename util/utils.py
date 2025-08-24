import time
import asyncio
import json
import psutil
from fastapi import Request


def event_stream():
    while True:
        yield f"The time is {time.strftime('%X')}\n\n"
        time.sleep(1)

async def system_stats_generator(request: Request):
    while True:
        if await request.is_disconnected():
            print("Client disconnected.")
            break

        cpu_usage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()

        stats = {
            "cpu_percent": cpu_usage,
            "memory_percent": memory_info.percent,
            "memory_used_mb": round(memory_info.used / (1024 * 1024), 2),
            "memory_total_mb": round(memory_info.total / (1024 * 1024), 2)
        }

        yield f"data: {json.dumps(stats)}\n\n"
        await asyncio.sleep(1)