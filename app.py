from fastapi import FastAPI,Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import util.utils as utils


app = FastAPI()

# Allow requests from http://localhost:8080 (from where index.html is served)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/stream-time")
def stream():
    #pass an event generator to StreamingResponse
    return StreamingResponse(utils.event_stream(), media_type="text/event-stream")

@app.get("/system-stats")
async def stream_system_stats(request: Request):
    return StreamingResponse(utils.system_stats_generator(request), media_type="text/event-stream")
