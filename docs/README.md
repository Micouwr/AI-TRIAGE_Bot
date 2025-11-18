# Documentation

This directory contains governance, compliance, and technical documentation for the AI-TRIAGE Bot.

## Files

### `iso42001_mapping.md`
Maps all bot features to ISO/IEC 42001 AI governance standards. This is your **compliance blueprint** showing how each component meets international AI management system requirements.

**Usage:** Reference this when auditing the bot or planning new features to ensure governance alignment.

---

## Governance Structure

The bot follows a modular governance design:

- **risk_controls/** - PII filters, escalation protocols, fallback mechanisms
- **scripts/** - Monitoring, validation, transparency, and quality assurance tools
- **lifecycle/** - Version history and change tracking
- **governance/** - Configuration and scope definitions

---

## For Auditors

To verify ISO/IEC 42001 compliance:
1. Check feature implementations in referenced script files
2. Verify test coverage in `tests/`
3. Review fallback logs in `fallback_log.json`
4. Validate decision transparency in `tools/view_fallbacks.py`

---

## Maintenance

Update this mapping when:
- Adding new bot features
- Modifying governance controls
- Changing classification logic
- Updating risk protocols

EOF
