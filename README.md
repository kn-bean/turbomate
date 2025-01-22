# TurboMate

TurboMate is a Python-based tool designed to manage running processes and resources on Windows, optimizing system performance. It monitors active processes and terminates those that exceed a specified CPU usage threshold to help maintain optimal system responsiveness.

## Features

- **Process Monitoring**: Continuously checks running processes and their CPU usage.
- **Automated Termination**: Automatically terminates processes that consume more CPU than the specified threshold.
- **Customizable Settings**: Users can configure the CPU usage threshold and the interval for system checks.

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## Usage

1. **Install Dependencies**: Ensure Python is installed on your system. Install the `psutil` library using pip:
   ```bash
   pip install psutil
   ```

2. **Run TurboMate**: Execute the script using Python:
   ```bash
   python turbomate.py
   ```

3. **Configuration**: Modify the `high_cpu_usage_threshold` and `check_interval` parameters in the `TurboMate` class to adjust the CPU usage threshold and the time interval between checks.

## Disclaimer

Use TurboMate with caution as it will terminate processes that exceed the CPU usage threshold. Ensure important applications are not inadvertently terminated. This tool is intended for educational purposes and should be used at your own risk.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.