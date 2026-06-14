# Data Classification Policy

## Purpose

This policy defines how company data should be classified, handled, stored, and shared. Correct classification ensures that sensitive information is protected appropriately and that employees know how to handle data they encounter in their work.

## Scope

This policy applies to all employees, contractors, and third parties who create, process, store, or transmit company data.

---

## Classification Levels

### Public

**Definition:** Information that is intentionally made available to the public or that would cause no harm if disclosed.

**Examples:**
- Marketing materials, blog posts, press releases.
- Job postings.
- Open-source code.
- Public documentation.

**Handling requirements:**
- No restrictions on sharing or storage.
- May be stored on personal devices and shared via any channel.

---

### Internal

**Definition:** Information intended for use within the company that is not sensitive but should not be shared externally without consideration.

**Examples:**
- Internal project documentation.
- Meeting notes and agendas (non-sensitive topics).
- Internal roadmaps and OKRs.
- Non-sensitive employee communications.

**Handling requirements:**
- Store on company-approved systems (Google Drive, SharePoint, Confluence).
- Do not post in public forums or share with external parties without manager approval.
- May be shared via company email and Slack.

---

### Confidential

**Definition:** Sensitive business information that could cause significant harm to the company, employees, or customers if disclosed.

**Examples:**
- Customer contracts and pricing.
- Employee salary and performance data.
- Financial forecasts and board materials.
- Product roadmaps and unreleased feature details.
- Security incident reports.
- Personally identifiable information (PII): names, email addresses, phone numbers, addresses.

**Handling requirements:**
- Store only in approved, access-controlled systems. Do not store in personal cloud accounts.
- Share only with individuals who have a business need to know.
- Encrypt before emailing externally (use secure file share links instead where possible).
- Do not discuss in public places or on public calls.
- Do not print unless necessary; if printed, store securely and shred when done.
- Remote access requires VPN.

---

### Restricted

**Definition:** The most sensitive category. Unauthorised disclosure could have severe legal, financial, or reputational consequences.

**Examples:**
- Customer personal and financial data subject to GDPR, CCPA, or PCI DSS.
- Authentication credentials, private keys, API secrets.
- Health-related personal data.
- Merger and acquisition information.
- Vulnerability details and penetration test reports.
- Litigation-sensitive communications.

**Handling requirements:**
- Access on a strict need-to-know basis only. Request access through your manager and IT Security.
- Must be stored in systems with encryption at rest and in transit.
- Never email externally without explicit Legal approval.
- Never transmitted via Slack or other chat tools.
- Must not be stored on local devices without full-disk encryption enabled (BitLocker/FileVault).
- Physical documents must be kept in a locked cabinet and destroyed via cross-cut shredding.
- Incidents involving Restricted data must be reported to IT Security and Legal within 1 hour of discovery.

---

## Data Handling Quick Reference

| Action | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Share externally without approval | ✅ | ❌ | ❌ | ❌ |
| Store in personal cloud | ✅ | ❌ | ❌ | ❌ |
| Share via Slack | ✅ | ✅ | ✅ (internal only) | ❌ |
| Email externally | ✅ | With care | Encrypted only | Legal approval required |
| Print | ✅ | ✅ | With care; shred after | Locked storage; cross-cut shred |
| Store on local device | ✅ | ✅ | Encrypted device only | Full-disk encryption + approval |

---

## Labelling

Documents containing Confidential or Restricted data should be labelled at the top with the classification level (e.g., `[CONFIDENTIAL]` in the document header). This helps recipients handle the document correctly.

For files stored in Google Drive or SharePoint, use the sensitivity labels configured in the DLP system. Contact IT if you are unsure how to apply a label.

---

## Data Retention

| Classification | Minimum retention | Maximum retention |
|---|---|---|
| Public | As needed | As needed |
| Internal | 1 year | 5 years |
| Confidential | Per data type (see Legal data retention schedule) | Per Legal |
| Restricted | Per data type and regulation (GDPR: typically 2–7 years) | Per Legal |

Do not delete Restricted or Confidential data without confirming the retention period has been met. When in doubt, ask Legal.

---

## Reporting Data Incidents

If you believe Confidential or Restricted data has been disclosed to an unauthorised party (accidentally or intentionally):

1. Do not attempt to cover it up or assess the impact yourself.
2. Report to IT Security immediately: `security@company.com`.
3. Preserve all evidence — do not delete emails, logs, or files.
4. Do not discuss the incident outside of the response team until Legal has advised.

GDPR and some other regulations require external notification within 72 hours of discovering a breach involving personal data. Early reporting internally is critical.

---

## Related Articles

- [Security Incident Response Runbook](security-incident-response-runbook.md)
- [Security Awareness FAQ](security-awareness-faq.md)
- [Remote Work FAQ](remote-work-faq.md)
