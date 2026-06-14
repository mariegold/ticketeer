"""Static data: enums, weights, templates, slot values."""

from datetime import datetime

SEED = 123

CATEGORIES = ["access", "hardware", "software", "network", "account", "security"]

STATUSES = ["resolved", "open", "escalated"]
STATUS_WEIGHTS = [0.60, 0.25, 0.15]

USERS = [
    "j.doe", "a.smith", "m.jones", "l.patel", "r.chen",
    "k.wilson", "s.nguyen", "b.garcia", "c.taylor", "p.brown",
    "d.lee", "h.martin", "f.white", "n.clark", "e.harris",
    "t.lewis", "o.walker", "i.hall", "u.young", "g.allen",
]
# Weighted: a few repeat offenders
USER_WEIGHTS = [
    3, 2, 2, 1, 1,
    5, 1, 1, 2, 1,
    1, 3, 1, 1, 1,
    4, 1, 1, 1, 1,
]

TEAM_BY_CATEGORY: dict[str, list[tuple[str, float]]] = {
    "access":   [("Identity & Access", 0.80), ("IT Ops", 0.20)],
    "hardware": [("Desktop Support",   0.90), ("IT Ops", 0.10)],
    "software": [("Desktop Support",   0.60), ("IT Ops", 0.40)],
    "network":  [("Network Ops",       0.90), ("IT Ops", 0.10)],
    "account":  [("Identity & Access", 0.80), ("Security", 0.20)],
    "security": [("Security",          0.90), ("IT Ops", 0.10)],
}

RESOLUTION_TIME_RANGES: dict[str, tuple[float, float]] = {
    "access":   (1.0,  8.0),
    "hardware": (4.0, 72.0),
    "software": (0.5, 24.0),
    "network":  (0.5, 16.0),
    "account":  (0.5,  4.0),
    "security": (2.0, 48.0),
}

START_DATE = datetime(2025, 1, 6)   # first Monday of 2025
END_DATE   = datetime(2026, 6, 2)

TEMPLATES: dict[str, dict[str, list[str]]] = {
    "access": {
        "subjects": [
            "Cannot access {system} — permission denied",
            "Request for {system} access for new hire {user}",
            "{system} access revoked unexpectedly",
            "Need elevated permissions on {system}",
            "Shared drive {drive} inaccessible after role change",
            "SSO login fails for {system}",
            "Access request for contractor {user}",
        ],
        "descriptions": [
            "Hi team, I'm unable to log into {system}. I get a 'permission denied' error. "
            "My role is {role} and I need access to complete {task}. This started {time_ref}.",
            "We have a new hire {user} joining {team_name} on {date_ref}. "
            "Please provision access to {system} and {system2}. Their manager is {manager}.",
            "After my role changed from {role} to {role2}, my access to {system} was revoked. "
            "I still need it for {task}. Can you restore it?",
            "I need elevated read/write permissions on {system} to {task}. "
            "Currently I only have read access. Urgency: {urgency}.",
        ],
        "resolutions": [
            "Access granted to {system} after manager approval received via email.",
            "Provisioned {system} and {system2} for user {user}. Welcome email sent.",
            "Role permissions updated in Active Directory. Access to {system} restored.",
            "Elevated permissions applied in {system}. User confirmed access restored.",
        ],
    },
    "hardware": {
        "subjects": [
            "{device} not powering on",
            "Laptop {model} keyboard unresponsive",
            "Monitor flickering on {user}'s workstation",
            "Docking station not detected on {model}",
            "{device} running extremely slowly",
            "Headset microphone not working in {app}",
            "Battery draining fast on {model}",
        ],
        "descriptions": [
            "My {device} ({model}) stopped working {time_ref}. "
            "It won't power on at all — no lights, no fan. "
            "I've tried a different power cable. I need it for {task}.",
            "The keyboard on my {model} is unresponsive. Some keys work, others don't. "
            "I spilled {liquid} on it {time_ref} but it dried out. Asset tag: {asset_tag}.",
            "My external monitor has been flickering since {time_ref}. "
            "It's a {monitor_model}. I've tried different cables. "
            "It's affecting my ability to {task}.",
            "My {model} is extremely slow. Startup takes over {minutes} minutes. "
            "Running {os}. Haven't installed anything new recently.",
        ],
        "resolutions": [
            "Replaced power adapter. Device powers on normally.",
            "Issued replacement keyboard. Old unit sent for recycling.",
            "Replaced DisplayPort cable. Monitor stable — no further flickering.",
            "Replaced docking station unit. All peripherals detected correctly.",
            "Performed disk cleanup and disabled startup items. Boot time reduced to under 2 min.",
            "Dispatched replacement laptop. Data migrated from backup. Old unit returned.",
        ],
    },
    "software": {
        "subjects": [
            "{app} crashes on {os} after {event}",
            "Cannot launch {app} — {error_code} error",
            "{app} freezes when {action}",
            "Error {error_code} in {app} during {action}",
            "{app} update broke {feature}",
            "Cannot install {app} — installer exits silently",
            "{app} not syncing with {system}",
        ],
        "descriptions": [
            "Hi team, {app} has been crashing since {time_ref}. "
            "I'm on {os}, version {version}. It crashes when I try to {action}. "
            "Error message: '{error_code}'. This is blocking {task}.",
            "{app} won't open. I double-click the icon and nothing happens. "
            "I've tried restarting. Running {os}. Last update was {time_ref}.",
            "After the latest {app} update, {feature} stopped working. "
            "The update was pushed {time_ref}. I need {feature} for {task}.",
            "Getting error '{error_code}' in {app} whenever I try to {action}. "
            "Started after I upgraded to {os}. Happens every time without fail.",
        ],
        "resolutions": [
            "Cleared {app} cache and reinstalled version {version}. No further crashes.",
            "Rolled back {app} to previous version. {feature} works again. "
            "Escalated update regression to vendor.",
            "Updated {os} compatibility patch applied. Issue resolved.",
            "Registry entry conflict identified and removed. {app} launches correctly.",
            "Granted missing DLL dependency. {app} installs and runs normally.",
        ],
    },
    "network": {
        "subjects": [
            "No internet access on floor {floor}",
            "VPN disconnects every {minutes} minutes",
            "Slow network speeds in {location}",
            "Cannot reach {system} from office network",
            "WiFi drops intermittently on {model}",
            "DNS resolution failing for {domain}",
            "Network printer {printer} unreachable",
        ],
        "descriptions": [
            "We have no internet access on floor {floor} since {time_ref}. "
            "Affects {count} workstations. Switch in room {room} may be the issue.",
            "My VPN connection to {system} drops every {minutes} minutes. "
            "I'm on {os}, using the {vpn_client} client. "
            "Error: '{error_code}'. Working from {location}.",
            "Network speeds in {location} are terrible since {time_ref}. "
            "Speedtest shows {speed} Mbps download, expected {expected} Mbps. "
            "Affects {count} people in the area.",
            "Cannot reach {system} from inside the office network. "
            "Works fine on my phone (mobile data). DNS or firewall rule change?",
        ],
        "resolutions": [
            "Replaced faulty switch on floor {floor}. All workstations restored.",
            "Updated VPN client from {old_version} to {version}. Stable for 24h.",
            "Access point firmware updated and channel changed. Speeds back to normal.",
            "Firewall rule corrected by Network Ops. {system} reachable from office.",
            "DNS cache flushed on internal resolver. Resolution working correctly.",
        ],
    },
    "account": {
        "subjects": [
            "Locked out of {system} account",
            "Password reset not working for {system}",
            "MFA device lost — need re-enrollment",
            "Account disabled after inactivity",
            "Cannot update email in {system}",
            "Duplicate accounts merged incorrectly in {system}",
            "Account not created after onboarding",
        ],
        "descriptions": [
            "I'm locked out of my {system} account. "
            "I tried resetting my password but the email isn't arriving. "
            "My username is {user}. Need access urgently for {task}.",
            "My MFA authenticator app was on my lost phone. "
            "I need to re-enroll a new device. Please verify my identity via {method}.",
            "My {system} account was disabled. I was on leave for {days} days. "
            "I need it re-enabled to {task}.",
            "The email address on my {system} account is wrong — it shows {old_email} "
            "but should be {new_email}. Password resets are going to the wrong inbox.",
        ],
        "resolutions": [
            "Account unlocked and password reset link sent to backup email.",
            "MFA re-enrollment completed after identity verified via video call.",
            "Account re-enabled. Inactivity policy exception approved by manager.",
            "Email address updated in {system} by IAM team.",
            "Duplicate accounts merged correctly. User verified all data intact.",
        ],
    },
    "security": {
        "subjects": [
            "Suspicious login attempt on {user}'s account",
            "Phishing email received — possible credential compromise",
            "Ransomware alert on workstation {asset_tag}",
            "Unauthorised USB device detected on {system}",
            "Data exfiltration alert for {user}",
            "SSL certificate expired on {system}",
            "Failed brute-force attack on {system}",
        ],
        "descriptions": [
            "I received an alert that someone tried to log into my {system} account "
            "from {location} at {time_ref}. I did not initiate this. "
            "Please lock the account and investigate.",
            "I clicked a link in an email that looked like it came from {system}. "
            "I realised immediately it was phishing. I did not enter credentials. "
            "Please check my account for suspicious activity.",
            "Our EDR tool flagged workstation {asset_tag} ({user}) for ransomware-like "
            "behaviour at {time_ref}. Machine has been isolated. Awaiting guidance.",
            "DLP system detected a large upload ({size} MB) from {user}'s machine to "
            "an external {system} endpoint. Investigating whether this was authorised.",
        ],
        "resolutions": [
            "Account locked, session tokens invalidated. No evidence of successful breach. "
            "User enrolled in security awareness training.",
            "Phishing URL blocked at gateway. Account audit shows no credential use. "
            "Incident closed as contained.",
            "Workstation reimaged from clean snapshot. Files restored from backup. "
            "Root cause: malicious macro in email attachment.",
            "Upload confirmed as authorised by manager. DLP rule tuned to prevent "
            "false positive. Incident closed.",
            "Certificate renewed and deployed. Monitoring confirms no downtime impact.",
        ],
    },
}

SLOT_VALUES: dict[str, list[str]] = {
    "system":       ["Jira", "Confluence", "GitHub", "Okta", "Salesforce", "Workday",
                     "AWS Console", "Azure Portal", "Slack", "Zoom", "SharePoint", "Datadog"],
    "system2":      ["Confluence", "Slack", "Zoom", "GitHub", "Workday"],
    "app":          ["Outlook", "Teams", "Slack", "Chrome", "Zoom", "VS Code",
                     "Salesforce", "Jira", "Excel", "Photoshop"],
    "os":           ["Windows 11", "Windows 10", "macOS 14 Sonoma", "macOS 13 Ventura"],
    "device":       ["laptop", "desktop workstation", "docking station", "monitor"],
    "model":        ["Dell XPS 15", "MacBook Pro 14\"", "Lenovo ThinkPad X1", "HP EliteBook 840"],
    "monitor_model":["Dell U2722D", "LG 27UK850", "BenQ PD2700U"],
    "error_code":   ["0x80070002", "403 Forbidden", "SSL_ERROR_BAD_CERT",
                     "NTSTATUS 0xC000006D", "ERR_CONNECTION_REFUSED", "1603"],
    "event":        ["Windows update", "OS upgrade", "plugin install", "reboot"],
    "action":       ["opening a large file", "joining a meeting", "syncing data",
                     "running a report", "uploading attachments"],
    "feature":      ["single sign-on", "calendar sync", "dark mode", "spell check",
                     "auto-save", "notifications"],
    "version":      ["22.3.1", "4.18.0", "3.5.2", "2024.1", "10.2"],
    "old_version":  ["22.1.0", "4.16.2", "3.4.0"],
    "floor":        ["2", "3", "4", "5"],
    "location":     ["Building A", "Building B", "the open-plan area", "the boardroom",
                     "the satellite office", "home office"],
    "vpn_client":   ["GlobalProtect", "Cisco AnyConnect", "OpenVPN"],
    "domain":       ["internal.corp", "api.internal", "git.corp", "docs.internal"],
    "printer":      ["HP-LaserJet-3F", "Canon-MFP-2A", "Xerox-5B"],
    "room":         ["3C", "2B", "4A", "5D"],
    "count":        ["8", "12", "20", "35"],
    "speed":        ["5", "8", "12"],
    "expected":     ["100", "200", "500"],
    "minutes":      ["10", "15", "20", "30"],
    "liquid":       ["water", "coffee", "tea"],
    "asset_tag":    ["LGT-4412", "LGT-3381", "LGT-5507", "LGT-2290", "LGT-6634"],
    "role":         ["analyst", "developer", "manager", "contractor"],
    "role2":        ["senior analyst", "tech lead", "project manager"],
    "task":         ["complete the quarterly report", "onboard a new client",
                     "deploy the hotfix", "attend the all-hands", "finish the audit"],
    "urgency":      ["high — deadline today", "medium", "low — nice to have"],
    "team_name":    ["Engineering", "Sales", "Finance", "Operations", "HR"],
    "manager":      ["j.doe", "k.wilson", "a.smith"],
    "date_ref":     ["Monday", "next week", "2025-09-01"],
    "time_ref":     ["this morning", "yesterday", "two days ago", "last Friday",
                     "after the last update"],
    "user":         ["j.doe", "a.smith", "m.jones", "l.patel", "r.chen"],
    "drive":        ["Marketing-Shared", "Finance-Q2", "Projects-2025"],
    "days":         ["14", "21", "30"],
    "method":       ["video call", "manager confirmation", "employee ID"],
    "old_email":    ["old.name@company.com", "firstname@company.com"],
    "new_email":    ["correct.name@company.com", "updated@company.com"],
    "size":         ["450", "1200", "3400"],
}
