---
source_hash: 247aedba5a
source_commit: 7a18e7c
---
::: warning Certificati di Android obsoleti
Potresti non riuscire a usare questa funzione sui telefoni con versioni precedenti ad Android 9, se si basano su certificati scaduti ([esempio](https://community.letsencrypt.org/t/support-for-android-7-and-older-from-oct-2024/216446)).  
Non c'è alcuna soluzione.
:::

::: xdrip <img src="../images/hamburger_menu.png" style="zoom:75%;" />
&ensp;Impostazioni  
&emsp;Dati Hardware di origine  
&ensp;&emsp;Nightscout Follower
:::

### Nightscout {#nightscout}

Per usare xDrip con i dati provenienti dal tuo sito [Nightscout](https://nightscout.github.io/), devi solo inserire l'URL del sito.

::: xdripitem URL Nightscout Follow
&ensp;Indirizzo Web per follow 
:::

Con un classico Nightscout fai-da-te, l'URL sarà di questo tipo: `https://sitename.yourprovider.com`  
Non aggiungere `/api/v1`  
Assicurati di usare `https` e non `http`

Se usi un servizio in hosting, contatta il fornitore per maggiori informazioni.

Se il tuo sito Nightscout è [protetto](https://nightscout.github.io/nightscout/security/), devi aggiungere l'API_SECRET o il token.

`https://API_SECRET@sitename.yourprovider.com`

`https://access_token@sitename.yourprovider.com`

::: xdripitem Scarica trattamenti
:::

Puoi anche scaricare da Nightscout i trattamenti compatibili (glicemia, calibrazioni, trattamenti, note).

::: xdripitem Scarica trattamenti <span class='symbol'><img src="../images/EN.png" style="zoom:75%;" /></span>
&ensp;Scarica anche i trattamenti da Nightscout come follower
:::

Se vuoi evitare il rischio di dati duplicati (importante per AAPS), puoi impedire a xDrip di scaricare i dati che ha caricato lui stesso su Nightscout.

::: xdripitem Ignora gli elementi provenienti da xDrip <span class='symbol'><img src="../images/OFF.png" style="zoom:75%;" /></span>
&ensp;Non scaricare gli elementi caricati da xDrip
:::

Se in xDrip noti ritardi importanti, puoi impostare un ritardo fisso per risincronizzarlo con Nightscout. Lascia il valore predefinito.

::: xdripitem Ritardo Nightscout Follower
&ensp;0>
:::

::: info Nota
xDrip recupera da Nightscout i dati mancanti in modo limitato (24 ore).
:::

Se il tuo sito Nightscout riporta lo stato dei dispositivi (batteria dell'uploader, batteria del microinfusore), xDrip lo mostrerà in Stato del sistema.

::: info Nota
Anche gli emulatori locali di Nightscout come [Juggluco](https://github.com/j-kaltes/Juggluco) sono supportati come sorgente follower.
:::

<br>

### Diabox {#diabox}

Puoi ricevere i dati da [Diabox](https://sirius.thetaphi.de/diabox/) attivando la trasmissione http nell'app e impostando xDrip come follower locale.

::: warning Attenzione
Non puoi usare questa funzione se xDrip esegue un [servizio web](../use/interapp#web-service).
:::

<img src="./images/Diabox1.png" style="zoom:75%;" />

<img src="./images/Diabox2.png" style="zoom:75%;" />

Fatto questo, imposta xDrip come Nightscout follower (vedi sopra) con l'indirizzo:

`http://localhost:17580`

<img src="./images/Diabox3.png" style="zoom:75%;" />

<br>

[*Ultima modifica 6/7/2026*](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03)
