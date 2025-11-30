# Tools Documentation - AI Triage Bot Prototype

**Last Updated:** 2025-11-29  
**Owner:** William Ryan Micou  
**Purpose:** Documentation for monitoring and audit tools  

---

## 📋 Overview

This directory contains tools for monitoring, auditing, and analyzing the AI Triage Bot system. These tools support ISO/IEC 42001:2023 compliance requirements for performance evaluation and audit readiness.

---

## 📁 Directory Structure
```
tools/
├── README.md              (This file)
├── __init__.py           (Package initialization)
└── fallback_viewer.py    (Fallback log analysis tool)
```

---

## 🔧 Available Tools

### Fallback Log Viewer (`fallback_viewer.py`)

**Purpose:** Human-readable interface for reviewing low-confidence ticket classifications  
**ISO Clause:** 9.1 (Monitoring), 9.2 (Internal Audit), 10.2 (Continual Improvement)  
**Status:** ACTIVE  
**Version:** 1.0  

**Features:**
- ✅ Load and parse JSONL fallback logs
- ✅ Filter by date range
- ✅ Filter by confidence score
- ✅ Filter by ticket category
- ✅ Filter by PII detection status
- ✅ Generate summary statistics
- ✅ Export results to CSV
- ✅ Display human-readable log entries

---

## 🚀 Quick Start

### Basic Usage
```bash
# View all fallback entries
python tools/fallback_viewer.py

# View entries from last 7 days
python tools/fallback_viewer.py --date-range 7

# View summary statistics only
python tools/fallback_viewer.py --stats-only

# View only low-confidence entries
python tools/fallback_viewer.py --max-confidence 0.3

# View only PII-flagged tickets
python tools/fallback_viewer.py --contains-pii

# Export to CSV
python tools/fallback_viewer.py --date-range 30 --export report.csv
```

---

## 📊 Command Reference

### All Available Options
```bash
python tools/fallback_viewer.py [OPTIONS]

Options:
  --log-path PATH          Path to fallback log file (default: fallback_log.jsonl)
  --date-range DAYS        Show entries from last N days
  --min-confidence X       Filter by minimum confidence score (0.0-1.0)
  --max-confidence X       Filter by maximum confidence score (0.0-1.0)
  --category CAT           Filter by ticket category
  --contains-pii           Show only PII-flagged tickets
  --no-pii                 Show only tickets WITHOUT PII
  --limit N                Limit number of entries displayed
  --export FILE            Export filtered results to CSV file
  --stats-only             Show only summary statistics
```

---

## 📈 Use Cases

### 1. Daily Review (Human Review Agents)

**Objective:** Review yesterday's flagged tickets
```bash
# Morning review - last 24 hours
python tools/fallback_viewer.py --date-range 1 --limit 20

# Get quick stats
python tools/fallback_viewer.py --date-range 1 --stats-only
```

**Expected Output:**
- Total entries from yesterday
- Category distribution
- Average confidence scores
- PII detection rate

---

### 2. Weekly Quality Audit

**Objective:** Assess classification accuracy trends
```bash
# Last 7 days with export
python tools/fallback_viewer.py --date-range 7 --export weekly_audit.csv

# Focus on very low confidence
python tools/fallback_viewer.py --date-range 7 --max-confidence 0.3
```

**Follow-up Actions:**
- Review CSV in spreadsheet software
- Calculate accuracy metrics
- Identify patterns in misclassifications
- Report findings to AI Governance Lead

---

### 3. PII Detection Audit

**Objective:** Validate PII detection accuracy
```bash
# All PII-flagged tickets this month
python tools/fallback_viewer.py --date-range 30 --contains-pii --export pii_audit.csv

# Check for false positives (manual review of CSV)
# Check for false negatives (sample non-PII tickets)
python tools/fallback_viewer.py --date-range 30 --no-pii --limit 100
```

**Metrics to Track:**
- False positive rate (target: < 10%)
- False negative rate (target: < 5%)

---

### 4. Category Performance Analysis

**Objective:** Identify which categories need tuning
```bash
# Filter by specific category
python tools/fallback_viewer.py --category software_issue --date-range 30

# Compare across categories (run separately for each)
python tools/fallback_viewer.py --category access_request --stats-only
python tools/fallback_viewer.py --category hardware_issue --stats-only
```

**Look for:**
- Categories with high fallback rates
- Patterns in misclassifications
- Need for new categories

---

## 📊 Understanding the Output

### Summary Statistics
```
===================================================================
📊 FALLBACK LOG SUMMARY STATISTICS
===================================================================

📈 Total Entries: 47

📂 Classification Distribution:
   software_issue      : 15 (31.9%)
   access_request      : 12 (25.5%)
   unknown             : 10 (21.3%)
   hardware_issue      : 7  (14.9%)
   billing_question    : 3  (6.4%)

🎯 Confidence Scores:
   Average: 0.38
   Range:   0.12 - 0.49

🔒 PII Detection:
   Tickets with PII: 5 (10.6%)

📅 Date Range:
   Oldest: 2025-11-22 08:15:23
   Newest: 2025-11-29 19:45:12
===================================================================
```

---

### Individual Entry Display
```
Entry #1
──────────────────────────────────────────────────────────────────
⏰ Timestamp:   2025-11-29T19:45:12.123456+00:00
📂 Category:    software_issue
🎯 Confidence:  0.42
🔒 Contains PII: No
📝 Ticket Text:
   Excel keeps crashing when I open large spreadsheets. Started 
   after yesterday's update.
```

---

## 🔍 Troubleshooting

### Common Issues

**Issue: "Warning: Log file not found"**
- **Cause:** No fallback_log.jsonl file exists yet
- **Solution:** Run classification first to generate logs, or specify different log path
- **Command:** `python tools/fallback_viewer.py --log-path path/to/your/log.jsonl`

**Issue: "Warning: Skipping malformed log entry"**
- **Cause:** Corrupted JSON in log file
- **Solution:** Tool will skip bad entries and continue. Check log file manually if needed.

**Issue: "No entries to display"**
- **Cause:** Filters are too restrictive
- **Solution:** Broaden filters or check date range

**Issue: CSV export shows strange characters**
- **Cause:** Encoding issue
- **Solution:** Open CSV with UTF-8 encoding in Excel/LibreOffice

---

## 📋 ISO/IEC 42001 Compliance

### Clause 9.1 - Monitoring, Measurement, Analysis

**Requirements Met:**
- ✅ Automated logging of low-confidence classifications
- ✅ Statistical analysis capabilities
- ✅ Trend identification through date filtering
- ✅ Category distribution tracking

**Usage:** Weekly analysis of fallback logs to assess system performance

---

### Clause 9.2 - Internal Audit

**Requirements Met:**
- ✅ Audit trail accessibility
- ✅ Filtering and sampling capabilities
- ✅ Export for audit documentation
- ✅ PII detection validation

**Usage:** Quarterly audits of classification accuracy and PII detection

---

### Clause 10.2 - Continual Improvement

**Requirements Met:**
- ✅ Pattern identification in misclassifications
- ✅ Feedback collection through analysis
- ✅ Data-driven improvement opportunities

**Usage:** Monthly review to identify system improvements

---

## 📅 Recommended Usage Schedule

### Daily (15 minutes)
```bash
# Quick morning check
python tools/fallback_viewer.py --date-range 1 --stats-only
```

**Review:**
- Total fallback entries
- Any unusual spikes
- PII detection count

---

### Weekly (30-60 minutes)
```bash
# Detailed weekly review
python tools/fallback_viewer.py --date-range 7 --export weekly_review.csv
```

**Actions:**
- Review 20-30 random entries
- Document patterns
- Calculate accuracy metrics
- Report to supervisor

---

### Monthly (2-3 hours)
```bash
# Comprehensive monthly audit
python tools/fallback_viewer.py --date-range 30 --export monthly_audit.csv

# PII audit
python tools/fallback_viewer.py --date-range 30 --contains-pii --export pii_audit.csv
```

**Actions:**
- Full accuracy assessment
- PII false positive/negative analysis
- Category performance review
- Recommendations for improvement

---

### Quarterly (4-6 hours)
**Full ISO 42001 audit using this tool + manual validation**

See: `../governance/audit_procedures.md` for complete audit checklist

---

## 🔄 Tool Maintenance

### Updates Needed When:
- New ticket categories added (no code change needed)
- New fields added to fallback log format (code update required)
- New filtering requirements identified (code update required)
- Export format changes needed (code update required)

### Version History
- **v1.0 (2025-11-25):** Initial release

---

## 📞 Contact

**Questions about fallback viewer?**
- **System Owner:** William Ryan Micou
- **See also:** `../governance/training_materials/reviewer_handbook.md` (Section: Using the Fallback Viewer Tool)

**Bug reports or feature requests:**
- Create an issue in GitHub repository
- Include example command and error output

---

## 🔗 Related Documentation

- **Reviewer Handbook:** `../governance/training_materials/reviewer_handbook.md` - Detailed usage guide
- **Audit Procedures:** `../governance/audit_procedures.md` - Audit framework using this tool
- **Admin Guide:** `../governance/training_materials/admin_technical_guide.md` - Monitoring section

---

## 🚀 Future Enhancements

Potential future additions to this directory:

- [ ] GUI version of fallback viewer
- [ ] Real-time monitoring dashboard
- [ ] Automated weekly report generator
- [ ] Performance benchmarking tool
- [ ] API health checker

**Note:** These are planned enhancements, not current features

---

**Document Version:** 1.0 | Created: 2025-11-29
```
