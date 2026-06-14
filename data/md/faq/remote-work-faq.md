# Remote Work FAQ

## Getting Set Up

**Q: What do I need to work from home effectively?**
You need:
- A company-issued laptop (personal devices are not supported for accessing internal systems).
- A stable internet connection — minimum 25 Mbps download, 10 Mbps upload recommended.
- The GlobalProtect VPN client installed (comes pre-installed on company laptops).
- Your Okta account with MFA configured on a personal device.

Optional but recommended:
- A wired Ethernet connection (more stable than Wi-Fi for video calls).
- A quality headset with a microphone (see [Hardware Standards](hardware-standards.md) for approved models).
- A secondary monitor (IT can provide one — submit a hardware request).

**Q: Does IT provide any equipment for home offices?**
Yes, within budget limits. You can request:
- An external monitor (one per employee).
- A keyboard and mouse.
- A USB hub or dock.
- A webcam (if your laptop lacks an adequate built-in camera).

Submit a `hardware` ticket with your home address for shipping. A manager approval may be required for high-value items.

**Q: My home Wi-Fi is slow. Will the company pay for an internet upgrade?**
There is a home internet stipend of $50/month for employees who are designated as fully remote. Contact HR to confirm your eligibility. IT does not directly manage home internet — contact your ISP for speed upgrades.

---

## VPN

**Q: Do I always need VPN when working remotely?**
VPN is required when accessing:
- Internal systems (Confluence, internal dashboards, code repositories on internal Git).
- Corporate email via a desktop client (browser access to Gmail/Outlook.com does not require VPN).
- Network file shares.

VPN is not required for:
- SaaS tools that use Okta SSO (Jira, Slack, Zoom, Salesforce) — these are accessible directly.

When in doubt, connect to VPN.

**Q: GlobalProtect says "Gateway not responding". What should I try?**
1. Check your internet connection first — open a browser and confirm you can reach a public site.
2. Check the [IT Status Page](https://status.internal) for any VPN outages.
3. Restart the GlobalProtect client (right-click the icon → Quit, then relaunch).
4. Restart your machine.
5. If none of these help, see the [VPN Troubleshooting Runbook](vpn-troubleshooting-runbook.md) or submit a ticket.

**Q: VPN is connected but I cannot reach internal sites.**
Your DNS may not be routing through VPN. Try:
```bash
nslookup confluence.internal
```
If the result is an external IP or NXDOMAIN, DNS is not working through VPN. Disconnect and reconnect VPN. If that does not help, submit a `network` ticket.

**Q: VPN disconnects me every 30 minutes. Is there a way to keep it connected?**
VPN sessions time out after 60 minutes of inactivity by default. If you are being disconnected more frequently, it may be a network issue on your end (see [VPN Troubleshooting Runbook](vpn-troubleshooting-runbook.md)). The session timeout cannot be extended beyond the security policy limit.

---

## Video Calls and Audio

**Q: My camera is not working in Zoom / Teams.**
1. Check that the app has camera permission: *System Preferences → Privacy & Security → Camera* (macOS) or *Settings → Privacy → Camera* (Windows).
2. Quit and relaunch the video app.
3. In Zoom/Teams settings, manually select your camera from the video device dropdown.
4. If using an external camera via a dock, try connecting it directly to the laptop's USB port.

**Q: There is an echo on my calls. Other people can hear themselves.**
Echo is caused by your microphone picking up your speakers. Solutions:
- Use a headset instead of laptop speakers.
- If using speakers, turn the volume down.
- In Zoom/Teams settings, enable *Background noise suppression* (set to high).
- Check that only one audio output device is active — multiple active outputs can cause feedback loops.

**Q: My internet is stable but video calls are choppy.**
Video calls are sensitive to latency and packet loss, not just bandwidth. Try:
1. Close other bandwidth-heavy applications (large file syncs, updates).
2. Use wired Ethernet instead of Wi-Fi.
3. In Zoom: enable *Low bandwidth mode* (*Settings → Video → HD* → off).
4. Ask other household members to reduce streaming during your call hours.

---

## Security

**Q: My family members use my home Wi-Fi. Is this a security issue?**
Your home Wi-Fi is untrusted from a corporate perspective — which is why VPN is required. As long as VPN is active, your corporate traffic is encrypted regardless of who else is on the network. As a best practice, keep your corporate device on a separate SSID (guest network) from household devices.

**Q: Can I print work documents at home?**
You can print to a personal printer, but be mindful of document sensitivity. Documents classified as Confidential or above should not be printed at home unless you have a secure shredding arrangement. See the [Data Classification Policy](data-classification-policy.md).

**Q: I left my work laptop unattended at a café. Should I report it?**
If it was unlocked and unattended: yes, report it to IT Security. Someone may have had physical access to it. IT will check the device logs remotely and may ask you to bring it in for inspection. If it was locked (screen lock active), the risk is lower, but still worth mentioning if you were away for more than a few minutes.
