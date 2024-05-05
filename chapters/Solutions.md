## Low-tech skilled family

As mentioned already before, the most prominent issues faced from their somewhat outdated and mixed knowledge of best practices. As they do not possess adequated skillset for completing complex tasks, the solutions for this profile will focus mainly on the usability aspect with a slight compromise on privacy and security. Some of the issues though cannot be solve other than by training the user for the best security practices, such as not installing multiple malware protection programs.
### Microsoft

Given that they are already using Windows on their work laptops and have bought a shared one for their kids, they are already familiar with this environment, which is a large advantage thanks to lower number of new thing to learn. Microsoft provides two services directly tailored for families:

- [Microsoft 365 Family subscription](https://support.microsoft.com/en-us/office/share-your-microsoft-365-family-subscription-b389b9ce-3ae3-4a82-9017-39d79972fcba#bkmk_benefits) that can be shared for up to 6 people and includes access to the up-to-date versions classical end-user software from Microsoft
- Microsoft Family Safety which provides an assortment of tools for monitoring the well-being of a child

#### Security

As for malware protection, Microsoft offers their Defender for both operating systems utilized by the family. On Windows the Defender is provided without any cost and comes enabled by default, while for Android it needs to be installed separately on every device together with a valid Microsoft 365 subscription. As this subscription also comes with the newest version of the Microsoft Office suite, it makes the currently used and insecure Office 2010 obsolete, consequently remediating the security threat of opening a maliciously crafted document that exploits known vulnerabilities of the old software.

By opting to use the default web browser on Windows, Microsoft Edge, it is possible to use their Microsoft account for synchronizing passwords across all their devices. The saved passwords are be automatically filled into web pages. Unlike Google, there is no option to look up saved passwords from a web UI, instead having always to log-into the Edge browser to view the saved passwords. If the user wants to show or copy the password manually, they first need to [fill-in their device log-in information](https://support.microsoft.com/en-us/topic/edit-your-passwords-in-microsoft-edge-38ef988f-5a65-4c6a-9db8-937995d3ae31). The passwords cannot be copied nor shown if the device has no lock-screen protection set, as shown on `TEX:\ref{fig:edgePassw}`. On Android, the Edge browser offers to generate a strong password when creating new account, while on Windows this feature needs to be explicitly turned on first inside [browser's settings](https://www.microsoft.com/en-us/edge/features/password-generator?form=MA13FJ). Lastly, the Edge browser on Android can be set as a service for filling login credentials to all other system application that support automatic field recognition.


![[Edge Password Copy.png|Password in Edge cannot be shown without a lock-screen in place]]
`TEX:\label{fig:edgePassw}`

If all of the passwords are saved inside the Microsoft Edge, the breach of the Microsoft account could lead to a possible breach of all other accounts. For that matter, it is imperative to secure the Microsoft account itself. One of the options that Microsoft provides is to use the account in a [passwordless](https://support.microsoft.com/en-us/account-billing/how-to-go-passwordless-with-your-microsoft-account-674ce301-3574-4387-a93d-916751764c43) manner, where the user, instead of typing password, uses an smartphone application to confirm log-in attempts with their bio-metric. Because there is no password involved, the user does not have to worry about remembering any complex sequence at all, which is crucial for an user with low password hygiene as in this profile. Next, as the Microsoft account can be used as a identity source on multiple other web services utilizing OAuth or OIDC protocol, the user can further minimize the number of used passwords while benefiting from the password-less authentication even on 3rd party servers.
#### Privacy

With the main privacy concern for children being that they use shared account on their laptop, the best possible solution would be to implement five distinct account -- one with regular permissions for each child and parent and one with elevated administrator permissions for parents. This will mitigate privacy dangers:

- for children that do not have to worry about their browsing history being shared or forgetting to log out
- for parents to separate their personal activity and data from their company-issued laptops

Having a separate administrator account will also improve the overall security standing of the device, as one user cannot simply install a system-wide malicious application. Next, for communication applications, the Viber can be replaced by Signal, that focuses on security without compromise and ease of use. On the other hand, neither Signal does not have an advantage in the area of data retention and chat message transfer, both of which need to be taken into an account when purchasing a new device.
#### Data retention

To solve the problem with non-redundant backup, the Family 365 subscription offers every member 1 TB of OneDrive storage, which should be enough for the important data. Furthermore, as OneDrive is integrated into Windows from the installation, it offers a seamless experience to set up and use, together with so-called virtual files. Virtual files are files that are shown as regular files while browsing directories on the disc, but are in fact downloaded from the cloud only when explicitly requested, saving space on local machine. Next, the OneDrive application is also available for Android, where it offers [automatic backups](https://support.microsoft.com/en-us/office/automatically-save-photos-and-videos-with-onedrive-for-android-66605e54-48b8-4f55-bcff-34159702e344) of taken photos and video. As OneDrive offers versioning, trashbin and [ransomware protection](https://support.microsoft.com/en-au/office/ransomware-detection-and-recovering-your-files-0d90ec50-6bfd-40f4-acc7-b8c12c73637f), it is a good solution to guard against accidental or even malicious data loss.

Another data loss can currently happen in relation to the Viber application being used as a main means of communication. Here, the Microsoft Teams, which is part of the Office Suite may step in as a replacement service. Even though it is a step down in terms of privacy, as it does not provide any form of end-to-end encryption, I would suggest using a service that is able to archive messages without any user interaction, as loosing messages may pose larges loss to the family than storing the messages on a servers with a somewhat reputable company.

#### Child safety

A specific category for this profile is the need of keeping the children safe both in virtual and physical world. For that matter, Microsoft's Family Safety provides those features, just as explained in previous chapters. By linking parents and children accounts, the parents can set-up parameters for their children devices.
### Google

As the family already has a Google accounts for their Android smartphones, it will not require them to create any new. Similar to the Microsoft, Google provides a dedicated service for the security of the children. The disadvantage may be that neither the Chrome browser nor Google Drive client is not installed on Windows devices by default and needs to be downloaded separately.
#### Security

On desktop, the most important part of security for the users may be the Google Chrome web browser. One of the security benefits in using this browser is its inbuilt phishing protection. [[@blogBrowseSafely]] Next, similarly to the Microsoft Edge, the Chrome browser has inbuilt password manager. On desktop, the password manager works similar to the Edge browser, offering the option to be notified when any of the saved passwords is found withing the list of known breached passwords. The main difference is that, when signed into the account, the passwords can be also shown within the Google [passwords web portal](https://passwords.google.com/), making it easier to access the passwords on any device. On Android, after sing in with their account, Google offers saving and auto-filling saved passwords by default, making the process friction-less. As with Microsoft account, when all passwords are being stored within the same account as e.g. email, a simple breach of this account could result into a breach of all account that the user has saved credentials for.

As for the vulnerable office suite, the Google provides its full-web-based office suite within Google Drive. As all documents are edited within the web browser, this solution should not possess any security vulnerabilities that are not present inside the browser itself. On the other hand, this suite may pose some compatibility problems that are explored more within the Data retention section. To further strengthen the security of the files stored on Google Drive or received to a GMail account, Google scans all files for malware or possible phishing documents. [[@bleepingcomputerGoogleDrive]].
#### Privacy

To solve the most notable privacy problem -- the children sharing the same account on their shared laptop -- Google does provide an option to define multiple Google Chrome profiles, where each of them has its own settings and active accounts. In contrast to the solution of creating multiple user accounts, this solution works more on a trust-based approach that the other child will not international launch other child's profile, but on the other hand is easier to set-up than creating a new Windows account. 

To replace Viber, the user may use Google Duo for calls, but there does not exist any suitable replacement for text messages.

#### Data retention

As Google Drive can be upgraded up to 2 TB of available storage with the shared Google One subscription, this should still be enough for the family data, though is a several step down from the total of up-to 6 TB of storage for Microsoft's One drive. For Windows the user may download the Google Drive application that will then allow them to access and synchronize stored files. All supported platforms, including smartphone apps, have the ability to mark certain files to be available even when not connected to the internet.

Given that Google has its own office suite with its own storage format and even though the suite offers most features that the user may need, it may not fully support all features that are available in the Microsoft Office. Conversion from the Microsoft office format into the format used by Google Drive may loose some of the special formatting, resulting into a partial loss of data. Furthermore, it makes it overall less comfortable to edit any documents from office suites. Next, to be able to edit documents offline, the user needs to install a Chrome extension.[[@googleDriveOffline]] Google Drive offers a trash bin and a version control, with a detailed differentials version history for the office documents.
#### Child safety

Additionally to the similar features in Microsoft Family Safety, the Google Family Link provides more direct control over the children account -- e. g. by allowing the parent to only allow the child to use SSO to application that do not require permissions except for name, email and profile picture, the child can safely log into any application without worrying about giving too much access to the account. 
### Synology

Given that the Synology requires an initial setup, it may be needed for the family to consult with a professional for the initial setup. Even after that, Synology does not provide easy solution to all outlined problems and the family will need to keep care of the device -- e. g. monitoring that the device is not after its end of life and still receives regular security updates.
#### Security

To replace the vulnerable Microsoft Office suite, Synology does offer its own office suite as a downloadable package for some of its models. This office suite works similarly to the Google Drive office suite, as it employs its own storage format and as such requires importing and exporting when working with third party office suites. [[@synoOffice]] This again presents the possible problem of some features not being fully supported by the Synology office.

Next, there is no password manager from Synology. Of course it is possible to self-host a password manager such as BitWarden using the generic Docker container feature of some of the Synology models, but I would advice against that as the family members cannot be expected to maintain self hosted password manager in a secure and safe manner.

Even though Synology can be used as a SSO source, it firsts needs to be configured as such with any application that should support it, making it unfeasible for the family.
#### Privacy

Except for the obvious advantage that the data does never leave family's owned devices,the most prominent way of how Synology may improve the privacy is if all the users do keep most of their files only stored there, as then they are protected by their account credentials as opposed having the files synchronized with the shared computer account. The Viber can be replaced by a Synology Chat package, that allows for basic chatting, while outsourcing video and audio calling to third-party applications such as JumpChat and Jitsi. [[@synoChat]]
#### Data retention

Given that the Synology works with the hard drives that are directly supplied by the user, they have a large impact on how resilient the system will be. As the storage is a single-time investment, it can be expected that the hard drive will have more capacity that the 6 TB offered by Microsoft O365 family subscription. Furthermore, we can probably expect the user to have only one hard drive, or set up RAID 0 to maximize the available storage, so the failure of one disc may mean a unrecoverable loss of stored data. To combat this, the user may set-up a secondary backup solution with e.g. cloud sync, or in-built Amazon Glacier backup. Though, both of these options require additional, possibly too complex, setup, while inquiring more costs.

On the other hand, the users may synchronize files from them computer automatically or have their taken media uploaded from their smartphone, so that the original data is still stored directly on the user's device. When files are modified or deleted, Synology provides both trash bin control and restoring old versions, with the Office package providing a nice user interface for the performed changes.
#### Child safety

As there is no direct control over what content can children access or directly monitor the child's online activity, the options for the child safety are severely limited. To be able to monitor at least the position of children, a 3rd party application may be recommend. As an example, the family can install an application called Find My Device (FMD) [[@fdroidFindDevice]], that is capable to respond to commands sent over SMS, so it does not need to rely on any specific service.
### Unsolved problems

Unfortunately, not all problems can be solved directly by any of these services, as they are either too complex or out of scope. First example for this may be the use of outdated Android devices, where the best option may be to buy new devices with declared duration of security updates. As for outdated router from ISP, the best course of action may be to ask the ISP to replace said router, as the family cannot be expected to manager their own router in a secure manner. Related to their router is a creation of a WiFi network for guests, where a router with an user-friendly web interface may help. Creating a separate WiFi network would also help with moving less-trusted devices into the more isolated network.

As for the possible privacy concerns of using the company-provided laptop for personal activities, here the user needs to consult their company laptop usage policy or contact their IT department. Last need that was not covered is performing a backup of the cloud storage service, such as even when the account is compromised and all data falls victim to e.g. ransomware attack, there is an option to restore said data. Solving this problem would increase the complexity of the solution, while the currently proposed solutions do already severly increase the data security.

## Low-tech skilled university student

- iCloud 
- Chrome??
- BitWarden
- MFA-protected main account
- Signal, Element
- Synology added, 

## Individual tech-skilled user

- CloudFlare for self hosting
- Google as main, also free VPS
- Does Microsoft have free VPS?

## Small technology company start-up

- Microsoft for cloud
- Cloudflare for self-hosting