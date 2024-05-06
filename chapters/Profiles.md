For the purposes of this thesis, I have prepared four profiles on which possible security, privacy and data retention threats may be presented. Each of the profiles is representing a typical user archetype. All data from which the profiles were created was obtained from discussion with relevant parties and personal experience. For the creation of each of the profiles, no less than 3 real-life samples were used, while the focus was more laid onto the negative patters observed as to better highlight solutions to the issues existing in the wild.
## Low-tech skilled family

A first introduced profile is of a family with middle-aged parents and two young children (aged 12 and 8). Any member of the family is expected to have a non-IT related education and occupation and as such also a small technology skill set, ranging on a average Digital competence level 3 [[@OECDSkillsMatter]]. Both parents work in accounting and were issued a laptop from they employer, the kids use a second-hand laptop with shared account.

### Hardware settings

As mentioned above, both parents were provided a laptop from work, while the kids received a single Windows laptop shared between them. Each family member also posses an older personal lower-to-mid range Android smartphone (priced under 7 000 Kč). To use as a backup solution of their most important data, the family has purchased a single 8 TB external HDD. Other than that, the family has one large-screen TV with Tizen OS. All devices are connected to a Wi-Fi router with single AP running.

### Software settings

All of their laptops are running Windows OS, while admin-level permissions are available only on their shared laptop. The family does not (intentionally) use any cloud service for storing data. Their family chat is primarily located on Viber, whereas children use Instagram as their main application to stay in touch with their friends. For their personal office works and for children's school purposes they are using a Microsoft Office 2010 suite, which they have payed for in the past. They are using default web browsers for each platform, meaning Chrome for their Android phones and Edge on their laptops.

### Digital hygiene

As their technological knowledge is in the level 3 range, they are supsectible to adverts and recommendations for software, resulting in multiple antivirus softwares and computer-cleaning programs being installed superfluously at once. They are also not bothered by any type of pop-up dialogs or warning, as they simply select continue on anything. During the early days of Internet, it was a common knowledge that anything uploaded to the Internet will forever stay on the Internet. For that matter, they are reluctant to intentionally (e.g. Viber uses Google Drive in background for message backups) use any cloud service. They have started with a Seznam.cz account for freemail services, but with the comming of Android phones, they have added a Google account for everyone. Nowadays they have multiple accounts for various social media (Facebook, TikTok, Instagram), hobby sites and so on. They are using two separate passwords, one "strong" for critical accounts (online banking and primary email account) and one easy-to-remember for all other accounts.

### Possible problems that are already solved

The family has already solved, or partially solved, some of possible issues that may arise from their common operations. Perhaps most importantly, the family does perform backups in some form. This is true both for their shared data (on external HDD) and for their Android phones, which do have backup to Google drive offered as default option. Next, the users are at least aware of basic security practices, so they are using antivirus software and more than one password. Finally, because their home network was set-up by their ISP, it can be considered as resilient and properly configured.

### Faced problems with current approach

There are numerous problems with the current approach that can be divided mainly into categories of privacy and computer security. To start with the security related issues, because the Android smartphones are older and were in the lower-to-mid price range, there is a good chance that they do no longer receive any security updates, meaning that any known security vulnerability may be exploited. This makes theses devices inappropriate for use with any personal data, especially baking applications with financials. As for their shared laptop, Office 2010 is [no longer supported](https://support.microsoft.com/en-us/office/end-of-support-for-office-2010-3a3e45de-51ac-4944-b2ba-c2e415432789), which in combination with their low digital competence may make them vulnerable to serious phishing and advertising attacks. The severity of this issue is also reinforced by using only two different passwords, where breach of at least one of them will result into a possible breach of multiple accounts. They are also unable to use the password manager built-into the web browser, as they use a different browser on every platform. Lastly, depending on their ISP, it is possible that they were issues an outdated router without relevant security patches, which may be issue mainly with smaller ISPs within less-densely populated areas.

As for privacy, the most notable issue can be found within the shared laptop, where issues may arise from one of the children forgetting to log out of their session without the web browser. On the other hand, the parents are using work laptops for personal agendas, which may be closely monitored by their employer (depending on the policy deployed by the company). The third risk for privacy is their smart TV which may audio of their conversation and send it for analysis to another worker without the knowledge of family. A final privacy risk may be linked with end-to-end encrypted chatting application Viber, which lists privacy as important aspect of this service ("Our mission is to protect your privacy so that you never have to think twice about what you can or can't share when you're using Viber." [[@viberHomeViber]]), but still stores a large collection of metadata on its servers. [[@FBIDataMessenger]]

A third category of problems consist of data retention and recovery. Even though the disc used for backup does provide a basic level of redundancy, it can still be easily destroyed e.g. by dropping it, by mistakenly deleting wrong files or simply by connecting it to a infected device. Furthermore, this solution lacks the ability to be performed automatically, which may result to the backups being severely outdated. A though must also be put into backing up of their family conversation on Viber, where all messages are lost after on-boarding on a new device unless backup was enabled. [[@ViberRestoreChat]]

### Needs that are currently not covered

Some of the needs that are currently not covered were already outlined within the current problems, namely a redundant backup solution prone to accidental or malicious deletion, with automatic schedule set to prevent backups being out of date. Next, the family is unaware about basic privacy settings regarding handling of smart devices. As last part of privacy and security combined, the family would benefit from setting up an isolated guest-only WiFi network, be it for security reasons of isolating untrusted IoT devices or for privacy reasons (guests).

Finally, there is a clear need for some form of password management.

And additionally above that, the parents are interested also in a physical security of their children. Ideally, the parents would want to have the ability to check the real-time position of a child and manage its online activity, to prevent any abuse.

## Low-tech skilled university student

The second profile is of an individual 20-years-old university student of non-technical program. This student is a Czech high-school absolvent, which, according to the expected level of high-school graduates would place them on level 4 of Digital competence scale. [[@DigiCompEduCZ]]

### Hardware settings

The profile of student is simpler in terms of hardware settings, because they are using devices and networks that are not managed by them, either at their dormitories or at their parents home. Nonetheless, the students possesses an iPhone 11 smartphone as their main device and Windows laptop for note-taking and school-related office work.

### Software settings

As their main device is iPhone with iOS, most of their software settings is centered around the Apple ecosystem -- all their photos and videos are automatically saved to iCloud, as these are a default settings of iOS, together with the full system backup. Because the free storage limit of iCloud is set to 5 GB[[@appleICloudPlans]], they need to use the paid plan to be able to fit into the limit. As they use their smartphone as their main device, it is also where they do create a majority of their online accounts, which they saved to the built-in Apple KeyChain.

For working with documents and note taking, they are using Office 365 suite provided by the university with linked Microsoft account.

### Digital hygiene

For theirs accounts, they do use Seznam as their main email provider without any MFA, but do also have a school-issues Microsoft account with Outlook for university-based operation and communication. Other than that, they do have a Apple account, social media accounts and many common accounts for multiple e-shops and hobby sites. Because iCloud is not preinstalled on Windows, they are not aware that it is possible use this application to synchronize files and passwords [[@appleICloudPasswords]], so instead they connect their phone using cable every time they need to copy photos and videos from their iPhone and retype all passwords manually when on desktop.
### Problems with current approach

Security-wise, the most critical problem with current set-up is Seznam account missing MFA, as up to 200 thousands people loose access to they Seznam account every year. 
[[@SeznamZtrataUctu]] Next, because they are re-typing all passwords manually on desktop, for convenience-sake they cannot be expected to use as complex password as if a fully random and long passwords were used.

Regarding data retention, there is a lack of backup from their Windows laptop, as it is not handled automatically by the Apple ecosystem.

### Already solved problems

Because data backup is enabled on iOS by default, the student can recover all their data easily in case of a lost device. This includes a good password policy, where all passwords are securely stored inside Apple KeyChain protected by Face ID or fingerprint.
### Needs not covered

Even though the Apple ecosystem solves a multiple of common issues for its user, its closeness produces new ones when trying to interact with systems outside of it. It makes it harder to interact with Windows PC and requires the iCloud for Windows software to be running on the PC for features like password sync with Google Chrome or Microsoft Edge.[[@appleICloudPasswords]] 

## Individual tech-skilled user

The third profile is again of a 20-years-old student, but with more IT-related experience and knowledge. It is safe to place them at least on level 6 of the digital competence scale, as they are expected to be "able to adapt to others in a complex context"[[@DigiCompLevels]]. As a student with lower income, they are reluctant to pay for software and services if they are able to find a cheaper alternative, even if it requires some level of tinkering with.

### Hardware settings

As they are able to configure their devices to an advanced degree and prefer to save financials, they are using a mid-range Android phone as their main mobile device. With that, they also possess a gaming laptop with Windows 11 running on it. Again, as this is a second profile of a student, there is not much of hardware device to be owned.

### Software settings

Software-wise, this profile differs significantly from the profile of low-tech student. Because for an Android phone a Google account is almost a requirements, it is the main account that the student uses. Because the Google ecosystem provides a multitude of services, including a mail service and file storage service Google drive, the student heavily utilizes these. As Android device often comes preinstalled with Google Photos application, which in the past offered unlimited backup storage [[@blogUpdatingGoogle]], the student uses this application to automatically backup all his photos and videos. Next, as Google offers a free online office suite, they also use the Google Drive for storing all their documents and notes. In the past, when finding the most fitting file synchronization and sharing service, they have also used Dropbox and Ulož.to, but have since forgotten about their accounts on these service.

For web browsing, they are using the Google Chrome web browser on both their laptop and Android phone with the build-in password manager synchronizing their passwords across all platforms. As additional protection, they also have set-up a MFA for all their accounts. For Google, their Android smartphone with the Google app installed works as a MFA agent, then for Microsoft and Steam account they have a separate application for each. As to not loose access to the accounts in case that the smartphone with MFA applications is not available, they have printed the recovery codes on the paper.

For communication with peers, they mostly use Telegram application on both smartphone and a laptop as an installable application.

On his gaming laptop, they are hosting a Minecraft server to play with their friends. Since they do not have a public IP address, they are using LogMeIn Hamachi software to create a P2P VPN.

### Digital hygiene

The student is aware of some of the security threats that they may become the victim so, so they are using a MFA whenever the service offers them to and are deploying randomly generated long passwords on other accounts. Furthermore, given that the recovery codes for their accounts are printed only once, it is possible that they have forgotten where they have put the codes and may not be able to locate them again if needed.
Because of their status as a student, they are often on travels from and to their university, where they connect to public WiFi networks in trains, buses and trams.

### Already solved problems

Thanks to the usage of a single web browser capable of password synchronization across multiple platforms, the user is able to have unique strong password for every account. Furthermore, on Windows, the Google Chrome is able to protect access to the passwords with the Windows account password. Next, the user will be notified if there is a reported breach for their account. [[@GoogleChromePasswordProtection]]

Even if (only) the password is leaked for one of their most critical account, there may not be any direct risk of the account compromise thanks to the deployment of MFA on these accounts.
### Problems with current approach

As the student takes security into account when dealing with managing login credentials, the biggest security threat may pose when the requirement of logging into his Google account every time they need to access their passwords. If they perform the login operation on an infected machine, it may be possible that their session may be stolen and used to extract data (passwords, browsing history) from their account. Secondly, there may be possible threats from other devices connected to the same LogMeIn Hamachi network or to the public network in public transportation.

The largest possible privacy issue is connected to the forgotten legacy account on Dropbox and Ulož.to, which may not be sufficiently protected and still contain personal data. Next possible privacy issue may be with Telegram -- a messenger that calls itself "... more secure than mass market messengers like WhatsApp and Line" [[@telegramFAQ]]. The main issue may be that the messenger itself does not have E2EE enabled unless a special feature is used ("Telegram’s special [secret chats](https://telegram.org/faq#secret-chats) use end-to-end encryption" [[@telegramFAQ]]), but in mainstream media is still being presented as if everything on Telegram was using E2EE  [[@lifehackerBestWhatsApp]] [[@tnWhatsapp]]  or the detail that a special feature must be turned on is omitted [[@techradarWhatsAppAlternatives]] [[@ziveNahraditWhatsApp]] , which may confuse or deceive any user into believing that every message on Telegram is protected with E2EE.

Regarding data retention, the student is backing up all their important data on Google Drive, which may be further improved by having a separate backup copy on another service. Not only because an account compromise could lead to the saved files being deleted by a malicious party, but also the service itself can break and the student could lose some of their files  [[@Toulas_2023]] [[@GoogleDriveRecovery]].
### Needs not covered

Even though the student has covered much of their needs, there may still be a room for an improvement with malware protection for their smartphone and a endpoint protection on untrusted WiFi networks for all their devices.

## Small technology company start-up

The final profile is for a small technology company that is currently in its start-up phase. As this is technology company, most of the people employed will be working directly as a member of IT/development team or will have service-related jobs, so they can be expected to have a digital competence of at least 6 [[@STEINLECHNER20211185]].

The company currently consts of approximately 20 employees which are meeting in a hybrid co-working center, so a portion of them can be expected to correct remotely from their home offices.

### Hardware settings

All employees are provided a MacBook laptop and iPhone smartphone from the company for their employment-related tasks. Next, the company has a self-managed Windows laptop located in their office that works as a dedicated company server.

### Software settings

The company was provided with a static public IPv4 address, which was assigned to their MikroTik router and acts as an OpenVPN and DNS server.  Their laptop-server is running Windows with Hyper-V providing multiple virtual servers for development and production purposes, while itself natively hosting [Jenkins](https://www.jenkins.io/) software to perform CI/CD jobs. In the rationale that all device on LAN had to already authorized, the Jenkins does not need any further login when accessing from a LAN address. All these virtual servers are remotely accessible through shared account created on SSH for Linux-based or RDP for Windows based. Passwords for said accounts are shared using a document hosted on Google drive.

In order for the employees to not have to remember the respective IP addresses of all their machines, they have set up a static DNS records on their MikroTik router that resolve addresses in format `xxxx.company.internal`. To be able to have valid HTTPS certificates, they have created a custom certification authority, which root certificate was installed to all company devices.

All their project files are stored inside private repositories on [main GitLab instance](https://gitlab.com/), but larger files (e.g. large binary files, promotional videos) are being transferred using USB flash discs.

### Digital hygiene

As this is a technology startup, most of the employees is fully aware that computer security should be implemented on some level, though as they are roughly aware what security contains, they may be unreasonably confident in detecting and avoiding all threats.

Next, as there is no central company monitoring software enforcing company device usage policy, the employees are using the devices also for personal matters.
### Problems with current approach

The most immediately notable security threat is a file with pain-text shared passwords, as its leak may lead to a compromise of multiple devices. Second problem may be with OpenVPN server on MikroTik router not supporting any form of MFA, meaning that a compromise of a single VPN account password could lead to a compromise of the whole company's internal network. With this issue is linked the Jenkins build server that does not require any additional log in when accessing from LAN, that is fully accessible in case of the local network compromise and could lead to failed automation jobs or malicious build being published. Additional issue is linked to the company having using own top-level domain name for internal purposes, as not only this approach introduces a single point of failure in case of the company's local DNS server malfunction, but the installation of a custom company's CA on all of its devices introduces two security threats:

1. As the company does not have any centralized ways to install CA certificate to all of their devices, it may be possible that some of the employees will not have it installed properly into their system and rather than spending time on resolving the issue, they will only ignore browser warning about unknown certificate. With that, the user may not safely differentiate between a man-in-the-middle attack and missing legitimate CA certificate.
2. If the private certificate of the company's internal CA is not stored properly and stolen, the attacker may then impersonate any website by simply generating a new certificate for it and launching a man-in-the-middle attack, which the user will not notice unless they analyze which organization has issued certificate for every website, which is unlikely. This attack could effectively remove any advantage of using TLS for communication, as any data sent could be intercepted and analyzed by the attacker.

Furthermore, as there is no centralized device management or monitoring software and the employees are using them for personal tasks, there is a risk of employees unintentionally bringing malware into company, or for insider threat to remain undetected.

Regarding data retention, as large files are transferred via unencrypted flash disc, this may lead to company-internal data being leaked in case of flash disc theft, or data loss as there is no direct system for backup of larger files.

Lastly, having all company servers to be running as virtual servers on a single Windows laptop poses a large single point of failure, either from the laptop and its OS being used in different ways than was designed for, or by simply having connectivity loss caused by ISP, company's router or simply the laptop applying new updates. Depending on the length of the outage, this could lead to a serious reputation damage for the company.
### Already solved problems

Even though not done securely, there is a strong want for password sharing. Next, as the code is versioned in git repository hosted by a reputable service, it may be considered safely backed up.
### Needs not covered

The company would definitely benefit from a scaleable virtual machine management that is not dependent on the current state of their ISP. Next, the company should implement some form of least-privilege separation between users accessing the virtual machines, that would streamline onboarding and offboarding of employees, perhaps best with a SSO from a single identity provider.  Lastly, a more robust solution for sharing larger files should be put in place in order to prevent data loss or data leak.

## Shared needs and problems

It is evident that there exists a pattern among the profiles, which can be categorized as a list of shared problems or needs which any user of any category may encounter. These problems or needs include:

- passwords or secret sharing and synchronization
- backing up important data
- malware endpoint protection
- sharing of documents.

It is notable that the requirement for backing up data is not comparable between storing the data for personal use or for long-term data preservation dictated by law for companies. Despite these differences in scale, it is observed that every presented user profile does include these needs in some form. It is easy  to conclude that it would be beneficial to find a single solution that addresses these needs, as the lower number of used services would lower the risk of setting them up incorrectly or insecurely. It is important to note that when discussing password management or sharing secrets, this thesis does also consider identity management services that can be used as single sign-on sources on the reasoning that not having to input any password is generally more secure than having a specifically generated password for each account. The reason behind this is that the user does not need to have the necessary capacity, knowledge, or skills to manage their passwords securely in the long term. By preferring services that provide a single sign-on service, the user does not need to keep more than a few passwords, mainly for the service itself and for other services that do not support any form of single single sing-on authentication.

## Summary of problems and needs

To provide an easier navigation within this thesis, an bullet point summary of current problems with and needs of all the profiles can be found in `TEX:\autoref{tab:ProfiSummary}`. 

```latex
\begin{landscape}
\begin{longtable}{p{4cm}p{7cm}p{7cm}}
    \caption{Summary profiles' needs and problems}\\ \toprule
    \label{tab:ProfiSummary}
    \textbf{Profile} &\textbf{Problems} & \textbf{Needs}\\
    \midrule

    \noindent Low-tech skilled family &
	\begin{itemize}
		\item unsupported office suite
		\item possibly outdated router
		\item no guest network separation
		\item complex chat history backup
		\item company laptops used for personal agenda
	\end{itemize} &
	\begin{itemize}
		\item password managment
		\item children account separation
		\item resilient personal data backup
		\item physical and virual security of children
	\end{itemize}\\
	
    \noindent Low-tech skilled university student &
    \begin{itemize}
		\item main mail account missing MFA
		\item having to re-type passwords on desktop
	\end{itemize} &
	\begin{itemize}
		\item sychronization of passwords with desktop
		\item automatic backup of desktop data
	\end{itemize}\\

    \noindent Individual tech-skilled user &
    \begin{itemize}
		\item sharing the account for password managment and for mail
		\item having P2P connections with untrusted parties
		\item forgotten accounts with leftover data
		\item using Telegram without E2EE
	\end{itemize} &
	\begin{itemize}
		\item having backup on multiple services
		\item smartphone malware proteciton
		\item more secure public WiFi usage
	\end{itemize}\\

    \noindent Small technology company start-up &
    \begin{itemize}
		\item plain-text shared password
		\item no MFA on VPN server
		\item custom top-level domain \& CA
		\item centralized device managment
	\end{itemize} &
	\begin{itemize}
		\item scaleable virtual machine managment
		\item least-privilege access
		\item secure file sharing
		\item SSO zero-trust authentication
	\end{itemize}\\

	\bottomrule

\end{longtable}
\end{landscape}
```
