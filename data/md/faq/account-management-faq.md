# Account Management FAQ

## Passwords

**Q: How do I change my password?**
Go to `company.okta.com`, click your name in the top-right corner → *Settings → Change Password*. Your new password must be at least 14 characters and include uppercase, lowercase, a number, and a special character. Passwords cannot be reused within the last 12 months.

**Q: How often do I need to change my password?**
The current policy requires a password change every 180 days. You will receive email reminders at 30, 14, and 3 days before expiry. If your password expires, you will be prompted to change it on your next login to Okta.

**Q: I forgot my password and cannot log in. What do I do?**
Go to `company.okta.com` and click *Forgot password?*. Enter your username and follow the instructions sent to your backup email address. If you do not have access to your backup email, submit a ticket or call the IT helpdesk. Do not ask a colleague to log in on your behalf.

**Q: My password reset email is not arriving.**
Check your spam/junk folder first. If it is not there, the backup email on your account may be outdated. Contact IT via phone or in person — we cannot verify your identity over email in this situation.

**Q: Can I use a password manager?**
Yes, and we encourage it. Approved password managers are listed in the [Approved Software List](approved-software-list.md). Do not store your corporate Okta password in a personal/unapproved password manager.

---

## Account Lockouts

**Q: My account is locked. What should I do?**
Accounts lock after 10 consecutive failed login attempts. Wait 15 minutes and try again — accounts auto-unlock after a short cooldown. If you cannot wait, submit a ticket or call the helpdesk and IT can unlock it immediately after verifying your identity.

**Q: Why was my account locked? I haven't been trying to log in.**
This could indicate someone else is attempting to access your account. Contact IT Security immediately. Do not wait — an account being repeatedly locked without your knowledge is a potential sign of a brute-force or credential-stuffing attack.

**Q: My account was disabled after I returned from extended leave. What do I do?**
Accounts inactive for more than 90 days are automatically disabled as a security measure. Submit an `account` ticket and have your manager confirm you are returning. IT will re-enable your account within one business day.

---

## MFA

**Q: I got a new phone. How do I transfer my MFA?**
Do not simply restore from a phone backup — authenticator app secrets may not transfer correctly. Before wiping your old phone:
1. Log into `company.okta.com`.
2. Go to *Settings → Security Methods*.
3. Add the new device using *Set up* next to Okta Verify.
4. Scan the QR code with your new phone.
5. Verify it works, then remove the old device.

If your old phone is already gone, submit a ticket for an MFA reset (see [Password Reset Runbook](password-reset-runbook.md)).

**Q: My MFA codes keep saying "incorrect" even though they look right.**
TOTP codes (the 6-digit rotating codes) are time-based. If your phone's clock is even slightly off, codes will fail. Go to your phone's date/time settings and ensure *Set automatically* is enabled. This resolves the issue in most cases.

**Q: Can I use SMS for MFA instead of an authenticator app?**
SMS MFA is available as a backup method but is not recommended as your primary factor. SIM-swapping attacks make SMS less secure. Please use Okta Verify or a hardware key (YubiKey) as your primary MFA method. See the [MFA Policy](mfa-policy.md) for full details.

**Q: I lost my YubiKey. What do I do?**
Report it immediately to IT Security — treat a lost YubiKey like a lost house key. IT will deactivate it and issue a replacement. There is a $30 replacement fee for lost keys (waived for the first occurrence). Do not attempt to use another person's YubiKey.

---

## Username and Profile

**Q: I changed my legal name. How do I update it in company systems?**
Name changes are initiated through HR in Workday. Once processed in Workday, IT will update your Active Directory account and email address. This typically propagates to downstream systems (Okta, Slack, Jira) within 24 hours. Submit a ticket if anything does not update after 48 hours.

**Q: My username is different from the format firstname.lastname — can it be changed?**
Usernames are standardised as `firstname.lastname`. If yours does not match this format (e.g., due to a legacy account or name change), submit a ticket. Changing a username affects email delivery and SSO sessions, so IT will coordinate a maintenance window.

**Q: I have two accounts in Jira / Confluence. Which one should I use?**
Use the account linked to your corporate email (`firstname.lastname@company.com`). If you have a legacy account, submit a ticket to have them merged — IT will migrate your content to the primary account and deactivate the duplicate.
