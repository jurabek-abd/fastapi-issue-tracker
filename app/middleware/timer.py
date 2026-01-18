import time

from fastapi import Request


async def timing_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter()
    response.headers["X-Process-Time"] = f"{end - start:.4f}s"
    return response
