# Approved Software List

## Purpose

This document lists software approved for installation on company-managed devices. Installing unapproved software is a policy violation and may trigger an endpoint security alert. If you need software not on this list, follow the request process at the bottom of this document.

Last reviewed: 2026-05-01

---

## Productivity and Collaboration

| Application | Windows | macOS | Notes |
|---|---|---|---|
| Microsoft 365 (Word, Excel, PowerPoint, Outlook) | ✅ | ✅ | Installed via MDM |
| Slack | ✅ | ✅ | Installed via MDM |
| Zoom | ✅ | ✅ | Installed via MDM |
| Google Chrome | ✅ | ✅ | Preferred browser |
| Mozilla Firefox | ✅ | ✅ | |
| Notion | ✅ | ✅ | Approved for personal notes; not for sensitive data |
| Loom | ✅ | ✅ | Screen recording for async comms |
| Miro | ✅ (web) | ✅ (web) | Browser-based only; no desktop app needed |

---

## Development Tools

| Application | Windows | macOS | Notes |
|---|---|---|---|
| Visual Studio Code | ✅ | ✅ | Installed via Software Center |
| JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.) | ✅ | ✅ | Licence managed via JetBrains Toolbox |
| Git | ✅ | ✅ | Git for Windows / Xcode CLT on macOS |
| Docker Desktop | ✅ | ✅ | Personal licence; IT manages company licence for CI |
| Postman | ✅ | ✅ | |
| Insomnia | ✅ | ✅ | Alternative to Postman |
| iTerm2 | ❌ | ✅ | macOS only |
| Windows Terminal | ✅ | ❌ | Windows only |
| WSL 2 (Windows Subsystem for Linux) | ✅ | ❌ | Ubuntu 22.04 recommended |
| Homebrew | ❌ | ✅ | macOS only; do not use to install unapproved apps |
| Python (3.10+) | ✅ | ✅ | Install via python.org or Homebrew/winget |
| Node.js (LTS) | ✅ | ✅ | Use nvm or fnm for version management |

---

## Security Tools

| Application | Windows | macOS | Notes |
|---|---|---|---|
| CrowdStrike Falcon | ✅ | ✅ | Mandatory EDR — do not disable |
| GlobalProtect VPN | ✅ | ✅ | Mandatory; installed via MDM |
| Okta Verify | ✅ | ✅ | Required for MFA |
| 1Password (business) | ✅ | ✅ | Company-managed password manager |
| Bitwarden | ✅ | ✅ | Approved alternative to 1Password |
| YubiKey Manager | ✅ | ✅ | For YubiKey configuration only |

---

## Design and Creative

| Application | Windows | macOS | Notes |
|---|---|---|---|
| Figma | ✅ (web) | ✅ | Desktop app also available |
| Adobe Creative Cloud | ✅ | ✅ | Requires a company-assigned licence — submit a ticket |
| Canva | ✅ (web) | ✅ (web) | Do not upload confidential data |

---

## Communication and Video

| Application | Windows | macOS | Notes |
|---|---|---|---|
| Slack | ✅ | ✅ | Primary messaging platform |
| Microsoft Teams | ✅ | ✅ | For external calls with Microsoft-ecosystem clients |
| Zoom | ✅ | ✅ | Primary video conferencing |
| Krisp | ✅ | ✅ | Noise cancellation — approved plugin |

---

## Not Approved (examples)

The following are explicitly **not approved** and will be blocked by endpoint security:

- BitTorrent clients or peer-to-peer file sharing applications.
- Remote desktop tools not managed by IT (AnyDesk personal, TeamViewer personal, Chrome Remote Desktop).
- Cryptocurrency mining software.
- Personal VPN clients (Mullvad, NordVPN, etc.) — use GlobalProtect only.
- Unapproved AI tools that upload company data to third-party servers — check with IT Security before using any AI coding assistant or similar tool.

---

## Requesting New Software

To request approval for software not on this list:

1. Submit a `software` ticket with the subject "Software approval request: [App Name]".
2. Include:
   - The application name and version.
   - The business justification (what problem it solves, who needs it).
   - A link to the vendor's privacy policy and data processing terms.
   - Whether a free tier is available or a licence purchase is needed.
3. IT Security will review the request within 5 business days.
4. If approved, the software will be added to the Software Center for self-service installation.

**Note:** Using software while its approval request is pending is not permitted.
