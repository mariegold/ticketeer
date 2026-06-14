# Software Issues FAQ

## Installation and Updates

**Q: How do I install a new application?**
Check the [Approved Software List](approved-software-list.md) first. If the software is approved, install it via the Software Center (Windows) or Managed Software Center (macOS) — no ticket needed. If it is not on the list, submit a `software` ticket requesting approval. Unapproved software cannot be installed on corporate devices without IT sign-off.

**Q: A software update is available but I cannot install it — I get an "administrator required" error.**
Most approved software updates are pushed automatically by MDM within 48 hours of release. If you need the update immediately, submit a `software` ticket and IT can trigger a remote push. Do not attempt to use workarounds to bypass admin restrictions.

**Q: Software Center is empty / not loading.**
This usually means your device has lost contact with the MDM server. Try:
1. Restart the device.
2. Connect to the corporate network or VPN.
3. Open Software Center again — it may take a few minutes to sync.
If it remains empty after 30 minutes, submit a ticket.

**Q: Can I install personal software on my work laptop?**
Personal software is not permitted on corporate devices unless it appears on the approved list. This policy exists to protect the company from malware and licence violations. If you have a legitimate use case, submit a software approval request.

---

## Crashes and Freezes

**Q: My application keeps crashing. What information should I include in a ticket?**
Please include:
- The application name and version number (usually found in *Help → About*).
- Your OS version.
- What you were doing when it crashed.
- Any error message or error code displayed.
- Whether it happens every time or intermittently.
- When it started — did it coincide with an update or OS change?

**Q: Outlook crashes every time I try to open an attachment.**
This is often caused by a corrupt Outlook profile or a conflict with a third-party add-in. Try:
1. Start Outlook in safe mode: hold `Ctrl` while clicking the Outlook icon (Windows).
2. If it works in safe mode, disable add-ins one by one (*File → Options → Add-ins → Manage COM Add-ins*).
3. If safe mode also crashes, your profile may be corrupt — submit a ticket for IT to rebuild it.

**Q: Microsoft Teams freezes when I join a meeting. My colleagues can hear me but I see a blank screen.**
Clear the Teams cache:
1. Quit Teams completely (check the system tray).
2. Delete the contents of `%appdata%\Microsoft\Teams` (Windows) or `~/Library/Application Support/Microsoft/Teams` (macOS).
3. Restart Teams.
If the issue persists, update Teams and your video driver.

**Q: My browser crashes on specific websites only.**
This is usually a browser extension conflict or a WebGL/hardware acceleration issue:
1. Try the site in a private/incognito window with extensions disabled.
2. If it works there, disable extensions one by one to find the culprit.
3. If it still fails, disable hardware acceleration: *Settings → Advanced → System → Use hardware acceleration when available* → off.

---

## Licence and Activation

**Q: I'm getting a "licence expired" error in Adobe Creative Cloud.**
Adobe licences are managed centrally. This usually means your licence was not renewed in time or your account was not included in the renewal. Submit a `software` ticket and IT will re-assign a licence within one business day.

**Q: Office apps say "Product deactivated". How do I fix this?**
1. Open any Office app, go to *File → Account*.
2. If you see *Sign in* or a red banner, sign in with your corporate email (`firstname.lastname@company.com`).
3. If you are already signed in and still see the error, sign out and back in.
4. If the issue persists, the licence may not be assigned to your account — submit a ticket.

---

## Compatibility and Configuration

**Q: An app works on my old laptop but not on my new one.**
The new device may be on a newer OS version that the app does not support. Check the app vendor's system requirements. If the app is approved and supported, submit a ticket and IT will investigate (driver conflicts, missing redistributables, etc.).

**Q: I upgraded to macOS Sonoma and now [app] won't open.**
Some apps have not yet been updated for the latest macOS. Check the vendor's release notes. IT can also check whether a compatible version is available. In the meantime, you may be able to run the app via Rosetta 2 (for Intel apps on Apple Silicon).

**Q: My PDF viewer is not the default on Windows. Every PDF opens in Edge.**
Right-click a PDF file → *Open with → Choose another app* → select your preferred viewer → check *Always use this app*. If you need Adobe Acrobat set as default across all corporate devices, submit a ticket.
