In this chapter, I present selected solutions for all of the profiles. These solutions that fit the profile best are described in more detail and accompanied by the possible solution of using a self-hosted Synology device instead of a cloud service. Even though all solutions try to map to the needs and problems of the presented profile as best as possible, in natural settings, it can be expected that the implemented solution will be a combination of all the presented ones, together with smaller SaaS products tailored for specific needs.

## Low-tech skilled family

As mentioned, the most prominent issues faced were their somewhat outdated and mixed knowledge of best practices. As they do not possess an adequate skill set for completing complex tasks, the solutions for this profile will focus mainly on usability, with a slight compromise on privacy and security. Some of the issues, though, can only be solved by training the user on the best security practices, such as not installing multiple malware protection programs.

### Microsoft

They are already using Windows on their work laptops and have bought a shared one for their kids, so they are already familiar with this environment. This is a significant advantage thanks to the fewer new things to learn. Microsoft provides two services directly tailored for families:

- Microsoft 365 Family subscription that can be shared for up to 6 people and includes access to the up-to-date versions classical end-user software from Microsoft
- Microsoft Family Safety, which provides an assortment of tools for monitoring the well-being of a child

#### Security

As for malware protection, Microsoft offers their Defender for both operating systems utilized by the family. On Windows, Defender is provided without cost and enabled by default. On Android, the Defender needs to be installed separately on every device, together with a valid Microsoft 365 subscription. As this subscription also comes with the newest version of the Microsoft Office suite, it makes the currently used and insecure Office 2010 obsolete, consequently remediating the security threat of opening a maliciously crafted document that exploits known vulnerabilities of the old software.

Using the default web browser on Windows, Microsoft Edge, it is possible to use their Microsoft account to synchronize passwords across all their devices. The saved passwords are automatically filled into web pages. Unlike Google, there is no option to look up saved passwords from a web UI; instead having always to log-into the Edge browser to view the saved passwords. Every time the user wants to show or copy the password manually, they first need to fill in their device login information. [[@edgePassword]] The passwords cannot be copied nor shown if the device has no lock-screen protection set, as shown on `TEX:\hyperref[fig:edgePassw]{figure}`. On Android, the Edge browser offers to generate a strong password when creating a new account, while on Windows, this feature needs to be explicitly turned on first inside browser's settings. [[@microsoftPasswordGenerator]] Lastly, the Edge browser on Android can be set as a service for filling login credentials for all other system applications that support automatic field recognition.

![[Edge Password Copy.png|Password in Edge cannot be shown without a lock-screen in place]]
`TEX:\label{fig:edgePassw}`

If all of the passwords are saved inside Microsoft Edge, the breach of the Microsoft account could lead to a possible breach of all other accounts. For that matter, it is imperative to secure the Microsoft account itself. One of the options that Microsoft provides is to use the account in a passwordless manner, where the user, instead of typing password, uses a smartphone application to confirm login attempts with their bio-metric. [[@microsoftPasswordless]] Because no password is involved, the user does not have to worry about remembering any complex sequence, which is crucial for a user with low password hygiene, as in this profile. Next, as the Microsoft account can be used as an identity source on multiple other web services utilizing OAuth or OIDC protocol, the user can further minimize the number of used passwords while benefiting from password-less authentication even on third-party servers.

#### Privacy

With the main privacy concern for children being that they use shared account on their laptop, the best possible solution would be to implement five distinct account -- one with regular permissions for each child and parent and one with elevated administrator permissions for parents. This will mitigate privacy dangers:

- for children who no longer have to worry about their browsing history being shared or forgetting to log out
- for parents to separate their activity and data from their company-issued laptops

Having a separate administrator account will also improve the overall security standing of the device, as one user cannot simply install a system-wide malicious application. Next, for communication applications, Viber can be replaced by Signal, which focuses on security without compromise and ease of use. On the other hand, neither Signal does persist messages after logging into a new device, unless additional steps are performed.

#### Data retention

To solve the problem with non-redundant backup, the Family 365 subscription offers every member 1 TB of OneDrive storage, which should be enough for the critical data. Furthermore, as OneDrive is integrated into Windows from the installation, it provides a seamless experience to set up and use, together with virtual files. Virtual files are shown as regular files while browsing directories on the disc but are downloaded from the cloud only when explicitly requested, saving space on the local machine. Next, the OneDrive application is also available for Android, where it offers automatic backups of taken photos and video. [[@microsoftAutoUpload]] As OneDrive offers versioning, trashbin and ransomware protection, it is an valid solution to guard against accidental or even malicious data loss. [[@microsoftRansomware]]

Another data loss can currently happen when the Viber application is used as a primary means of communication. Microsoft Teams, part of the Office Suite, may step in as a replacement service. Even though it is a step down in terms of privacy, as it does not provide any form of end-to-end encryption, I would suggest using a service that can archive messages without any user interaction, as losing messages may pose a more significant discomfort to the family than storing the messages on a server with a somewhat reputable company encrypted.

#### Child safety

A specific category for this profile is the need to keep children safe in the virtual and physical worlds. For that matter, Microsoft's Family Safety provides those features, just as explained in previous chapters. By linking parents' and children's accounts, the parents can set up parameters for their children's devices.

### Google

The family already has a Google account for their Android smartphones, so it will not require them to create any new ones. Like Microsoft, Google provides a dedicated service for the security of children. The disadvantage is that neither the Chrome browser nor Google Drive client is installed on Windows devices by default and needs to be downloaded separately.

#### Security

On desktops, the most essential part of security for users may be the Google Chrome web browser. One of the security benefits of using this browser is its built-in phishing protection. [[@blogBrowseSafely]] Next, like the Microsoft Edge, the Chrome browser has an inbuilt password manager. On the desktop, the password manager works similarly to the Edge browser, offering the option to be notified when any saved passwords are found within the list of known breached passwords. The main difference is that, when signed into the account, the passwords can also be shown within the Google [passwords web portal](https://passwords.google.com/), making accessing the passwords on any device easier. On Android, after signing in with their account, Google offers to save and auto-fill saved passwords by default, making the process frictionless. As with Microsoft accounts, when all passwords are being stored within the same account, e.g. email, a simple breach of this account could result in a breach of all accounts for which the user has saved credentials.

As for the vulnerable office suite, Google provides its full-web-based office suite within Google Drive. As all documents are edited within the web browser, this solution should not possess any security vulnerabilities that are not present inside the browser itself. On the other hand, this suite may pose some compatibility problems that are explored more within the Data retention section. To further strengthen the security of the files stored on Google Drive or received to a Gmail account, Google scans all files for malware or possible phishing documents. [[@bleepingcomputerGoogleDrive]].

#### Privacy

To solve the most notable privacy problem -- the children sharing the same account on their shared laptop- Google provides an option to define multiple Google Chrome profiles, each with its own settings and active accounts. In contrast to creating multiple user accounts, this solution works more on a trust-based approach in that the other child will not internationally launch another child's profile. However, it is easier to set up than creating a new Windows account. 

The user may use Google Duo for calls to replace Viber, but no suitable replacement for text messages exists.

#### Data retention

As Google Drive can be upgraded to up to 2 TB of available storage with the shared Google One subscription, this should still be enough for the family data. However, it is a several step down from the total of up to 6 TB of storage for Microsoft's One drive. For Windows, the user may download the Google Drive application to access and synchronize stored files. All supported platforms, including smartphone apps, can make specific files available even when not connected to the internet.

Given that Google has its storage format for the Office suite, and even though it offers most of the features that the user may need, it may only partially support some features available in Microsoft Office. Conversion from the Microsoft Office format into the format used by Google Drive may maintain some special formatting, resulting in partial data loss. Furthermore, editing any documents from Office suites makes it less comfortable. Next, the user needs to install a Chrome extension to edit documents offline.[[@googleDriveOffline]] Google Drive offers a trash bin and version control, with a detailed differentials version history for the office documents.

#### Child safety

In addition to similar features in Microsoft Family Safety, the Google Family Link provides more direct control over children's accounts. By allowing the parent to allow the child to use SSO only for applications that do not require permissions except for name, email, and profile picture, the child can safely log into any application without worrying about giving too much access to the account. 

### Synology

Given that Synology requires an initial setup, it may be necessary for the family to consult with a professional for the initial setup. Even after that, Synology does not provide easy solutions to all outlined problems, and the family will need to keep care of the device -- e.g., monitoring that the device is not after its end of life and still receives regular security updates.

#### Security

To replace the vulnerable Microsoft Office suite, Synology does offer its office suite as a downloadable package for some of its models. This office suite works similarly to the Google Drive office suite, as it employs its storage format and, as such, requires importing and exporting when working with third-party office suites. [[@synoOffice]] This again presents the possible problem of some features not being fully supported by the Synology office.

Next, there needs to be a password manager from Synology. Of course, it is possible to self-host a password manager such as BitWarden using the generic Docker container feature of some of the Synology models. However, I advise against that, as the family members cannot be expected to maintain a self-hosted password manager in a secure and safe manner.

Even though Synology can be used as an SSO source, it first needs to be configured as such with any application that should support it, making it unfeasible for the family.

#### Privacy

Except for the obvious advantage that the data does never leave family-owned devices, the most prominent way how Synology may improve privacy is if all the users keep most of their files only stored there, as then they are protected by their account credentials as opposed to having the files synchronized with the shared computer account. The Viber can be replaced by a Synology Chat package that allows basic chatting while outsourcing video and audio calling to third-party applications such as JumpChat and Jitsi. [[@synoChat]]

#### Data retention

Given that Synology works with the hard drives that the user directly supplies, they significantly impact how resilient the system will be. As the storage is a single-time investment, the hard drive is expected to have more capacity than the 6 TB offered by the Microsoft O365 family subscription. Furthermore, we can probably expect the user to have only one hard drive or set up RAID 0 to maximize the available storage, so the failure of one disc may mean an unrecoverable loss of stored data. To combat this, the user may set up a secondary backup solution, e.g., CloudSync or an in-built Amazon Glacier backup. However, both options require additional setup, possibly too complex, while inquiring more costs.

On the other hand, users may synchronize files from their computers automatically or have their taken media uploaded from their smartphones to store the original data directly on the user's device. When files are modified or deleted, Synology provides both trash bin control and restoring old versions, with the office package providing an convenient user interface for the view of performed changes.

#### Child safety

As there is no direct control over what content children can access or directly monitor the child's online activity, the options for the child's safety are severely limited. A third-party application may be recommended to monitor at least the children's position. As an example, the family can install an application called Find My Device (FMD) [[@fdroidFindDevice]], which is capable of responding to commands sent over SMS, so it does not need to rely on any specific service.

### Unsolved problems

Unfortunately, not all problems can be solved directly by these services, as they are too complex or out of scope. The first example of this may be the use of outdated Android devices, where the best option may be to buy new devices with a declared duration of security updates. As for an outdated router from the ISP, the best course of action may be to ask the ISP to replace it, as the family cannot be expected to manage their router securely. Related to their router is creating a WiFi network for guests, where a router with a user-friendly web interface may help. Creating a separate WiFi network would also help with moving less-trusted devices into the more isolated network.

As for the possible privacy concerns of using the company-provided laptop for personal activities, here the user needs to consult their company laptop usage policy or contact their IT department. The last need that was not covered is performing a backup of the cloud storage service, such as when the account is compromised and all data falls victim to, e.g., a ransomware attack, there is an option to restore said data. Solving this problem would increase the complexity of the solution, while the currently proposed solutions have already severely increased data security.

## Low-tech skilled university student

The specificity of low-tech skilled university students is in the closeness of the Apple ecosystem combined with a Windows laptop.

### Apple

As the student is already using their smartphone as their main device, they are already used to services provided by Apple by default. Furthermore, as the services are well integrated into iOS, it would be helpful to have a solution that uses the same services on other platforms.

#### Security

The most crucial security aspect to cover for this profile is the missing MFA for the primary mail account hosted on Seznam. For this, there exist three solutions:

- moving away from Seznam to iCloud mail, which has integrated MFA confirmation into the iOS

- install a separate [Seznam application](https://apps.apple.com/us/app/seznam-cz/id950278657) to approve login
- utilize Apple KeyChain as a TOTP code generator

The first solution is time-consuming and, as some services do not allow changing email addresses after account creation, potentially impossible. The second solution is the most secure, as the user can review every login login and act accordingly, but it requires additional application installation.

The third solution may be the most viable, as it uses an application that the user is already comfortable with. This solution also contributes to the user's need to synchronize the password to their desktop, as all the user needs to do is install iCloud for Windows and a web browser extension. [[@appleICloudPasswords]]

![[Pasted image 20240506163134.png|Apple KeyChain providing the option to add TOTP]]

#### Privacy

By default, iCloud Drive offers encryption in transit and at rest, which should be enough for regular use. Furthermore, when combined with the MFA-protected Apple ID account, no unauthorized party should be able to access the stored data.

#### Data retention

If the users purchase at least 200 GB of storage, it should be enough to store all their critical data. Unlike other cloud storage providers, Apple does not support versioning files, but only allows of restoration of deleted files from the trash bin. [[@appleVersionHistory]] This may become a disadvantage if the users accidentally rewrite their files, e.g., when using an external office suite and saving an empty document instead of an existing one. The taken photos are uploaded automatically from iOS by default, while for synchronization with a Windows computer, the user needs to download and install the iCloud application.

### Microsoft

Microsoft's main advantage over services provided by Google is its already present integration of Microsoft Edge and OneDrive into the Windows OS. Its solutions are also slightly cheaper than comparable products. Furthermore, as the student is already using O365 via its university subscription, they already have all services free of charge for the length of their studies.

#### Security

As with Apple, there is an option to use the TOTP secret in the Microsoft Authenticator application, which users should already use if they have MFA enabled for their Microsoft account.

As presented in the solution to the family profile, Microsoft Edge can hold and synchronize saved passwords to multiple sites. Same as on Android, Microsoft Edge can be changed as the default auto-fill source inside the iOS settings, solving the password management and synchronization between different platforms and systems.

#### Privacy

Same as the default settings of iCloud Drive, the data is encrypted both in transit and at rest. The protection of the Microsoft account with MFA enabled using Microsoft Authenticator is comparable to the security of Apple ID account.

#### Data retention

As more than 100 GB of storage may be needed for all documents and photos, the next available tier has a storage size of 1 TB. Compared to iCloud Drive, OneDrive offers support for file versioning.

As OneDrive is already included in the Windows OS, users do not have to install anything new. On iOS, they need to download the OneDrive application, which can automatically upload photos and videos.

### Synology

For the individual student with low-tech skills, purchasing a Synology device may be too expensive and overly complex to set up. Furthermore, as the student can be expected to be travelling between their home, dormitory and school, they need to think about the device's physical placement in case of the device or power failure.

#### Security

As there is no direct option to perform password management or storing MFA tokens instead of directly hosting Docker containers, I conclude Synology as unsuitable for this profile.


#### Privacy

As with the family profile, Synology's main advantage in terms of privacy is that the data are stored on the user-owned device. Other than that, for the purposes of this profile, there are no significant privacy features.

#### Data retention

For the purposes of this profile, there is no significant difference in terms of features when compared to the Microsoft OneDrive. The most crucial difference is that the user is now responsible for managing the storage device.

## Individual tech-skilled user

As this user is more experienced, we can expect them to be able to understand or create their own even more complex solutions. First, as this profile is more interested in privacy, they may consider switching from their main Google account to Proton, which offers features similar to those the user currently uses. A second advantage of Proton is that it offers a private VPN service that solves the need to protect their device when connecting to untrusted networks.

Next, one of the needs of this profile is to create a distinct account for password management and for other actions. As a separate account for password management, the user may consider BitWarden password manager. This manager is available for all user platforms, can be accessed through web UI so that the user does not need to install additional software, e.g. on university computers, and can also be used to auto-fill on smartphones and web browsers via extensions.

### Google

The student already uses a Google account for their daily tasks, so they do not need to create any new accounts for this service. Its main advantage over Microsoft is its always-free tier with VPS, so the student does not need to worry about checking when their free starting credit will run out.

#### Security

For hosting the Minecraft server for their friends, it is possible to set up the free Google VPS, which is doable either with experience or by following some online hosting tutorials. By default, as the Google VPS's shell can be accessed directly through web UI and the firewall allows only a limited number of ports, this leaves out the need to manage SSH keys or restrict access with a manual firewall configuration, simplifying the process. Furthermore, by moving the hosting away from the student's device, they achieve higher uptime and, in case of compromise of the Minecraft server, security for the data on the student's device.

#### Data retention

To solve the double-backup problem, which could serve as a last resort in case a malicious party gains access to the currently used cloud storage and purges original files even from the trash bin, Google offers an S3-API compatible solution called Google Storage. With only 5 GB of free storage, the user must change to a paid subscription. The user may set up a system schedule to copy all their local files or whole Google Drive into this remote storage with a program such as [rclone](https://rclone.org/googlecloudstorage/). As this setup setup is more complicated, it can be severely simplified with the usage of Synology, as shown below.

### Cloudflare

Even though Cloudflare is more business-oriented, it may prove usable for some student dues due to its provided hosting and tunnelling solutions, data storage and VPN.

#### Security

Even though Cloudflare does not allow it to host the Minecraft server directly, its ZeroTrust network can replace the currently used LogMeIn Hamachi. It can be configured as a direct replacement, where the routes are configured to point to the friend group devices, providing no additional benefit.

The second option requires configuring a tunnel pointing to the student's device and selecting which port should be forwarded. This approach provides additional security because only required ports are exposed, decreasing the possible attack surface.

#### Privacy

To solve the issue of privacy and security threats of connecting to untrusted networks, the student may use the free VPN software 1.1.1.1.

#### Data retention

Similarly to Google, Cloudflare provides its S3-API-compatible storage called R2. As the provided free storage is only 10 GB of space, it is reasonable to expect that the user will be required to pay a monthly fee for the stored data. The storing procedure may be the same as outlined for the Google solution.

### BackBlaze

As BackBlaze is a service specializing only in data backup, it cannot cover most of the user's needs, except for the double backup. The first option that BackBlaze offers is its B2 Cloud Storage, which has an S3-compatible API and can be used in the same way as Google Storage or Cloudflare R2. 

The second option is the unlimited personal backup for \$99 per year, which the user may install on their Windows laptop to perform a full backup of their data, together with versioning.

### Synology

For this profile, Synology may solve many needs alone or with other presented services.

#### Security

Like a VPS, Synology can run arbitrary software as a docker container. This means that Synology can host the Minecraft server, achieving a higher uptime than on a laptop and security for the same reasons shown within the Google solution. Remote access to Synology can then be provided by Cloudflare or through a third-party virtual network provider with a step-by-step guide such as [ZeroTier](https://docs.zerotier.com/synology/).

#### Data retention

Synology provides an option to perform a backup to Amazon Glacier via an official package. Another option may be to use a CloudSync package capable of synchronizing with a remote endpoint and optionally encrypting data on the remote side. Two of the previously shown solutions for this profile -- Google Cloud Storage and BackBlaze B2 -- are directly supported, so setting them up for backup is relatively straightforward. To use Cloudflare R2 as a backup endpoint, the CloudSync package supports a generic S3-compatible API endpoint.

### Unsolved problems

One of the current problems that cannot be solved easily is the deletion of forgotten accounts, as no presented service currently automates this process. The first step to deleting old accounts is to find out which accounts exist. This can be significantly simplified if the user has already used password management software so that they can search for saved accounts there. Otherwise, they may need to determine if the email address for every service in question is used. After the services and accounts are identified, they may use a service such as [Just Delete Me](https://backgroundchecks.org/justdeleteme/) that lists many services and steps or direct links to delete accounts for them.

The second unresolved problem is for the E2EE chat application, where the user uses Telegram. One option to achieve E2EE for one-to-one conversations would be to turn on the Secret chats feature, but another application must be used for group conversations. Here, an alternative could be presented Signal, which uses E2EE by default for everything or WhatsApp, which does collect and store some data about user's communication unencypted [[@FBIDataMessenger]].

A third unresolved issue is the smartphone endpoint protection, where, in addition to the already used-by-default Google Play Protect, the student may install additional applications, such as Microsoft Defender, if provided by the university.

## Small technology company start-up

The specificity of the small-technology start-up profile is that when services are unavailable, it may lead to revenue loss. As the start-up has a higher budget than students and is staffed with IT professionals, it is possible to present more complex solutions that may take a significant amount of time to set up.

### Microsoft

As Microsoft provides a range of services for cloud management for companies, it is possible to resolve the needs of this profile by moving the infrastructure to the cloud. However, given the volume of different services and configuration options, the administrator may require some training before securely setting up the whole system.

The company IT administrator may start by creating a new Microsoft Entra ID (previously known as Azure Active Directory) instance, with which the company gains the possibility to structure company employees into groups, making the process of moving into the least-privilege access philosophy easier. With a Microsoft account, employees are now able to use the account as an SSO source for multiple applications. Furthermore, suppose a web application is not configured to support SSO login (such as companies Jenkins). In that case, it can be placed behind Azure's built-in authentication mechanism, which will first require the user to authenticate against it before any request is left to pass to the target application.

Azure directly supports managing VMs, solving the need for a more scaleable approach. Next, the company can directly register a new domain name with an automatic generation of a TLS certificate, making the internal custom top-level domain with custom DNS obsolete. When everything is moved into the cloud, there is no longer any need for a VPN server to be used on the internal company network. 

For secure storage and sharing of files, employees may use their OneDrive subscription, which offers 1 TB per employee, which should be enough for generic company data. To share secrets that should not be stored directly on OneDrive, the company may use Azure Key Vault, which offers secure storage and management of secrets and certificates.

The last need is centralized device management, which can be solved by Microsoft Intune, which directly supports enrolling macOS and iOS devices.

### Google

Google offers services similar to Microsoft's, though under different product names. To secure access to the web application with the Zero Trust access model, the administrator may use the Identity-Aware Proxy. Like Microsoft, Google offers automatic setup and renewal of TLS certificates. For secure sharing of files, the users may use Google Drive to share secrets with the Secret Manager. Device management can be done with the Google device management software.

Where Google differs from Microsoft is the storage space available to the users. In Google's case, the storage is set at 2 TB, but it costs roughly double the price of Microsoft's solution. Furthermore, O365 for business offers a Microsoft Teams subscription capable of performing video and chat messaging, while Google Workspace offers only video conferences. The second difference is that Google no longer offers domain registration, as it was outsourced to Squarespace on September 7 2023. [[@googleDomains]]

### Synology + Cloudflare

Even though Synology itself does support a wide range of needs for this profile, it lacks the option to create a VPN server with MFA, purchase a custom domain, or protect hosted applications with zero trust. To solve this, the administrator can set up a Cloudflare tunnel on the Synology device to connect it to the Cloudflare Zero Trust. As the Synology account offers MFA protection and can be used as an OIDC-compatible SSO source, by exposing the Synology DSM interface either via QuickConnect or via the publicly accessible tunnel, the Cloudflare Zero Trust can be set to perform authentication via the local Synology accounts.

By using the Cloudflare WARP clients on the company devices, the employees can connect to the hosted Synology device after logging in through the SSO. The advantage of connecting the company device via the WARP client is that the Cloudflare administrator can see basic information about connected devices and linked users, posing as a basic form of centralized device management.

Even when not connecting via the public internet, Cloudflare offers to set up zero trust authentication before letting the requests pass through, similar to the Google and Microsoft solutions. Cloudflare does offer domain registration, with all tunnels having a valid HTTPS certificate for their subdomains, regardless of whether the target service uses HTTP or HTTPS.

Synology has to ability to run arbitrary docker containers or whole virtual machines, so hosting company's services is simple and manageable. Synology also offers per-user or per-group permissions, making it easy to implement least-privilege access. As a NAS device, sharing files is one of its core features, mainly when combined with the encryption of data on rest, which Synology natively supports.

The obvious drawbacks of this solution still persist, where Synology still poses as a single point of failure in case of power outage or connectivity downtime. Next, the physical security of this device is more important than with other profiles, as accidental dropping or theft of the device could lead again to service unavailability or company-confidential data leakage. Lastly, there is a need for a password manager or secret-sharing software capable of sharing passwords and secrets, where, like for other profiles, an external service such as Bitwarden needs to be used.