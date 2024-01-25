- digicomp level 6, because of service company [[Digital competence]]/[[@STEINLECHNER20211185]]
## Profile description
- 20 employees
- hybrid working in co-working center
- MacBooks and iPhones are company-provided
- Windows Laptop as a server
  - Hyper-V virtual machines with shared SSH Linux accounts and RDP Windows accounts
- need to access internal network
  - OpenVPN on a virtual Linux machine with static password, with dynamic IP
- have a file on Google Drive with shareds passwords
- self-hosted Jenkins
  - no login needed for LAN network
- using custom DNS `xxxx.company.internal` with custom CA
- code stored on public GitLab
- larger files shared through USB
## Problems with current approach
- Laptop with classical Windows OS is not suitable for multi-user server usage
- shared SSH accounts and RDP accounts may lead to harder decommissioning of leaving employees
- OpenVPN does not support MFA
- Jenkins is not protected with Zero Trust in mind
- having to include custom CA into all their devices
- needs to use their own DNS, otherwise internal company will not resolve
## Already solved problems
- password sharing
- versioning code
## Needs not covered
- scalable VM/VPS managment
- sharing secrets securely
- least-privilege separation between users
- secure file sharing for data loss prevention