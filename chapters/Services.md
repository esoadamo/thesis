In this chapter, I will explore various existing services that can help address the problems outlined in the previous chapter, with preference for those solutions that can effectively solve most of the user needs at once. This chapter contains well-known examples that may cover a majority of user requirements, while additionally examining smaller-scale solutions that focus on a specific subset of tasks. Lastly, I will introduce a unique solution that involves self-hosting everything on a Synology NAS device as a control group for the other solutions in later chapters.
## Microsoft

The first large provider of security as a service that we are going to introduce in this thesis is Microsoft. Microsoft's most well-known product is the operating system Windows, which is currently available in its version 10 or 11 dominates the market of desktop OS. Other that that, Microsoft also provides a large spectrum of cloud-based services for both individuals and company-based use.
### Provided cloud services

Microsoft cloud service services, called Microsoft 365, are ranging from its email freemail account to OneDrive cloud storage together with an full-featured browser-based office suite.`TEX:\footnote{Microsoft does provide much larger range of cloud-based services, including cloud computing, but these services are out of scope of this thesis and as such are not included}` Although, the freemail account is not a requirement, as when creating a new Microsoft account, the user may decide if they do want to reuse their existing email account or create a new mail account. In its free version, the user has the capacity of 5 GB for cloud storage and 15 GB for mail storage, if they have chosen to also create a mail account [[@onedrivePricing]].
This storage can be extended to 50 GB or 1 TB in paid plans, the business plans do start with 1 TB shared or 1 TB per employee.


![[Microsoft 365 Individual Pricing.png|Pricing and feature comparison for Microsoft 365 individual subscription]]

![[Microsoft 365 Business Pricing.png|Pricing and feature comparison for Microsoft 365 business subscription]]

### Identity management

After its creation, the Microsoft account can be used as a single sign-on source for other applications. For more technical users and complex scenarios, the accounts can be assigned to groups within Microsoft Azure portal, though the exact procedure is out of scope for this thesis. For companies, Microsoft also provides advanced security features such as data loss prevention for filtering documents and email messages for company-confidential data, or specifying labels assigned to assets together with polices, that can apply encryption to the data and prevent its accidental leakage [[@microsoftApplyEncryption]].
### Family services

For the Android OS Microsoft provides a Family Safety application. After installing this application on both the parent's and the children's phone, the parents gain the ability take a look at the children's position, be notified when children reach certain locations such as their school or home, or they can impose limits on how much of applications for which time the child can actually use per day. There is also a possibility of recording all his strokes to protect the children against cyber-bullying.[[@microsoftPhoneMonitoring]]  As the application is installed as an administrator of the device, it has the authority to require parent's approval before installation of any new application. Furthermore, when using the Microsoft Edge browser on the smartphone or desktop, the parent can monitor all visited sites and create a whitelist of allowed sites for the child. These features are also available on a desktop version od Edge.

![[Family Safety Members.png|Microsoft Family Safety showing position of children]]

![[Pasted image 20240501184149.png|Microsoft Family Safety asking parent to allow access to application]]

![[Pasted image 20240501184257.png|Microsoft family safety activity overview]]

![[Pasted image 20240501184729.png|Microsoft Family Safety preventing launch of other web browser than Microsoft Edge]]
### Desktop integration

As an operating system from Microsoft, Windows seamlessly integrates with the company's ecosystem of services. Windows also comes preinstalled with OneDrive application or Microsoft Defender, an endpoint malware protection program. Additionally, the operating system features contain also a Microsoft Smart Screen, which verifies the authenticity of applications before launching them. This security measure ensures that only trusted applications are allowed to run on the computer, unless explicitly disabled. When using BitLocker-encrypted hard drive, Microsoft also provides an option to recover encryption keys from the online portal if needed.
## Google

Google is the second large provider of security as a service introduced in this thesis. Unlike Microsoft, which has a large portion of the desktop market, Google has a large coverage of the smartphone market with its Android OS as new devices with this system do often come with pre-installed Google applications. Google is also well-known for its web browser, Google Chrome.
### Cloud services

Google provides various publicly available free services -- perhaps most importantly its free mail service GMail and cloud storage Google Drive. These services come with a shared free 15 GB of storage and do include a full web-based office suite. With a Google One subscription plan, the storage can be extended for up to 2 TB of storage, that can be shared with up to 5 other people. 

![[Pasted image 20240429211526.png|Google One Subscription plans]]

### Smartphone services

When installing new applications through Google Play, the applications have already been processes by Google Play Protect and deemed as non-malicious.[[@googleblogFoughtApps]] Next, because of sometimes slow rolling out of security updates for Android devices by third-party manufacturers, Google has introduces Google Play Services, that can be used to apply security patches even.[[@androidcentralGooglePlay]] To recover misplaced device, Google offers a web portal that is able to contact device and show its real-time location on map or force the device to start ringing. On Android, Google also offers the ability to perform a backup and restore of all apps that support it on a fresh or new device. [[@googleBackRestore]]

### Family services

Similarly to Microsoft's Family Safety, Google presents its own service called Family Link. This service, after linking parent and children accounts, allows for seeing the physical location of the child in real time or for specifying which applications and sites can they access with optionally imposing time limits. The controls can be more granular on per-Google-app basis, meaning that the parent can currently configure control restrictions for:

- Google Play Store
- YouTube
- Google Chrome
- Google search
- Google Assistant
- Google Photos

These restrictions are applied whenever possible, e.g. Youtube and Google search options are enforced whenever the child logs in with their account, while Google Chrome settings are used on all platforms.

![[Pasted image 20240501184116.png|Google Family Link showing the position of children]]

![[Pasted image 20240501184329.png|Child attempting to install application requires approval form Google Family Link]]

![[Pasted image 20240501184528.png|Google Family Link asking parent to approve installation on child's device]]

![[Pasted image 20240501184816.png|Google Family Link preventing the child from accessing disallowed site in Google Chrome]]

Furthermore, the parent can control the whole device more closely, they can remotely lock the device, enable or disable installation of applications outside Google Play, turn developer options on or off or directly manage permissions of each application -- e.g. removing microphone permission from web browser and checking an option that only the parent can allow application to access microphone on the child's device. Next, the parent has a detailed control of the child's Google account -- they can set required parent's approval on every sing-in attempt to the child's account or when the child uses their Google account to sign into third party app. They can also directly change the child's account password or delete the account altogether.
## Apple

Another ecosystem that provides security as a service is the Apple ecosystem. Even though all of the Apple services are mostly closed for devices produced by the company, it provides a wide range of services for them.

### Identity management

Apple provides an option to create a new free account, called Apple ID, for its products. This account is essential for the correct working of Apple-produced devices, as currently, it is needed to be able to install new software from Apple store. Together with this Account, the user may choose to also create a new mail account on icloud.com domain. This account can be subsequently used as a identity source for other services, e. g. it is the only option for SSO login to the Cloudflare Dashboard. The login process to the Apple account itself can be set in such a way so that it requires login confirmation as a MFA on user's existing device.

![[Pasted image 20240430084545.png|Login form for a Cloudflare Dashboard portal]]
### Cloud services

The main point of cloud services provided by Apple for general consumers is its cloud storage iCloud. With a free Apple ID account on a Apple device, the user gets only 5 GB of storage. Though, this storage can be extended with payed subscription. By default, the Apple automatically backs-up both all taken photos to the iCloud and the whole device itself. As this does not require any action to be taken by user, it can be considered as a secure-by-default solution. On the other hand, it can quickly drain the available free storage, pushing user to the payed subscription. Other than this tiered subscriptions, there exists also the possibility to use so-called [Web-only access to iCloud](https://support.apple.com/en-us/102447), which offers only 1 GB of space.

![[Pasted image 20240430085537.png|Payed subscription plans for iCloud]]

Apple also provides a full office suite, available for both all Apple-produced devices and for web access using iCloud.

Another security feature that is available on the Apple devices by default is its password manager iCloud Keychain. This manager is set to auto-fill on the iOS by default and is protected by the same measures as the device's lock screen. 

### Smartphone 

For Apple devices, Apple provides an E2EE communication service called iMessage. However, as with many Apple products, this service cannot currently be used outside of the Apple ecosystem.

For families, it may be useful that the iOS provides a location sharing feature, where one person can select contact which are then able to see the position updated in real time. As with both Google and Microsoft, there is a web UI for locating a misplaced device.

## Proton

Proton is a Swiss-based company providing SaaS focused primarily on privacy. Its services include E2EE mail account Proton Mail with contacts manager, cloud storage Proton Drive and calendar Proton Calendar. Except for that, Proton offers also a no-log VPN service ProtonVPN. The free version of account includes 1 GB of storage for mail, 5 GB of storage for Drive and 1 connected device to VPN. This can be upgraded to 500 GB of total storage shared between mail and Drive for individuals or 3 TB of storage for family tarif. Furthermore, payed tariffs offer the ability to add custom domains for Proton Mail.[[@protonCreateFree]] For the purposes of this thesis, I will consider the Mail Plus plan same as the free plan, as it primarily focuses only on the mail portion of Proton services and as such does not have many of the features of other payed subscriptions.

![[Pasted image 20240501154113.png|Proton pricing plans]]

Unlike Google or Microsoft, Proton Drive does not currently offer any office suite, so all files must be edited externally. On the other hand, Proton provides desktop applications for Windows and Mac, while Linux can be integrated with software such as [rclone](https://rclone.org/protondrive/). The mobile application on Android has the ability to automatically upload all taken photos. All deleted files stay inside trash bin, until it is manually emptied. For payed subscription, the the Drive keeps up to 200 versions of files for up to 10 years. The E2EE is preserved even when sharing files through links and the shares can be password-protected with optional expiration date.

Proton Pass password manager is structured into so-called vaults, which can be shared with other people. In free version, the user can create up to 2 vaults and share it with up to 2 other accounts. For payer plans, the user can create up to 50 vaults, share them with up to 10 other accounts and use the manager also as a TOTP generator. The passwords stored inside the manager can be accessed either through web UI, extension for popular web browsers, native application for smartphone OSs and Windows, with macOS and Linux applications coming soon.[[@protonDownloadProton]] On smartphones, the Proton Pass can be used to auto-fill passwords throughout the system.
## Bitwarden

As special solution for SaaS that does not cover wide range of needs, but instead focuses only one one specific area, I would like to introduce Bitwarden. This solution can be found in [[@Pecuch2021thesis]] and [[@Ciernikova2022thesis]]. Bitwarden is a open-source password manager that is available both as an extension to the web browser and as a native application on most popular platforms. It supports standart features such as auto-filling of passwords, but also advanced features where it can pose as a virtual WebAuthn token. Another service available with a free Bitwaden account is so-called [Bitwaden Send](https://bitwarden.com/products/send/) capable of sending E2EE text as a link with an expiration date and optional password protection.

The Bitwarden also provides a payed subscription tiers for individuals, families and business, where the added features are the option to share saved credentials, send arbitrary files through Bitwarden Send or use the Bitwarden client as an TOTP keychain. For business plans, there is an option to set-up login through SSO. 

## CryptPad

CryptPad is a service that focuses maily on a E2EE cloud storage. It is similar to Proton Drive, but with an addition a full office suite contained inside web-UI. The user can either self-host their own Crypt dat instance, use the [official CryptPad](https://cryptpad.fr/) instance, or use one of [third party instances](https://cryptpad.org/instances/).  When using the official instance, any registered user obtains 1 GB of free storage, while with payed subscription it can be upgraded to to 50 GB. Every stored file can be shared with other users or by a link. A special features are the ability of a document to self-destruct after being opened e.g. by the recipient of the shared link to it and a permanent chat for every document. Additionally to the office suite, CryptPad also integrates a calendar and ability to create virtual teams with multiple users.

A main downside of the CryptPad, for the purposes of this thesis, is the inability to integrate with other systems. To quote directly from the documentation: "The way encryption is currently used in CryptPad does not allow syncing with the local file system." [[@cryptPadFAQ]] This limitation severely decreases the ease of usage as any user must either keep all their document directly in the cloud or export them manually to the local drive. A second largest obstacle, at least for the official instance, is that the maximal size of each file is only 25 MB for free account and 150 MB for the highest tier of payed account.

![[CryptPad main menu.png|The main menu of CryptPad with folder and files selection]]

![[CryptPad sheets.png|Modifying sheet on CryptPad with simple formula]]

![[CryptPad rich text.png|Modifying rich text document on CryptPad]]

## Synology

All of the before mentioned services are sharing the property of being executed in the cloud. As some of the services do require a monthly-payed subscription to function properly, I am presenting a solution that should be capable of handing the needs of the users in a similar manner. 

As the control group, we can include Synology network storage, which is a standalone device that you can purchase for a few thousand crowns when both first-hands or near two thousand crowns when both form a second hand. Even though this device is primarily supposed to be used for storing files, it does actually come with a large plug-in system and the main advantage of Synology is that it actually provide a convenient bridge between using a cloud-based solution and by self-hosting everything yourself, as it does come with very convenient GUI for configuration, which even intermittently or late-beginner users should be able to configure to their needs. This GUI is web-based and after creating a main account, you are able to download more plugins, which include Thunder server, Contacts server, and many more, and one of the main advantages is that on your devices, you have the ability to run self-hosted Docker container, which means that you are able to run pretty much everything. Under the hood, the newer Synology systems do actually use ETRFS by default, meaning that you get support for checksum files to watch for corruption and use your hard drives and software write to have multiple hard drives connected into one for larger storage. A very important feature of Synology is that it is possible to configure something called Synology Quick Connect to be able to access your Synology device remotely, as it does actually This Quick Connect is for up to 250 users and 10 devices, and as you can see, if you configure this yourself, you are able to achieve a self-hosted solution with the obvious downside being the obvious upside of this solution is that you get a solution that you pay only once for, and you get running forever, with the obvious disadvantage of decreased physical security of your data and having to somewhat manage the server itself. Another disadvantage may be that the Synology devices do actually reach the end of their lifetime, and after the EOL, no more security updates may be published, which may actually put your data at high risk if you do not invest into a newer device, even though the old one is still functioning pretty well. Furthermore, Synology does actually provide anti-virus scan for stored files and nice client for full disk backup of your Windows operating system. Another module that Synology provides is a single sign-on server, where you can actually use your configured Synology users as a program source of truth to work into other applications.
