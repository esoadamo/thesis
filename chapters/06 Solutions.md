In this chapter, I present selected solutions for all of the profiles. These solutions that fit the profile best are described in more detail and accompanied by the possible solution of using a self-hosted Synology device instead of a cloud service. Even though all solutions try to map to the needs and problems of the presented profile as best as possible, in natural settings, it can be expected that the implemented solution will be a combination of all the presented ones, together with smaller SaaS products tailored for specific needs.

## Low-tech skilled family

As mentioned, the most prominent issues faced were their somewhat outdated and mixed knowledge of best practices. As they do not possess an adequate skill set for completing complex tasks, the solutions for this profile will focus mainly on usability, with a slight compromise on privacy and security. Some of the issues, though, can only be solved by training the user on the best security practices, such as not installing multiple malware protection programs.

### Microsoft

They are already using Windows on their work laptops and have bought a shared one for their kids, so they are already familiar with this environment. This is a significant advantage thanks to the fewer new things to learn. Microsoft provides two services directly tailored for families, which complement each other:

- Microsoft 365 Family subscription that can be shared for up to 6 people and includes access to the up-to-date versions of classical end-user software from Microsoft
- Microsoft Family Safety, which provides an assortment of tools for monitoring the well-being of a child

#### Security

As for malware protection, Microsoft offers their Defender for both operating systems utilized by the family. On Windows, Defender is provided without cost and enabled by default. On Android, the Defender needs to be installed separately on every device, together with a valid Microsoft 365 subscription. As this subscription also comes with the newest version of the Microsoft Office suite, it makes the currently used and insecure Office 2010 obsolete, consequently remediating the security threat of opening a maliciously crafted document that exploits known vulnerabilities of the old software.

If all of the passwords are saved inside Microsoft Edge, the breach of the Microsoft account could lead to a possible breach of all other accounts. For that matter, it is imperative to secure the Microsoft account itself. Here, the ability to use the Microsoft account in a passwordless manner can be fully utilized to protect this account and all accounts that the family will sign into using SSO at once.

#### Privacy

With the main privacy concern for children being that they use shared account on their laptop, the best possible solution would be to implement five distinct account -- one with regular permissions for each child and parent and one with elevated administrator permissions for parents. This will mitigate privacy dangers:

- for children who no longer have to worry about their browsing history being shared or forgetting to log out
- for parents to separate their activity and data from their company-issued laptops

Having a separate administrator account will also improve the overall security standing of the device, as one user cannot simply install a system-wide malicious application. Next, for communication applications, Viber can be replaced by Signal, which focuses on security without compromise and ease of use. On the other hand, neither Signal does persist messages after logging into a new device, unless additional steps are performed.

#### Data retention

To solve the problem with non-redundant backup, the Family 365 subscription offers every member 1 TB of OneDrive storage, which should be enough for the critical data. Furthermore, as OneDrive is integrated into Windows from the installation, it provides a seamless experience to set up and use. For Android, the family may set up the application to automatically upload taken photos to mitigate problems of lost of damaged device.

Another data loss can currently happen when the Viber application is used as a primary means of communication. Microsoft Teams, part of the Office Suite, may step in as a replacement service. Even though it is a step down in terms of privacy, as it does not provide any form of end-to-end encryption, I would suggest using a service that can archive messages without any user interaction, as losing messages may pose a more significant discomfort to the family than storing the messages on a server with a somewhat reputable company encrypted.

#### Child safety

A specific category for this profile is the need to keep children safe in the virtual and physical worlds. For that matter, Microsoft's Family Safety provides those features, just as explained in previous chapters. By linking parents' and children's accounts, the parents can set up parameters for their children's devices.

### Google

The family already has a Google account for their Android smartphones, so it will not require them to create any new ones. Like Microsoft, Google provides a dedicated service for the security of children. The disadvantage is that neither the Chrome browser nor Google Drive client is installed on Windows devices by default and needs to be downloaded separately.
#### Security

On desktops, the most essential part of security for users may be the Google Chrome web browser, together with its phishing protection and password manager. As with Microsoft accounts, when all passwords are being stored within the same account, e.g. email, a simple breach of this account could result in a breach of all accounts for which the user has saved credentials.

As for the vulnerable office suite, the Google provided full-web-based office suite within Google Drive could be used as a replacement. As all documents are edited within the web browser, this solution should not possess any security vulnerabilities that are not present inside the browser itself. On the other hand, this suite may pose some compatibility problems that are explored more within the Data retention section.

#### Privacy

To solve the most notable privacy problem -- the children sharing the same account on their shared laptop- Google provides an option to define multiple Google Chrome profiles, each with its own settings and active accounts. In contrast to creating multiple user accounts, this solution works more on a trust-based approach in that the other child will not internationally launch another child's profile. However, it is easier to set up than creating a new Windows account. 

The user may use Google Duo for calls to replace Viber, but no suitable replacement for text messages exists.

#### Data retention

As Google Drive can be upgraded to up to 2 TB of available storage with the shared Google One subscription, this should still be enough for the family data. However, it is a several step down from the total of up to 6 TB of storage for Microsoft's One drive.

Given that Google has its storage format for the Office suite, and even though it offers most of the features that the user may need, it may only partially support some features available in Microsoft Office. Conversion from the Microsoft Office format into the format used by Google Drive may maintain some special formatting, resulting in partial data loss.

#### Child safety

In addition to similar features in Microsoft Family Safety, the Google Family Link provides more direct control over children's accounts. By allowing the parent to allow the child to use SSO only for applications that do not require permissions except for name, email, and profile picture, the child can safely log into any application without worrying about giving too much access to the account. 

### Synology

Given that Synology requires an initial setup, it may be necessary for the family to consult with a professional for the initial setup. Even after that, Synology does not provide easy solutions to all outlined problems, and the family will need to keep care of the device -- e.g., monitoring that the device is not after its end of life and still receives regular security updates.

#### Security

To replace the vulnerable Microsoft Office suite, the family can use the Synology web-based office suite. Though, as it uses its own storage format, this approach again presents the possible problem of some features not being fully supported by the Synology office.

Next, there needs to be a password manager from Synology. Of course, it is possible to self-host a password manager such as BitWarden using the generic Docker container feature of some of the Synology models. However, I advise against that, as the family members cannot be expected to maintain a self-hosted password manager in a secure and safe manner.

Even though Synology can be used as an SSO source, it first needs to be configured as such with any application that should support it, making it unfeasible for the family.

#### Privacy

Except for the obvious advantage that the data does never leave family-owned devices, the most prominent way how Synology may improve privacy is if all the users keep most of their files only stored there, as then they are protected by their account credentials as opposed to having the files synchronized with the shared computer account. The Viber can be replaced by a Synology Chat package that allows basic chatting while outsourcing video and audio calling to third-party applications such as JumpChat and Jitsi. [[@synoChat]]

#### Data retention

Given that Synology works with the hard drives that the user directly supplies, they significantly impact how resilient the system will be. As the storage is a single-time investment, the hard drive is expected to have more capacity than the 6 TB offered by the Microsoft O365 family subscription. Furthermore, we can probably expect the user to have only one hard drive or set up RAID 0 to maximize the available storage, so the failure of one disc may mean an unrecoverable loss of stored data. To combat this, the user may set up a secondary backup solution, e.g., CloudSync or an in-built Amazon Glacier backup. However, both options require additional setup, possibly too complex, while inquiring more costs.

On the other hand, users may synchronize files from their computers automatically or have their taken media uploaded from their smartphones to store the original data directly on the user's device.

#### Child safety

As there is no direct control over what content children can access or directly monitor the child's online activity, the options for the child's safety are severely limited. A third-party application may be recommended to monitor at least the children's position. As an example, the family can install an application called Find My Device (FMD) [[@fdroidFindDevice]], which is capable of responding to commands sent over SMS, so it does not need to rely on any specific service.

### Unsolved problems

Unfortunately, not all problems can be solved directly by these services, as they are too complex or out of scope. The first example of this may be the use of outdated Android devices, where the best option may be to buy new devices with a declared duration of security updates. As for an outdated router from the ISP, the best course of action may be to ask the ISP to replace it, as the family cannot be expected to manage their router securely. Related to their router is creating a WiFi network for guests, where a router with a user-friendly web interface may help. Creating a separate WiFi network would also help with moving less-trusted devices into the more isolated network.

As for the possible privacy concerns of using the company-provided laptop for personal activities, here the user needs to consult their company laptop usage policy or contact their IT department. The last need that was not covered is performing a backup of the cloud storage service, such as when the account is compromised and all data falls victim to, e.g., a ransomware attack, there is an option to restore said data. Solving this problem would increase the complexity of the solution, while the currently proposed solutions have already severely increased data security.

### Final recommendations

For the profile of a family, out of all the services presented, the services provided by Google and Microsoft are the most fitting and almost interchangeable in terms of solving needs and problems and pricing. Microsoft may be preferable, as it provides higher overall storage space at a slightly lower price. Next, it also comes with an up-to-date version of the Microsoft Office suite, which has no compatibility problems. On the other hand, if 2 TB of shared storage is enough and a more granular control over the child's account is preferable, with only the web-based office suite being sufficient for the user's needs, Google services are a viable solution.

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

The third solution may be the most viable, as it uses an application that the user is already comfortable with. This solution also contributes to the user's need to synchronize the password to their desktop, as all the user needs to do is install iCloud for Windows and a web browser extension.

#### Privacy

By default, iCloud Drive offers encryption in transit and at rest, which should be enough for regular use. Furthermore, when combined with the MFA-protected Apple ID account, no unauthorized party should be able to access the stored data.

#### Data retention

If the users purchase at least 200 GB of storage, it should be enough to store all their critical data.  Though the inability of iCloud to properly version files can become a disadvantage if the users accidentally rewrite their files, e.g., when using an external office suite and saving an empty document instead of an existing one. The taken photos are uploaded automatically from iOS by default, while for synchronization with a Windows computer, the user needs to download and install the iCloud application.

### Microsoft

Microsoft's main advantage over services provided by Google is its already present integration of Microsoft Edge and OneDrive into the Windows OS. Its solutions are also slightly cheaper than comparable products. Furthermore, as the student is already using O365 via its university subscription, they already have all services free of charge for the length of their studies.

#### Security

As with Apple, there is an option to use the TOTP secret in the Microsoft Authenticator application, which users should already use if they have MFA enabled for their Microsoft account.

As already stated, Microsoft Edge can hold and synchronize saved passwords to multiple sites. Same as on Android, Microsoft Edge can be changed as the default auto-fill source inside the iOS settings, solving the password management and synchronization between different platforms and systems.

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

### Unsolved problems

As every one of the problems or needs was solved by at least one of the presented solutions, there are no leftover unresolved problems.

### Final recommendations

Because the student uses the iPhone as their primary device and already interacts with the Apple ecosystem, it is most convenient for them to use the same services on their laptop. On the other hand, OneDrive from Microsoft provides the additional benefit of restoring an older version of files, which may be preferable if the user is working on longer documents, as this would prevent accidental overwriting. However, this comes at the cost of having only half the storage (1 TB for OneDrive, 2 TB for iCloud Drive) at a comparable price.

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

### Final recommendations

Even though Microsoft and Google services can handle most of the problems and needs, they may not be the best solution overall. The main drawback is that it would require a complex cloud environment setup and may become costly, which could become a problem for a student with limited income. Instead, a solution consisting of more specialized services can be recommended, as these services have lower pricing for the solved needs. Bitwarden can be used for separate password management, BackBlaze can be utilized for double-redundant backup, and Cloudflare can create a VPN among friends and browse public networks more safely. A viable solution is to outsource server hosting to Synology, which can be connected in the same way as stated above.

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

Synology has to ability to run arbitrary docker containers or whole virtual machines, so hosting company's services is simple and managable. Synology also offers per-user or per-group permissions, making it easy to implement least-privilege access. As a NAS device, sharing files is one of its core features, mainly when combined with the encryption of data on rest, which Synology natively supports.

The obvious drawbacks of this solution still persist, where Synology still poses as a single point of failure in case of power outage or connectivity downtime. Next, the physical security of this device is more important than with other profiles, as accidental dropping or theft of the device could lead again to service unavailability or company-confidential data leakage. Lastly, there is a need for a password manager or secret-sharing software capable of sharing passwords and secrets, where, like for other profiles, an external service such as Bitwarden needs to be used.

### Unsolved problems

As every one of the problems or needs was solved by at least one of the presented solutions, there are no leftover unresolved problems.

### Final recommendations

All of the problems and needs can be solved by migrating to a cloud environment from Google or Microsoft. Both of these companies offer similar services and both offer a possibly higher uptime than by continuing to self-host. Though, there are some smaller differences in auxiliary services, where Microsoft supports a direct registration of domain names and provides its Microsoft Team application for both text and video communication, while Google Meet supports only video conferences. Next, Google Drive pricing for business plans relevant to this profile provide double the storage space compared to Microsoft plans, but for double the price.

Though, if the company does want to have a fixed pricing for its services, instead of pay-as-you-go pricing of cloud environments, the company may achieve similar results by connecting self-hosted Synology services with Cloudflare ZeroTrust. Nevertheless, the company needs to know about and accept the risks that arise from hosting on their own hardware.

## Summary of selected solutions

To provide more straightforward navigation within this thesis, a bullet point summary of each profile's selected solution and its advantages and disadvantages can be found: 

- for low-tech skilled family in `TEX:\autoref{tab:SoluSummaryFamily}`
- for low-tech skilled university student in `TEX:\autoref{tab:SoluSummaryLowStud}`
- for individual tech-skilled user in `TEX:\autoref{tab:SoluSummarySkillStud}`
- for small technology company start-up in `TEX:\autoref{tab:SoluSummaryComp}`


```latex
\begin{landscape}
\begin{longtblr}[
		caption = {Low-tech skilled family's summary of selected solutions},
		label = {tab:SoluSummaryFamily}
	]{
		colspec = {|p{2.5cm}|p{7.3cm}|p{7.3cm}|},
	}
	
    Solution & Advantages & Disadvantages\\
    Microsoft &
	\begin{itemize}
		\item integrated chatting application
		\item password-less login
		\item Microsoft Office suite
		\item larger available storage space
	\end{itemize} &
	\begin{itemize}
		\item missing web UI for accesing passwords
	\end{itemize}\\

	Google &
	\begin{itemize}
		\item more granular control over child account
		\item simple to set up multiple user profiles within Google Chrome
		\item web UI for accessing passwords
	\end{itemize} &
	\begin{itemize}
		\item missing chatting application
		\item custom office file formats
	\end{itemize}\\

	Synology &
	\begin{itemize}
		\item one-time payment
		\item adjustable storage space
		\item intergated chatting applicaiton
	\end{itemize} &
	\begin{itemize}
		\item complex to set up
		\item custom office file formats
		\item no children physical protection
		\item no password manager
	\end{itemize}\\

\end{longtblr}
\end{landscape}
```


```latex
\begin{landscape}
\begin{longtblr}[
		caption = {Low-tech skilled university student's summary of selected solutions},
		label = {tab:SoluSummaryLowStud}
	]{
		colspec = {|p{2.5cm}|p{7.3cm}|p{7.3cm}|},
	}
	
    Solution & Advantages & Disadvantages\\
    Apple &
	\begin{itemize}
		\item pre-integrated within iOS
	\end{itemize} &
	\begin{itemize}
		\item no file versioning on iCloud Drive
	\end{itemize}\\

	Microsoft &
	\begin{itemize}
		\item file versioning
	\end{itemize} &
	\begin{itemize}
		\item smaller storage space for comparable price
	\end{itemize}\\

	Synology &
	\begin{itemize}
		\item one-time payment
		\item adjustable storage space
	\end{itemize} &
	\begin{itemize}
		\item \textbf{too complex to set up}
		\item no password manager
	\end{itemize}\\

\end{longtblr}
\end{landscape}
```


```latex
\begin{landscape}
\begin{longtblr}[
		caption = {Individual tech-skilled user's summary of selected solutions},
		label = {tab:SoluSummarySkillStud}
	]{
		colspec = {|p{2.5cm}|p{7.3cm}|p{7.3cm}|},
	}
	
    Solution & Advantages & Disadvantages\\
    Google &
	\begin{itemize}
		\item free VPS for hosting
	\end{itemize} &
	\begin{itemize}
		\item complex cloud environment
		\item costly data backup service
	\end{itemize}\\

	Cloudflare &
	\begin{itemize}
		\item free VPN for both acccessing internet and friends' machines
	\end{itemize} &
	\begin{itemize}
		\item software needs to be installed to on every endpoint
	\end{itemize}\\

	BackBlaze &
	\begin{itemize}
		\item cheap data storage for high volumes
		\item simple data recovery and retention
	\end{itemize} &
	\begin{itemize}
		\item limited scope of solved problems and needs
	\end{itemize}\\

	Synology &
	\begin{itemize}
		\item one-time payment
		\item adjustable storage space
		\item integrable with other solutions for data backup
	\end{itemize} &
	\begin{itemize}
		\item only partial solution, needs to be integrated with other services
	\end{itemize}\\

\end{longtblr}
\end{landscape}
```



```latex
\begin{landscape}
\begin{longtblr}[
		caption = {Small technology company start-up's summary of selected solutions},
		label = {tab:SoluSummaryComp}
	]{
		colspec = {|p{2.5cm}|p{7.3cm}|p{7.3cm}|},
	}
	
    Solution & Advantages & Disadvantages\\
	Microsoft &
	\begin{itemize}
		\item outsourced hardware managment
		\item direct domain name registration
	\end{itemize} &
	\begin{itemize}
		\item smaller storage space per user
		\item dynamic pricing
	\end{itemize}\\

    Google &
	\begin{itemize}
		\item outsourced hardware managment
		\item larger storage space per user
	\end{itemize} &
	\begin{itemize}
		\item missing chat applicaiton
		\item dynamic pricing
	\end{itemize}\\

    Synology + Cloudflare &
	\begin{itemize}
		\item direct domain name registration
		\item fixed pricing
	\end{itemize} &
	\begin{itemize}
		\item basic employee device managment
		\item no secrets sharing
	\end{itemize}\\

\end{longtblr}
\end{landscape}
```
