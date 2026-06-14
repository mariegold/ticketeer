# Hardware Standards

## Purpose

This document defines the standard hardware configurations approved for company use. IT procures, configures, and supports only the models listed here. Non-standard hardware may not be supported and cannot be connected to the corporate network without prior approval.

Last reviewed: 2026-04-15

---

## Standard Laptop Models

All laptops are configured with the company MDM profile (Microsoft Intune for Windows, Jamf for macOS) before issue.

### Primary — Engineering and Technical Roles

| Model | CPU | RAM | Storage | Display | OS |
|---|---|---|---|---|---|
| **Apple MacBook Pro 14" (M4 Pro)** | Apple M4 Pro | 24 GB | 512 GB SSD | 14.2" Liquid Retina XDR | macOS Sequoia |
| **Apple MacBook Pro 16" (M4 Max)** | Apple M4 Max | 36 GB | 1 TB SSD | 16.2" Liquid Retina XDR | macOS Sequoia |
| **Dell XPS 15 (9530)** | Intel Core Ultra 7 | 32 GB | 1 TB NVMe SSD | 15.6" OLED Touch | Windows 11 Pro |

### Standard — Office and Business Roles

| Model | CPU | RAM | Storage | Display | OS |
|---|---|---|---|---|---|
| **Apple MacBook Air 13" (M4)** | Apple M4 | 16 GB | 256 GB SSD | 13.6" Liquid Retina | macOS Sequoia |
| **Lenovo ThinkPad X1 Carbon (Gen 12)** | Intel Core Ultra 5 | 16 GB | 512 GB SSD | 14" IPS | Windows 11 Pro |
| **HP EliteBook 840 G11** | Intel Core Ultra 5 | 16 GB | 512 GB SSD | 14" IPS | Windows 11 Pro |

### Role-Based Upgrades

| Role | Default upgrade |
|---|---|
| Data Science / ML | MacBook Pro 16" M4 Max with 48 GB RAM |
| Video/Design (Creative team) | MacBook Pro 16" M4 Max + external GPU where applicable |
| Executive | MacBook Pro 14" M4 Pro (preferred) or Dell XPS 15 |

---

## Hardware Refresh Cycle

| Device type | Refresh interval |
|---|---|
| Laptops | 4 years from issue date |
| Monitors | 5 years |
| Peripherals (keyboard, mouse) | 3 years or on failure |
| Docking stations | 4 years |

Devices past their refresh date are eligible for replacement regardless of condition. Devices can be replaced earlier if:
- Repaired twice within 12 months.
- Hardware fault prevents normal use and repair is not cost-effective.
- Business need requires a capability not available in the current device (e.g., a role change requiring Apple Silicon for on-device ML).

---

## Standard Peripherals

### Monitors

| Model | Size | Resolution | Connection |
|---|---|---|---|
| **Dell U2724D** | 27" | 2560 × 1440 (QHD) | USB-C / DisplayPort |
| **LG 27UK850-W** | 27" | 3840 × 2160 (4K) | USB-C / HDMI / DisplayPort |
| **BenQ PD2725U** | 27" | 3840 × 2160 (4K) | USB-C / Thunderbolt |

All standard monitors support USB-C with Power Delivery for single-cable laptop connections.

### Docking Stations

| Model | Compatible with | Ports |
|---|---|---|
| **CalDigit TS4 (Thunderbolt 4)** | MacBook Pro/Air | 3× USB-A, 5× USB-C/TB4, SD card, 2× display |
| **Dell WD22TB4 (Thunderbolt 4)** | Dell XPS, ThinkPad | 4× USB-A, 3× USB-C, HDMI, 2× DisplayPort |
| **Plugable UD-4VPD (USB-C)** | HP EliteBook | 4× USB-A, 2× USB-C, 2× HDMI, SD card |

### Keyboards and Mice

| Item | Model | Notes |
|---|---|---|
| Keyboard (standard) | Logitech MX Keys | Bluetooth + USB-C; Windows and macOS layout |
| Keyboard (mechanical) | Keychron K3 Pro | Available on request; brown switches default |
| Mouse | Logitech MX Master 3S | Bluetooth; ergonomic |
| Mouse (vertical) | Logitech MX Vertical | Available on ergonomic/RSI request |

### Headsets

| Model | Type | Best for |
|---|---|---|
| **Jabra Evolve2 55** | Wireless over-ear | Open offices, heavy call usage |
| **Sony WH-1000XM5** | Wireless over-ear, ANC | Noisy environments |
| **Jabra Evolve2 30** | Wired USB | Budget option; reliable for calls |
| **Apple AirPods Pro (2nd gen)** | In-ear, wireless | Available for eligible roles (Engineering, Sales) |

---

## Non-Standard Hardware

Hardware not on this list (including personal devices, gaming peripherals, or items purchased without IT approval) is not supported and may not be connected to the corporate network. To request approval for non-standard hardware, submit a `hardware` ticket with the justification and a link to the product specs.

---

## Related Articles

- [Hardware Replacement Runbook](hardware-replacement-runbook.md)
- [Hardware FAQ](hardware-faq.md)
- [Onboarding IT Checklist](onboarding-it-checklist.md)
