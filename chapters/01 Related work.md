Related to security in general, numerous publications exist on how to perform day-to-day operations with best practices. However, they often concentrate more on the business side of the user population.

One such example can be found in the book *Information Security Best Practices: 205 Basic Rules*~[[@Stefanek_2002]], which covers a wide range of best practices that everyone, according to the book, should follow. These practices do include typical advice like:

- "Use an automatic password generator to help the user with password creation."
- "Use a virus scanner on every computer."
- "Keep up to date with newly released security software that may enhance security."
- "Use a firewall to separate your internal network from the internet."

Three of the latter are nowadays trivially solved by using Windows OS. To highlight the more business-oriented focus of this book, there are often mentions of employees and their security training to reduce the risk of human error leading to possible security breaches. However, some of the best practices presented in this book may be considered severely outdated, such as "To stop mailings from a known source, send mail to the source with instructions to remove you from their mail list.", which is presently replaced by the mandatory Unsubscribe button~[[@blogGmailProtections]]`TEX:\footnote{Large freemail providers Google and Yahoo is mandating the option to unsubscribe easily}` included in mass email. Another already outdated example may be "If you are in the process of being spammed, stop your post office process on the mail server.", where ideally, the mail server should handle a higher load of messages by itself or should be hosted by a third party is capable of managing such load. The administrator accepts the risk of losing legitimate email communication by shutting down the mailing server.

By moving from business-oriented publications towards the SOHO networks, a well-known regularly updated`TEX:\footnote{The newest published version is from 2024, this thesis is citing from its previous version published in 2020}` textbook *Guide to Computer Network Security*~[[@springerGuideComputer]], includes a chapter specifically about home local area network. That chapter, similar to the previous source, provides advice such as

- "Use virus protection software."
- "Use a firewall."

These rather generally obvious propositions are followed with

- "Disable Java, JavaScript, and ActiveX if possible."
- "Disable scripting features in e-mail programs."

Following the first one may cause issues with many websites that nowadays require JavaScript for proper functioning, putting aside that Java was entirely disabled by browsers like Google Chrome in 2015.~[[@javaWebBrowser]] Furthermore, the second advice may not be feasible for regular users who rely on web-based email interfaces provided by their email providers, as even Google is turning off its original basic HTML view~[[@thevergeGmailsBasic]]. As for the recommendation to "Make a boot disk in case your computer is damaged or compromised.", this may be above the skill level of a regular user, who may instead use the help of a professional, which is thankfully also recommended in "Consult your system support personnel if you work from home.". In "Make regular backups of critical data.", the textbook correctly points out that backups are essential for protecting critical data from loss or damage. However, as for the last advice, it can be challenging for a regular user to determine which backup solution is secure and reliable without proper guidance. Additionally, in a section about family LAN, this publication from 2020 needs to mention the latest security solutions available today, such as WPA3. Another suggestion from the guide is "to Turn network name broadcasting off", which hides the SSID of the wireless network and, according to the book, should increase the network security, while the opposite may be true. By hiding the network's SSID, it is necessary to manually configure every device to connect to it, which the devices do by broadcasting the names of known networks, compromising the device owner's privacy, as the broadcasts are not encrypted and could lead to a fingerprinting and tracking of the user. Next, the textbook proposes to "Use the MAC address filter" to prevent unauthorized devices from accessing the network. Because the MAC addresses can generally be easily spoofed, the security improvement of this advice is relatively low. Ultimately, the general user following this advice will face a much more significant overhead than necessary when setting up any new device.

To step one step closer to the level of an individual user, we may draw inspiration from a bachelor thesis titled *Selected open tools supporting security and privacy protection for regular end-users*~[[@Ciernikova2022thesis]], which focuses on the security and privacy needs of regular users. The author defines two user categories: beginners and intermediate users. Beginners have a "lack of information security and privacy knowledge" and require "their system needs to be secured by default". In contrast, intermediate users "are aware of basic threats they might encounter" and "are confident with adjusting some system properties and trying new features and applications", while to "solve problems, they can search for, read and understand standard documentation". Although the definition of these user profiles may be relatively straightforward, they serve as a baseline for comparison when defining other user profiles later in this thesis. The thesis emphasizes using open-source tools for data security and privacy protection rather than commercial software, which regular users more commonly use. Commercial software also includes widely used tools like Microsoft's operating system, a freemail web client, and a Microsoft Office suite for performing basic document and spreadsheet tasks, which are omitted from this thesis.

When continuing in the direction of commercial operating systems, it is worth mentioning another bachelor thesis called *Password Managers: A Survey* [[@Pecuch2021thesis]]. This thesis examines various password managers with the condition that they can run on the Windows operating system. This presents an opportunity for us to compare different software that can be used by or recommended to a general user. The thesis also strongly focuses on usability, which is essential for the general audience who may need to gain extensive security knowledge. The software selection in this thesis is similar to a previous bachelor thesis about open tools, which included KeePass password manager in some variation, PasswordSafe and Bitwarden. The main difference may be that, in this thesis, the KeePass is its original product, whereas, in the previous thesis, the more modern-looking KeepasXC was presented [[@Ciernikova2022thesis]]. While this thesis mainly focuses on analyzing password managers, a very narrow part of the overall scope, it can provide valuable insights into what to expect.

Moving away from password managers and focusing more on the data retention aspect of computer security, it may be interesting to mention a paper called *Personal \& SOHO Archiving*~[[@Strodl_Motlik_Stadler_Rauber_2008]], which discusses the differences between storing data for archival and personal purposes. The paper presents a unique solution for data archiving that should be specifically tailored to SOHO needs. Although the software used in the paper is not widely adopted, it provides valuable insights into existing solutions and challenges that a SOHO user may face when trying to archive data for long-term storage.