# Profiles

For the purposes of this thesis, I have prepared a three profiles each representing a typical user archetype. All profiles were compiled from discussions with relevant parties, personal experience and put into kontext using digital competence framework. None of the original parties posses all of the outlined problems, as they were constructed to better highlight possible solutions. (*[[Profiles]]*)

## Low-tech skilled family

A first introduced profile is of a family with middle-aged parents and two young children (aged 12 and 8). Any member of the family is expected to have a non-IT related education and occupation and as such also a small technology skillset, ranging on a average Digital competence level 3 [[@OECDSkillsMatter]]. Both parents work in accounting and were issued a laptop from they employer, the kids use a second-hand laptop with shared account.

### Hardware settings

As mentioned above, both parents were provided a laptop from work, while the kids received a single Windows laptop shared between them. Each family member also posses an older personal lower-to-mid range Android smartphone (priced under 7 000 Kč). To use as a backup solution of their most important data, the family has purchaged a single 8 TB external HDD. Other than that, the family has one large-screen TV with Tizen OS. All devices are connected to a Wi-Fi router with single AP running.

### Software settings

All of their laptops are running Windows OS, while admin-level permissions are available only on their shared laptop. The family does not (intentionally) use any cloud service for storing data. Their family chat is primarily located on Viber, whereas children use Instagram as their main application to stay in touch with their friends. For their personal office works and for children's school purposes they are using a Microsoft Office 2010 suite, which they have payed for in the past. They are using default web browsers for each platform, meaning Chrome for their Android phones and Edge on their laptops.

### Digital hygiene

As their technological knowledge is in the level 3 range, they are supsectible to adverts and reccomendations for software, resulting in multiple antivirus softwares and computer-cleaning programs being installed superfluously at once. They are also not bothered by any type of pop-up dialogs or warning, as they simply select continue on anything. During the early days of Internet, it was a common knowledge that anything uploaded to the Internet will forever stay on the Internet. For that matter, they are reluctant to intentionally (e.g. Viber uses Google Drive in background for message backups) use any cloud service. They have started with a Seznam.cz account for freemail services, but with the comming of Android phones, they have added a Google account for everyone. Nowadays they have multiple accounts for various social media (Facebook, TikTok, Instagram), hobby sites and so on. They are using two separate passwords, one "strong" for critical accounts (online banking and primary email account) and one easy-to-remember for all other accounts.

### Possible problems that are already solved

The family has already solved, or partially solved, some of possible issues that may arise from their common operations. Perhaps most importantly, the family does perform backups in some form. This is true both for their shared data (on external HDD) and for their Android phones, which do have backup to Google drive offered as default option. Next, the users are at least aware of basic security practices, so they are using antivirus software and more than one password. Finally, because their home network was set-up by their ISP, it can be considered as resilient and properly configured.

### Faced problems with current approach

There are numerous problems with the current approach that can be divided mainly into categories of privacy and computer security. To start with the security related issues, because the Android smartphones are older and were in the lower-to-mid price range, there is a good chance that they do no longer receive any security updates, meaning that any known security vulnerability may be *(TODO: TEMU as a malware? link known Android zero day? Pegasus?)* exploited. This makes theses devices inappropriate for use with any personal data, especially baking applications with financials. As for their shared laptop, Office 2010 is [no longer supported](https://support.microsoft.com/en-us/office/end-of-support-for-office-2010-3a3e45de-51ac-4944-b2ba-c2e415432789), which in combination with their low digital competence may make them vulnerable to serious phishing and advertising attacks. The severity of this issue is also reinforced by using only two different passwords, where breach of at least one of them will result into a possible breach of multiple accounts. They are also unable to use the password manager built-into the web browser, as they use a different browser on every platform. Lastly, depending on their ISP, it is possible that they were issues an outdated router without relevant security patches, which may be issue mainly with smaller ISPs within less-densely populated areas.

As for privacy, the most notable issue can be found within the shared laptop, where issues may arise from one of the children forgetting to log out of their session without the web browser. On the other hand, the parents are using work laptops for personal agendas, which may be closely monitored by their employer (depending on the policy deployed by the company). The third risk for privacy is their smart TV which may audio of their conversation and send it for analysis to another worker without the knowledge of family. A final privacy risk may be linked with end-to-end encrypted chatting applicaiton Viber, which lists privacy as important aspect of this service ("Our mission is to protect your privacy so that you never have to think twice about what you can or can't share when you're using Viber." [[@viberHomeViber]]), but still stores a large collection of metadata on its servers. [[@FBIDataMessenger]]

A third category of problems consist of data retention and recovery. Even though the disc used for backup does provide a basic level of redundancy, it can still be easily destroyed e.g. by dropping it, by mistakenly deleting wrong files or simply by connecting it to a infected device. Furthermore, this solution lacks the ability to be performed automatically, which may result to the backups being severely outdated. A though must also be put into backing up of their family conversation on Viber, where all messages are lost after on-boarding on a new device unless backup was enabled. [[@ViberRestoreChat]]

### Needs that are currently not covered

Some of the needs that are currently not covered were already outlined within the current problems, namely a redundant backup solution prone to accidental or malicious deletion, with automatic schedule set to prevent backups being out of date. Next, the family is unaware about basic privacy settings regarding handling of smart devices. As last part of privacy and security combined, the family would benefit from setting up an isolated guest-only WiFi network, be it for security reasons of isolating untrusted IoT devices or for privacy reasons (guests).

Finally, there is a clear need for some form of password management.

And additionally above that, the parents are interested also in a physical security of their children. Ideally, the parents would want to have the ability to check the real-time position of a child and manage its online activity, to prevent any abuse.

*([[Profile of Family with low-tech skills]])*

## Low-tech skilled university student

The second profile is of an individual 20-years-old university student of non-technical program. This student is a Czech high-school absolvent, which, according to the expected level of high-school graduates would place them on level 4 of Digital competence scale. [[Digital competence]][[@DigiCompEduCZ]]

### Hardware settings

The profile of student is simpler in terms of hardware settings, because they are using devices and networks that are not managed by them, either at their dormitories or at their parents home. Nonetheless, the students possesses an iPhone 11 smartphone as their main device and Windows laptop for note-taking and school-related office work.

### Software settings

As their main device is iPhone with iOS, most of their software settings is centered around the Apple ecosystem -- all their photos and videos are automatically saved to iCloud, as these are a default settings of iOS, together with the full system backup. Because the free storage limit of iCloud is set to 5 GB[[@appleICloudPlans]], they need to use the paid plan to be able to fit into the limit. As they use their smartphone as their main device, it is also where they do create a majority of their online accounts, which they saved to the built-in Apple Keychain. *TODO: Do users know about iCloud for Windows?*

### Digital hygiene

For theirs accounts, they do use Seznam as their main email provider without any MFA, but do also have a school-issues Microsoft account with Outlook for university-based operation and communication. Other than that, they do have a Apple account, social media accounts and many common accounts for multiple e-shops and hobby sites.

### Problems with current approach

Security-wise, the most critical problem with current set-up is Seznam account missing MFA, as up to 200 thousands people loose access to they Seznam account every year. 
[[@SeznamZtrataUctu]].

Regarding data retention, there is a lack of backup from their Windows laptop, as it is not handled automatically by the Apple ecosystem.

### Already solved problems

Because data backup is enabled on iOS by default, the student can recover all their data easily in case of a lost device. This includes a good password policy, where all passwords are securely stored inside Apple KeyChain protected by Face ID or fingerprint.

### Needs not covered

Even though the Apple ecosystem solves a multiple of common issues for its user, its closeness produces new ones when trying to interact with systems outside of it. It makes it harder to interact with Windows PC and requires the iCloud for Windows software to be running on the PC for features like password sync with Google Chrome or Microsoft Edge.[[@appleICloudPasswords]] 

## Individual tech-skilled user
