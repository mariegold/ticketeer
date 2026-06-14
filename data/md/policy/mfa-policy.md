# Multi-Factor Authentication (MFA) Policy

## Purpose

This policy establishes the requirements for multi-factor authentication (MFA) across all company systems. MFA significantly reduces the risk of account compromise — even if a password is stolen or guessed, a second factor prevents unauthorised access.

## Scope

This policy applies to all employees, contractors, and third-party users who access company systems. There are no exceptions for seniority or role.

## MFA Requirements

### Mandatory systems (MFA always required)

MFA must be configured and active for:
- Okta (company identity provider — this covers all SSO-integrated apps)
- AWS Console and AWS CLI
- GitHub (all organisations under `github.com/company`)
- Google Workspace Admin Console
- Cloudflare
- Any system with access to production infrastructure or sensitive customer data

### Encouraged but not yet mandatory

- Jira and Confluence (covered by Okta SSO — MFA at the Okta level is sufficient)
- Slack (Okta SSO)
- Zoom (Okta SSO)

---

## Approved MFA Methods

Methods are listed in order of preference. Use the highest-ranked method you can.

| Rank | Method | Notes |
|---|---|---|
| 1 | **Hardware security key (YubiKey 5 series)** | Phishing-resistant. Issued on request — see below. |
| 2 | **Okta Verify (push notification)** | Approved authenticator app. Easy to use and phishing-resistant when combined with number matching. |
| 3 | **TOTP authenticator app** | Google Authenticator, Authy, 1Password TOTP. Acceptable but more susceptible to real-time phishing than push. |
| 4 | **SMS one-time code** | Backup method only. SIM-swap risk makes this unsuitable as a primary factor. |

**Not approved:**
- Email OTP (too easily compromised if email is compromised)
- Security questions
- "Remember this device for 30 days" without a registered second factor

---

## YubiKey Issuance

Hardware keys are available to all employees on request. To request one:
1. Submit an `account` ticket with subject "YubiKey request".
2. IT will issue a YubiKey 5C NFC (USB-C + NFC) or YubiKey 5 NFC (USB-A + NFC) depending on your laptop model.
3. IT will register the key to your Okta account during a brief setup session (in-person or video call).

**Loss or damage:** Report immediately to IT Security. The lost key will be deactivated. Replacements have a $30 fee (waived for first occurrence).

---

## Enrollment and Setup

### Enrolling Okta Verify

1. Go to `company.okta.com` and log in with your password.
2. Navigate to *Settings → Security Methods*.
3. Click *Set up* next to *Okta Verify*.
4. Download the Okta Verify app on your phone (iOS or Android).
5. Scan the QR code shown on screen.
6. Approve a test push notification to confirm setup.

### Enrolling a TOTP app

1. In Okta settings → *Security Methods → Set up* next to *Google Authenticator*.
2. Open your TOTP app and scan the QR code.
3. Enter the 6-digit code to confirm.

### Enrolling a YubiKey

Contact IT to complete this setup — YubiKey registration requires the key to be physically present at time of enrollment.

---

## Recovery

If you lose access to your MFA device:
1. Call the IT helpdesk or submit a ticket immediately.
2. IT will verify your identity before resetting any factor (see [Password Reset Runbook](password-reset-runbook.md)).
3. Do not attempt to bypass MFA by sharing credentials with a colleague.

Backup codes are available in Okta for some account types. These are one-time use and should be stored securely (e.g., in your approved password manager or a physical safe). Do not store them in an unencrypted file on your laptop.

---

## Policy Enforcement

- MFA is enforced at the Okta level via sign-on policies. Accounts without MFA configured will be blocked from logging in after the grace period has expired.
- New employees must configure MFA within 3 business days of their start date.
- Contractors must configure MFA before their first day of access.
- Compliance is monitored monthly. Accounts without a registered MFA factor will be flagged and their managers notified.

---

## Related Articles

- [Password Reset Runbook](password-reset-runbook.md)
- [Account Management FAQ](account-management-faq.md)
- [Security Awareness FAQ](security-awareness-faq.md)
- [Security Incident Response Runbook](security-incident-response-runbook.md)
