In this chapter, I will explore various existing services that can help address the problems outlined in the previous chapter, with a preference for those solutions that can effectively solve most of the user needs at once. This chapter contains well-known examples that may cover most user requirements while also examining smaller-scale solutions focusing on a specific subset of tasks. Lastly, in later chapters, I will introduce a unique solution that involves self-hosting everything on a Synology NAS device as a control group for the other solutions.

## Microsoft

The first large security provider as a service that we will introduce in this thesis is Microsoft. Microsoft's most well-known product is Windows, currently available in version 10 or 11, dominating the desktop OS market. Besides that, Microsoft also provides a large spectrum of cloud-based services for individuals and company-based use.

### Cloud services

Microsoft cloud service services called Microsoft 365, range from its freemail account to OneDrive cloud storage together with a full-featured browser-based office suite. Although, the freemail account is not a requirement, when creating a new Microsoft account, the user may decide if they do want to reuse their existing email account or create a new mail account. For Windows, the preinstalled OneDrive client supports virtual files. Virtual files are shown as regular files while browsing directories on the disc but are downloaded from the cloud only when explicitly requested, saving space on the local machine. In free version of OneDrive, the user has the capacity of 5 GB for cloud storage and 15 GB for mail storage, if they have chosen also to create a mail account. [[@onedrivePricing]]

This storage can be extended to 50 GB or 1 TB in paid plans (`TEX:\autoref{fig:Microsoft 365 Individual Pricing.png}` ). The business plans start with 1 TB shared or 1 TB per employee (`TEX:\autoref{fig:Microsoft 365 Business Pricing.png}`). [[@onedrivePricing]]

![[Microsoft 365 Individual Pricing.png|Pricing and feature comparison for Microsoft 365 individual subscription]]

![[Microsoft 365 Business Pricing.png|Pricing and feature comparison for Microsoft 365 business subscription]]

For more business-related use cases, Microsoft provides a cloud hosting service Azure. New customers are presented with a 30-day \$200 free credit and popular services free for 12 months. These popular services also include Linux or Windows virtual machines (`TEX:\autoref{fig:Azure Free Products.png}`). Other than that, there is also a range of always-free services (with some limitations), such as Functions or Azure DevOps, a service for hosting Git repos and performing CI/CD.`TEX:\footnote{Microsoft does provide a much more extensive range of cloud-based services, such as databases, but these services are out of scope of this thesis and as such are not included}`  [[@microsoftFree]]

![[Azure Free Products.png|Azure provided 12 months free for virtual machines]]

### Identity management

After its creation, the Microsoft account can be used as a single sign-on source for other applications. For more technical users and complex scenarios, the accounts can be assigned to groups within the Microsoft Azure portal. For companies, Microsoft also provides advanced security features such as data loss prevention for filtering documents and email messages for company-confidential data or specifying labels assigned to assets together with policies that can apply encryption to the data and prevent its accidental leakage [[@microsoftApplyEncryption]]. To help manage multiple company-owned devices and assure compliance with company policies (such as password complexity policies), Microsoft provides Intune, available for all major desktop and smartphone OSs. [[@microsoftIntune]] 

One of the options that Microsoft provides is to use the account in a passwordless manner, where the user, instead of typing password, uses a smartphone application to confirm login attempts with their bio-metric. [[@microsoftPasswordless]] Because no password is involved, the user does not have to worry about remembering any complex sequence, which is crucial for a user with low password hygiene. Next, as the Microsoft account can be used as an identity source on multiple other web services utilizing OAuth or OIDC protocol, the user can further minimize the number of used passwords while benefiting from password-less authentication even on third-party servers.
### Smartphone services

Using the default web browser Microsoft Edge, it is possible to use the Microsoft account to synchronize passwords across all user's devices. The saved passwords are automatically filled into web pages. There is no option to look up saved passwords from a web UI; instead having always to log-into the Edge browser to view the saved passwords. Every time the user wants to show or copy the password manually, they first need to fill in their device login information. [[@edgePassword]] The passwords cannot be copied nor shown if the device has no lock-screen protection set, as shown on `TEX:\autoref{fig:Edge Password Copy.png}`. On Android, the Edge browser offers to generate a strong password when creating a new account, while on Windows, this feature needs to be explicitly turned on first inside browser's settings. [[@microsoftPasswordGenerator]] Lastly, the Edge browser on Android can be set as a service for filling login credentials for all other system applications that support automatic field recognition.

The OneDrive application is also available for Android, where it offers automatic backups of taken photos and video. [[@microsoftAutoUpload]] As OneDrive offers versioning, trashbin and ransomware protection, it is an valid solution to guard against accidental or even malicious data loss. [[@microsoftRansomware]]

![[Edge Password Copy.png|Password in Edge cannot be shown without a lock-screen in place]]


### Family services

For the Android OS, Microsoft provides a Family Safety application. After installing this application on both the parents and the children's phones, the parents gain the ability to take a look at the children's position (`TEX:\autoref{fig:Family Safety Members.png}`), be notified when children reach specific locations such as their school or home, or they can impose limits on how much of applications for which time the child can use per day (`TEX:\autoref{fig:Family Safety More Time.png}`). There is also a possibility of recording all their strokes to protect the children against cyber-bullying. [[@microsoftPhoneMonitoring]] Furthermore, when using the Microsoft Edge browser on the smartphone or desktop, the parent can monitor all visited sites and create an allowlist of allowed sites for the child (`TEX:\autoref{fig:Family Safety Web Activity.png}`). As the application is installed on the smartphone as an administrator of the device, it has the authority to prevent launching of third party web browsers that do not have the same controls and safeguards in place (`TEX:\autoref{fig:Family Safety Prevents Lauching Chrome.png}`).

![[Family Safety Members.png|Microsoft Family Safety showing position of children]]

![[Family Safety More Time.png|Microsoft Family Safety asking parent to allow access to application]]

![[Family Safety Web Activity.png|Microsoft family safety activity overview]]

![[Family Safety Prevents Lauching Chrome.png|Microsoft Family Safety preventing launch of other web browser than Microsoft Edge]]

### Desktop integration

As an operating system from Microsoft, Windows seamlessly integrates with the company's services ecosystem. Windows comes preinstalled with the OneDrive application or Microsoft Defender, an endpoint malware protection program. The operating system features also contain a Microsoft Smart Screen, which verifies the authenticity of applications before launching them. This security measure ensures that only trusted applications are allowed to run on the computer unless explicitly disabled. When using a BitLocker-encrypted hard drive, Microsoft also provides an option to recover encryption keys from the online portal if needed.

## Google

Google is the second largest SaaS provider introduced in this thesis. Unlike Microsoft, which has a large portion of the desktop market, Google has extensive smartphone market coverage with its Android OS. New devices with this system often come with preinstalled Google applications.

Google is also well-known for its web browser, Google Chrome. One of the security benefits of using this browser is its built-in phishing protection. [[@blogBrowseSafely]] Next, like the Microsoft Edge, the Chrome browser has an inbuilt password manager. On the desktop, the password manager works similarly to the Edge browser, offering the option to be notified when any saved passwords are found within the list of known breached passwords. The main difference is that, when signed into the account, the passwords can also be shown within the Google [passwords web portal](https://passwords.google.com/), making accessing the passwords on any device easier.

### Cloud services

Google provides various publicly available free services, perhaps most importantly, its free mail service, Gmail, and cloud storage, Google Drive. These services include a shared free 15 GB of storage and a full web-based office suite. With a Google One subscription plan, the storage can be extended to up to 2 TB, which can be shared with up to 5 others (`TEX:\autoref{fig:Google One Individual Pricing.png}`). [[@googleOne]] When in company settings with more than six people, Google offers its Google Workspace solution, which provides company mail hosting solution, video conferences via Google Meet and storage for Google Drive ranging from 30 GB to 5 TB per user, or more with undisclosed pricing (`TEX:\autoref{fig:Google Workspace Pricing.png}`). [[@googleWorkspace]] Google Drive offers a trash bin and version control, with a detailed differentials version history for the office documents. To further strengthen the security of the files stored on Google Drive or received to a Gmail account, Google scans all files for malware or possible phishing documents. [[@bleepingcomputerGoogleDrive]]

To access files stored on Google Drive on Windows, the user may download the Google Drive application to access and synchronize stored files. All supported platforms, including smartphone apps, can make specific files available even when not connected to the internet. Though, if the user wants to edit documents within the web office suite, they need to install a Chrome extension to edit documents offline. [[@googleDriveOffline]]

![[Google One Individual Pricing.png|Google One Subscription plans]]

![[Google Workspace Pricing.png|Google Workspace subscription plans]]

For more advanced use cases, Google offers its cloud hosting solution, Google Cloud. This cloud provides standard features such as VPS hosting, functions, containers, databases and more. One of the specifics of the Google Cloud is that it provides a 90-day \$300 free trial and also a range of always-free services, including a always-free VPS with specifications as shown on `TEX:\autoref{fig:Google Always Free Tier.png}`. [[@googleFreeCloud]] With company settings, Google offers device management and support for all major desktop and smartphone OSs. [[@googleMDM]]

![[Google Always Free Tier.png|Free VPS specifications provided by Google Cloud]]

### Smartphone services

When installing new applications through Google Play, the applications have already been processed by Google Play Protect and are deemed non-malicious. [[@googleblogFoughtApps]] Next, because of sometimes slow rolling out of security updates for Android devices by third-party manufacturers, Google has introduces  a feature to the preinstalled Google Play Services, that can be used to apply security patches on its own. [[@androidcentralGooglePlay]] To recover a misplaced device, Google offers a web portal that can contact the device and show its real-time location on the map or force the device to start ringing. On Android, Google also offers the ability to perform a backup and restore all apps supporting it on a fresh or new device. [[@googleBackRestore]] Next, Google offers to save and auto-fill saved passwords by default, making the process frictionless.

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

Apple provides an option to create a new free account, called Apple ID, for its products. This account is essential for the correct working of Apple-produced devices, as currently, it is needed to be able to install new software from the Apple store. With this account, the user may also create a new mail account on the icloud.com domain. This account can be subsequently used as an identity source for other services, e.g., the only SSO login option to the Cloudflare Dashboard (`TEX:\autoref{fig:Cloudflare Login.png}`). The login process to the Apple account itself can be set to require login confirmation in a form of MFA on the user's existing device.

![[Cloudflare Login.png|Login form for a Cloudflare Dashboard portal with Apple ID as a only SSO option]]

### Cloud services

Apple's main point of cloud services for general consumers is its cloud storage, iCloud Drive. With a free Apple ID account on an Apple device, the user gets only 5 GB of storage. However, this storage can be extended with a paid subscription. By default, Apple automatically backs up all photos taken and the whole device to the iCloud Drive. As this does not require any action to be taken by the user, it can be considered a secure-by-default solution. On the other hand, it can quickly drain the available free storage, pushing users to the paid subscription. Unlike other cloud storage providers, Apple does not support versioning files, but only allows of restoration of deleted files from the trash bin. [[@appleVersionHistory]] The paid subscription is priced monthly at [[@appleICloudPlans]] (`TEX:\autoref{fig:iCloud Plans.png}`):

- 25 CZK for 50 GB
- 79 CZK for 200 GB
- 249 CZK for 2 TB
- 749 CZK for 6 TB
- 1490 CZK for 12 TB

Other than these tiered subscriptions, the possibility exists to use so-called Web-only access to iCloud, which offers only 1 GB of space. [[@appleWebonlyAccess]]

![[iCloud Plans.png|Payed subscription plans for iCloud]]

Apple also provides a complete office suite for all Apple-produced devices and web access using iCloud.

Another security feature that is available on Apple devices by default is its password manager, iCloud Keychain. This manager is set to auto-fill on iOS by default and is protected by the same measures as the device's lock screen. It is possible to access the passwords stored within the Keychain on Windows with the dedicated iCloud application and browser extension. [[@appleICloudPasswords]] App Keychain can generate TOTP codes, as shown on `TEX:\autoref{fig:Apple Keychain.png}`.

![[Apple Keychain.png|Apple KeyChain providing the option to add TOTP]]


### Smartphone services

For Apple devices, Apple provides an E2EE communication service called iMessage. However, as with many Apple products, this service cannot currently be used outside the Apple ecosystem.

For families, it may be helpful that iOS provides a location-sharing feature, where one person can select contacts and see the position updated in real-time. As with Google and Microsoft, there is a web UI for locating a misplaced device.

## Proton

Proton is a Swiss-based company providing SaaS focused primarily on privacy. Its services include an E2EE mail account, Proton Mail with contacts manager, cloud storage Proton Drive and calendar Proton Calendar. Proton also offers a no-log VPN service, ProtonVPN. The free version of the account includes 1 GB of storage for mail, 5 GB of storage for Drive and one connected device to VPN. This can be upgraded to 500 GB of storage shared between mail and Drive for individuals or 3 TB for family tariff (`TEX:\autoref{fig:Proton Pricing.png}`). Furthermore, paid tariffs allow the addition of custom domains for Proton Mail. [[@protonCreateFree]] For the purposes of this thesis, I will consider the Mail Plus plan the same as the free plan, as it primarily focuses only on the mail-services portion of Proton services and, as such, does not have many of the features of other paid subscriptions. For business plans, the offered storage is 15 GB or 500 GB, while a customizable enterprise plan can be arranged (`TEX:\autoref{fig:Proton business pricing.png}`). [[@protonBusiness]]

![[Proton Pricing.png|Proton invidual pricing plans]]

![[Proton business pricing.png|Proton business pricing plans]]

Unlike Google or Microsoft, Proton Drive does not offer an office suite, so all files must be edited externally. For Windows and Mac, Proton Drive provides desktop applications, while Linux can be integrated with software such as [rclone](https://rclone.org/protondrive/), where the user can open their files in a local editor of their choosing. The mobile application on Android can automatically upload all taken photos. All deleted files stay inside the trash bin until it is manually emptied. For a paid subscription, Drive keeps up to 200 versions of files for up to 10 years. The E2EE is preserved even when sharing files through links, and the shares can be password-protected with an optional expiration date.

Proton Pass password manager is structured into so-called vaults, which can be shared with others. In the free version, the user can create up to 2 vaults and share them with up to 2 other accounts. For payed plans, the user can create up to 50 vaults, share them with ten other accounts, and use the manager as a time-based one-time password (TOTP) generator. The passwords stored inside the manager can be accessed either through web UI, an extension for popular web browsers, or a native application for smartphone OSs and Windows, with macOS and Linux applications coming soon. [[@protonDownloadProton]] On smartphones, the Proton Pass can auto-fill passwords throughout the system.

## Cloudflare

Cloudflare SaaS solutions target companies or IT enthusiasts more than regular individuals, as its central core of services is providing secure web application hosting. However, Cloudflare's range of services is broad so that I will focus only on those relevant to the solutions in this thesis. [[@cloudflareEverywhereSecurity]] As for pricing, all of the services discussed in this thesis are free with limits set such as a single person or start-up should not reach them, with some exceptions.

With a Cloudflare account, the user can use R2 -- a cloud storage service with S3-compatible API, free for up to 10 GB of stored data [[@cloudflareR2]]. For most services to function, the users first need to link a domain with their Cloudflare account, either by registering it directly on Cloudflare or pointing domain DNS servers toward Cloudflare. After that, the user gains access to a Cloudflare Zero Trust dashboard.

Within the Zero Trust dashboard, it is possible to configure the following services:

- Access -- enforces policies, such as users having to authenticate via SSO with MFA enabled until they are allowed to access the application itself (`TEX:\autoref{fig:CFA Login.png}`) [[@cloudflareAccess]]
- Routes -- after installing a connector on an endpoint device, it is possible to set IP address ranges that should be forwarded through [[@cloudflarePrivateNetworks]]
- Tunnel -- after installing a connector, can specify which subdomain should be forwarded through to a specific IP address and port combination [[@cloudflareTunnel]]

![[CFA Login.png|Cloudflare Access requiring sign in with two configured SSO providers before allowing access to the application]]

For HTTP-only or HTTPS-only tunnels, there is no additional software required, while for non-HTTP applications, additional software is required to be installed on the machine that tried to access the resource -- WARP client for desktop, Cloudflare One Agent app for iOS and Android. The user logs in to the additional software before any access is allowed so that policies can be enforced correctly.

Other than that, Cloudflare offers a free VPN service called 1.1.1.1 for all major smartphone and desktop OS. This VPN service can switch between functioning as a DNS resolver only or forwarding all data through it, optionally blocking malware or adult sites. [[@one1111Free]]

## Bitwarden

As a special solution for SaaS that does not cover a wide range of needs but instead focuses only on one specific area, I would like to introduce Bitwarden. This solution can be found in [[@Pecuch2021thesis]] and [[@Ciernikova2022thesis]]. Bitwarden is an open-source password manager that is available as an extension to the web browser and a native application on the most popular platforms. It supports standard features such as auto-filling of passwords but also advanced features where it can pose as a virtual WebAuthn token. Another service available with a free Bitwarden account is the so-called [Bitwarden Send](https://bitwarden.com/products/send/), capable of sending E2EE text as a link with an expiration date and optional password protection.

Bitwarden also provides paid subscription tiers for individuals, families and businesses, where the added features are the option to share saved credentials, send arbitrary files through Bitwarden Send or use the Bitwarden client as a TOTP keychain. There is an option for business plans to set up login through SSO. Individual plan costs are set at \$10 per year, family \$40 per year for up to 6 users. Business plans start at \$4 per month per user, with SSO included with a plan priced at \$6 per month per user.  [[@bitwardenPricing]]

## BackBlaze

BackBlaze is a cloud-archiving solution focusing on file versioning and deletion prevention. It offers two products:

- Computer Backup for backing up personal computers with unlimited storage (`TEX:\autoref{fig:BBPricing.png}`) [[@backblazeComputerCloudPricing]]
- B2 Cloud Storage with S3-compatible API with pay-as-you-go pricing (fixed pricing is available for purchases of 20+ TB, `TEX:\autoref{fig:B2B Pricing.png}`) [[@backblazeCloudStoragePricing]]

Computer Backup is supported for Windows and Mac OS, while its default setting is to perform a backup of all data across all user profiles. Its unlimited storage for a fixed price makes it a perfect service when the user wants to ensure everything is properly stored. [[@backblazeSupportedOperating]]

B2 Cloud Storage works by creating buckets into which the data is uploaded. Except for standard features like versioning of files, B2 offers to set a so-called Object Lock, which prevents modification or deletion of files for a given period, which is useful for protecting against ransomware attacks or compliance with local laws. [[@backblazeObjectLock]]

![[BBPricing.png|BackBlaze Computer Backup pricing comparison]]

![[B2B Pricing.png|BackBlaze B2 Cloud Storage pricing comparison]]

## CryptPad

CryptPad is a service that focuses mainly on E2EE cloud storage. It is similar to Proton Drive but with the addition of an entire office suite contained inside the web UI. The user can either self-host their CryptPad instance, use the [official CryptPad](https://cryptpad.fr/) instance, or use one of [third-party instances](https://cryptpad.org/instances/). When using the official instance, any registered user obtains 1 GB of free storage, while with a paid subscription, it can be upgraded to 50 GB. Every stored file can be shared with other users or by a link. A specific feature is the ability of a document to self-destruct after being opened, e.g. by the recipient of the shared link to it, and a permanent chat for every document. Additionally, in the office suite, CryptPad integrates a calendar and the ability to create virtual teams with multiple users.

For this thesis, the main downside of the CryptPad is the inability to integrate with other systems. To quote directly from the documentation: "The way encryption is currently used in CryptPad does not allow syncing with the local file system." [[@cryptPadFAQ]] This limitation severely decreases the ease of usage as any user must either keep all their document directly in the cloud or export them manually to the local drive. The second most significant obstacle, at least for the official instance, is that the maximum size of each file is only 25 MB for free accounts and 150 MB for the highest tier of paid accounts.

![[CryptPad main menu.png|The main menu of CryptPad with folder and files selection]]

![[CryptPad sheets.png|Modifying sheet on CryptPad with simple formula]]

![[CryptPad rich text.png|Modifying rich text document on CryptPad]]

## Synology

All of the before-mentioned services share the property of being hosted in the cloud. As some of the services require a monthly subscription to function properly, I am presenting a local solution that should be capable of handling the needs of the users in a similar manner.

Synology NAS is a standalone embedded devices with CPU, RAM and empty disc slots. The discs are supposed to be purchased and installed by the user separately, giving the user full control over how much storage is available. The models differ in CPU performance, RAM size or the number of available disc slots. The primary purpose of the Synology NAS is to be connected to the LAN and easy to configure.

After the separate disc are inserted, the device boots into the DiskStation Manager operating system. Initially, the system consists of a simple web UI for creating an administrator account and setting up the actual topology of drives. The default options are to use Btrfs as a file system, taking advantage of the native support of extent checksum and RAID. After that, the administrator can create additional volumes, and users can then access said volumes through services enabled by the administrator, such as web UI, SMB, FTP, WebDAV, and more. The most prominent disadvantage of using Synology devices is that, unlike cloud-based services, they can reach their end-of-life and may be cut off from all security updates. The second disadvantage that needs to be considered is that with a physical device, the administrator needs to take care of its physical security and protect it from accidental damage or theft.

![[Pasted image 20240501192143.png|Synology DSM Web UI with opened file manager]]

### Provided services

Even though initially, the system supports only file sharing, a wide range of packages exists that can be directly installed to extend the system's functions. These packages include CardDAV for contact synchronization, CloudSync for synchronization with other storage providers (with the option to encrypt the remote content, which may be helpful for backup of local data), VPN server, RADIUS server and many more. Some devices allow the execution of arbitrary docker images or entire virtual machines via Virtual Machine Manager, making it easy to run practically any service.

![[Pasted image 20240501192735.png|Some of the existing Synology DSM packages]]

For basic cloud-storage-like functionality, installing the Synology Drive Client on the desktop is possible, which will then synchronize the user's local files with Synology drive and vice versa. [[@synologySyncFiles]] On a smartphone, the user may install the DS Photo application and set up an automatic upload of newly taken media. [[@synologyPhotoAndroid]][[@synologyPhotoSynology]] For editing documents, Synology does offer its web-based office suite as a downloadable package for some of its models. This office suite works similarly to the Google Drive office suite, as it employs its storage format and, as such, requires importing and exporting when working with third-party office suites. [[@synoOffice]] When files are modified or deleted, Synology provides both trashbin and restoring old versions, with the office package providing an convenient user interface for the view of performed changes. 

For more business-related usage, Synology can perform full-system backups of endpoint devices~[[@synologyBackEntire]], work as a web-mail client or server, host web pages and more.

### Account management

If an SSO Server package is installed, the local Synology account can be used as an SSO source. Other applications can be configured to accept this service with OIDC protocol, including the Cloudflare Zero Trust. [[@synologyServiceServer]] Or, the administrator can enable and set up the Directory Server package for LDAP. The accounts may be protected with an MFA using supported methods, such as approved sign-in, OTP code, or hardware security key. [[@synology2FactorAuthentication]]

### Remote connection

Synology itself provides a feature called QuickConnect, that, after creating a public Synology account, allows to create a device ID that will make the device accessible through the internet without the need to set any port forwarding. The administrator can select which services they want to route publicly through the QuickConnect. [[@synologyQuickConnectSynology]] Another option may be to set up a Cloudflare tunnel that will route a custom subdomain to a specific port on the local Synology device through the ability to run arbitrary docker images.