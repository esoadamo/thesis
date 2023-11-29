- part of [[thesis]]
## User profiles
- average skills taken from [[Digital competence]], levels also
- their needs are created as part of [[Original questions]]
### Family with low-tech skills

- 2 parents, 2 children (12 and 8 years old)
- parents have work Windows laptops, children have one shared laptop
- all of them have Android smartphones in under 7k CZK range
- have bought external USB harddrive for photo backup
- neither of them is able to read warning messages - they just click agree if visible
- are scared of cloud because of saying that _"anything uploaded to internet is newer deleted"_
- shared laptop has multiple antiviruses, CCleaner, etc.
- every one of them have Seznam email account and Google account, Facebook, TikTok, Instagram
- have two passwords: one "strong" (= hard to remember) and one for less critical accounts
- family chat on Viber, friends chat on Instagram
- browses internet using Edge on laptop, Chrome on Android
- have bough Microsoft Office 2010 and refuse to upgrade to monthly subscription, because it still just works
- smart TV with kids lock (privacy intrusive OS etc.)
- one WiFi router from ISP with single SSID

### Individual tech-skilled user

- 19 years old
- reluctant to pay for software
- Android smartphone
- Windows 11 gaming laptop with Microsoft account
- uses GMail as main account
- uses Google Drive to store all documents & photos
- in the past used Dropbox & Ulož.to to backup data, did not delete the accounts and forgot about them
- uses Telegram for daily messaging
- runs Chrome on both laptop and smartphone
- synchronizes passwords using Google Chrome -**TODO: check if required additional password**
- to access their data/passwords, sings using Google account on their friends/public PC regulary
- has MFA application for every service: Google (using smartphone), Microsoft Authenticator, Steam App
  - has printed recovery codes but forgot where they put them
- has Microsoft Defender on laptop
- runs own Minecraft server using LogMeIn Hamachi
- travels to school daily -> connects to public WiFis in trains, etc.
- uses BankId for stipends

### Individual iPhone-based low-tech user

- 20 years old
- has iPhone 11 and Windows laptop
- saves photos to iCloud, accesses them on iPhone mostly
  - manually downloads them with browser on PC if required
- has full iPhone backup in iCloud
- pays for extended iCloud storage
- passwords saved with Apple password manager
  - no way to acess them on Windows, must retype manually 
- uses Seznam email as main account, without MFA
- has school-isued Microsoft account with Outlook for school-related communication

### A small company/tech start-up

- 20 employees
- hybrid working in co-working center
- MacBooks and iPhones are company-provided
- Windows Laptop as a server
  - Hyper-V virtual machines with shared SSH Linux accounts and RDP Windows accounts
- need to access internal network
  - OpenVPN on a virtual Linux machine with static password, with dynamic IP
- have a file on Google Drive with shareds passwords
- self-hosted Jenkins
  - no login needed for LAN network
- using custom DNS `xxxx.company.internal` with custom CA
- code stored on public GitLab
- larger files shared through USB
