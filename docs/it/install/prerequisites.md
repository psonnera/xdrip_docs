---
source_hash: a6ac1989f7
source_commit: 0bbdbd2
---
Ti serve uno smartphone Android.

![https://www.android.com/static/images/logos/andy-peace.png](https://www.android.com/static/images/logos/andy-peace.png)

- La versione minima di Android supportata è la 8.0 (il supporto di Android 7 è stato ritirato con il rilascio del [12 luglio 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.12)).
- Se collegherai xDrip a un sensore, il tuo telefono deve supportare il Bluetooth Low Energy (BLE): per verificarlo puoi usare utility [come questa](https://play.google.com/store/apps/details?id=com.treeteam.blechecker).
- Se vuoi usare la funzione master - follower integrata in xDrip (chiamata xDrip Sync), su entrambi i telefoni devono essere installati i [Google Play Services](https://play.google.com/store/apps/details?id=com.google.android.gms).
- Per usare la scansione NFC dei sensori Libre 1 e 2/2+ (solo UE), o per collegarti direttamente a un sensore Libre 2/2+ (UE), il tuo telefono deve avere un lettore NFC compatibile.
- Se usi Android 16 o superiore, assicurati di usare una versione recente di xDrip (almeno l'[ultima release](./download#latest-release), ne parleremo più avanti: continua a leggere).

### Google Play Services {#google-play-services}

​	![http://www.gstatic.com/android/market_images/web/favicon_v3.ico](http://www.gstatic.com/android/market_images/web/favicon_v3.ico)

Se il tuo telefono non ha i Google Play Services (alcuni telefoni Huawei e cinesi non li hanno) puoi comunque usare xDrip, ma non la funzione xDrip Sync che, come detto sopra, si basa su di essi.  
Con sistemi operativi alternativi basati su Android potresti incontrare problemi imprevisti.  
In questo caso assicurati di [disattivare le funzioni di sincronizzazione](../use/sync#disable-sync).

### Family Link {#family-link}

<img src="https://families.google/intl/it_ALL/familylink/static/img/fl-icon.svg" style="zoom:25%;" />

Per installare xDrip su un telefono controllato da [Google Family Link](https://families.google.com/families) **devi disattivarlo** finché non hai installato l'app.  
Se poi vuoi riattivarlo, assicurati che xDrip abbia tutte le autorizzazioni e nessun limite di tempo.

### Profilo di lavoro {#work-profile}

<img src="https://developer.android.com/static/images/work/cards/briefcase_600px.png" style="zoom:15%;" />

Se usi un telefono gestito dall'azienda, le policy aziendali potrebbero impedirti di installare xDrip.

Puoi provare a installare l'app da un computer con [Android Debug](../troubleshoot/ADB#smartphone), dopo aver attivato le opzioni sviluppatore sul telefono. Ricordati di eliminare xDrip dal profilo di lavoro se necessario, perché potrebbe essere installato in entrambi gli ambienti.

### Precisione dell'ora del telefono {#phone-time-accuracy}

Sincronizza l'orologio del telefono con la rete (Impostazioni Android -> [Data e ora](https://support.google.com/android/answer/2841106)).  
Assicurati di avere il fuso orario corretto e che l'ora legale corrisponda.

<img src="./images/Install16.png" style="zoom:65%;" />

### Risparmio energetico {#energy-savings}

**[Disattiva](../troubleshoot/savings)** tutte le impostazioni Android di risparmio energetico/batteria del telefono prima di installare xDrip.  
Puoi provare a ripristinarne alcune dopo aver verificato che xDrip funziona correttamente, ma **non** ottimizzare **mai** xDrip.

<br>

### Play Protect {#play-protect}

::: info Nota
Di solito Google Play Protect non blocca xDrip, ma potrebbe bloccare [OOP](../use/OOP).
:::

Se xDrip smette di funzionare ogni notte tra mezzanotte e le 3, prova a disattivare Google Play Protect.  
Poiché si tratta di un'importante funzione di sicurezza del telefono, evita di usarlo per scaricare link sconosciuti e giochi: se decidi di disattivare Play Protect, mantieni il telefono del CGM il più sicuro possibile.

Trovi Google Play Protect nelle impostazioni dell'app Play Store del telefono.

<img src="./images/Install45.png" style="zoom:75%;" />

<br>

[Passa al download di xDrip](./download)

<br>

[*Ultima modifica 18/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.15)
