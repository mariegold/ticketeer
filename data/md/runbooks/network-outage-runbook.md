# Network Outage Runbook

## Overview

This runbook guides IT support and Network Ops through diagnosing and resolving network outages — from a single user's connectivity loss to a floor-wide or building-wide incident. It covers wired and wireless networks, internal DNS, and ISP-level failures.

## Scope

| Issue type | Owner |
|---|---|
| User's device cannot connect to Wi-Fi | Desktop Support (initial triage) |
| Wi-Fi down for a group of users | Network Ops |
| Wired network/switch failure | Network Ops |
| Internal DNS failure | Network Ops |
| ISP/WAN link failure | Network Ops + ISP escalation |
| VPN issues | See [VPN Troubleshooting Runbook](vpn-troubleshooting-runbook.md) |

## Procedure

### 1. Scope the outage

The first task is to determine how many users are affected and where.

**Single user:**
- Start at the device level (Section 2).
- Likely cause: device configuration, driver, or user-specific VLAN assignment.

**Multiple users on the same floor / room:**
- Skip to Section 3 (switch/AP investigation).
- Likely cause: access point failure, switch port/VLAN issue, DHCP exhaustion.

**Entire building / multiple floors:**
- Skip to Section 4 (core infrastructure).
- Likely cause: core switch failure, uplink failure, ISP outage.

**Multiple sites:**
- Escalate immediately to Network Ops lead and check the ISP status page.
- Likely cause: WAN link failure, BGP route issue, upstream ISP incident.

### 2. Single-user device triage

1. Ask the user to check their physical connection:
   - **Wi-Fi:** Is the Wi-Fi adapter enabled? Is the SSID `CorpNet` (not a guest network)?
   - **Wired:** Is the Ethernet cable seated? Is the LED on the switch port lit?

2. Run a basic connectivity check:
   ```bash
   ping 8.8.8.8          # test internet
   ping 10.0.0.1         # test default gateway
   nslookup confluence.internal   # test internal DNS
   ```

3. If the gateway ping fails: the issue is local (device or switch port). Try a different port or cable.

4. If the gateway ping succeeds but internet fails: DNS or routing issue. Try:
   ```bash
   nslookup google.com 8.8.8.8    # test with external DNS
   ```
   If this resolves: internal DNS is broken (escalate to Network Ops).
   If this also fails: ISP/routing issue (escalate to Network Ops).

5. Check for IP address conflicts:
   - Windows: `ipconfig /all` — look for `169.254.x.x` (APIPA) indicating DHCP failure.
   - macOS/Linux: `ip addr` or `ifconfig`.
   - If APIPA: release and renew (`ipconfig /release && ipconfig /renew` on Windows, or disconnect/reconnect on macOS).

6. Update or roll back the network driver if all else fails at the device level.

### 3. Access point / switch investigation

For multi-user outages on the same floor or room:

1. Identify the affected access point or switch:
   - Check the network topology map in NetBox (`netbox.internal`).
   - Cross-reference the physical room with the switch closet serving it.

2. SSH into the suspect switch:
   ```
   ssh admin@<switch-ip>
   show interfaces status         # look for err-disabled or down ports
   show spanning-tree             # check for STP loops
   show log last 50               # review recent error messages
   ```

3. For access point issues:
   - Log into the Wi-Fi controller (Cisco WLC or Meraki Dashboard).
   - Check AP status: is it online? What is the client count?
   - If the AP shows *Disconnected*: check the PoE port on the switch (PoE budget may be exceeded).

4. Common switch fixes:
   - **Err-disabled port:** `interface <port>; shutdown; no shutdown`
   - **DHCP exhaustion:** check DHCP pool utilisation in the DHCP server; expand pool or clear stale leases.
   - **STP loop:** identify the offending port from the spanning-tree log and disable it.

5. If the switch itself is unresponsive: check physical power, console in via serial if needed, or replace the unit if hardware failure is confirmed.

### 4. Core infrastructure and ISP escalation

For building-wide or multi-site outages:

1. Check the core router/firewall (Cisco ASA or Palo Alto):
   - Is the management interface reachable?
   - Review BGP peer state: `show bgp summary`
   - Check WAN interface status: `show interface <wan-if>`

2. Check the ISP's status page and contact their NOC:
   - Provider A (primary): `1-800-xxx-xxxx` — reference account number in the IT run book (physical binder in server room).
   - Provider B (failover): failover should be automatic via BGP; if not, contact Network Ops lead.

3. If the WAN link is down and failover has not triggered:
   - Manually adjust BGP local preference to shift traffic to the standby link.
   - Document the change and set a reminder to revert once the primary is restored.

4. Communicate the outage:
   - Post in `#it-status` Slack channel with: time started, scope, current status, ETA.
   - Update the IT Status Page.
   - For outages > 30 minutes, notify affected team leads.

### 5. Resolution and post-incident

1. Confirm connectivity is restored for all affected users before closing the ticket.
2. Update the IT Status Page to *Resolved* with a brief summary.
3. Post a closing message in `#it-status`.
4. For outages > 1 hour or affecting > 20 users: write a brief incident summary (cause, duration, resolution, prevention steps) and file in the Jira Network Ops project.

## Escalation

| Situation | Escalate to |
|---|---|
| Multi-floor outage | Network Ops on-call immediately |
| Core switch or router failure | Network Ops lead + IT Manager |
| ISP WAN link down | ISP NOC + Network Ops lead |
| Security-related network anomaly | IT Security |

## Related Articles

- [VPN Troubleshooting Runbook](vpn-troubleshooting-runbook.md)
- [Remote Work FAQ](remote-work-faq.md)
