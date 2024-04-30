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

#### Security

#### Privacy

#### Data retention

#### Child safety

### Synology

#### Security

#### Privacy

#### Data retention

#### Child safety

### Unsolved problems
- outdated android devices
- outdated router
- privacy on work laptop
- smart TV on separate network
- double backup (but not needed)
- handling of smart devices
- guest WiFi network

--- 

- need help with setup
- cover sync
- still can be broken
	- azure glacier

- Microsoft
	- integrated OneDrive
		- buy 1 TB
	- Family link
	- Edge
	- Teams? Signal?
- Google
	- Chrome -- needs to be downloaded

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