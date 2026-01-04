
import docker
import time

client = docker.from_env()

container = client.containers.run(
    "busybox",
    "sleep 3600",
    detach=True
)

print(f"Container {container.id[:12]} is running...")

time.sleep(1)

exec_result = container.exec_run("hostname")

hostname = exec_result.output.decode().strip()
print("Hostname of container:", hostname)

container.stop()
container.remove()
