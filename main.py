from fastapi import FastAPI, Request
import logging
import time
import threading

app = FastAPI()


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
