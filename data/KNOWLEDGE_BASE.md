# Knowledge Base Dataset

18 synthetic IT support articles across three categories, written by Claude to cover the same domain as the ticket data.

## Structure

| Directory | Files | Content |
|---|---|---|
| `faq/` | 6 | Q&A articles for common issues (access, accounts, hardware, software, security, remote work) |
| `policy/` | 6 | Internal IT policies (MFA, data classification, approved software, hardware standards, on/offboarding) |
| `runbooks/` | 6 | Step-by-step procedures (access provisioning, password reset, VPN troubleshooting, network outage, hardware replacement, security incident response) |

## Generation

Articles were prompted individually with a description of the IT helpdesk context and the target topic. Each article follows a consistent structure: a short intro, section headings, and concrete steps or rules. No post-processing was applied.

Topics were chosen to complement the ticket categories (`access`, `hardware`, `software`, `network`, `account`, `security`) so that realistic queries have matching knowledge_base content.
