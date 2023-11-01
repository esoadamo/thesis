# Using Cloudflare Access for exposing self-hosted LAN applications

Self-hosting applications at one's home provides benefits over using their cloud-native alternativates. These benefits may include privacy (your data is stored at your hardware vs in cloud with 2nd party),
overall cost (effectively paying only for electricity and harware up-front vs paying for subscription tier every month/anually). On the other hand, perhaps as its most prominent disadvantage,
self-hosted applications at one's home are usually only available from inside the local area network, whereas cloud-native application can be accessed from anywhere with Internet connection. In this text, I will focus of solutions that are taylored for SOHO (small-office and home-office) settings.

## Classical solutions

There exists multiple options how to access LAN-only applications from the Internet, each with its custom set of up- and downsides. Please see that in none of the classical solutions listed below is discussed the problematics of IPv4 and IPv6 running at the same time, as most of the approaches allow for only one at the time. Furthermore, no approach deals with modern security practices as Zero Trust in any way by itself.

### Public IP address

With some of the largest Czech ISP (internet service providers) it is possible to obtain a public IP address[@vodafone-public][@o2-public][@tmobile-public] that directs all traffic directly to a router in possesion of the SOHO administrator (admin for the purposes of this text). The IP address may be provided as a benefit from ISP, for fixed price or, much more commonly, for monthly price. This solutions offers the largest freedom for the admin, as they are free to taylor the network stack to their liking by simply setting up port forwardings on their ingress router. On the other hand, this solution may be disadvantegous in terms of security (admin is fully responsible for setting correct access controls)  and flexibility (if the admin does use some form of centralized configuration, configuring the rules properly may steadily become infeasible with in more complex settings).

### VPN service with exposed ports

Some VPN providers like ProtonVPN[@proton-port] and ExpressVPN[@express-port] provide an option to forward single (TCP/UDP) port from the VPN's public IP adress to a  local machine or specific LAN address. The main advantage of this approach is the ease of setup  and little technical knowledge barrier when compared to other solutions, when the admin can simply install VPN provider's official GUI application and enable port forwarding. The drawbacks are evident, with a only single port, the option to host multiple applications is severly limited, unless the admin decides to use additional local solutions such as a [reverse proxy](https://www.haproxy.org/) for multiple HTTP-based applications or a [protocol multiplexer](https://github.com/yrutschle/sslh) for a specialized list of supported applications. One possibility to overcome this obstacle may be to hosts a VPN server on the explosed port that will allow client devices to access the LAN upon connection. Newertheless, the port number and IP address provided from the VPN service may change, which may require additional reconfiguration on client devices.

### Creating a custom tunnel with VPS

Another approach may be to purchage a cheap VPS (virtual private server), which typically has a public IP address. Then it is possible to setup a custom VPN server that the services on LAN will be connected to or directly use the remote port fowrading SSH option to directly forward the traffic from VPS to the self-hosted application. Because the VPS acts as a proxy, this approach may be suitable for both IPv4 and IPv6 even when the ISP is IPv4-only or IPv6 only. On the other hand, using a VPS as a proxy adds a new layer of complexity -- the reponse time is increased by the time that it takes to forward the request from VPS to LAN and back, while the connection may fail e.g. when the VPS reboots because of applied updates. It also places additional requirements onto the admin, who now needs also to properly configure the VPS as not to allow unauthorized access, which can be an obstacle for admins without previous experience with managing remote servers.

### Using a dedicated P2P software

An option that relies solely on the clients talking directly to each other, usually with a help of nodes that act as a middlemans exchaning information about connected clients to each other.  Examples of such software may be [LogMeIn Hamachi](https://www.vpn.net/), [n2n](https://github.com/ntop/n2n/releases) and [gsocket](https://github.com/hackerschoice/gsocket/). Most prominently, the Hamachi is targeted on regular users, requiring little to no technical knowledge. This makes the entry barrier almost non-existent. On the other hand, it requires special software to be installed on both server and, because of its P2P nature, clients and may be blocked on more restricted networks like airports or hotel lobbies.

## CFA

## CF Zero Trust

- HomeAssistant cache
- NextCloud SAML

## OICD proxy

## WARP

### References

- [proton-port](https://protonvpn.com/support/port-forwarding/)
- [express-port](https://www.expressvpn.com/support/knowledge-hub/router-app-port-forwarding/)
- [vodafone-public](https://www.vodafone.cz/pece/internet-data/internet-v-pocitaci/pevna-ip-adresa/)
- [o2-public](https://www.o2.cz/osobni/internet/pevna-ip-adresa-pro-internet-na-doma)
- [tmobile-public](https://www.t-mobile.cz/podpora/caste-dotazy/-/refId/faq-1304712526356-session-8260C0FB1BA18264E33A6F7291350053inst03)
