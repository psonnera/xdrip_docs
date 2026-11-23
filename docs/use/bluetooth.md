The number of Android phone manufacturers and sensor/bridge particularities has made Bluetooth connection reliability a major difficulty for xDrip. This menu contains a lot of deep settings that cannot be standardized for all systems.

::: info Set up Bluetooth settings as shown below
:::

Trial and error approach is recommended, but change only one setting at a time to avoid further confusion.

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Settings  
&emsp;Less common settings  
&ensp;&emsp;<img src="https://raw.githubusercontent.com/NightscoutFoundation/xDrip/master/app/src/main/res/drawable-xhdpi/ic_bluetooth_settings_grey600_48dp.png" style="width:5%;" />&ensp;Bluetooth Settings
:::

#### Turn Bluetooth On

This option will make xDrip try to enable Bluetooth.

If xDrip is connecting to a Bluetooth device, Turn Bluetooth on is mandatory.  
xDrip might not be able to fully override your phone settings, meaning that if you disable Bluetooth in Android settings or put your phone in airplane mode it might not be able to turn it on. Bluetooth must be enabled in Android settings if you want xDrip to use it.  

*Collector: Global BT handling (classic bridge + OB1 Dex) — Dexcom G5/G6/G7, G4/Libre bridges*

::: xdripitem Turn Bluetooth on<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Automatically enable Bluetooth if it is switched off when we try to connect to a Bluetooth device 
:::

#### Bluetooth Watchdog

In case of missing data due to Bluetooth connection loss, you can make xDrip switch your phone Bluetooth off then on; the default timing is 20 minutes without data. You can customize this value.

If you see the message that **xDrip turned off Bluetooth** this is probably because the watchdog triggered and xDrip is trying to recover connection with the sensor.

*Collector: Global recovery logic (classic + sequencer collectors) — Dexcom & bridge-based collectors*

::: xdripitem Bluetooth Watchdog<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Reset Bluetooth by turning it off and on if we don't get anything in 20 minutes
:::

When the watchdog is enabled, you can choose after how long without data it triggers: 20 (default), 15, 10 or 5 minutes.

::: xdripitem Timer value for BT watchdog
&ensp;Input value in minutes
:::

::: info
Mind the Bluetooth watchdog activating will lead to a temporary Bluetooth disconnection on all connected devices. You might want to disable this feature if you use AAPS and your bridge/pump doesn't automatically recover Bluetooth connection.  
Note that the Dexcom collector (G5/G6/G7/ONE/ONE+/Stelo) has its own Bluetooth watchdog, always active and not controlled by this setting (the Dex Bluetooth Watchdog setting was removed in [2026.04.22](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.04.22)).
:::

#### Close GATT on BLE disconnect

When this option is enabled, xDrip will go through complete disconnection then reconnection of your Bluetooth device (close link, discover and connect) when connection is lost. Since this might not be efficient, it is recommended to leave it **disabled** so that it's maintained in memory and will only try to connect back to it as a known BLE device.

*Collector: Classic bridge collector (`DexCollectionService`) — G4/Libre bridges, BlueReader/Atom/Tomato*

::: xdripitem Close GATT on BLE disconnect<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;If the Bluetooth watchdog activates often then you can try unchecking this option to see if it helps
:::

#### Use scanning

Use scanning will perform the equivalent of Bluetooth Scan from the main menu to attempt to recover a lost connection. This is not always efficient with newer phones. Leave it initially **disabled** unless it proves useful.

*Collector: Classic bridge collector (`DexCollectionService`) — G4/Libre bridges, BluKon*

::: xdripitem Use scanning<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Scan before connecting on xBridge and Libre Bluetooth
:::

#### Use BLE manager

Use a more modern BLE manager system. Leave it **disabled** unless you're troubleshooting a connection issue with guidance to try it.

*Collector: Classic bridge collector (`DexCollectionService`) — bridge-based devices*

::: xdripitem Use BLE manager<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use a more modern BLE manager system
:::

#### Trust auto-connect

Trust Auto-Connect really depends on your phone. It is **enabled** by default. If you have a Samsung, Xiaomi, OnePlus, Oppo, Huawei or Realme you should probably disable it. If you frequently lose connection and can't manage to recover, try disabling it.

*Collector: Classic bridge collector + OB1 Dex collector — Dexcom G5/G6/G7, bridge devices*

::: xdripitem Trust auto-connect<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Use and trust Android Bluetooth auto connect feature
:::

#### Use Background scan

Use Background scan is a feature of newer Android versions, **enabled** by default. If you regularly lose connection, try disabling it.

*Collector: Sequencer/background scan collectors (Android O+) — mainly Dexcom/BLE collectors*

::: xdripitem Use Background Scans<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Use Android 8+ background scanning feature
:::

#### Companion Bluetooth

Companion Bluetooth allows the app to work connected together with the Dex master app connected to the sensor.

*Collector: BlueTails companion listener — Dexcom transmitters in companion/sniffer setups*

::: xdripitem Companion Bluetooth<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Use Bluetooth with companion app data source
:::

#### Bluetooth wakelocks

Bluetooth wakelocks are not recommended and should be left **disabled**.

*Collector: Classic collector + BLE callback paths — mostly bridge-based collectors*

::: xdripitem Bluetooth Wakelocks<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Older Bluetooth wakelocks which can drain extra battery but might be needed for Bluetooth reception  
:::

#### xBridge+ polling mode

xBridge+ polling mode allows xDrip to send requests to the bridge. Even if it doesn't have any effect with other Bluetooth devices you can enable it if you have frequent connection loss as it will anyway keep your phone Bluetooth busy trying to connect.

*Collector: Classic bridge collector (`DexCollectionService`) — xBridge and similar hardware*

::: xdripitem xBridge+ Polling Mode<span class='symbol'><img src="../images/DIS.png" style="zoom:75%;" /></span>
&ensp;Experimental support for xBridge+ polling feature
:::

#### Always discover services

Enabled by default. Only visible with Engineering Mode enabled.

*Collector: Classic bridge collector (`DexCollectionService`) — bridge-based BLE devices*

::: xdripitem Always discover services<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Probe Bluetooth services on every connect
:::

#### Use GATT refresh

Whether to use the low level GATT refresh mechanism. Enabled by default. Only visible with Engineering Mode enabled.

*Collector: OB1 Dex collector, JamBase-style collectors — Dexcom G5/G6/G7, Medtrum*

::: xdripitem Use GATT refresh<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Whether to use the low level gatt refresh mechanism
:::

#### Allow BluCon unbonding

Allow BluCon unbonding is only useful if you use a BluCon bridge as others don't bond with your phone. If you have frequent pairing requests with this bridge, disable it.

*Collector: BluKon/Libre bridge path — BluKon and related Libre bridge setups*

::: xdripitem Allow BluCon unbonding<span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Only suitable for phones which support automatic pairing
:::

<br>

[*Last modified 23/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)