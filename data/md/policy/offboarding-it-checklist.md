# IT Offboarding Checklist

## Purpose

This checklist ensures that when an employee leaves the company, all access is revoked promptly and securely, and company hardware is recovered. Incomplete offboarding is a significant security risk — access left active after departure can be exploited.

> **Time-sensitive:** Account deactivation must be completed by end of business on the employee's last day, or earlier if the departure is involuntary.

---

## Trigger

HR initiates the offboarding process by submitting an IT offboarding request at least 5 business days before the last working day (for planned departures). For involuntary terminations, IT must be notified simultaneously with the employee.

Required information from HR: employee name, username, last working day, departure type (voluntary / involuntary / contractor end), and whether any email or file access needs to be delegated to a manager.

---

## Involuntary Departures — Immediate Actions

For involuntary terminations (redundancy, dismissal for cause), perform these steps **immediately** upon notification:

- [ ] Disable the Okta account (revokes SSO access to all apps instantly).
- [ ] Revoke all active Okta sessions.
- [ ] Disable the Active Directory account.
- [ ] Notify the employee's manager that access has been revoked.
- [ ] Coordinate with HR and Legal if there are legal hold or investigation requirements — do not delete any data until cleared.

---

## Standard Offboarding Checklist

### Identity and Access

- [ ] **Okta:** Deactivate account on last day end-of-business. This cascades to all SAML/OIDC-integrated apps.
- [ ] **Active Directory:** Disable the account and move to the "Disabled Users" OU.
- [ ] **Email:** Disable login but set up a forwarding rule (to manager) for 30 days post-departure. After 30 days, disable the account completely.
- [ ] **GitHub:** Remove from all company organisations and teams.
- [ ] **AWS:** Remove IAM user and any group memberships. Revoke any long-lived access keys.
- [ ] **Salesforce:** Deactivate user account (Salesforce retains data ownership records).
- [ ] **Datadog:** Remove user.
- [ ] **PagerDuty / on-call tools:** Remove from all schedules and escalation policies immediately.
- [ ] **Shared accounts and passwords:** If the employee had knowledge of any shared credentials (emergency break-glass accounts, etc.), rotate those passwords immediately and record in the password manager.
- [ ] **VPN certificates / client configs:** If using certificate-based VPN, revoke the certificate.

### Cloud and Infrastructure Access

- [ ] Review and revoke any personal API keys or tokens created by the employee (check GitHub, AWS, and any internal developer portals).
- [ ] If the employee had production access, perform an access audit of the last 30 days of activity and document it.
- [ ] Remove from any Cloudflare, DNS, or domain management accounts.

### Hardware Recovery

- [ ] Contact the employee (or their manager for involuntary) to arrange device return.
  - **In-office:** Return at IT desk on last day. Employee signs the Asset Return Form.
  - **Remote:** IT sends a prepaid return shipping box. Device must be returned within 10 business days of last day.
- [ ] Update AssetTiger: record return date, set status to *Available* (if device is within refresh cycle) or *Pending Wipe* (if near end-of-life).
- [ ] Perform a factory reset / device wipe:
  - **macOS:** Erase All Content and Settings via System Preferences.
  - **Windows:** MDM-triggered wipe via Intune, or manual reset via Windows Recovery.
- [ ] Confirm wipe completion is logged in AssetTiger.
- [ ] Recover any peripherals (monitor, keyboard, dock) if the employee was remote and received equipment.

### Data and Files

- [ ] If the employee's manager requests access to their files:
  1. Grant the manager temporary access to the departing employee's Google Drive or OneDrive (30-day window).
  2. Document the grant in the offboarding ticket.
  3. Revoke after 30 days.
- [ ] Do not delete any files until the data retention period for the employee's role has been confirmed with Legal.
- [ ] For employees with access to Restricted data: notify IT Security so an access audit can be performed.

### Communication

- [ ] Set up an email auto-reply on the departing user's mailbox:
  > "Thank you for your message. [Name] is no longer with Company. For assistance, please contact [manager name] at [email]."
- [ ] Notify relevant team leads that the employee's access has been revoked.
- [ ] If the employee was a system owner or admin: ensure ownership is transferred to a current employee before the last day.

---

## Post-Departure

- [ ] 30 days after departure: disable email forwarding and auto-reply; archive the mailbox per retention policy.
- [ ] 90 days after departure: confirm all access has been fully removed (run quarterly access review report for this account).
- [ ] Close the offboarding ticket.

---

## Checklist Completion

All items must be checked and the ticket updated with:
- Date and time of Okta deactivation.
- Date hardware was returned (or expected return date).
- Name of IT staff who completed each section.
- Any exceptions or items pending (e.g., awaiting hardware return) with a follow-up date.

---

## Related Articles

- [Access Provisioning Runbook](access-provisioning-runbook.md)
- [Onboarding IT Checklist](onboarding-it-checklist.md)
- [Security Incident Response Runbook](security-incident-response-runbook.md)
- [Data Classification Policy](data-classification-policy.md)
