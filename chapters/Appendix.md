## Questionnaires

- students
- teachers
- individuals with iPhone

## Author's solution

Initially, I have started self-hosting stored files using a dedicated Windows XP device inside a basement with Windows folder sharing. My reasoning for self-hosting most of the software As this solution was not very stable in a long term, I have moved to a dedicated Linux machine with Apache web server with [ownCloud](https://owncloud.com/) . For some time, I have experimented with a P2P VPN software such as [N2N](https://github.com/ntop/n2n) to be able access my ownCloud instance even when not within the same LAN. I have abandoned this solution because it required the N2N to be installed and properly configured on all devices and made it impossible to access the site on devices that I did not own. For that, I have bought my first domain together with the cheapest Czech-based VPS I could find. On that VPS I have installed a reverse-proxy tool [HAProxy](https://www.haproxy.org/) and OpenVPN server to forward requests to certain subdomains to the server on my LAN.

Since that, I have bought more VPS, moved away to my own apartment with a new machine, started managing LANs with own routers and with the process of learning how to do all of this I have accumulated a lot of technical debt. My current solution is:

- one cheap VPS dedicated to hosting a WireGuard VPN that connects all my other VPSs and home servers
- second cheap VPS serving as an entry point to my network, with HAproxy that forwards requests to the relevant servers
- one more powerful, but cheap VPS that hosts most of publicly-accessible docker containers and static websites
- refurbished laptop in my apartment that acts as a file-storage server with NextCloud running in docker
- refurbished desktop PC in my parent's house that acts as a hypervisor for virtually running images of the old servers that I have used before and did not have enough time to migrate yet

It is obvious that this solution has certain drawbacks, mainly that there are multiple single-points of failure -- if e.g. the VPN VPS fails, it cuts of all connection between any two other of my servers. If the entry VPS fails, none of my services are publicly available. Or, if the more powerful VPS hosting most of my websites fails, it may again disturb multiple services at once. Probably due to my cost-saving selection of hosting providers, these outages do happen quite often -- some weeks, my services my have less than 50 % uptime. Next, as the number of devices I manage grows over the time, it becomes more and more time consuming to keep everything well-maintained.

For these reasons, I have slowly started to migrate to a more cloud-based solutions -- beginning with transferring my mail self-hosting to paid Proton Mail subscription, moving my static websites to a free Cloudflare pages and the most critical dynamic web apps to a free Google Cloud Compute Engine VPS. These three changes should largely improve the uptime of my most critical services, such as my personal webpage, status monitoring tool [UptimeKuma](https://github.com/louislam/uptime-kuma) and privacy-friendly web analytics software [Plausible](https://plausible.io/).

- TODO
	- backups
	- devices
	- moving to docker