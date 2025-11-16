# Contributing Guidelines - AI Triage Bot

This project is designed with audit-ready governance in mind.  
All contributions must maintain strict accuracy, truthfulness, and compliance with ISO/IEC 42001 principles.

---

## 1. Updating Governance Documentation

Whenever you commit changes that affect governance, compliance, or auditability, you **must update both**:

- `lifecycle/version_history.md`  
  - Add a new row for the change.  
  - Populate the **Date** column with the actual commit date (from `git log` or GitHub commit history).  
  - Mark items as **Planned** until implemented.  
  - Never add placeholders — only record completed work truthfully.

- `docs/iso42001_mapping.md`  
  - Map the new feature or script to the relevant ISO/IEC 42001 clause(s).  
  - Update the **Status / Date** column to match `version_history.md`.  
  - If the feature is not yet implemented, mark it as **Planned** or **Future**.

---

## 2. Commit Messages

- Use clear, descriptive commit messages.  
- Reference the governance impact, e.g.:  
  - `feat: add schema validator (Clause 6 - Risk Management)`  
  - `docs: update version history for v0.4 (Nov 2025)`  

This ensures traceability between code and governance docs.

---

## 3. Synchronization

- Dates in `README.md` and `docs/iso42001_mapping.md` must always match `lifecycle/version_history.md`.  
- `version_history.md` is the **single source of truth** for milestone dates.  
- Once synchronization tooling is set up, a note will be added to each doc header:  
  *“Dates in this document are synchronized with lifecycle/version_history.md for audit clarity.”*

---

## 4. Testing and Audit Evidence

- Add or update tests in `tests/` whenever new functionality is introduced.  
- Ensure fallback logs (`fallback_log.json`) remain reproducible.  
- Document escalation protocols in `risk_controls/` when risk handling changes.

---

## 5. Review Process

- All pull requests must include:  
  - Updated governance docs (`version_history.md` and `iso42001_mapping.md`)  
  - Clear commit messages referencing ISO clauses  
  - Evidence of testing (updated or new test files)

---

By following these guidelines, contributors ensure the AI Triage Bot remains **audit-ready, transparent, and compliant**.