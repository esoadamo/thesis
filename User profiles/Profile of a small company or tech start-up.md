- digicomp level 6, because of service company [[Digital competence]]/[[@STEINLECHNER20211185]]
## Profile description
- [x] 20 employees
- [x] hybrid working in co-working center
- [x] MacBooks and iPhones are company-provided
- [x] Windows Laptop as a server
  - [x] Hyper-V virtual machines with shared SSH Linux accounts and RDP Windows accounts
- [x] need to access internal network
  - [ ] OpenVPN on a virtual Linux machine with static password, with dynamic IP
- [x] have a file on Google Drive with shareds passwords
- [x] self-hosted Jenkins
  - [x] no login needed for LAN network
- [x] using custom DNS `xxxx.company.internal` with custom CA
- [x] code stored on public GitLab
- [x] larger files shared through USB
## Problems with current approach
- [x] Laptop with classical Windows OS is not suitable for multi-user server usage
- [x] shared SSH accounts and RDP accounts may lead to harder decommissioning of leaving employees
- [x] OpenVPN does not support MFA
- [x] Jenkins is not protected with Zero Trust in mind
- [x] having to include custom CA into all their devices
- [x] needs to use their own DNS, otherwise internal company will not resolve
- [x] USB destroyed or leaked
## Already solved problems
- [x] password sharing
- [x] versioning code
## Needs not covered
- [x] scalable VM/VPS managment
- [x] sharing secrets securely
- [x] least-privilege separation between users
- [x] secure file sharing for data loss prevention