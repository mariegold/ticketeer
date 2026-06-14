# Access Provisioning Runbook

## Overview

This runbook covers the end-to-end process for granting system access to employees. It applies to new hire provisioning, role-change access updates, and contractor onboarding. Follow these steps in order to ensure consistent, auditable access grants.

## Prerequisites

- The access request must be submitted via a ticket (category: `access`) or through the IT portal.
- Manager approval must be on record before any access is granted. For contractor access, the sponsoring employee's manager must approve.
- The requester's identity must be verifiable in Workday (for employees) or the vendor management system (for contractors).

## Procedure

### 1. Validate the request

Open the submitted ticket and confirm:
- The requester's username exists in Active Directory.
- The requested system is listed in the [Approved Software List](approved-software-list.md).
- Manager approval is attached (email forward or ticket comment from manager's account).
- If the request is for elevated/admin permissions, a second approval from the IT Security team is required.

### 2. Determine the access level

Check the system's access matrix (maintained in Confluence under *IT / Access Control Matrices*):
- **Read** — view-only; appropriate for cross-team collaborators and auditors.
- **Read/Write** — standard for active contributors.
- **Admin** — restricted to team leads and IT staff; requires dual approval.

If the requested level is not in the matrix, default to Read and escalate the exception to the Identity & Access team.

### 3. Create or update the account

**For SaaS systems (Okta-managed):**
1. Log into the Okta Admin Console.
2. Navigate to *Directory → People*, search for the user.
3. Under *Applications*, click *Assign Applications* and select the target app.
4. Set the role/group as determined in step 2.
5. Click *Save*.

**For self-managed systems (GitHub, AWS, internal tools):**
1. Follow the system-specific provisioning guide linked from the Confluence access matrix.
2. Add the user to the appropriate group/role.
3. Confirm via the system's audit log that the change took effect.

**For shared drive access (SharePoint / Google Drive):**
1. Navigate to the drive or folder.
2. Click *Share* → *Manage access*.
3. Add the user's email and set the appropriate permission level.
4. Uncheck *Notify people* if the ticket already covered communication.

### 4. Update Active Directory group membership (if applicable)

Some systems rely on AD group membership synced via Okta. If the system uses AD groups:
1. Open *Active Directory Users and Computers*.
2. Locate the target group (naming convention: `APP-{SystemName}-{Role}`).
3. Add the user's AD account to the group.
4. Allow up to 15 minutes for Okta sync.

### 5. Notify the user

Reply to the original ticket with:
- Confirmation of what access was granted.
- Login URL and any first-login instructions.
- Link to the relevant user guide or onboarding doc.
- Ticket resolution status set to `resolved`.

### 6. Document the change

Log the change in the Access Grant Register (Confluence: *IT / Access Grant Register*):
- Date, ticket ID, system, user, access level, approver name.

## Verification

Ask the user to confirm they can log in and reach the intended resources. If they report issues within 24 hours, re-open the ticket and troubleshoot before closing.

## Escalation

| Situation | Escalate to |
|---|---|
| Manager approval cannot be confirmed | Identity & Access team lead |
| System not in Okta or access matrix | IT Security |
| Admin/elevated access request | IT Security (dual approval) |
| User account missing from Active Directory | IT Ops (directory sync issue) |

## Related Articles

- [MFA Policy](mfa-policy.md)
- [Onboarding IT Checklist](onboarding-it-checklist.md)
- [Offboarding IT Checklist](offboarding-it-checklist.md)
- [Approved Software List](approved-software-list.md)
