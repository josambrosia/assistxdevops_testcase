from fastapi import FastAPI, Response
import time
import threading

app = FastAPI()

@app.get("/")
def root():
    return {"Hello World"}


@app.get("/burn-cpu")
def burn_cpu(seconds: int = 10):


    def cpu_stress(duration: int):
        end_time = time.time() + duration
        while time.time() < end_time:
            _ = 10 ** 10 

    thread = threading.Thread(target=cpu_stress, args=(seconds,))
    thread.start()

    return {"status": "CPU burn started", "duration_seconds": seconds}
