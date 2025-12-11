from fastapi import FastAPI, Request
import logging
import time
import threading

# ========== WIB Logging ==========
WIB_OFFSET = 7 * 3600
logging.Formatter.converter = lambda *args: time.gmtime(time.time() + WIB_OFFSET)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI()

# Log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    client_ip = request.headers.get("x-forwarded-for", request.client.host)
    method = request.method
    path = request.url.path

    logging.info(f"ACCESS: {client_ip} -> {method} {path}")

    return await call_next(request)

@app.get("/")
def root():
    return {"message": "Hello World. AssistX test. Welcome to Dev environment"}

@app.get("/burn-cpu")
def burn_cpu(seconds: int = 10):

    logging.warning(f"CPU BURN TRIGGERED for {seconds}s")

    def cpu_stress(duration: int):
        end_time = time.time() + duration
        while time.time() < end_time:
            _ = 10 ** 10

    thread = threading.Thread(target=cpu_stress, args=(seconds,))
    thread.start()

    return {"status": "CPU burn started", "duration_seconds": seconds}
