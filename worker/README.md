### Initially:

main.py:

```bash
print("Worker Started")
```

After running docker compose up, the worker container kept stopping and restarting. This happened because the container needs an active running process to stay alive. main.py executes the print statement and stops, resulting in the container stopping as well.

### Solution:

```bash
import time

print("Worker Started")

while True:
    time.sleep(60)
```

An infinite loop is used to keep the process alive.
The process is paused for 60s using sleep() to reduce CPU usage