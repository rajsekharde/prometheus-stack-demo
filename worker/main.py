import time

print("Worker Started")

while True:
    time.sleep(60)
    # Pauses execution for 60s, and returns to top of loop
    # CPU usage spikes without it