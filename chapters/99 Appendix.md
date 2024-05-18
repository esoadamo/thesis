## Profile data collecting
`TEX:\label{pt:partCounts}`

During the writing of this thesis, I have sent the following questions to students (n=5) of non-it universities:

- Do you consciously back up your photos/videos?
- Do you consciously back up documents/school notes?
- Do you use a password manager? For example, Apple KeyChain?
- Do you use email on your iPhone? Possibly through their Mail app or some other app?
- Do you use some form of multi-level login/MFA/PassKeys?
- Do you use the iCloud app for Windows? Possibly for what?

Next, I performed a discussion about password practices with (n=27) high-school students and high-school teachers (n=33), with questions such as:

- Do you have more than three complex passwords that you remember?
- Do you use passphrases instead of passwords?
- Do you use a password manager?
- Did you ever used some form of password-less login?

With students (n=27), I have also performed a discussion about data retention, backups and privacy with instant messaging applications:

- Do you know how to back up data?
- Do you use some form of backup?
- Have you ever heard of or used cloud storage?
- Do you know what a NAS device or Synology is?
- Which messaging applications do you use?
- Could you order them in terms of privacy?
- Do you know what E2EE is?
- Which of these applications utilize E2EE?

## Author's solution

To stress why selecting a simple-to-manage solution from the beginning is essential, I am including the approach and history of what solution I implement. This solution is currently far from perfect, and as such can show how technical debt can be quickly created when learning to achieve hosting goals on the go.

I started self-hosting stored files using a dedicated Windows XP device with Windows folder sharing. My initial reasoning for self-hosting most of the software was the cost of cloud storage, though now the privacy aspect has already surpassed it. As this solution was not very stable in the long term, I have moved to a dedicated Linux machine with an Apache web server with [ownCloud](https://owncloud.com/). For some time, I have experimented with P2P VPN software such as [N2N](https://github.com/ntop/n2n) to access my ownCloud instance even when not within the same LAN. I abandoned this solution because it required the N2N to be installed and properly configured on all devices, making it impossible to access the site on devices I did not own. For that, I bought my first domain with the cheapest Czech-based VPS I could find. On that VPS, I have installed a reverse-proxy tool [HAProxy](https://www.haproxy.org/) and an OpenVPN server to forward requests to specific subdomains to the server on my LAN.

Since then, I have bought more VPS, moved away to my apartment with a new machine, and started managing LANs with own routers. I have accumulated much technical debt while learning how to do all of this. My current solution is:

- one cheap VPS dedicated to hosting a WireGuard VPN that connects all my other VPSs and home servers
- second cheap VPS serving as an entry point to my network, with HAproxy that forwards requests to the relevant servers
- one more powerful but cheap VPS that hosts most of the publicly accessible docker containers and static websites

- refurbished laptop in my apartment that acts as a file-storage server with [NextCloud](https://nextcloud.com/) running in docker
- refurbished desktop PC in my parent's house that acts as a hypervisor for virtually running images of the old servers that I had used before and did not have enough time to migrate yet

This solution has certain drawbacks, mainly that multiple single points of failure exist. For example, if the VPN VPS fails, it cuts all connections between any two of my servers. If the entry VPS fails, none of my services are publicly available through internet. Alternatively, if the more powerful VPS hosting most of my websites fails, it may again disturb multiple services. Due to my cost-saving selection of hosting providers, these outages happen quite often -- some weeks, my services have less than 50 \% uptime. Next, as the number of devices I manage grows over time, keeping everything well-maintained becomes more and more time-consuming.

For these reasons, I have slowly started to migrate to more cloud-based solutions -- beginning with transferring my mail self-hosting to a paid Proton Mail subscription, moving my static websites to free Cloudflare pages and the most critical dynamic web apps to a free Google Cloud Compute Engine VPS. These three changes should vastly improve the uptime of my most critical services, such as my personal webpage, status monitoring tool [UptimeKuma](https://github.com/louislam/uptime-kuma) and privacy-friendly web analytics software [Plausible](https://plausible.io/).

As for the physical servers, the current settings with virtual servers running on top of another Linux server encounter decreased performance. To solve this issue, I have begun transferring services from the virtual machines into docker containers that run directly on the bare-metal OS. In addition to increasing performance, I now keep the configuration of my docker containers inside a git-versioned docker-compose file, simplifying the overall configuration management.

My automated backup routine for my physical servers consists of replicating all shared data via `rclone` bi-directional sync. Data not supposed to be shared or from my VPSs is backed up using [borg](https://borgbackup.readthedocs.io/en/stable/) to a single server with the largest attached storage. Borg provides compression and deduplication of data with authenticated encryption. Furthermore, it can be executed over SSH in so-called append-only mode, where, even if the data was mistakenly deleted from the original storage, it cannot be deleted from the remote storage. As to have multiple backups in case of a e.g. power surge, the encrypted backup data is copied to a remote location using [rsync](https://github.com/rsyncproject/rsync).

As most devices interacting with local networks are either Linux, Windows or Android, the self-hosted NextCloud works flawlessly for file synchronization and automatic upload. The issues are with a few iOS devices, where the automatic upload to NextCloud only sometimes works, and the app needs to be opened manually to start the upload process. On the other hand, thanks to the direct support of CalDav and CardDav inside iOS, the synchronization of tasks, calendar events and contacts is practically effortless. The physical security is handled by a NextCloud application [PhoneTrack](https://apps.nextcloud.com/apps/phonetrack). This application can be configured as a remote endpoint of multiple position-tracking applications. After that, the position of a device is recorded in configured intervals and can be shared with other NextCloud users. This solution was chosen as it is privacy-respecting, multi-platform and can generate GPX files as an output, which is helpful for further data manipulation.