# Using Cloudflare Access for exposing self-hosted LAN applications

Self-hosting applications at one's home provides benefits over using their cloud-native alternativates. These benefits may include privacy (your data is stored at your hardware vs in cloud with 2nd party),
overall cost (effectively paying only for electricity and harware up-front vs paying for subscription tier every month/anually). On the other hand, perhaps as its most prominent disadvantage,
self-hosted applications at one's home are usually only available from inside the local area network, whereas cloud-native application can be accessed from anywhere with Internet connection.

## Existing solutions

There exists multiple options how to access LAN-only applications from the Internet:

- public IP
- ProtonVPN exposed port
- VPS with tunnel
- hamachi/n2n/gsocket

Does not have auth/complicated/unavailable for most users+IPv4 only/no zero-trust.
