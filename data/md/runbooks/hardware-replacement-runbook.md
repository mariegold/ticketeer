# Hardware Replacement Runbook

## Overview

This runbook guides Desktop Support through replacing employee hardware — primarily laptops, but also peripherals (keyboards, mice, monitors, docking stations). It covers triage, spare stock management, data migration, and asset tracking.

## Prerequisites

- The replacement request must be submitted as a ticket (category: `hardware`).
- The defective device's asset tag must be recorded in the ticket.
- Check spare stock levels in the IT asset management system (AssetTiger) before promising a replacement timeline.

## Scope

| Device type | Covered by this runbook |
|---|---|
| Laptops (all models) | Yes |
| External monitors | Yes |
| Keyboards and mice | Yes |
| Docking stations | Yes |
| Mobile phones | No — contact HR/Finance |
| Printers | No — contact Network Ops |

## Procedure

### 1. Triage: repair vs. replace

Before committing to a full replacement, assess whether the device can be repaired:

**Replace immediately (no repair attempt):**
- Device will not power on and power adapter swap has been tried.
- Physical damage (cracked screen, liquid damage beyond keyboard spill).
- Device is more than 4 years old (past refresh cycle — see [Hardware Standards](hardware-standards.md)).
- Data from the device is inaccessible due to storage failure.

**Attempt repair first:**
- Single peripheral fault (keyboard, trackpad, battery) on a device under 4 years old.
- Software/firmware issue causing hardware-like symptoms.
- Minor issues (intermittent Wi-Fi, loose port) — schedule a depot appointment.

### 2. Check spare stock

Log into AssetTiger and filter by:
- *Status: Available*
- *Category: Laptop* (or relevant device type)
- *Location: IT Storeroom*

If no suitable spare is available:
- Check if a spare can be sourced from another office.
- If lead time will exceed 3 business days, notify the user and their manager.
- For critical roles (on-call engineers, executives), escalate to the IT manager for priority sourcing.

### 3. Data backup and migration

**If the device is functional enough to boot:**
1. Ask the user to log in and confirm their files are synced to OneDrive/Google Drive.
2. Verify that the following are cloud-backed: Documents, Desktop, Downloads folders.
3. Note any local applications that need reinstalling on the new device.
4. If any data is not cloud-backed, attach an external drive and manually copy it.

**If the device will not boot:**
1. Remove the SSD (if replaceable) and attach via USB enclosure to another machine.
2. Copy critical files from the user's home directory.
3. If the SSD is soldered or encrypted, attempt BitLocker/FileVault recovery:
   - Recovery key is stored in Azure AD (Windows) or Apple Business Manager (macOS).
4. If data recovery fails, inform the user and their manager before proceeding.

### 4. Prepare the replacement device

1. Retrieve the spare from the IT storeroom and record its asset tag.
2. Power on the device and confirm it reaches the login screen.
3. Enroll it in the MDM (Microsoft Intune for Windows, Jamf for macOS):
   - Intune: device self-enrolls on first Azure AD login.
   - Jamf: run `sudo jamf enroll` or use the enrollment URL.
4. Wait for MDM profiles and managed apps to install (typically 10–30 minutes).
5. Verify that corporate apps (Slack, Zoom, endpoint protection) are installed.

### 5. Hand over the replacement

1. Meet the user in person or ship the device using the IT courier account.
2. Have the user sign the Asset Handover Form (in the IT storeroom binder or DocuSign template).
3. Walk the user through logging in and verify they can access their cloud files.
4. Confirm VPN connectivity if the user is remote (see [VPN Troubleshooting Runbook](vpn-troubleshooting-runbook.md)).

### 6. Retire the defective device

1. Update AssetTiger: set the old device's status to *Defective — Pending Disposal*.
2. If under warranty, initiate a manufacturer warranty claim:
   - Dell: ProSupport portal
   - Apple: GSX or Apple Business Manager
   - Lenovo: Lenovo Partner Hub
3. If out of warranty and beyond repair, log it for the next e-waste collection run.
4. Before disposal: confirm the SSD has been wiped using NIST 800-88 guidelines (use DBAN or manufacturer secure-erase tool). Record the wipe completion in AssetTiger.

### 7. Close the ticket

- Set status to `resolved`.
- Resolution notes: old asset tag, new asset tag, data migration outcome, MDM enrolment confirmed Y/N.

## Typical Resolution Times

| Device type | Spare available | Spare not available |
|---|---|---|
| Laptop | 4–8 hours (same day) | 2–5 business days |
| Monitor | 1–2 hours | 1–3 business days |
| Keyboard/mouse | < 1 hour | Next delivery |
| Docking station | 1–2 hours | 1–3 business days |

## Escalation

| Situation | Escalate to |
|---|---|
| No spare available, critical user | IT Manager |
| Data recovery failure | IT Manager + inform user's manager |
| Device under active warranty dispute | Vendor account manager |
| Hardware failure affecting multiple devices (batch defect) | IT Manager + notify vendor |

## Related Articles

- [Hardware Standards](hardware-standards.md)
- [Hardware FAQ](hardware-faq.md)
- [Onboarding IT Checklist](onboarding-it-checklist.md)
