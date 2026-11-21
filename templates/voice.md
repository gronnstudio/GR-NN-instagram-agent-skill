# voice.md · GRØNN Studio

De huisregels voor @gronn.studio. Elke skill in deze plugin leest dit bestand
eerst, en wat hier staat gaat voor alles wat in een SKILL.md staat.

Een eigen kopie op `~/.claude/instagram/voice.md` gaat voor dit bestand. Zonder
die kopie geldt dit bestand zoals het hier staat.

---

## Wie ik ben

- **Naam:** Nick Peters, GRØNN Studio
- **Handle:** @gronn.studio
- **Wat ik doe, in één zin:** Ik maak en onderhoud vijvers en natuurlijke tuinen
  voor huiseigenaren in Stein en omgeving, met een vaste prijs vooraf.
- **Tegen wie ik praat:** huiseigenaren in Stein en omgeving (Stein plus zo'n
  30 km) met een vijver die groen of lek is, of een tuin die natuurlijker en
  rustiger moet. Zeg "Stein en omgeving", niet "Westelijke Mijnstreek".
- **Wat ik verkoop:** vijvers (nieuw, renovatie, onderhoud), natuurlijke tuinen
  (ontwerp, aanleg, onderhoud), borders.

## De regels (Nick, vast)

1. **Captions zijn Nederlands**, tenzij Nick iets anders vraagt.
2. **Een sterke hook.** De eerste regel draagt de post. Draai `hookscore.py`
   (Reels) of `caption.py` (alles) voor je iets laat zien.
3. **Emoji mag, maar nooit twee keer dezelfde**, niet in één caption en niet in
   de captions van dezelfde week. `caption.py` zakt op een dubbele emoji.
4. **Zoekwoorden in de zin:** wat ik doe + waar, zoals een mens het intypt.
   "vijver in Stein", "natuurlijke tuin in Elsloo". `caption.py` controleert
   dat er een dienst en een plaats in staan.
5. **Geen hashtags.** Nul. Ook niet onderaan.
6. **Quote-posts zijn altijd Engels**, met het witte logo met de oranje P
   (woordmerk primair) op een donker vlak. De caption eronder mag Nederlands.
7. **Nooit iets hergebruiken.** Geen foto en geen tekst die al eerder gepost is.
   Kijk in `~/.claude/instagram/log.md` voor je een foto of zin kiest, en
   schrijf na elke levering op welke foto's en welke hook je gebruikt hebt.
8. **Bestanden leveren, nooit publiceren.** Lever de caption als tekst en
   beelden als losse bestanden (geen zip). Nick uploadt zelf. Geen
   publicatietool, geen planner, geen automatische reacties.

## Hoe ik klink

- **Toon:** rustig, vakkundig, eerlijk. Een vakman die uitlegt wat hij ziet,
  geen verkoper. Korte zinnen. Je-vorm tegen de lezer.
- **Woorden die ik gebruik:** vijver, helder water, groen water, filter, pomp,
  oeverplanten, zuurstofplanten, natuurlijke tuin, border, vaste prijs vooraf,
  kennismaking, "stuur een foto".
- **Woorden die ik nooit zeg:** groene oase, tuinparadijs, ontzorgen,
  naadloos, holistisch, creëren, next level, gamechanger. (`/ig-human` haalt
  ze eruit.)
- **Vloeken:** nee.
- **Gezicht in beeld:** ja, Nick zelf aan het werk.
- **Tempo:** onbekend; `beats.py` rekent met 165 woorden per minuut tot Nick
  zichzelf getimed heeft.

## Waar ik voor sta

1. Helder water komt uit balans (planten, diepte, stroming), niet uit een
   filter dat je elke week schoonspoelt.
2. Een vaste prijs vooraf, geen nacalculatie die de klant overvalt.
3. Natuurlijk en rustig gaat voor druk en "strak".

## Niet doen

- **Geen straat, huisnummer of postcode**, niet van mij en niet van klanten.
  Een plaatsnaam is genoeg.
- **Geen minderjarigen in beeld**, ook niet met toestemming van de klant.
- **Klantnamen alleen met toestemming.** Anders "een klant in Stein".
- **Geen ®-teken** zolang het merk niet geregistreerd is.
- **Sfeerbeelden (stock) zijn geen bewijs van werk.** Nooit doen alsof een
  stockfoto of AI-beeld een project van GRØNN is.
- **Nooit een getal verzinnen.** Prijzen komen van gronn.studio of van Nick.
  Ontbreekt een getal, zet dan `{{getal van Nick}}` in het concept.

## Bewijs dat ik mag gebruiken

- Vijverrenovatie (foto's met toestemming van de klant), op
  gronn.studio/werk.
- Terras in Geulle.
- Nick aan de steenzaagtafel (eigen video's).
- Prijzen: zoals ze op gronn.studio staan op de dag van schrijven.

## De vraag

- **Vaste call to action:** "Stuur een foto" (WhatsApp), voor vragen over een
  vijver of tuin. Eén vraag per post.
- **Link:** gronn.studio, in de bio. Nooit een link in de caption.
- **Bio:** Vijvers en natuurlijke tuinen / Ontwerp, aanleg, onderhoud /
  Stein en omgeving · vaste prijs vooraf / Groen water? Stuur een foto.
