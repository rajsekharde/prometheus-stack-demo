# Demo project for testing monitoring stack

## Tools:
 - node-exporter: host system metrics
 - cadvisor: container metrics
 - prometheus: metrics collection & processing

## Monitoring using Prometheus UI:

Run the project:

```bash
docker compose up --build -d
```

Visit the Prometheus UI page:

```bash
http://localhost:9090
```

Status > Target Health: Check if node-exporter and cadvisor are running

**Query:**

Use Graph or Table to view query results

### Useful PromQL query commands:


**Host total CPU usage:**

```bash
sum(rate(node_cpu_seconds_total{mode!="idle"}[1m]))
```

Tells how many CPU cores are currently being burned


**Host CPU saturation %:**

```bash
1 - avg(rate(node_cpu_seconds_total{mode="idle"}[1m]))
```

Tells what fraction of total CPU is not idle


**Per-Container CPU usage:**

```bash
sum by (name) (rate(container_cpu_usage_seconds_total{name!=""}[1m]))
```

Tells how many cores each container is consuming


**Host used memory (real):**

```bash
node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes
```

Tells how much memory the kernel cannot immediately give back


**Host memory usage %:**

```bash
1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)
```


**Per container memory usage:**

```bash
sum by (name) (container_memory_working_set_bytes{name!=""})
```


**Host disk memory usage:**

```bash
(node_filesystem_size_bytes{fstype!~"tmpfs|overlay"}
-
node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"})
/
node_filesystem_size_bytes{fstype!~"tmpfs|overlay"}
```

Tells how full real disks are


**Host disk read/write throughput:**

```bash
# Read
sum(rate(node_disk_read_bytes_total[1m]))

#Write
sum(rate(node_disk_written_bytes_total[1m]))
```

Shows bytes per second moving through physical disks


**Per container disk I/O:**

```bash
# Read
sum by (name) (rate(container_fs_reads_bytes_total{name!=""}[1m]))

# Write
sum by (name) (rate(container_fs_writes_bytes_total{name!=""}[1m]))
```


**Host total network in/out:**

```bash
# Receive
sum(rate(node_network_receive_bytes_total{device!="lo"}[1m]))

# Transmit
sum(rate(node_network_transmit_bytes_total{device!="lo"}[1m]))
```

Tells how many bytes per second cross the machine boundary


**Per container network:**

```bash
# Receive
sum by (name) (rate(container_network_receive_bytes_total{name!=""}[1m]))

# Transmit
sum by (name) (rate(container_network_transmit_bytes_total{name!=""}[1m]))
```

**Container restarts (death detector):**

```bash
time() - container_start_time_seconds{name!=""}
```

Sawtooths: system is not healthy. It is respawning


**Load average(CPU pressure):**

```bash
node_load1
```

High load + low CPU usage = IO wait or lock contention


**Memory pressure early warning:**

```bash
High load + low CPU usage = IO wait or lock contention
```
