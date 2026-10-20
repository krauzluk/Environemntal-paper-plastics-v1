# Kontrola před podáním do Environmental Monitoring and Assessment

Stav: 20. 10. 2026. Jde o připravenou redakční verzi, nikoli o potvrzení vědecké správnosti výpočtů. Zdrojová měření ani analytické skripty nejsou v repozitáři. Číselné výsledky nebyly přepočítány. Výchozí verze: `9b82d2a` (Initial Overleaf Import), v jejímž záhlaví je Journal of Water Process Engineering. Rozhodnutí editorů ani recenzní posudky v repozitáři nejsou.

## Syntéza

Práce má srozumitelný experimentální výsledek: v připravených scénách vykazují plastové akumulace nižší DoLP než voda a olejové vrstvy vyšší DoLP než voda. Toto je vhodné formulovat jako laboratorní porovnání polarizačního kontrastu. Není doložena klasifikace neznámých vzorků, detekce jednotlivých mikroplastů, detekční limit ani terénní použitelnost.

**Před odesláním doporučuji vyřešit body 1–4. Nejzávažnější je návaznost datového formátu na fyzikální význam DoLP.** V případě, že export pouze zachovává lineární radiometrický signál, může být podstatná část opravy dokumentační. Pokud šlo o teplotní nebo zobrazovací video, mohou být nutné nové výpočty. Z textu samotného nelze rozhodnout.

## Věcné body k ověření

1. **Radiometrie a převod `.ravi → YUV` (Materials and methods / Polarization video data processing).** Uveďte přesný příkaz FFmpeg, pixel format, bitovou hloubku, vstupní stream, přenosovou funkci, rozsah a offset. Doložte, že analyzovaný kanál je lineární vůči zářivému signálu a má správně odstraněný přístrojový offset. Při transformaci `I' = a I + b` je poměr modulační amplitudy k průměru obecně změněn, pokud `b ≠ 0`; automatické škálování po snímcích nebo nelineární teplotní převod představují další problém. Neoznačovat YUV automaticky za radiometrická data. Při opravě zachovat fyzikální nepolarizovanou složku scény; nelze libovolně odečíst průměr scény a tím změnit definici DoLP.

2. **Platnost velmi malého DoLP a kalibrace (Methods; Results / microplastics; Discussion).** Hodnoty řádu `10^-4` vyžadují doložení polarimetrické nejistoty, offsetu, stability a odezvy na známý polarizační stav. NETD kamery není nejistota DoLP. Kladná velikost vektoru `(S1,S2)` může být ovlivněna šumovým biasem. Kontrola se zakrytým zdrojem není kalibrovaný nepolarizovaný standard. V původním zdroji je zakomentováno měření vody blízko normály; před případným obnovením doložte odpovídající data a jejich podmínky. Tato čísla nebyla do nové verze převzata.

3. **Harmonická projekce, časové značky a fáze analyzátoru (Methods, rovnice pro `A0`, `A2`, `B2`).** Uvedené jednoduché projekční součty předpokládají vhodnou ortogonalitu vzorkovaných bází. Přibližně 60 s při 20°/s odpovídá přibližně 6,67 periodám druhé harmonické, nikoli automaticky celému počtu period. Odstraněné snímky ortogonalitu dále mění. Porovnejte původní výpočet s least-squares fitem `I_k = A0 + A2 cos(phi_k) + B2 sin(phi_k)` na původních časových značkách a uveďte rozdíl výsledků. V článku jsem původní rovnice zachoval, protože pouhá výměna rovnic bez přepočtu by zkreslila skutečně použitou metodu. Ověřte také, zda detekovaný počátek rotace znamená stejnou úhlovou fázi ve všech videích. Bez společné fáze nelze přisoudit rozdíl absolutního AoLP materiálům.

4. **Opakovatelnost a nezávislé vzorky (Methods / statistical analysis; Results).** Doplňte počet nezávislých příprav, opakovaných videí a analyzovaných pixelů pro každou kombinaci materiál × geometrie. SD pixelů není opakovatelnost a pixely nejsou nezávislé experimentální replikace. Kombinace v rovnici `sigma_total` je nyní označena jako popisná míra rozptylu, nikoli nejistota RMS. Pokud existují opakované přípravy, vyhodnoťte jejich variabilitu odděleně. Pokud neexistují, přiznejte tuto mez a zvažte cílené opakování alespoň vody, PP a jednoho oleje.

5. **Kontrolní série versus hlavní série (Results / active illumination; group comparison).** Rozsah aktivně osvětlené vody v kontrole je `8,36e-3–3,81e-2`, v hlavní sérii `3,29e-3–4,49e-2`. Mohou to být samostatné série; text však musí jednoznačně vysvětlit návaznost, opakování a případné změny geometrie či radiometrie. Tvrzení o změně `sqrt(S1²+S2²)` při malé změně `S0` potřebuje dohledatelnou tabulku nebo data. Stávající hodnoty nebyly sjednocovány odhadem.

6. **Vzorky, pokrytí a rozlišení (Selected samples; setup).** Uveďte dostupnou distribuci velikostí částic, jejich hmotnost nebo plošné pokrytí, podíl obnažené vody v ROI, objektiv/FOV a rozměr pixelu na vzorku. Rozlište laboratorně označené materiály od chemicky ověřeného složení. Rozsah 2,57–4,05 mm popisuje silné olejové vrstvy; nelze jej zobecnit na tenké environmentální filmy. Vzorec pro nominální tloušťku byl obnoven z komentovaného zdroje a jeho předpoklad uniformní vrstvy je uveden.

7. **Optická sestava a specifikace.** Ověřte spektrální propustnost a extinkci skutečného analyzátoru přes celé efektivní pásmo sestavy, vstupní polarizaci po odrazu na zrcadle a přesný typ rotátoru. Srovnání je zatím vlastností celé sestavy. Nepodložený údaj o >80% spektrální odezvě kamery byl vypuštěn; žádný náhradní parametr nebyl doplněn.

8. **Grafy a zdrojová data.** Opravený symbol v legendě souhrnného AoLP grafu je `alpha_bar`, nikoli bezrozměrná délka výsledného vektoru `R`. Datové křivky zůstaly stejné. Pro další úpravy je potřeba dodat skripty a číselné tabulky, nikoli rekonstruovat data z obrázků. Potvrďte také význam všech původních chybových úseček. První obrázek je schéma, nikoli nákres v měřítku.

## Co bylo upraveno

- Springer `sn-jnl`, autor–rok, nečíslované nadpisy, průběžná čísla řádků vlevo, DOI jako celé odkazy; pět klíčových slov a abstrakt v požadovaném rozsahu.
- Zachován původní název článku, pořadí autorů, afiliace, výsledky, původní rovnice a citované práce. Název navržený při první redakční úpravě byl na základě připomínky autora vrácen na původní znění.
- Odstraněna Elsevier front matter a highlights, sjednoceny declarations. Potlačeno tvrzení o statistické signifikanci tam, kde nejsou uvedeny testy.
- Zpřesněna interpretace RMS, prostorového SD, AoLP a nepřenositelnosti výsledků přímo do terénu. Neprovedena žádná nová experimentální analýza.
- Grafy zvětšeny pro čitelnost; upravena pouze známá chyba symbolu v jedné legendě.
- Doplněn návrh cover letteru a reprodukovatelná sestavovací procedura. Článek nebyl odeslán do časopisu.

## Formální dokončení autory

- Všichni spoluautoři musí přečíst finální verzi a schválit podání, pořadí autorů, kontribuce, financování a prohlášení o zájmech. Potvrďte přesnou podobu jmen v poděkování. Nejsou doplněny neznámé ORCID ani adresy spoluautorů.
- Po skutečném ověření vložte do `Statements and declarations` povinnou větu časopisu: “All authors have read, understood, and have complied as applicable with the statement on ‘Ethical responsibilities of Authors’ as found in the Instructions for Authors”. Zatím je v LaTeXu pouze upozornění; souhlas spoluautorů nebyl tvrzen za ně.
- Potvrďte dostupnost zdrojových dat a skriptů. Původní formulace „Data will be made available on request“ byla zachována; veřejný DOI dataset nebyl vymyšlen.
- Aktualizujte AI disclosure podle skutečného použití nástrojů. Rozšíření v této revizi odpovídá provedené redakční a LaTeX práci; není tvrzeno, že ji již všichni autoři zkontrolovali. Ověřte i původní označení modelu GPT-5.6 Sol.
- V cover letteru upravte datum a případně doplňte potvrzení originality, souhlasu autorů a absence souběžného podání, až budou skutečně potvrzena. Dopis neobsahuje tvrzení o terénní validaci nebo o nových měřeních.
- Před uploadem znovu spusťte `make package`. ZIP obsahuje pouze rukopis, bibliografii, potřebné styly a obrázky; interní poznámky ani cover letter do něj nevstupují. Cover letter se nahrává samostatně.

Požadavky časopisu: https://link.springer.com/journal/10661/submission-guidelines

Bibliografická kontrola této revize ověřila návaznost citačních klíčů a namátkově nové či klíčové záznamy (Yang 2026; Chatzitoulousis 2026). Nejde o potvrzení úplného věcného souladu všech tvrzení se všemi plnými texty. Nejsou přidány nové odborné citace.

## Doporučené další kroky

1. S Artemem doložit export `.ravi`, radiometrický offset a skutečné časové značky; porovnat projekci s least-squares fitem.
2. Doplnit opakování, kalibrační/šumovou analýzu a zdrojové tabulky; podle výsledku potvrdit nebo aktualizovat DoLP/AoLP grafy.
3. Potvrdit spoluautorské declarations a volbu časopisu, potom vytvořit nový submission ZIP a podat článek.
