# Log Analyzer

A tool that reads server log files and shows useful reports.

## Requirements
Python 3.8 or above

## Installation
pip install -r requirements.txt

## How to Generate Test Log File
python scripts/generate_logs.py

## How to Run
python log_analyzer.py server.log

## What It Shows
.Status code counts (200, 401, 404, 500)
.Top 3 slowest endpoints
.Incomplete/malformed lines count