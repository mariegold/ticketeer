# Password Reset and MFA Recovery Runbook

## Overview

This runbook covers resetting passwords and recovering MFA (multi-factor authentication) access for employees who are locked out of their accounts. It applies to Okta-managed accounts, which serve as the identity provider for all SaaS systems including Jira, Confluence, GitHub, Slack, Salesforce, and the AWS Console.

> **Important:** Always verify the requester's identity before performing any reset. Account takeover via social engineering is a real threat vector.

## Prerequisites

- The reset request must come through a ticket (category: `account`) or an in-person visit to the IT desk with a valid employee ID.
- For remote requests, identity verification is required before proceeding (see Step 1).

## Procedure

### 1. Verify identity

**In-person:** Check the employee's photo ID badge. If the badge photo does not match the person, do not proceed — escalate to Security.

**Remote (video call):**
1. Join a video call with the employee.
2. Ask them to hold their photo ID badge up to the camera.
3. Cross-reference with their Workday profile photo.
4. If there is any doubt, escalate to the employee's manager for confirmation.

**Remote (ticket-only — lower-risk scenarios):**
Acceptable only if:
- The request comes from a ticket created while the user was still authenticated (i.e., they have a locked account, not a compromised one), AND
- The reset is for a non-privileged account.

Otherwise, require video verification.

### 2. Password reset

#### Self-service (preferred — no IT action needed)

Direct the user to the self-service reset page first:
1. Go to `https://company.okta.com`.
2. Click *Forgot password?*
3. Enter their username (`firstname.lastname`).
4. Choose *Send email* — a reset link goes to their registered backup email.

If the user has lost access to their backup email too, proceed to the manual reset below.

#### Manual reset via Okta Admin Console

1. Log into the Okta Admin Console (`admin.okta.com`).
2. Navigate to *Directory → People*.
3. Search for the user by name or username.
4. Click the user's name → *More Actions → Reset Password*.
5. Select *Send email* to send a reset link to their backup email, OR select *Set password* to set a temporary password directly (use only when backup email is also inaccessible).
6. If setting a temporary password, communicate it to the user over a secure channel (Signal, in-person) — never over email or Slack.
7. Check *User must change password on next login*.

### 3. Unlock a locked account

Accounts lock after **10 failed login attempts**. If the password is correct but the account is locked:

1. In Okta Admin Console → *Directory → People* → find the user.
2. Check their status — it will show *Locked Out*.
3. Click *Unlock* — the user can log in immediately with their existing password.
4. Advise the user to check their keyboard's Caps Lock and verify they are using their current password.

### 4. MFA recovery

MFA recovery is required when an employee loses or replaces their authenticator device.

#### Step A — Confirm it is not a device configuration issue

Ask the user:
- Did they recently get a new phone?
- Did they reinstall their authenticator app?
- Are their phone's date/time set to *automatic*? (Wrong time causes TOTP codes to fail.)

If the time is wrong: fixing it resolves the issue without a full reset.

#### Step B — Reset MFA factor via Okta

1. Okta Admin Console → *Directory → People* → find the user.
2. Click the user → *More Actions → Reset Multifactor*.
3. Select which factors to reset (Okta Verify, Google Authenticator, SMS, etc.).
4. Click *Reset Selected Factors*.
5. The user will be prompted to re-enroll on next login.

#### Step C — Guide re-enrollment

1. User logs in with their password at `company.okta.com`.
2. Okta prompts them to set up a new factor.
3. Recommend **Okta Verify** (app-based) over SMS for security.
4. For Okta Verify: user scans the QR code with their new device.
5. Confirm the user can complete a full login with the new factor.

### 5. Resolve ticket

- Mark the ticket `resolved`.
- Note in the resolution field: what was reset, how identity was verified, and the date.

## Verification

Have the user:
1. Log into `company.okta.com` with their new credentials.
2. Access one downstream app (e.g., open Jira or Slack via SSO).
3. Confirm all their apps and data are intact.

## Escalation

| Situation | Escalate to |
|---|---|
| Cannot verify identity remotely | Employee's manager + IT Security |
| User suspects account compromise | IT Security immediately (do not reset — preserve forensics) |
| Backup email also compromised | IT Security |
| Executive or admin account | IT Security required for dual approval |

## Related Articles

- [MFA Policy](mfa-policy.md)
- [Account Management FAQ](account-management-faq.md)
- [Security Incident Response Runbook](security-incident-response-runbook.md)
