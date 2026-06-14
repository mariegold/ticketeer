# VPN Troubleshooting Runbook

## Overview

This runbook helps IT support staff diagnose and resolve VPN connectivity issues reported by employees working remotely or connecting to internal systems from outside the office network. The company uses **GlobalProtect** as the primary VPN client and **Cisco AnyConnect** as a legacy backup for specific teams.

## Prerequisites

- Confirm the user's OS version and VPN client version before starting.
- Check the [IT Status Page](https://status.internal) for any active VPN infrastructure incidents before troubleshooting individual clients.
- Have the user open a terminal (macOS/Linux) or PowerShell (Windows) to run diagnostic commands.

## Common Symptoms and Causes

| Symptom | Likely cause |
|---|---|
| Cannot connect at all | Wrong gateway address, firewall blocking port 443/UDP 4501 |
| Connects but drops every 10–20 min | Split-tunnel misconfiguration, ISP throttling UDP |
| Connects but cannot reach internal resources | DNS not routing through VPN, incorrect split-tunnel routes |
| Authentication loop / login keeps failing | Expired Okta session, MFA device change, account locked |
| "Gateway not responding" error | VPN gateway overload or maintenance window |

## Procedure

### 1. Confirm infrastructure health

Before touching the client, check:
1. Open the IT Status Page and confirm no active VPN incidents.
2. Ping the VPN gateway from the NOC: `ping gp-gateway.internal.corp`
3. If the gateway is unreachable from inside, escalate immediately to Network Ops — do not continue troubleshooting the client.

### 2. Collect client diagnostics

Ask the user to run:

**GlobalProtect (macOS/Linux):**
```bash
/Applications/GlobalProtect.app/Contents/Resources/gp-diagnostics.sh
```
The report saves to `~/Desktop/GPdiagnostics.txt`. Ask the user to attach it to the ticket.

**GlobalProtect (Windows):**
1. Right-click the GlobalProtect icon in the system tray.
2. Select *Collect Logs*.
3. Submit the `.zip` file from `C:\Users\<user>\AppData\Local\Palo Alto Networks\GlobalProtect\`.

**Cisco AnyConnect:**
```
Start → Cisco AnyConnect Secure Mobility Client → Diagnostics → Export
```

### 3. Check client version

Minimum supported versions:
- GlobalProtect: **6.2.x** or later
- Cisco AnyConnect: **4.10.x** or later

If the user is on an older version:
1. Direct them to the Software Center (Windows) or Managed Software Center (macOS).
2. Install the latest version.
3. Restart the machine and retry connection.

### 4. Verify gateway and portal address

The correct settings are:
- **Portal:** `vpn.company.com`
- **Gateway:** auto-selected (do not override manually unless instructed)

If the user has manually entered a gateway, clear it and let the portal auto-discover.

### 5. Troubleshoot authentication failures

If the user reaches the login screen but cannot authenticate:
1. Confirm the username format is `firstname.lastname` (not email address).
2. Have the user log into `okta.company.com` in a browser — if that also fails, the issue is account-level, not VPN. Open an `account` ticket.
3. If Okta login works but VPN does not, the SAML assertion may be cached incorrectly. Ask the user to:
   - Sign out of GlobalProtect completely.
   - Clear the browser cache for `okta.company.com`.
   - Reconnect.

### 6. Fix intermittent disconnects

If the VPN connects but drops periodically:
1. Check if the user is on Wi-Fi. Switch to Ethernet if possible.
2. Ask the user's ISP or router model — some consumer routers aggressively time out UDP sessions. Switching the VPN transport to TCP can help:
   - In GlobalProtect preferences, set *Preferred Mode* to **SSL/TLS (TCP)**.
3. If on a corporate network (office visiting another site), check for double-NAT or port filtering with Network Ops.

### 7. DNS not resolving internal hostnames

Symptom: VPN is connected (green icon) but `git.corp` or `confluence.internal` don't load.

1. Ask the user to run: `nslookup git.corp` — expected result is an internal IP in `10.x.x.x` range.
2. If the DNS response is an external IP or NXDOMAIN, the VPN DNS push is not working.
3. Collect the GlobalProtect logs and escalate to Network Ops with the ticket.

## Verification

Ask the user to:
1. Connect to VPN and confirm the icon shows **Connected**.
2. Open a browser and navigate to `confluence.internal` — should load without errors.
3. If they reported a specific internal service failing, test that service explicitly.

## Escalation

| Situation | Escalate to |
|---|---|
| VPN gateway unreachable from NOC | Network Ops (P1 if affects multiple users) |
| Authentication failures after client fix | Identity & Access team |
| Persistent DNS issues after client fix | Network Ops |
| VPN works but specific app unreachable | App owner team + Network Ops |

## Related Articles

- [Remote Work FAQ](remote-work-faq.md)
- [Network Outage Runbook](network-outage-runbook.md)
- [MFA Policy](mfa-policy.md)
