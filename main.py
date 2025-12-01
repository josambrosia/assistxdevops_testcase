from fastapi import FastAPI, Response
import time
import threading

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello World"}


@app.get("/burn-cpu")
def burn_cpu(seconds: int = 10):
    """
    Endpoint untuk membuat CPU load spike.
    Default 10 detik.
    Gunakan ?seconds=20 (misal) untuk memanjangkan durasi.
    """

    def cpu_stress(duration: int):
        end_time = time.time() + duration
        while time.time() < end_time:
            _ = 10 ** 10  # operasi berat berulang

    # Jalankan busy-loop di thread agar request tidak timeout
    thread = threading.Thread(target=cpu_stress, args=(seconds,))
    thread.start()

    return {"status": "CPU burn started", "duration_seconds": seconds}
