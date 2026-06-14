# Access & Permissions FAQ

## General

**Q: How do I request access to a new system?**
Submit a ticket with category `access`. Include the system name, the level of access you need (read or read/write), and the business reason. Your manager will be contacted for approval. Most access requests are fulfilled within one business day.

**Q: How long does access provisioning take?**
Standard access to Okta-managed systems (Jira, Confluence, Slack, GitHub, etc.) is typically granted within 4 hours during business hours. Systems that require manual provisioning (legacy internal tools, some vendor portals) may take up to 2 business days.

**Q: Do I need manager approval for every access request?**
Yes. All access grants require written manager approval on record. For contractor access, the sponsoring employee's manager must approve. Admin or elevated permissions additionally require approval from the IT Security team.

**Q: I was just promoted / changed roles. Will my access update automatically?**
No. Role changes in Workday do not automatically update system permissions. You need to submit an access ticket referencing your new role. Your manager should also submit any access removal requests for systems you no longer need.

**Q: Can I request access on behalf of someone else?**
Yes, but the approval chain must still be complete. Submit the ticket from your own account but clearly state you are requesting on behalf of the other person. Their manager must still approve.

---

## Specific Systems

**Q: How do I get access to the AWS Console?**
Submit an `access` ticket specifying: the AWS account name, the IAM role you need (e.g., ReadOnly, Developer, Admin), and the business justification. AWS Console access requires IT Security approval in addition to manager approval. Allow 1–2 business days.

**Q: I need access to a Salesforce sandbox for testing. Is this different from production access?**
Yes. Sandbox access follows the same approval process but is typically granted faster and with broader permissions. Clearly note "sandbox only" in your request. Production Salesforce access requires additional Salesforce Admin review.

**Q: How do I get access to a shared mailbox or distribution list?**
Submit a ticket specifying the shared mailbox address and whether you need send-as or send-on-behalf permissions. The owner of the mailbox (usually a team manager) will be asked to approve.

**Q: A colleague is leaving and I need to inherit their file access. How does this work?**
Do not ask the leaving employee to share files directly with you — this will be revoked during offboarding anyway. Submit an access ticket explaining the business need. IT will work with the relevant data owner to grant you appropriate access after verifying with your manager.

---

## Troubleshooting

**Q: My access worked yesterday but now I'm getting "permission denied". What happened?**
A few common causes:
1. Your Okta session expired — try logging out and back in.
2. Your group membership was changed as part of a scheduled access review.
3. The system had a permission misconfiguration that was corrected.
Submit an `access` ticket and IT can check the audit log to identify the change.

**Q: I can see a folder in SharePoint but cannot open any files. Why?**
You likely have "can view" access to the folder but not to the files inside, which may inherit different permissions. Submit a ticket specifying the exact folder path and the files you need to access.

**Q: My SSO login to a third-party tool keeps failing even though I have access in Okta.**
First, try clearing your browser cookies and cache for that site. If it still fails, check whether the tool requires a specific browser (some older integrations do not support Firefox). If the issue persists, submit a ticket — the SAML assertion configuration between Okta and the tool may need adjustment.

**Q: I have admin access to a system but a specific admin feature says I don't have permission.**
Some systems have granular sub-permissions within the admin role. Submit a ticket describing exactly which feature you need — IT will check whether a specific permission group needs to be assigned.

---

## Access Reviews

**Q: I received an email asking me to review my team's access. What is this?**
IT runs quarterly access reviews where managers are asked to confirm or revoke their team's access to sensitive systems. Please respond promptly — accounts not reviewed within the deadline will be suspended until the review is complete.

**Q: Someone on my team no longer needs access to a system. How do I revoke it?**
Submit an `access` ticket with the person's name, the system, and a note that access should be removed. You can also use the quarterly access review process. Do not ask the user themselves to delete their own account — this is handled by IT.
