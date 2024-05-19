For this thesis, I have prepared four profiles on which possible security, privacy and data retention threats may be presented. Each of the profiles represents a typical user archetype. All of the profile characteristics and the proposed solutions in later chapters are based on the DigiComp levels shown in the previous chapter. Additional data from which the profiles were created, such as their settings, needs and problems, was obtained from discussions with relevant parties and personal experience. For the creation of each of the profiles a number of real-life samples ranging from 5 to 33 were collected. The exact numbers together with questions and discussed areas can be found in `TEX:\autoref{pt:partCounts}`. During the constructions of profiles, the focus was more laid on the negative patterns observed to better highlight solutions to the issues existing in the wild. This means that no profile is a direct representation of one party, but rather a worst-case scenario of combination of frequently occurring malpractices. 

## Low-tech skilled family

The first introduced profile is of a family with middle-aged parents and two young children (aged 12 and 8). Any family member is expected to have a non-IT related education and occupation and, as such, a small technology skill set, ranging on an average Digital competence level 3 [[@OECDSkillsMatter]]. Both parents work in accounting and were issued a laptop from their employer; the kids use a second-hand laptop with a shared account.

### Hardware settings

As mentioned above, both parents were provided with a laptop from work, while the kids received a single Windows laptop shared between them. Each family member also possesses an older, lower-to-mid-range Android smartphone (priced under 7,000 CZK). The family has purchased a single 8 TB external HDD as a backup solution for their most important data. Other than that, the family has one large-screen TV with Tizen OS. All devices are connected to a WiFi router with a single AP running.

### Software settings

All their laptops run Windows OS, while admin-level permissions are available only on their shared laptop. The family does not (intentionally) use any cloud service to store data. Their family chat is primarily on Viber, whereas children use Instagram as their primary application to stay in touch with friends. For their personal office work and children's school purposes, they use a Microsoft Office 2010 suite, which they have previously paid for. They use default web browsers for each platform, meaning Chrome for their Android phones and Edge on their laptops.

### Digital Hygiene

As their technological knowledge is in the level 3 range, they are susceptible to adverts and recommendations for software, resulting in multiple antivirus software and computer-cleaning programs being installed superfluously. They are also not bothered by any pop-up dialogues or warnings, as they simply select continue on anything. During the early days of the internet, it was common knowledge that anything uploaded to it would forever stay on it. For that matter, they are reluctant to intentionally (e.g. Viber uses Google Drive in the background for message backups) use any cloud service. They have started with a Seznam.cz accounts for freemail services, but with the arrival of Android phones, they have added a Google account for everyone. Nowadays, they have multiple accounts on various social media platforms (Facebook, TikTok, Instagram), hobby sites, and so on. They use two passwords, one *"strong"* for critical accounts (online banking and primary email account) and one easy-to-remember for all other accounts.

### Possible problems that are already solved

The family has already solved, or partially solved, some of the possible issues that may arise from their everyday operations. Perhaps most importantly, the family does perform backups in some form. This is true for their shared data (on external HDD) and Android phones, which have backup to Google Drive as the default option. Next, the users are at least aware of basic security practices, so they use antivirus software and multiple passwords. Finally, because their ISP set up their home network, it can be considered resilient and properly configured.

### Faced problems with the current approach

There are numerous problems with the current approach that can be divided mainly into categories of privacy and computer security. To start with the security related issues, because their Android smartphones are older and are in the lower-to-mid price range, there is a good chance that they no longer receive any security updates, meaning that any known security vulnerability may be exploited. This makes these devices inappropriate for use with any personal data, especially baking applications with financials. As for their shared laptop, Office 2010 is [no longer supported](https://support.microsoft.com/en-us/office/end-of-support-for-office-2010-3a3e45de-51ac-4944-b2ba-c2e415432789), which in combination with their low digital competence may make them vulnerable to severe phishing attacks. The severity of this issue is also reinforced by using only two different passwords, where a breach of at least one of them will result in a possible breach of multiple accounts. They also cannot use the password manager built into the web browser, as they use a different browser on every platform. Lastly, depending on their ISP, they were issued an outdated router without relevant security patches, which may be an issue mainly with smaller ISPs within less-densely populated areas.

As for privacy, the most notable issue can be found within the shared laptop, where issues may arise from one of the children forgetting to log out of their session without the web browser. On the other hand, the parents are using work laptops for personal agendas, which may be closely monitored by their employer (depending on the policy deployed by the company). The third risk for privacy is their smart TV, which may record audio of their conversation and send it for analysis to third parties without the knowledge of the family. A final privacy risk may be linked with the end-to-end encrypted chatting application Viber, which lists privacy as an important aspect of this service ("Our mission is to protect your privacy so that you never have to think twice about what you can or cannot share when you are using Viber." [[@viberHomeViber]]), but still stores a large collection of metadata on its servers. [[@FBIDataMessenger]]

A third category of problems consists of data retention and recovery. Even though the disc used for backup provides a basic level of redundancy, it can still be easily destroyed, e.g., by dropping it, mistakenly deleting wrong files, or simply connecting it to an infected device. Furthermore, this solution cannot be performed automatically, which may result in the backups being outdated. A thought must also be put into backing up their family conversation on Viber, where all messages are lost after onboarding on a new device unless backup is explicitly enabled. [[@ViberRestoreChat]]

### Needs that are currently not covered

Some of the needs that needed to be covered were already outlined in the current problems, namely a redundant backup solution prone to accidental or malicious deletion, with the automatic schedule set to prevent backups from being outdated. Next, the family must be aware of basic privacy settings for handling smart devices. As the last part of privacy and security combined, the family would benefit from setting up an isolated guest-only WiFi network for the security reasons of isolating untrusted IoT devices or for privacy reasons (guests).

Finally, there is a clear need for some form of password management.

Moreover, the parents are also interested in the physical security of their children. Ideally, the parents would want to have the ability to check the real-time position of a child and manage its online activity to prevent any abuse.

## Low-tech skilled university student

The second profile is of a 20-year-old university student in a non-technical program. This student is a Czech high-school absolvent, which, according to the expected level of high-school graduates, would place them on level 4 of the Digital competence scale. [[@DigiCompEduCZ]]

### Hardware settings

The student profile is more straightforward regarding hardware settings because they use devices and networks they do not manage at their dormitories or at their parent's home. Nonetheless, the students possess an iPhone 11 smartphone as their primary device and a Windows laptop for note-taking and school-related office work.

### Software settings

As their primary device is an iPhone with iOS, most of their software settings are centred around the Apple ecosystem -- all their photos and videos are automatically saved to iCloud, as these are default settings of iOS, together with the complete system backup. Because the free storage limit of iCloud is set to 5 GB [[@appleICloudPlans]], they need to use the paid plan to fit into the limit. While using their smartphone as their primary device, they create most of their online accounts there, credentials to which they save to the built-in Apple KeyChain.

To work with documents and note-taking, they use the Office 365 suite provided by the university with a linked Microsoft account.

### Digital Hygiene

For their accounts, they do use Seznam as their main email provider without any MFA. However, they were issued a school-issued Microsoft account with Outlook for university-based operation and communication. They also have an Apple account, social media accounts and many common accounts for multiple e-shops and hobby sites. Because iCloud is not preinstalled on Windows, they are not aware that it is possible to use this application to synchronize files and passwords [[@appleICloudPasswords]], so instead, they connect their phone using cable every time they need to copy photos and videos from their iPhone and retype all passwords manually when on desktop.

### Problems with current approach

Security-wise, the most critical problem with the current set-up is the Seznam account missing MFA, as up to 200 thousand people lose access to their Seznam account every year. [[@SeznamZtrataUctu]] Next, because they are retyping all passwords manually on the desktop, for convenience's sake, they cannot be expected to use as complex passwords as if entirely random and long passwords were used.

Regarding data retention, there is a lack of backup from their Windows laptop, as it is not handled automatically by the Apple ecosystem.

### Already solved problems

Because data backup is enabled on iOS by default, the student can recover all their data quickly in case of a lost device. This includes a good password policy, where all passwords are securely stored inside Apple KeyChain, protected by Face ID or fingerprint.

### Needs not covered

Even though the Apple ecosystem solves multiple common issues for its users, its closeness produces new ones when interacting with systems outside of it. It makes it harder to interact with Windows PCs and requires the iCloud for Windows software to run on the PC for features like password sync with Google Chrome or Microsoft Edge. [[@appleICloudPasswords]] 

## Individual tech-skilled user

The third profile is again of a 20-year-old student, but with more IT-related experience and knowledge. It is safe to place them at least on level 6 of the digital competence scale, as they are expected to be "able to adapt to others in a complex context" [[@DigiCompLevels]]. As a student with lower income, they are reluctant to pay for software and services if they are able to find a cheaper alternative, even if it requires some level of tinkering.

### Hardware settings

As they can configure their devices to an advanced degree and prefer to save financials, they use a mid-range Android phone as their primary mobile device. They also possess a gaming laptop with Windows 11 running on it. Again, as this is a second profile of a student, there is little hardware device to be owned.

### Software settings

Software-wise, this profile differs significantly from the profile of low-tech student. As for an Android phone a Google account is a requirement`TEXT:\footnote{Unless the user is using a de-Googled variant of Android, which is out of the scope of this thesis.}`, it is the primary account that the student uses. Because the Google ecosystem provides a multitude of services, including a mail service and file storage service, Google Drive, the student heavily utilizes these. Android devices often come preinstalled with the Google Photos application, which, in the past, offered unlimited backup storage [[@blogUpdatingGoogle]]; the student uses this application to automatically back up all their photos and videos. Next, as Google offers a free online office suite, they also use Google Drive to store all their documents and notes. In the past, when finding the most fitting file synchronization and sharing service, they have also used Dropbox and Ulož.to but have since forgotten about their accounts on this service.

For web browsing, they use the Google Chrome web browser on both their laptop and Android phone, and the built-in password manager synchronizes their passwords across all platforms. They have also set up an MFA for all their accounts as additional protection where applicable. For Google, their Android smartphone with the Google app installed works as an MFA agent, and for Microsoft and Steam accounts, they have a separate application for each. They have printed the recovery codes on paper to keep access to the accounts in case the smartphone with MFA applications is unavailable.

For communication with peers, they mostly use the Telegram application on smartphones and laptops as an installable application.

They are hosting a Minecraft server on their gaming laptop to play with their friends. Since they do not have a public IP address, they are using LogMeIn Hamachi software to create a P2P VPN.

### Digital Hygiene

The student is aware of some of the security threats they may become the victim of, so they are using an MFA whenever the service offers them and deploying randomly generated long passwords on other accounts. Furthermore, given that the recovery codes for their accounts are printed only once, it is possible that they need to remember where they have put the codes and may not be able to locate them again if needed.

Because of their student status, they often travel from and to their university, connecting to public WiFi networks on trains, buses, and trams.

### Already solved problems

Thanks to a single web browser capable of password synchronization across multiple platforms, the user can have unique strong passwords for every account. Furthermore, on Windows, Google Chrome can protect access to the passwords with the Windows account password, which may serve as a basic level of protection against an attacker with physical access. Next, the user will be notified if there is a reported breach of their account. [[@GoogleChromePasswordProtection]]

Even if (only) the password is leaked for one of their most critical accounts, there may not be any direct risk of account compromise thanks to the deployment of MFA on these accounts.

### Problems with current approach

As the student takes security into account when managing login credentials, the biggest security threat may be the need to log into their Google account every time they need to access their passwords. If they perform the login operation on an infected machine, their session may be stolen and used to extract data (passwords, browsing history) from their account. Secondly, there may be threats from other devices connected to the same LogMeIn Hamachi network or the public network in public transportation.

The most significant possible privacy issue is connected to the forgotten legacy account on Dropbox and Ulož.to, which may not be sufficiently protected and still contain personal data. The next possible privacy issue may be with Telegram -- a messenger that calls itself "... more secure than mass market messengers like WhatsApp and Line" [[@telegramFAQ]]. The main issue may be that the messenger itself does not have E2EE enabled unless a unique feature is used ("Telegram's special [secret chats](https://telegram.org/faq#secret-chats) use end-to-end encryption" [[@telegramFAQ]]), but in mainstream media is still being presented as if everything on Telegram was using E2EE [[@lifehackerBestWhatsApp]][[@tnWhatsapp]] or the detail that a particular feature must be turned on is omitted [[@techradarWhatsAppAlternatives]][[@ziveNahraditWhatsApp]], which may confuse or deceive any user into believing that every message on Telegram is protected with E2EE.

Regarding data retention, the student is backing up all their important data on Google Drive, which may be further improved by having a separate backup copy on another service. Not only because an account compromise could lead to the saved files being deleted by a malicious party but also because the service itself can break, and the student could lose some of their files [[@Toulas_2023]][[@GoogleDriveRecovery]].

### Needs not covered

Even though the student has covered much of their needs, there may still be room for improvement with malware protection for their smartphone and endpoint protection on untrusted WiFi networks for all their devices.

## Small technology company startup

The final profile is for a small technology company that is currently in its startup phase. As this is a technology company, most of the people employed will be working directly as a member of the IT/development team or will have service-related jobs, so they can be expected to have an average digital competence level of at least 6 [[@STEINLECHNER20211185]].

The company currently consists of approximately 20 employees meeting in a hybrid co-working centre, so a portion of them can be expected to connect remotely from their home offices.

### Hardware settings

All employees are provided with a company's MacBook laptop and iPhone smartphone for their employment-related tasks. Next, the company has a self-managed Windows laptop in their office that works as a dedicated server.

### Software settings

The company was provided with a static public IPv4 address assigned to their MikroTik router, which acts as an OpenVPN and DNS server. Their laptop server runs Windows with Hyper-V, providing multiple virtual servers for development and production purposes, while itself natively hosts [Jenkins](https://www.jenkins.io/) software to perform CI/CD jobs. In the rationale that all devices on LAN have to be already authorized to be there in a first place, Jenkins does not need any further login when accessing from a LAN address. All these virtual servers are remotely accessible through shared accounts created on them via SSH for Linux-based or RDP for Windows-based machines. Passwords for said accounts are shared using a document hosted on Google Drive.

In order for the employees to not have to remember the respective IP addresses of all their machines, they have set up static DNS records on their MikroTik router that resolve addresses in the format `xxxx.company.internal`. To have valid HTTPS certificates, they have created a custom certification authority with a root certificate installed on all company devices.

All their project files are stored inside private repositories on [central GitLab instance](https://gitlab.com/), but larger files (e.g. large binary files, promotional videos) are being transferred using USB flash discs.

### Digital Hygiene

As this is a technology startup, most employees know that computer security should be implemented on some level. However, though as they are roughly aware what security contains, they may be unreasonably confident in detecting and avoiding all threats.

Next, as there is no central company monitoring software enforcing company device usage policy, employees also use the devices for personal matters.

### Problems with current approach

The most immediately notable security threat is a file with plain-text shared passwords, as its leak may lead to a compromise of multiple devices. The second problem may be with the OpenVPN server on the MikroTik router not supporting any form of MFA, meaning that a compromise of a single VPN account password could compromise the whole company's internal network. This issue is linked to the Jenkins build server, which does not require any additional login when accessing from LAN, which is fully accessible in case of the local network compromise and could lead to failed automation jobs or malicious build being published. An additional issue is linked to the company using its top-level domain name for internal purposes, as not only does this approach introduce a single point of failure in case of the company's local DNS server malfunction, but the installation of a custom company's CA on all of its devices introduces two security threats:

1. As the company does not have any centralized ways to install the CA certificate on all of their devices, it may be possible that some of the employees will not have it installed properly into their system, and rather than spending time on resolving the issue, they will only ignore browser warning about unknown certificate. With that, the user may need help distinguishing between a man-in-the-middle attack and a missing legitimate CA certificate.

2. If the private certificate of the company's internal CA is not stored correctly and is stolen, the attacker may then impersonate any website by simply generating a new certificate for it and launching a man-in-the-middle attack, which the user will not notice unless they analyze which organization has issued a certificate for every website, which is unlikely. This attack effectively removes practically any advantage of using TLS for communication, as the attacker could intercept and analyze any data sent.

Furthermore, as there is no centralized device management or monitoring software and the employees are using them for personal tasks, there is a risk of employees unintentionally bringing malware into the company or for insider threats to remain undetected.

Regarding data retention, as large files are transferred via unencrypted flash discs, this may lead to company-internal data being leaked in case of flash disc theft or data loss, as there is no direct system for the backup of larger files.

Lastly, having all company servers running as virtual servers on a single Windows laptop poses a significant single point of failure, either from the laptop and its OS being used in different ways than was designed for or by simply having connectivity loss caused by ISP, company's router or the laptop applying new updates. Depending on the length of the outage, this could lead to severe reputation damage for the company.

### Already solved problems

Even though it is not done securely, there is a centralized way to manage credentials and secrets. Next, as the code is versioned in a git repository hosted by a reputable service, it may be considered safely backed up.

### Needs not covered

The company would benefit from a scaleable virtual machine management that is not dependent on the current state of its ISP. Next, the company should implement some form of least-privilege separation between users accessing the virtual machines, which would streamline the onboarding and offboarding of employees, perhaps best with an SSO from a single identity provider. Lastly, a more robust solution for sharing larger files should be implemented to prevent data loss or data leak.

## Shared needs and problems

A pattern exists among the profiles, which can be categorized as a list of shared problems or needs that any user of any category may encounter. These problems or needs include:

- passwords or secret sharing and synchronization
- backing up important data
- malware endpoint protection
- sharing of documents.

Notably, the requirement for backing up data differs between storing the data for personal use or long-term data preservation dictated by law for companies. Despite these differences in scale, it is observed that every presented user profile does include these needs in some form. Finding a single solution that addresses these needs would be beneficial, as the lower number of used services would lower the risk of setting them up incorrectly or insecurely. It is important to note that when discussing password management or sharing secrets, this thesis also considers identity management services that can be used as single sign-on sources on the reasoning that not having to input any password is generally more secure than having a specifically generated password for each account. This is because the user  does not need to have the necessary capacity, knowledge, or skills to manage their passwords securely in the long term. By preferring services that provide a single sign-on service, the user does not need to keep more than a few passwords, mainly for the service itself and other services that do not support single single single single single authentication.

## Summary of problems and needs

To provide more straightforward navigation within this thesis, a bullet point summary of current problems with and needs of all the profiles can be found in `TEX:\autoref{tab:ProfiSummary}`.

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
		\item smartphone malware protection
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
