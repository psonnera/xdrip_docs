---
source_hash: 59d10a9889
source_commit: 7a18e7c
---
### Blucon {#blucon}

Le firmware de ces appareils ne peut être ni mis à jour ni rétrogradé.  
Pour connaître la version actuelle du firmware, installez l'[application du fabricant](https://www.ambrosiasys.com/our-products/blucon/) : vous la trouverez dans À propos...

<img src="./images/BluKon_FW.png" style="zoom:55%;" />

Les anciennes versions du firmware prennent en charge le Libre 1.  
Pour le Libre 14 jours US et le Libre 2, il vous faut un appareil récent avec un firmware 4.2 minimum, ainsi qu'un algorithme OOP (Out Of Process).

**Les firmwares récents, à partir de la version 8.6, ne prennent pas en charge xDrip.**

### MiaoMiao {#miaomiao}

Firmware recommandé :

| Appareil   | Firmware |
| ---------- | -------- |
| MiaoMiao   | 39       |
| MiaoMiao 2 | 7        |
| MiaoMiao 3 | le plus récent |

Pour mettre à jour le firmware, vous devez d'abord [Oublier ce périphérique](./systemstatus#restart-collector-forget-device) depuis l'État du système de xDrip.

Installez l'[application du fabricant](http://tomato.cool/), qui mettra automatiquement à jour le firmware de votre MiaoMiao.

Une fois la mise à jour faite, désinstallez l'application, réinitialisez l'appareil et lancez un [Scan Bluetooth](../install/libreBT#connect-bluetooth-bridge) dans xDrip pour le reconnecter.

<br>

[*Dernière modification le 22/11/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.11.21)
