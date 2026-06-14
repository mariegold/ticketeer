# Hardware FAQ

## Laptops

**Q: My laptop will not turn on. What should I try before submitting a ticket?**
1. Hold the power button for 10 seconds to force a hard reset.
2. Try a different power cable or adapter if you have one available.
3. Connect the laptop to power and wait 5 minutes, then try again (battery may be completely flat).
4. If there are no lights, no fan, and no response after these steps, submit a `hardware` ticket — do not attempt to open the device yourself.

**Q: My laptop battery drains very fast. Is this a hardware fault?**
Battery degradation is normal over time. First, check battery health:
- **macOS:** Hold `Option`, click the Apple menu → *System Information → Power → Cycle Count*. A cycle count above 1000 indicates significant degradation.
- **Windows:** Run `powercfg /batteryreport` in Command Prompt. Review the *Design Capacity* vs *Full Charge Capacity* ratio.

If capacity is below 70% of original design, the battery qualifies for replacement under the hardware refresh policy. Submit a `hardware` ticket. If the battery is draining fast but health looks normal, check for runaway background processes.

**Q: When is my laptop due for a refresh?**
The hardware refresh cycle is 4 years from the issue date recorded in AssetTiger. You can check your device's issue date by submitting a ticket or checking with your IT contact. Laptops older than 4 years are automatically eligible for replacement. See [Hardware Standards](hardware-standards.md) for current standard models.

**Q: My laptop keyboard has a few stuck or broken keys. Can I get it repaired without a full replacement?**
Yes, if the device is under 4 years old. Submit a `hardware` ticket noting the specific keys affected and the laptop model. For unibody designs (most modern MacBooks and some ThinkPads), keyboard replacement may require sending the device in for a day — IT will provide a loaner if needed.

**Q: My laptop is running very slowly. Is this a hardware issue?**
Often not — slow performance is commonly caused by software (too many startup apps, full disk, browser with many tabs, pending OS updates). Try these before submitting a ticket:
1. Restart the laptop (if you have not in several days).
2. Check disk space: at least 15% free space is recommended.
3. Check Task Manager (Windows) or Activity Monitor (macOS) for processes consuming high CPU or RAM.
4. Run any pending OS updates.
If performance is still poor after these steps, submit a ticket — the device may need a RAM upgrade or SSD replacement.

---

## Monitors and Displays

**Q: My external monitor is not being detected.**
1. Try unplugging and replugging the cable at both ends.
2. If using a dock, try connecting the monitor directly to the laptop.
3. Try a different cable (DisplayPort, HDMI, or USB-C).
4. On macOS: *System Preferences → Displays → Detect Displays*.
5. On Windows: right-click desktop → *Display settings → Detect*.
6. Restart the laptop with the monitor connected.
If none of these work, the issue may be the cable, the dock, or the monitor's input board — submit a ticket.

**Q: My monitor has a flickering image. What causes this?**
Flickering is usually a cable issue or a refresh rate mismatch:
1. Try a different cable first.
2. Check the monitor's refresh rate: *Display Settings → Advanced display → Refresh rate*. Set it to the monitor's native rate (usually 60Hz or 144Hz).
3. If connected via HDMI, try DisplayPort instead — HDMI can be more sensitive to cable quality.
4. If the flickering is internal (visible even without a cable), the monitor's backlight or panel may be failing — submit a ticket.

**Q: Can I use two external monitors with my laptop?**
Most modern laptops support two external displays, but it depends on your docking station and GPU. Check the [Hardware Standards](hardware-standards.md) document for your model's display output limits. If you need a dual-monitor setup and your current dock does not support it, submit a ticket — IT may be able to provide a compatible dock.

---

## Docking Stations and Peripherals

**Q: My docking station is not charging my laptop.**
Charging via dock requires a USB-C dock that supports Power Delivery (PD). Check that:
1. The dock's power adapter is connected and the dock's power LED is on.
2. The USB-C cable between the dock and laptop is rated for PD (not all USB-C cables carry power).
3. The dock is compatible with your laptop model — check [Hardware Standards](hardware-standards.md).
If charging still does not work, submit a ticket.

**Q: My Bluetooth mouse/keyboard keeps disconnecting.**
1. Check the battery level first.
2. Move the device closer to the laptop — Bluetooth range is typically 10 metres but can be less in busy offices.
3. On macOS: remove the device from Bluetooth preferences and re-pair it.
4. On Windows: *Settings → Bluetooth → Remove device*, then pair again.
5. If it keeps disconnecting even when close, there may be radio interference from nearby devices — try switching the device to a 2.4GHz USB dongle instead if supported.

**Q: My headset microphone is not working in Zoom / Teams.**
1. Check that the headset is set as the default recording device:
   - **Windows:** Right-click the speaker icon → *Sound settings → Input → Choose your input device*.
   - **macOS:** *System Preferences → Sound → Input → select headset*.
2. Check in-app audio settings (Zoom/Teams both have their own input device selection).
3. If using a USB headset, try a different USB port.
4. Test the microphone in the OS's audio settings panel to confirm it is picking up sound.

---

## Reporting Hardware Issues

**Q: What information should I include in a hardware ticket?**
- The device type and model (e.g., "Dell XPS 15, 2023").
- The asset tag (a sticker usually on the bottom of the device).
- A clear description of the symptom and when it started.
- What you have already tried.
- Your location (for on-site support scheduling).
