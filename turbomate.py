import psutil
import os
import time

class TurboMate:
    def __init__(self, high_cpu_usage_threshold=80, check_interval=5):
        self.high_cpu_usage_threshold = high_cpu_usage_threshold
        self.check_interval = check_interval

    def get_running_processes(self):
        """Retrieve a list of currently running processes."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes

    def terminate_process(self, pid):
        """Terminate a process by its PID."""
        try:
            os.kill(pid, 9)
            print(f"Terminated process with PID: {pid}")
        except Exception as e:
            print(f"Failed to terminate process {pid}: {e}")

    def optimize_system(self):
        """Optimize system by monitoring and managing processes."""
        while True:
            print("Checking system status...")
            processes = self.get_running_processes()
            for process in processes:
                if process['cpu_percent'] > self.high_cpu_usage_threshold:
                    print(f"Process {process['name']} (PID: {process['pid']}) is using {process['cpu_percent']}% CPU.")
                    self.terminate_process(process['pid'])
            time.sleep(self.check_interval)

if __name__ == "__main__":
    turbomate = TurboMate()
    turbomate.optimize_system()