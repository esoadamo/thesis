In this chapter, I will explore various existing services that can help address the problems outlined in the previous chapter, with a preference for those solutions that can effectively solve most of the user needs at once. This chapter contains well-known examples that may cover most user requirements while examining smaller-scale solutions focusing on a specific subset of tasks. Lastly, in later chapters, I will introduce a unique solution that involves self-hosting everything on a Synology NAS device as a control group for the other solutions.

## Microsoft

The first large security provider as a service that we will introduce in this thesis is Microsoft. Microsoft's most well-known product is Windows, currently available in version 10 or 11, dominating the desktop OS market. Besides that, Microsoft also provides a large spectrum of cloud-based services for individuals and company-based use.

### Provided cloud services

Microsoft cloud service services called Microsoft 365, range from its email freemail account to OneDrive cloud storage together with a full-featured browser-based office suite.`TEX:\footnote{Microsoft does provide a much more extensive range of cloud-based services, including cloud computing, but these services are out of scope of this thesis and as such are not included}` Although, the freemail account is not a requirement, as when creating a new Microsoft account, the user may decide if they do want to reuse their existing email account or create a new mail account. In its free version, the user has the capacity of 5 GB for cloud storage and 15 GB for mail storage, if they have chosen also to create a mail account [[@onedrivePricing]].

This storage can be extended to 50 GB or 1 TB in paid plans, and the business plans start with 1 TB shared or 1 TB per employee.

![[Microsoft 365 Individual Pricing.png|Pricing and feature comparison for Microsoft 365 individual subscription]]

![[Microsoft 365 Business Pricing.png|Pricing and feature comparison for Microsoft 365 business subscription]]

For more business-related use cases, Microsoft provides a cloud hosting service Azure. New customers are presented with a 30-day \$200 free credit and popular services free for 12 months. These popular services also include Linux or Windows virtual machines. Other than that, there is also a range of always-free services (with some limitations), such as Functions or Azure DevOps, a service for hosting Git repos and performing CI/CD.

![[Pasted image 20240507103156.png|Azure provided 12 months free for virtual machines]]

### Identity management

After its creation, the Microsoft account can be used as a single sign-on source for other applications. For more technical users and complex scenarios, the accounts can be assigned to groups within the Microsoft Azure portal, though this thesis's exact procedure is out of scope. For companies, Microsoft also provides advanced security features such as data loss prevention for filtering documents and email messages for company-confidential data or specifying labels assigned to assets together with policies that can apply encryption to the data and prevent its accidental leakage [[@microsoftApplyEncryption]]. To help manage multiple company-owned devices and assure compliance with company policies (such as password complexity policies), Microsoft provides Intune, available for all major desktop and smartphone OSs. [[@microsoftIntune]] 

### Family services

For the Android OS, Microsoft provides a Family Safety application. After installing this application on both the parents and the children's phones, the parents gain the ability to take a look at the children's position, be notified when children reach specific locations such as their school or home, or they can impose limits on how much of applications for which time the child can use per day. There is also a possibility of recording all his strokes to protect the children against cyber-bullying.[[@microsoftPhoneMonitoring]] As the application is installed as an administrator of the device, it has the authority to require the parent's approval before installing any new application. Furthermore, when using the Microsoft Edge browser on the smartphone or desktop, the parent can monitor all visited sites and create an allowlist of allowed sites for the child. These features are also available on a desktop version of Edge.

![[Family Safety Members.png|Microsoft Family Safety showing position of children]]

![[Pasted image 20240501184149.png|Microsoft Family Safety asking parent to allow access to application]]

![[Pasted image 20240501184257.png|Microsoft family safety activity overview]]

![[Pasted image 20240501184729.png|Microsoft Family Safety preventing launch of other web browser than Microsoft Edge]]

### Desktop integration

As an operating system from Microsoft, Windows seamlessly integrates with the company's services ecosystem. Windows also comes preinstalled with the OneDrive application or Microsoft Defender, an endpoint malware protection program. The operating system features also contain a Microsoft Smart Screen, which verifies the authenticity of applications before launching them. This security measure ensures that only trusted applications are allowed to run on the computer unless explicitly disabled. When using a BitLocker-encrypted hard drive, Microsoft also provides an option to recover encryption keys from the online portal if needed.

## Google

Google is the second largest security provider as a service introduced in this thesis. Unlike Microsoft, which has a large portion of the desktop market, Google has extensive smartphone market coverage with its Android OS. New devices with this system often come with preinstalled Google applications. Google is also well-known for its web browser, Google Chrome.

### Cloud services

Google provides various publicly available free services, perhaps most importantly, its free mail service, GMail, and cloud storage, such as Google Drive. These services include a shared free 15 GB of storage and a full web-based office suite. With a Google One subscription plan, the storage can be extended to up to 2 TB, which can be shared with up to 5 others. [[@googleOne]] When in company settings with more than six people, Google offers its Google workspace solution, which offers company mail hosting solution, video conferences via Google Meet and storage for Google Drive ranging from 30 GB to 5 TB per user, or more with undisclosed pricing. [[@googleWorkspace]]

![[Pasted image 20240429211526.png|Google One Subscription plans]]

![[Pasted image 20240508105111.png|Google Workspace subscription plans]]

For more advanced use cases, Google offers its cloud hosting solution, Google Cloud. This cloud provides standard features such as VPS hosting, functions, containers, databases... One of the specifics of the Google Cloud is that it provides a 90-day \$300 free trial and also a range of always-free services, including a signal-free VPS. [[@googleFreeCloud]] With company settings, Google offers device management and support for all major desktop and smartphone OSs. [[@googleMDM]]

![[Pasted image 20240507094955.png|Free VPS specifications provided by Google Cloud]]

### Smartphone services

When installing new applications through Google Play, the applications have already been processed by Google Play Protect and are deemed non-malicious.[[@googleblogFoughtApps]] Next, because of sometimes slow rolling out of security updates for Android devices by third-party manufacturers, Google has introduces Google Play Services, that can be used to apply security patches even.[[@androidcentralGooglePlay]] To recover a misplaced device, Google offers a web portal that can contact the device and show its real-time location on the map or force the device to start ringing. On Android, Google also offers the ability to perform a backup and restore all apps supporting it on a fresh or new device. [[@googleBackRestore]]

### Family services

Similarly to Microsoft's Family Safety, Google presents its service called Family Link. After linking parent and children accounts, this service allows for seeing the child's physical location in real-time or specifying which applications and sites they can access while optionally imposing time limits. The controls can be more granular on per-Google-app basis, meaning that the parent can currently configure control restrictions for:

- Google Play Store
- YouTube
- Google Chrome
- Google search
- Google Assistant
- Google Photos

These restrictions are applied whenever possible, e.g. YouTube and Google search options are enforced whenever the child logs in with their account, while Google Chrome settings are used on all platforms.

![[Pasted image 20240501184116.png|Google Family Link showing the position of children]]

![[Pasted image 20240501184329.png|Child attempting to install application requires approval form Google Family Link]]

![[Pasted image 20240501184528.png|Google Family Link asking parent to approve installation on child's device]]

![[Pasted image 20240501184816.png|Google Family Link preventing the child from accessing disallowed site in Google Chrome]]

Furthermore, the parent can control the whole device more closely; they can remotely lock the device, turn on or off installation of applications outside Google Play, turn developer options on or off or directly manage permissions of each application -- e.g. removing the microphone permission from a web browser and checking an option that only the parent can allow the application to access the microphone on the child's device. Next, the parent has detailed control of the child's Google account -- they can set the required parent's approval on every sign-in attempt to the child's account or when the child uses their Google account to sign into a third-party app. They can also change the child's password directly or delete the account.

## Apple

Another ecosystem that provides security as a service is the Apple ecosystem. Even though all of Apple's services are mostly closed for devices produced by the company, it provides a wide range of services for them.

### Identity management

Apple provides an option to create a new free account, called Apple ID, for its products. This account is essential for the correct working of Apple-produced devices, as currently, it is needed to be able to install new software from the Apple store. With this account, the user may also create a new mail account on the icloud.com domain. This account can be subsequently used as an identity source for other services, e.g., the only SSO login option to the Cloudflare Dashboard. The login process to the Apple account itself can be set to require login confirmation as an MFA on the user's existing device.

![[Pasted image 20240430084545.png|Login form for a Cloudflare Dashboard portal]]

### Cloud services

Apple's main point of cloud services for general consumers is its cloud storage, iCloud Drive. With a free Apple ID account on an Apple device, the user gets only 5 GB of storage. However, this storage can be extended with a paid subscription. By default, Apple automatically backs up all photos taken and the whole device to the iCloud Drive. As this does not require any action to be taken by the user, it can be considered a secure-by-default solution. On the other hand, it can quickly drain the available free storage, pushing users to the paid subscription. The paid subscription is priced monthly at [[@appleICloudPlans]]:

- 25 CZK for 50 GB
- 79 CZK for 200 GB
- 249 CZK for 2 TB
- 749 CZK for 6 TB
- 1490 CZK for 12 TB

Other than these tiered subscriptions, the possibility exists to use so-called [Web-only access to iCloud](https://support.apple.com/en-us/102447), which offers only 1 GB of space.

![[Pasted image 20240430085537.png|Payed subscription plans for iCloud]]

Apple also provides a complete office suite for all Apple-produced devices and web access using iCloud.

Another security feature that is available on Apple devices by default is its password manager, iCloud Keychain. This manager is set to auto-fill on iOS by default and is protected by the same measures as the device's lock screen. 

### Smartphone 

For Apple devices, Apple provides an E2EE communication service called iMessage. However, as with many Apple products, this service cannot currently be used outside the Apple ecosystem.

For families, it may be helpful that iOS provides a location-sharing feature, where one person can select contacts and see the position updated in real-time. As with Google and Microsoft, there is a web UI for locating a misplaced device.

## Proton

Proton is a Swiss-based company providing SaaS focused primarily on privacy. Its services include an E2EE mail account, Proton Mail with contacts manager, cloud storage Proton Drive and calendar Proton Calendar. Proton also offers a no-log VPN service, ProtonVPN. The free version of the account includes 1 GB of storage for mail, 5 GB of storage for DriveDrive and one connected device to VPN. This can be upgraded to 500 GB of storage shared between mail and Drive for individuals or 3 TB for family tariff. Furthermore, paid tariffs allow the addition of custom domains for Proton Mail.[[@protonCreateFree]] For the purposes of this thesis, I will consider the Mail Plus plan the same as the free plan, as it primarily focuses only on the main portion of Proton services and, as such, does not have many of the features of other paid subscriptions.

![[Pasted image 20240501154113.png|Proton pricing plans]]

Unlike Google or Microsoft, Proton Drive does not offer an office suite, so all files must be edited externally. On the other hand, Proton provides desktop applications for Windows and Mac, while Linux can be integrated with software such as [rclone](https://rclone.org/protondrive/). The mobile application on Android can automatically upload all taken photos. All deleted files stay inside the trash bin until it is manually emptied. For a paid subscription, Drive keeps up to 200 versions of files for up to 10 years. The E2EE is preserved even when sharing files through links, and the shares can be password-protected with an optional expiration date.

Proton Pass password manager is structured into so-called vaults, which can be shared with others. In the free version, the user can create up to 2 vaults and share them with up to 2 other accounts. For payer plans, the user can create up to 50 vaults, share them with ten other accounts, and use the manager as a TOTP generator. The passwords stored inside the manager can be accessed either through web UI, an extension for popular web browsers, or a native application for smartphone OSs and Windows, with macOS and Linux applications coming soon.[[@protonDownloadProton]] On smartphones, the Proton Pass can auto-fill passwords throughout the system.

## Cloudflare

Cloudflare SaaS solutions target companies or IT enthusiasts more than regular individuals, as its central core of services is providing secure web application hosting. However, Cloudflare's range of services is broad so that I will focus only on those relevant to the solutions in this thesis. [[@cloudflareEverywhereSecurity]] As for pricing, all of the services discussed in this thesis are free with limits set such as a single person or start-up should not reach them, with some exceptions.

With a Cloudflare account, the user can use R2 -- a cloud storage service with S3-compatible API, free for up to 10 GB of stored data [[@cloudflareR2]]. For most services to function, the users first need to link a domain with their Cloudflare account, either by registering it directly on Cloudflare or pointing domain DNS servers toward Cloudflare. After that, the user gains access to a Cloudflare Zero Trust dashboard.

Within the Zero Trust dashboard, it is possible to configure the following services:

- Access -- enforces policies, such as users having to authenticate via SSO with MFA enabled until they are allowed to access the application itself [[@cloudflareAccess]]
- Routes -- after installing a connector on an endpoint device, it is possible to set IP address ranges that should be forwarded through [[@cloudflarePrivateNetworks]]
- Tunnel -- after installing a connector, can specify which subdomain should be forwarded through to a specific IP address and port combination [[@cloudflareTunnel]]

![[Pasted image 20240507195336.png|Cloudflare Access requiring sign in with two configured SSO providers before allowing access to the application]]

For HTTP-only or HTTPS-only tunnels, there is no additional software required, while for non-HTTP applications, additional software is required to be installed on the machine that tried to access the resource -- WARP client for desktop, Cloudflare One Agent app for iOS and Android. The user logs in to the additional software before any access is allowed so that policies can be enforced correctly.

Other than that, Cloudflare offers a free VPN service for all major smartphone and desktop OS. This VPN service can switch between functioning as a DNS resolver only or forwarding all data through it, optionally blocking malware or adult sites.

## Bitwarden

As a special solution for SaaS that does not cover a wide range of needs but instead focuses only on one specific area, I would like to introduce Bitwarden. This solution can be found in [[@Pecuch2021thesis]] and [[@Ciernikova2022thesis]]. Bitwarden is an open-source password manager that is available as an extension to the web browser and a native application on the most popular platforms. It supports standard features such as auto-filling of passwords but also advanced features where it can pose as a virtual WebAuthn token. Another service available with a free Bitwaden account is the so-called [Bitwaden Send](https://bitwarden.com/products/send/), capable of sending E2EE text as a link with an expiration date and optional password protection.

Bitwarden also provides paid subscription tiers for individuals, families and businesses, where the added features are the option to share saved credentials, send arbitrary files through Bitwarden Send or use the Bitwarden client as a TOTP keychain. There is an option for business plans to set up login through SSO. 

## BackBlaze

BackBlaze is a cloud-archiving solution focusing on file versioning and deletion prevention. It offers two products:

- Computer Backup for backing up personal computers with unlimited storage [[@backblazeComputerCloudPricing]]

- B2 Cloud Storage with S3-compatible API with pay-as-you-go pricing (fixed pricing is available for purchases of 20+ TB) [[@backblazeCloudStoragePricing]]

Computer Backup is supported for Windows and Mac OS, while its default setting is to perform a backup of all data across all user profiles. Its unlimited storage for a fixed price makes it a perfect service when the user wants to ensure everything is properly stored. [[@backblazeSupportedOperating]]

B2 Cloud Storage creates buckets into which the data is uploaded. Except for standard features like versioning of files, B2 offers to set a so-called Object Lock, which prevents modification or deletion of files for a given period, which is useful for protecting against ransomware attacks or compliance with local laws. [[@backblazeObjectLock]]

![[Pasted image 20240507181120.png|BackBlaze Computer Backup pricing comparison]]

![[Pasted image 20240507181210.png|BackBlaze B2 Cloud Storage pricing comparison]]

## CryptPad

CryptPad is a service that focuses mainly on E2EE cloud storage. It is similar to Proton Drive but with the addition of an entire office suite contained inside the web UI. The user can either self-host their Crypt that instance, use the [official CryptPad](https://cryptpad.fr/) instance, or use one of [third-party instances](https://cryptpad.org/instances/). When using the official instance, any registered user obtains 1 GB of free storage, while with a paid subscription, it can be upgraded to 50 GB. Every stored file can be shared with other users or by a link. A special feature is the ability of a document to self-destruct after being opened, e.g. by the recipient of the shared link to it, and a permanent chat for every document. Additionally, in the office suite, CryptPad integrates a calendar and the ability to create virtual teams with multiple users.

For this thesis, the main downside of the CryptPad is the inability to integrate with other systems. To quote directly from the documentation: "The way encryption is currently used in CryptPad does not allow syncing with the local file system." [[@cryptPadFAQ]] This limitation severely decreases the ease of usage as any user must either keep all their document directly in the cloud or export them manually to the local drive. The second most significant obstacle, at least for the official instance, is that the maximum size of each file is only 25 MB for free accounts and 150 MB for the highest tier of paid accounts.

![[CryptPad main menu.png|The main menu of CryptPad with folder and files selection]]

![[CryptPad sheets.png|Modifying sheet on CryptPad with simple formula]]

![[CryptPad rich text.png|Modifying rich text document on CryptPad]]

## Synology

All of the before-mentioned services share the property of being executed in the cloud. As some of the services require a monthly subscription to function properly, I am presenting a solution that should be capable of handling the needs of the users in a similar manner.

![[Pasted image 20240501190623.png|An example listing of Synology NAS on an e-shop]]

Synology NAS is a device that boots into the DiskStation Manager operating system after entering one or more hard drives. Initially, the system consisted of a simple web UI for creating an administrator account and setting up the actual topology of drives. The default options are to use BTFS as a file system, taking advantage of the native support of extent checksum and RAID. After that, the administrator can create additional volumes, and users can then access said volumes through services enabled by the administrator, such as web UI, SMB, FTP, WebDAV, and more. The most prominent disadvantage of using Synology devices is that, unlike cloud-based services, they can reach their end-of-life and may be cut off from all security updates. The second disadvantage that needs to be considered is that with a physical device, the administrator needs to take care of its physical security and protect it from accidental damage or theft.

![[Pasted image 20240501192143.png|Synology DSM Web UI with opened file manager]]

### Provided services

Even though initially, the system supported only file sharing, a wide range of packages existed that could be directly installed to extend the system's functions. These packages include CardDAV for contact synchronization, CloudSync for synchronization with other storage providers (with the option to encrypt the remote content, which may be helpful for backup of local data), VPN server, RADIUS server and many more. Some devices allow the execution of arbitrary docker images or entire virtual machines via Virtual Machine Manager, making it easy to run practically any service.

![[Pasted image 20240501192735.png|Some of the existing Synology DSM packages]]

For basic cloud-storage-like functionality, installing the Synology Drive Client on the desktop is possible, which will then synchronize the user's local files with Synology drive and vice versa.[[@synologySyncFiles]]. On a smartphone, the user may install the DS Photo application and set up an automatic upload of newly taken media. [[@synologyPhotoAndroid]][[@synologyPhotoSynology]]

For more business-related usage, Synology can perform full-system backups of endpoint devices~[[@synologyBackEntire]], work as a web-mail client or server, host web pages and more.

### account management

If an SSO Server package is installed, the local Synology account can be used as an IDM source. Other applications can be configured to accept this service with OIDC protocol, including the Cloudflare Zero Trust. [[@synologyServiceServer]] Or, the administrator can enable and set up the Directory Server package for LDAP. The accounts may be protected with an MFA using supported methods, such as approved sign-in, OTP code, or hardware security key. [[@synology2FactorAuthentication]]

### Remote connection

Synology itself provides a feature called QuickConnect, that, after creating a public Synology account, allows to create a device ID that will make the device accessible through the internet without the need to set any port forwarding. The administrator can select which services they want to route publicly through the QuickConnect.[[@synologyQuickConnectSynology]] Another option may be to set up a Cloudflare tunnel that will route a custom subdomain to a specific port on the local Synology device through the ability to run arbitrary docker images.