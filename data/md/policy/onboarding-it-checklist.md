# IT Onboarding Checklist

## Purpose

This checklist covers everything IT needs to set up for a new employee before and during their first week. It is used by IT staff processing onboarding requests and can also be shared with new hires so they know what to expect.

---

## Before Day 1 (IT Actions)

These tasks should be completed at least 2 business days before the employee's start date. HR must submit the onboarding request in the IT portal with: full name, username, job title, department, manager, start date, and laptop preference.

### Account Creation

- [ ] Create Active Directory account (`firstname.lastname`).
- [ ] Create Okta account and assign to the employee's department group.
- [ ] Set initial password and flag for reset on first login.
- [ ] Assign to correct Okta groups (grants access to core apps: Jira, Confluence, Slack, Zoom, Workday).
- [ ] Create corporate email address (`firstname.lastname@company.com`).
- [ ] Add to distribution lists relevant to the department.
- [ ] Create GitHub account or invite to org (if technical role).
- [ ] Provision role-specific systems (Salesforce for Sales, AWS for Engineering, etc.) — see manager's access request.

### Hardware

- [ ] Retrieve or order the standard laptop for the role (see [Hardware Standards](hardware-standards.md)).
- [ ] Enroll the device in MDM (Intune for Windows, Jamf for macOS).
- [ ] Confirm MDM profiles have applied and corporate apps are installed.
- [ ] Prepare any requested peripherals (monitor, keyboard, mouse, headset, dock).
- [ ] Label device with IT asset tag and record in AssetTiger (new asset entry).
- [ ] Prepare shipping label if the employee is remote.

---

## Day 1 — New Hire Experience

### If in-office

1. IT desk appointment (schedule 30 minutes).
2. Hand over the laptop and peripherals. Employee signs the Asset Handover Form.
3. Walk through first-login: AD password change → Okta setup → MFA enrollment.
4. Confirm the employee can log into Slack, Jira, and their email.
5. Provide the IT self-service portal URL and helpdesk contact.

### If remote

1. Device shipped to home address — confirm delivery before start date.
2. Send a Day 1 IT welcome email to the employee's personal email (pre-configured, not yet logged into corporate email):
   - Corporate email address and username.
   - Link to `company.okta.com` for first login.
   - Instructions for MFA setup.
   - IT helpdesk contact.
3. Schedule a 20-minute video call to verify setup and answer questions.

---

## Week 1 Checklist (New Hire Self-Service)

Share this section with the new hire:

- [ ] Change your initial password at `company.okta.com` → *Settings → Change Password*.
- [ ] Set up MFA using Okta Verify on your phone (see [MFA Policy](mfa-policy.md)).
- [ ] Log into Slack — introduce yourself in `#general`.
- [ ] Log into Jira and Confluence — confirm you can access your team's project space.
- [ ] Open the Software Center (Windows) / Managed Software Center (macOS) and install any role-specific tools.
- [ ] Review the [Approved Software List](approved-software-list.md) before installing any additional applications.
- [ ] Read the [Data Classification Policy](data-classification-policy.md) and [Security Awareness FAQ](security-awareness-faq.md).
- [ ] Complete the IT Security awareness training module (link sent via email in week 1).
- [ ] Test VPN: connect to GlobalProtect and confirm you can reach `confluence.internal`.

---

## Access Provisioning Reference

Standard access granted to all new employees via Okta group membership:

| System | Access level | How |
|---|---|---|
| Jira | Developer (can create and edit tickets in assigned projects) | Okta group |
| Confluence | Editor (all company spaces) | Okta group |
| Slack | Member | Okta group |
| Zoom | Licensed (up to 300 participants per meeting) | Okta group |
| Google Workspace | Full access (Drive, Docs, Sheets, etc.) | Okta group |
| Workday | Employee self-service | Okta group |

Role-specific access (AWS, GitHub orgs, Salesforce, Datadog, etc.) is granted separately based on the manager's access request submitted during onboarding.

---

## IT Contacts

| Need | Contact |
|---|---|
| Urgent setup issue on Day 1 | IT helpdesk: `it@company.com` or `ext. 100` |
| Hardware issue | Desktop Support: `desktop@company.com` |
| Security question | IT Security: `security@company.com` |
| General questions | IT portal: `help.internal` |

---

## Related Articles

- [Access Provisioning Runbook](access-provisioning-runbook.md)
- [Hardware Standards](hardware-standards.md)
- [MFA Policy](mfa-policy.md)
- [Offboarding IT Checklist](offboarding-it-checklist.md)
