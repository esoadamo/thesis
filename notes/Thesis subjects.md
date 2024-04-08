[[notes/thesis]]
## Favorite subject

- intrusion detection
  
  - [NEMEA](https://github.com/CESNET/Nemea)?
  - detection of possibly bad behavior and informs home users

- smaller low-budget scale-institutions/individuals

- integration of existing systems

- usable security
  
  - check-list for common users with stories

- network probes - SNORT
  
  ## Topics

- home security?
  
  - ESP32 that looks through the network and reports problems?
    - maybe a Pi Zero for more powerfull OPs?
  - something like [Turris](https://www.turris.com/en/) but not a router, just a separated device?
  - detects outdated IoT devices?
    - cheap IP cameras, ....

- phantom version app migration?

- home network intrusion detection?

- on-prem security?
  
  - scanning/evaluation
    - Wazuh
  - many amateur/junior programmers will buy VPS but do not known how to properly secure it

## Meeting

- was security increased with client isolation/wpa3
  - / analysis in SOHO
    - home routers are unable to analyse all the traffic
    - DNS, ...
  - where does normal person store its cloud data in a cloud
  - analysis of (home) networks
- TikTok & FB & SnapChat & Ashley Madison & analysis of its data
  - methodoly design (from simmilar analysis of the same kind)
  - use tools to go through the methodology
  - MiMT
- Zero Trust in small-network design
  - House NAS
  - With help of agents - *"Will this help home users?"*
  - CloudFlare Zero-Trust solution for personal free
  - *"How can Cloudflare help home networks"*
- SaaS for SOHO
  - What solutions are on marked & compare them
    - price, quality, scope
    - mails, antiviturs, EDR, tablets, LDAP, SSO....
  - Can work with different scenarios
    - student with one laptop
    - family with 4 computers
    - small company with 20 employees

## TODO

- research till week & quick update
  - articles, thesis, (blogs.)
- have more info till two weeks

## Resources

- [Cloudflare Zero Trust](https://www.cloudflare.com/zero-trust/)
  - [What Is Zero Trust](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/)
- [Auth0 | The OpenID Connect Handbook](https://auth0.com/resources/ebooks/the-openid-connect-handbook#!)
- [The Hidden Dangers of Public Wi-Fi](https://thehackernews.com/2023/08/the-hidden-dangers-of-public-wi-fi.html)
  - seems more like and ad for SafeDNS
- [Securing Your Legacy: Identities, Data, and Processes](https://www.darkreading.com/vulnerabilities-threats/securing-your-legacy-identities-data-and-processes)
- [Why Legacy System Users Prioritize Uptime Over Security](https://www.darkreading.com/edge/why-legacy-system-users-prioritize-uptime-over-security)
  - more business-oriented
- [Tuya Smart and Amazon Web Services Collaborate to Establish an IoT Security Lab](https://www.darkreading.com/ics-ot/tuya-smart-and-amazon-web-services-collaborate-to-establish-an-iot-security-lab)
- [Considerations for Reducing Risk When Migrating to the Cloud](https://www.darkreading.com/google-cloud-security/considerations-for-reducing-risk-when-migrating-to-the-cloud)
  - Google-cloud related
- [Disposed-of Gadgets Can Lead to Wi-Fi Network Hacks, Kaspersky Says](https://www.darkreading.com/vulnerabilities-threats/disposed-of-gadgets-can-lead-to-wi-fi-network-hacks-kaspersky-says)
  - [Wi-Fi hacking in recycled printers, computers and smart-home equipment | Kaspersky official blog](https://www.kaspersky.com/blog/wifi-protection-for-gadget-disposal/48774/)
  - [Smart device vulnerabilities and securing against them | Kaspersky official blog](https://www.kaspersky.com/blog/how-to-secure-smart-home/47472/)
- [Review on Wireless Security Protocols (WEP, WPA, WPA2 & WPA3)](https://d1wqtxts1xzle7.cloudfront.net/65316864/CSEIT1953127-libre.pdf?1609578021=&response-content-disposition=inline%3B+filename%3DReview_on_Wireless_Security_Protocols_WE.pdf&Expires=1694013751&Signature=aAgbr4sVUeTO27N1DJi7cX6wCYXE4Et~sB6a7DIS39TWnXL-DUo0C7n5Ra-YkfrfpybFz2uvGuErDuJpj4Jy2khI-l6zX1CjI2681RdEduf1LxqahmqbCdxcBhn5hxSTYmsHSRAk7dqmSH-MeWlhDH0Soc~gUVYKqc5YjYgi76RtOlJnmgtrnTE9qLlkVh7g6uepMxMI5IjvSqp69kd4AvxaJ-ydY4S8KjXwpncfCLLEyFDaKPzcdWY6nCui1tDMrhvAfl6BEpgkh4MKy3RjVIStPsIF6yPiG44EexUuRuOV4rECfXnf9WENcs0Lwz4JY9g7fixB8c99vP-m6VkHBA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
  - forward secrecy
- [Wireless LAN Security in a SOHO Environment: A Holistic Approach - Christian Wimmer - Knihy Google](https://books.google.cz/books?hl=cs&lr=&id=okttAQAAQBAJ&oi=fnd&pg=PA2&dq=soho+security&ots=rdUAcBtGcf&sig=Xbj7isPzduA0H3thdunO9wAyVOY&redir_esc=y#v=onepage&q=soho%20security&f=false)
  - behind paywall
- [[Insecurity by Obscurity: A Review of SoHo Router Literature from a Network Security Perspective](https://commons.erau.edu/cgi/viewcontent.cgi?article=1060&context=jdfsl)](https://commons.erau.edu/jdfsl/vol4/iss3/1/)
  - talks about how manuals are confusing for average users
- [Securing Home Wi-Fi with WPA3 Personal](https://ieeexplore.ieee.org/abstract/document/9369629)
  - [WPA3 | TP-Link](https://www.tp-link.com/us/wpa3/)

## Meeting 2

- shared mailboxes
- big focus on identity managment
  - Home Assistant, wifi for children only
  - Synology LDAP
- password managers, shared passwords
- what areas are people using? What do users need?
  - it student vs art student
  - need shared storage, office software
  - people are afraid -> antivirus (EDR)
  - console showing the healt of devices
    - licenses & scaling
- IM sources: **Cloudflare, 365, Google, Synology (is on-prem)**
  - TrueNAS (custom solution, smaller focus)
  - my implementation? As Docker container?
  - Avast, Mega, Dropbox do that too or not?
  - GitLab has SSO? vs Gitea
- knowledge base & processes records
- every group puts focus on different areas with different priorities
- **TODO**: go trough what microsoft offers & what cloudflare offers
- do we still need VPN? guest accounts? guest wifis? + privacy consideration
- spam & mailbox protection
  - custom domain with mail
  - Microsoft payed, Cloudflare; Seznam free; Protonmail; DDG Privacy mail?
- show antipaters
  - refuse to update
  - personal vs service account
  - what if device is lost
    - files backup & disc encryption
      - Uložto storage & Mega & OneDrive & Google Drive
        - can it do SAML
  - zero trust chapter?
- cloud bank accounting 
- automation
  - https://www.make.com/en
  - IFTT
  - zappier
  - idoklad
  - IM in state services & Bank Id
- how to keep software updated
  - WinRar
  - unsupported software - Office 10
- **take a look at what services are offered -> to be analyzed**
- **best security guidelines for SoHo**
- **revide old SoHo reccomendatation**
- till two weeks again