# Security Incident Response Runbook

## Overview

This runbook describes how to respond to security incidents reported through IT support tickets or flagged by automated tooling (EDR, DLP, SIEM). It covers initial triage, containment, investigation, and closure for the most common incident types in a SaaS environment.

> **When in doubt, contain first, investigate second.** It is better to briefly disrupt a legitimate user than to allow a breach to spread.

## Incident Classification

| Severity | Description | Response time |
|---|---|---|
| P1 — Critical | Active breach, ransomware, mass data exfiltration | Immediate (24/7) |
| P2 — High | Credential compromise, phishing with successful click, suspicious admin activity | Within 2 hours |
| P3 — Medium | Phishing received (no click), unauthorised device, policy violation | Within 8 hours (business hours) |
| P4 — Low | Security awareness query, minor policy question | Next business day |

## Common Incident Types

### 1. Suspicious login / account compromise

**Indicators:** Login from unexpected geography, unusual hours, multiple failed attempts followed by success, user reports they did not initiate a login.

**Containment:**
1. Immediately terminate all active Okta sessions for the affected user:
   - Okta Admin → *Directory → People* → user → *More Actions → Revoke Sessions*.
2. Force a password reset (see [Password Reset Runbook](password-reset-runbook.md)).
3. Reset MFA factors.
4. Lock the account if the user cannot be reached for verification within 30 minutes.

**Investigation:**
1. Pull Okta System Log for the user (last 7 days): filter by `actor.alternateId = username`.
2. Note all IP addresses, user agents, and geolocations of successful logins.
3. Check which applications were accessed after the anomalous login.
4. If sensitive apps (AWS, GitHub, Salesforce) were accessed, notify the data owners.
5. Correlate with Datadog SIEM for any unusual API calls or data downloads.

**Resolution:**
- If confirmed compromise: file a formal incident report in Jira Security project, notify CISO.
- If false positive: re-enable account, document findings in ticket, close P3 or below.

### 2. Phishing — email received

**Indicators:** User reports a suspicious email asking for credentials, claiming to be IT/HR/a vendor, containing unexpected attachments or links.

**Triage:**
1. Ask the user: *"Did you click any links or enter any credentials?"*
   - **No click:** Classify P3. Proceed to remediation.
   - **Clicked link:** Escalate to P2. Check for credential entry.
   - **Entered credentials:** Escalate to P1. Treat as active compromise (see section 1).

**Remediation (no click):**
1. Ask the user to forward the email as an attachment to `security@company.com`.
2. Extract the sender domain and any URLs from the email headers.
3. Submit the URL to the email gateway block list (Proofpoint admin console).
4. Check if the phishing email reached other employees: search mail logs in Google Workspace Admin or M365 for the sender.
5. If widespread: send a company-wide alert via IT communications Slack channel.

### 3. Ransomware / malware alert

**Indicators:** EDR (CrowdStrike) alert, user reports files changing names or becoming inaccessible, unusual CPU/disk activity.

**Containment — immediate:**
1. Isolate the machine from the network **immediately**:
   - CrowdStrike Falcon: *Host Management → Contain Host*.
   - If CrowdStrike is unavailable: ask the user to disconnect from Wi-Fi and unplug the Ethernet cable.
2. Do **not** shut down the device — memory forensics may be needed.
3. Alert the IT Security lead and CISO within 15 minutes.

**Investigation:**
1. In CrowdStrike, review the Process Tree for the alert to identify the execution chain.
2. Identify Patient Zero: when was the malicious process first executed? What launched it?
3. Common vectors: malicious email attachment (macro), drive-by download, compromised USB.
4. Check if lateral movement occurred: did the malware attempt to access network shares or other hosts?

**Recovery:**
1. Wipe and reimage the device (see [Hardware Replacement Runbook](hardware-replacement-runbook.md) for MDM re-enrolment steps).
2. Restore user data from the most recent clean backup (OneDrive version history or IT-managed backup).
3. Do **not** restore from a backup taken after the incident date.
4. Once reimaged and enrolled: confirm EDR agent is active and reporting.

### 4. Unauthorized data exfiltration (DLP alert)

**Indicators:** DLP system (Nightfall, Symantec DLP) flags a large upload to an external service, sensitive data detected in an unapproved location.

**Triage:**
1. Identify the user, destination, file size, and content type from the DLP alert.
2. Check with the user's manager: *"Was this upload authorised for business purposes?"*
3. If authorised: tune the DLP rule to reduce false positives. Close P4.
4. If not authorised or manager is unsure: escalate to P2 and investigate.

**Investigation:**
1. Pull network logs for the user's machine around the alert time.
2. Identify what data was uploaded (file names, content snippets if available).
3. Determine destination: personal cloud storage, competitor domain, unknown endpoint?
4. Check if this is a pattern (repeat offences in the past 30 days).

**Containment (if confirmed):**
1. Block the destination domain at the web proxy.
2. Preserve evidence before taking any action that modifies the user's machine.
3. Involve HR and Legal before interviewing the employee.

## Post-Incident Actions (all P1/P2 incidents)

1. Write an incident report within 5 business days:
   - Timeline of events.
   - Root cause.
   - Containment and remediation steps taken.
   - Systems and data affected.
   - Lessons learned and follow-up actions.
2. File the report in the Jira Security project and link it to the original ticket.
3. Schedule a post-mortem for P1 incidents within 10 business days.

## Escalation Matrix

| Situation | Escalate to |
|---|---|
| Active breach (P1) | IT Security Lead + CISO immediately |
| Data of regulated type exposed (PII, financial) | Legal + CISO |
| Ransomware with lateral movement | IT Security Lead + external IR firm |
| Incident involves an executive account | CISO + direct notification to Executive team |

## Related Articles

- [Password Reset Runbook](password-reset-runbook.md)
- [Security Awareness FAQ](security-awareness-faq.md)
- [Data Classification Policy](data-classification-policy.md)
- [MFA Policy](mfa-policy.md)
