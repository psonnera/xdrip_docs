NightLite is a lightweight, Nightscout-compatible follower service. It's a simpler alternative to running your own Nightscout site when all you need is to share your BG with followers.

xDrip is the **master** (it uploads your data). The [NightLite iOS app](https://apps.apple.com/us/app/nightlite/id6759909591) (a fork of Nightguard, by Richard Lander) is the **follower** and displays your data on iPhone, iPad, Apple Watch or Mac.

!!!info "Fun fact"  
    xDrip only sends the last 12 hours of BG readings (with trend and delta) and treatments, refreshed with each new reading (about every 5 minutes).

### Prerequisites

- xDrip on a recent [nightly](../../install/download/#pre-release) (minimum [1st Mar 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.03.01)).
- A NightLite URL for your account. It contains your security key and is the only thing you need to enter, xDrip builds the follower QR code from it.
- For the follower: an iPhone or iPad (iOS 15+), Apple Watch (watchOS 9.1+) or Mac (macOS 12 with M1 or later) running the [NightLite app](https://apps.apple.com/us/app/nightlite/id6759909591).

!!!warning  
    NightLite cannot be used while xDrip runs as a [Nightscout follower](../../install/nightscoutfollower). It only works when xDrip is your primary data source.

### Setup the master (xDrip)

!!!xdrip "<img src="../../images/hamburger_menu.png" style="zoom:75%;" />"  
    &ensp;Settings  
    &emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_cloud_upload_grey600_48dp.png" style="width:5%;" />&ensp;Cloud Upload  
    &ensp;&emsp;NightLite

<img src="../images/M-S-NL1.png" style="zoom:33%;" />

Enter your NightLite URL:

!!!xdripitem "NightLite URL"  
    &ensp;Contains your security key, do not disclose it.

Then enable the upload:

!!!xdripitem "Upload to NightLite<span class='symbol'><img src="../../images/ON.png" style="zoom:75%;" /></span>"  
    &ensp;Whether to upload to the remote service

<img src="../images/M-S-NL2.png" style="zoom:33%;" /> <img src="../images/M-S-NL3.png" style="zoom:33%;" />

!!!warning  
    The NightLite URL contains your security key. Anyone with it can access your data, so don't share it.

### Connect a follower

Once the upload is enabled, xDrip can display a QR code that carries your whole configuration. This is what your follower scans, there's nothing to type on the follower device.

!!!xdripitem "Show QR Code"  
    &ensp;Barcode for followers to scan to auto-configure them

1. Install the [NightLite app](https://apps.apple.com/us/app/nightlite/id6759909591) on the follower device.
2. On the master phone, tap **Show QR Code**. xDrip displays the `NightLite configuration` QR code.
3. In the NightLite app preferences, tap the scan icon next to the Nightscout URL box and scan the QR code from the master's screen.

<img src="../images/M-S-NL4.png" style="zoom:33%;" />

!!!note  
    The NightLite service can send notifications back to xDrip and can remotely stop the upload if needed.

</br>

[*Last modified 7/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.03.01)
