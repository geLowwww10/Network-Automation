# Network Automation Project

## Overview
This project automates the process of changing network configurations on routers using NETCONF, YANG data modeling, and Python. It integrates with WebEx Teams for notifications.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Ensure your device supports NETCONF and configure it with the proper credentials.
3. Set up your WebEx bot token and room ID in `config/config.json`.

## How to Run
Run the `main.py` script:
```bash
python scripts/main.py