# Security Awareness FAQ

## Phishing and Suspicious Emails

**Q: How do I know if an email is a phishing attempt?**
Common signs:
- **Urgency or pressure:** "Act now or your account will be closed."
- **Unexpected sender:** An email claiming to be from IT, HR, or a vendor but coming from an unusual address (e.g., `it-support@company-helpdesk.net` instead of `@company.com`).
- **Mismatched links:** Hover over links before clicking. If the URL shown at the bottom of your browser does not match where you'd expect to go, do not click.
- **Generic greetings:** "Dear user" instead of your name.
- **Requests for credentials, MFA codes, or wire transfers** — legitimate internal systems will never ask for these via email.

**Q: I received a suspicious email. What should I do?**
1. Do **not** click any links or download attachments.
2. Do **not** reply to the sender.
3. Forward the email as an attachment to `security@company.com` (do not just forward normally — that may strip headers). In Outlook: *More → Forward as attachment*.
4. Delete the email from your inbox.
5. If you accidentally clicked a link, report it immediately — even if you did not enter any credentials.

**Q: I think I clicked a phishing link. Am I in trouble?**
You will not be penalised for reporting promptly. What matters is that we can contain the risk quickly. Contact IT Security immediately at `security@company.com` or call the helpdesk. Tell them exactly what you clicked and what the page looked like. Time matters — the sooner we know, the faster we can act.

**Q: I received a password reset email that I did not request. What should I do?**
Do not click the link. Report it to `security@company.com`. Someone may have your email address and is attempting a password reset. IT will check whether any login attempts were made against your account.

**Q: I got a call from someone claiming to be IT asking for my password. Is this legitimate?**
No. IT will **never** ask for your password, MFA code, or session token over the phone or email. If you receive such a call, hang up and report it to `security@company.com` with the caller's number and the time of the call. This is a social engineering (vishing) attempt.

---

## Safe Browsing and Device Use

**Q: Can I use my work laptop for personal browsing?**
Occasional personal use is tolerated, but your browsing activity on corporate devices is monitored and logged. Avoid sites that would be inappropriate in a workplace context. Do not use your work laptop as your primary personal device.

**Q: Is it safe to use public Wi-Fi for work?**
Only if you are connected to VPN. Public Wi-Fi (cafes, hotels, airports) is untrusted and your traffic can be intercepted. Always connect to VPN before accessing internal systems or corporate email. See [Remote Work FAQ](remote-work-faq.md) for setup guidance.

**Q: Can I plug a USB drive into my work laptop?**
USB storage is monitored and restricted by policy. Approved USB devices (company-issued encrypted drives) are allowed. Personal USB drives are blocked by the endpoint security tool. If you have a legitimate business need to use a USB drive, submit a ticket and IT Security can approve a specific device.

**Q: A website is asking me to install a browser extension. Should I do it?**
Only install browser extensions that are on the approved list. Malicious browser extensions are a common attack vector — they can read your cookies, intercept passwords, and exfiltrate data. If you need a specific extension for work, submit a software approval request.

---

## Passwords and Credentials

**Q: Is it okay to share my password with a colleague to help them with a task?**
Never. Sharing credentials is a policy violation and means accountability for any actions taken under your account is lost. If a colleague needs access, submit an access request. If a task requires your credentials specifically, there is an architectural problem — contact IT to find a proper solution.

**Q: I noticed my password appeared in a data breach notification. What should I do?**
Change your corporate Okta password immediately and submit a ticket. Check whether you used the same password anywhere else — if so, change those too. Reusing corporate passwords for personal accounts is a significant risk.

**Q: My manager asked for my credentials to fix something on my account. Should I give them?**
No. Managers do not need your credentials and should not be asking for them. If something needs to be fixed on your account, IT can do it directly without your password. Report this to `security@company.com` — even if it was innocent, it is a security awareness gap.

---

## Data Handling

**Q: Can I email work documents to my personal email to work from home?**
This is not the recommended approach and may trigger a DLP (data loss prevention) alert. Instead, use company-approved cloud storage (OneDrive, Google Drive) and access documents from there, or use the VPN to access internal systems. If you have a specific exception case, discuss it with your manager and IT Security.

**Q: I accidentally sent an email with sensitive data to the wrong person. What do I do?**
Act immediately:
1. In Outlook or Gmail, use the *Recall* feature if available (works within a few minutes if the recipient has not opened it).
2. Contact the recipient directly and ask them to delete it.
3. Report the incident to IT Security — depending on the data type, there may be a legal notification obligation.
Do not wait to see if the recipient noticed — report it regardless.
