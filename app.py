from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# Allow requests from http://localhost:8080 (where index.html is served)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def event_stream():
    while True:
        yield f"data: The time is {time.strftime('%X')}\n\n"
        time.sleep(1)

@app.get("/stream-time")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
