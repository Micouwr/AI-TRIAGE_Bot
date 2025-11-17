# Monitoring Scripts

This directory contains scripts for monitoring the health and performance of the AI Triage Bot Prototype. These scripts are essential for ensuring the bot operates within expected parameters and for quickly identifying issues.

## Purpose

- Track and log the status of the bot's processing pipeline.
- Detect and handle failures or fallbacks in the system.
- Provide audit trails for compliance with governance standards.

## ISO/IEC 42001 Alignment

- **Clause 5 (Accountability)**: Ensures traceability of monitored stages.
- **Clause 6 (Risk Management)**: Detects failures and triggers retries.
- **Clause 8 (Auditability)**: Logs all monitoring events with timestamps.

## Audit Notes

- Logs are maintained for a minimum of 90 days.
- Weekly reviews are conducted by the oversight team.

## How to Use

The monitoring scripts can be run as part of the bot's operational checks. They provide real-time feedback on the bot's performance and can be used to trigger alerts or manual interventions when issues arise.
