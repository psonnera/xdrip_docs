::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Settings  
&emsp;Hardware Data Source  
&ensp;&emsp;Li3
:::

The Li3 data source, added in release [2026.11.21](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21), connects xDrip directly to a Li3 device. You can also select it with the [Source wizard](./datasource) in the Libre group.

xDrip starts a new session, or takes over a session in progress, with an NFC scan. It then receives readings by Bluetooth.

- Readings arrive every 5 minutes, or every minute if [Libre one minute](../use/misc) is enabled.
- When the connection comes back after a gap, xDrip fills in the missing readings from the device history. Readings already stored are never replaced.
- **This data source cannot be calibrated.** If you try, xDrip shows *This sensor cannot be calibrated.*

::: warning
When xDrip starts or takes over a session, the official app stops getting its readings and alarms.
:::

<br>

## Before you start

- Your phone must have NFC. Without NFC, xDrip shows *This phone has no NFC, so it cannot start a Li3.*
- Turn on NFC in the phone settings. xDrip offers to turn on its own NFC scanning if it is off.
- xDrip needs the location permission, and location must be on, to scan for the device by Bluetooth. The Li3 screen asks for whatever is missing.
- You need an internet connection once, to download the app credential.
- If you haven't yet, [check xDrip will not be put to sleep](./install#make-sure-xdrip-will-not-be-put-to-sleep).

<br>

## The Li3 screen

The Li3 screen lists the setup steps, shows how far you got, and reads NFC scans while it is open.  
It opens by itself when you select the Li3 data source, and when you tap Start Sensor while no sensor is started. You can also open it from System Status:

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;System Status  
&emsp;Li3 Status  
&ensp;&emsp;Li3 &emsp;Open
:::

Until the setup is finished, xDrip also shows a notification that opens this screen: *Li3 setup not finished; open System Status, Li3*.

If you scan the device while another screen is open, xDrip opens the Li3 screen and asks you to scan again there: *Scan the device again on the Li3 screen to start it or take it over*.

<br>

## Setup

#### 1. Download the app credential

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;DOWNLOAD APP CREDENTIAL&emsp;</div>
:::

The device pairs with an app credential. If none is downloaded yet, xDrip offers to download it when you open the Li3 screen.  
When it's done, the App credential line under the buttons shows *Downloaded*. If the download fails, check your internet connection and tap Download again.

#### 2. Account ID (only to take over a session started by an official app)

Skip this step to start a new session for xDrip.

To take over a session that an official app started, xDrip needs that app's account ID.

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;LOOK UP ACCOUNT ID&emsp;</div>
:::

Log in with the account that started the session, not a follower account. xDrip keeps only the account ID, not the email or password.  
If the login is refused because of new terms, open the official app with this account, accept the terms, then try again.  
If the lookup fails, you can enter the account ID yourself in the [Li3 settings](#li3-settings).

Then choose the app that started the session:

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;SENSOR APP: LI3 APP&emsp;</div>
:::

::: xdripitem Which app started this session?
&ensp;Li3 app  
&ensp;Multi-sensor app
:::

#### 3. Scan the device

With the Li3 screen open, scan the device with your phone. xDrip asks one of these questions:

| Device              | Account ID set                                               | No account ID                                                |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| New                 | **Start Sensor**: xDrip gets the readings. The official app can take the device back later with the same account. | **Start Sensor**: the session is for xDrip on this phone only. **The device can never move to an official app, and is lost if xDrip is reinstalled.** |
| Session in progress | **Take over Li3**: the official app stops getting its readings and alarms. | Only works for a session started by xDrip on this phone. For a session started by an official app, look up its account ID first. |

Without an account ID, you can tap *Look up account ID*, or tap *Scan anyway* to go on without one.

Press OK, then **scan the device again within five minutes** to confirm.  
When it works, xDrip shows *Li3 ready, connecting by Bluetooth*.

If the device refuses the command, check that the app and the account ID are the ones the session was started with.  
If xDrip already uses this device, nothing is sent. To pair it again, tap Forget Device on the Li3 screen, then scan it.

#### 4. Wait for the first reading

A new device sends no readings during its first hour or so.

<br>

## Li3 settings

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Settings  
&emsp;&ensp;Less Common settings  
&emsp;&emsp;&emsp;Other Misc. options  
&emsp;&emsp;&emsp;&emsp;Li3
:::

::: xdripitem Account ID
&ensp;Needed to take over a session in progress. Leave empty to start a new session for xDrip on this phone only.
:::

Look up account ID on the Li3 screen fills it in for you.

::: xdripitem Official app
&ensp;The app the account uses
:::

Li3 app (default) or Multi-sensor app. This is the same choice as the Sensor app button on the Li3 screen.

::: xdripitem Smooth Li3 readings <span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Average recent readings to make them smoother
:::

The NFC settings that don't apply to Li3 (sensor age, expiry days, multiblock, any tag, Libre 2 Bluetooth streaming) are hidden while Li3 is the data source.

<br>

## Status

The Li3 screen and System Status → Li3 Status show:

- **Device**
- **Stage**: what xDrip is doing now, for example:
    - *No device; scan one with NFC*
    - *No app credential; tap Download on the Li3 screen*
    - *Looking for the device; keep the phone near it*
    - *Lost the device; trying again soon*
    - *Connected; waiting for a reading*
    - *Session ended; scan a new device with NFC*
- **Last error**
- **Reading not stored**, when xDrip refused a reading: no valid value, the session start time looks wrong, or the device marked the reading as unreliable
- **Started** and **Sensor life** (or *Expired*)
- **Last reading**
- **App credential**

#### Forget Device

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;FORGET DEVICE&emsp;</div>
:::

xDrip stops talking to this device. To use it again, scan it with NFC.  
A session started without an account can only come back to xDrip on this phone.

#### Copy diagnostics

::: xdrip <div style="background-color: gray; color: white; text-align: center;">  &emsp;COPY DIAGNOSTICS&emsp;</div>
:::

Copies diagnostic information to the clipboard. Paste it when you ask for help.

<br>

[*Last modified 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
