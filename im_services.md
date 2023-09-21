# Identity Managment for families

## Microsoft

- [Microsoft family safety docs](https://support.microsoft.com/en-us/account-billing/microsoft-family-safety-bb97220e-9dd8-4b4a-9d15-8194d5941dc5)
- ![780c6db41f3413a038a1c6078b707d46.png](./assets/780c6db41f3413a038a1c6078b707d46.png)
- [Microsoft family safety sales pitch](https://www.microsoft.com/cs-cz/microsoft-365/family-safety?ocid=cmm15zkky0u&rtc=1)
  - ![93509b1aa144c2641669c027b072872d.png](./assets/93509b1aa144c2641669c027b072872d.png)
  - net filtering works by blocking browsers other than Edge
  - [Phone app](https://www.microsoft.com/en-us/microsoft-365-life-hacks/privacy-and-safety/protect-your-family-how-to-select-a-phone-monitoring-app) allows for key-logging
  - payed ransomware protection & 6TB of OneDrive space
  - up to 6 accounts
- [Microsoft Entra - Secure Identities and Access | Microsoft Security](https://www.microsoft.com/en-us/security/business/microsoft-entra)
  - [Microsoft Entra Plans and Pricing | Microsoft Security](https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing)
  - says free, but could not find it
  - has basic free tier that should be enough for most users
  - for some reason I see many personal details of MUNI people
  - ![](materials/entry-muni-users.png)
  - ![entra-muni-devices.png](materials/entra-muni-devices.png)
  - [Přidání existujícího předplatného Azure do tenanta - Microsoft Entra | Microsoft Learn](https://learn.microsoft.com/cs-cz/azure/active-directory/fundamentals/how-subscriptions-associated-directory?amp%3Bclcid=0x5)
  - [Vytvoření bezplatného vývojářského tenanta Azure Active Directory - Microsoft Entra | Microsoft Learn](https://learn.microsoft.com/cs-cz/azure/active-directory/verifiable-credentials/how-to-create-a-free-developer-account)
- [Set up sign-up and sign-in with a Microsoft Account - Azure AD B2C | Microsoft Learn](https://learn.microsoft.com/en-us/azure/active-directory-b2c/identity-provider-microsoft-account?pivots=b2c-user-flow)
- **TODO: Proklikat https://account.microsoft.com/?ref=MeControl&refd=www.microsoft365.com**
  - cena pomocí triku prodloužení?

## Google

- ~~[Identity and Access Management &nbsp;|&nbsp; IAM &nbsp;|&nbsp; Google Cloud](https://cloud.google.com/iam/)~~
  - ~~*"provided on no additional charge"*~~
  - ~~[Overview of Google identity management &nbsp;|&nbsp; Cloud Architecture Center &nbsp;|&nbsp; Google Cloud](https://cloud.google.com/architecture/identity/overview-google-authentication)~~
  - is only for access to the Cloud
- [Identity Platform &nbsp;|&nbsp; Google Cloud](https://cloud.google.com/identity-platform)
- **TODO: Google Workspace**
- **TODO: GSuite for family existuje?**

## Synnogy

- https://c2.synology.com/en-global/pricing/identity
- on prem
- free for up to 250 users and 10 devices

## Clouflare

- **[Cloudflare One](https://www.cloudflare.com/cloudflare-one/)**, [the story of](https://iframe.cloudflarestream.com/dc64ca8874298041945c9a6924c82b4b?preload=metadata)
- [Family tag on blog](https://blog.cloudflare.com/tag/families/)
  - [Overview of services for family](https://blog.cloudflare.com/shields-up-free-cloudflare-services-to-improve-your-cyber-readiness/)
- [Zero trust sales page](https://www.cloudflare.com/zero-trust/)
  - Integrates with SSO [source](https://www.cloudflare.com/learning/access-management/what-is-sso/)
    - An [identity provider (IdP)](https://www.cloudflare.com/learning/access-management/what-is-an-identity-provider/) is a service that stores and verifies user identity. IdPs are typically cloud-hosted services, and they often work with single sign-on (SSO) providers to authenticate users.
  - [Glossary](https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/)
  - [Zero trust network access learning](https://www.cloudflare.com/learning/access-management/what-is-ztna/)
    - explains ZTNA & endpoints & SDP (software defined perimeter)
  - [CF Access](https://www.cloudflare.com/zero-trust/products/access/)
    - Create an aggregation layer for secure access to all your self-hosted, SaaS, or non-web applications
    - Connect users faster and more safely than a VPN
    - Try it forever for up to 50 users with our Free plan
    - has nice video presenting all its pros
    - can use CF Warp client as an agent
- [SASE](https://www.cloudflare.com/learning/access-management/what-is-sase/)
  - _"Secure access service edge, or SASE, is a cloud-based IT model that bundles software-defined networking with network security functions and delivers them from a single service provider."_
  - components: Secure web gateways (SWG), Cloud access security broker (CASB), Zero Trust Network Access (ZTNA), [Firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/)
    - [next-generation firewall (NGFW)](https://www.cloudflare.com/learning/security/what-is-next-generation-firewall-ngfw/)
      - Intrusion prevention system (IPS), Deep packet inspection (DPI), Application control (what each application can access)
- [IAM](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)
  - pretty basic
  - [CASB (cloud access security broker)](https://www.cloudflare.com/learning/access-management/what-is-a-casb/)
    - Visibility - shows undocummented systems
    - Data security - provides DLP (Data loss prevention)
    - Threat protection - anti-mallware & sandboxing & URL filtering .…
    - Compliance - self explaining

### TODO

- cloud backup & device search & antivirus & family safety
  - kolem Google workspace
- Vašek má Synnology disk!
- [Box - Nextcloud](https://nextcloud.com/box/)
- on-prem - zmínit hardwarovou bezpečnost
- seznam.cz poskytuje Open-ID?
  - přihlášení na vašem webu pomocí Seznam účtu?
- synchronizace všeho po ukradení notebooku?
  - prý umí Synnology
- pozor na krabicové officy - not in scope of this thesis
- Klárka - doptat na věci
- tisky? WiFi?
