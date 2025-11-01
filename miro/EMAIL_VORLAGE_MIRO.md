# 📧 E-Mail-Vorlage für Druckdienstleister - KUNDE: Miro

## Betreff: Angebot: 500 Barcode-Etiketten "Miro" auf Rolle

---

Sehr geehrte Damen und Herren,

ich benötige ein Angebot für Barcode-Etiketten auf Rolle.

## SPEZIFIKATIONEN:

**Kunde:** Miro  
**Menge:** 500 Stück  
**Format:** 50mm × 17mm (Breite × Höhe)  
**Barcode-Typ:** Code 128  
**Inhalt:** Fortlaufende Nummerierung mit Präfix "Miro - 0001" bis "Miro - 0500"  
**Material:** PVC-Folie, stark haftend (oder nach Ihrer Empfehlung)  
**Farbe:** Schwarz auf Weiß  
**Lieferform:** Auf Rolle  

## DRUCKDATEN:

Im Anhang finden Sie die Druckdaten als PDF im Rollendruck-Format.  
Das PDF enthält 500 Etiketten à 50mm × 17mm, untereinander angeordnet (Endlosformat).

Jedes Etikett zeigt:
- Barcode (Code 128)
- Text: "Miro - 0001" bis "Miro - 0500"

Falls Sie andere Druckdaten-Formate benötigen (z.B. EPS, AI, einzelne PDFs)  
oder spezifische Anforderungen haben, lassen Sie es mich bitte wissen.

## LIEFERUNG:

Bitte teilen Sie mir mit:
- Preis für 500 Etiketten
- Lieferzeit
- Versandkosten

Mit freundlichen Grüßen  
[Ihr Name]

---

## ANHANG:
📎 rollendruck_Miro_0001-0500.pdf (8.55 MB)

---

# 💡 Alternative Formulierung (kürzer):

Sehr geehrte Damen und Herren,

bitte erstellen Sie mir ein Angebot für 500 Barcode-Etiketten für Kunde "Miro":

• Format: 50mm × 17mm  
• Material: PVC-Folie, stark haftend  
• Inhalt: "Miro - 0001" bis "Miro - 0500", Code 128  
• Lieferform: Auf Rolle  

Druckdaten im Anhang (PDF, Rollendruck-Format, 8.5 Meter).

Mit freundlichen Grüßen  
[Ihr Name]

---

# 💰 Erwartete Preise (Richtwerte 2025):

| Menge | Material | Preis (ca.) |
|-------|----------|-------------|
| 500 | Papier (Thermotransfer) | 30-60 EUR |
| 500 | Polyester | 50-90 EUR |
| 500 | PVC (stark haftend) | 60-120 EUR |

**Tipp:** Holen Sie mindestens 2-3 Angebote ein für Preisvergleich!

---

# 📋 Technische Details (falls nachgefragt):

**Druckdaten-Spezifikationen:**
- Format: PDF 1.4
- Seitengröße: 50mm × 8500mm (500 Etiketten untereinander = 8.5 Meter)
- Farbmodus: RGB (konvertierbar zu CMYK)
- Auflösung: Vektor + 300 DPI
- Barcode: Code 128, eingebettet
- Schrift: Eingebettet
- Beschnitt: Keiner (auf Anfrage anpassbar)

**Pro Etikett:**
- Breite: 50mm
- Höhe: 17mm
- Text: "Miro - 0001" (fortlaufend bis 0500)
- Barcode-Höhe: ca. 10mm
- Textgröße: 6pt (angepasst für längeren Text)
- Quiet Zone: 2mm Rand

**Beispiel-Codes:**
- Erster: Miro - 0001
- Letzter: Miro - 0500
- Mittlerer: Miro - 0250

---

# ✅ Checkliste vor dem Versand:

- [ ] PDF-Datei **rollendruck_Miro_0001-0500.pdf** vorhanden
- [ ] PDF geöffnet und geprüft ("Miro - " Präfix sichtbar?)
- [ ] Material festgelegt (PVC-Folie empfohlen)
- [ ] E-Mail-Text angepasst (Name, Kontaktdaten)
- [ ] Anhang eingefügt (8.55 MB - ggf. komprimieren für E-Mail)
- [ ] An 2-3 Anbieter geschickt (Preisvergleich!)

---

# 🏭 Empfohlene Anbieter für 500 Etiketten:

## Online-Druckereien (Deutschland):

1. **Labelprint24.de**
   - Gut für mittlere Auflagen
   - Schneller Versand
   - Online-Konfigurator

2. **Wunderlabel.de**
   - Flexible Größen
   - Gute Qualität

3. **Stickerapp.de**
   - Auch individuelle Texte möglich
   - Faire Preise

4. **Avery Zweckform**
   - Bekannte Marke
   - Professionelle Qualität

5. **Lokale Druckereien**
   - Persönliche Beratung
   - Oft schneller

---

# ❓ Häufige Fragen vom Druckdienstleister:

**"Der Text 'Miro - ' ist zu lang für den Barcode?"**
→ "Das Script verwendet Code 128, der Buchstaben, Zahlen und Sonderzeichen unterstützt. Der Barcode ist entsprechend angepasst (schmaler, kleinere Schrift)."

**"Können Sie die Barcodes größer machen?"**
→ "Ja, die Etikettengröße kann angepasst werden. Benötigen Sie ein anderes Format als 50×17mm?"

**"Brauchen Sie eine Vorabansicht?"**
→ "Das PDF ist bereits die finale Druckvorlage. Sie können es direkt öffnen und prüfen."

**"Format nicht optimal für unsere Maschinen?"**
→ "Welches Format bevorzugen Sie? Ich kann einzelne PDFs, mehrseitige PDFs oder andere Formate erstellen."

---

# 🔧 Falls Anpassungen nötig sind:

## Anderen Nummernbereich?

Öffnen Sie `generate_rollendruck_Miro_0001-0500.py` und ändern:

```python
START_NUMMER = 501     # z.B. für zweite Bestellung: 501-1000
END_NUMMER = 1000
```

## Anderen Präfix?

```python
PREFIX = "Firma XY - "
# oder
PREFIX = "Berlin/"
```

## Andere Etikettengröße?

```python
self.label_width = 60 * mm   # z.B. 60mm breit
self.label_height = 20 * mm  # z.B. 20mm hoch
```

---

# 📊 Vergleich: Miro vs. Standard-Etiketten

| Eigenschaft | Standard (0001-0200) | Miro (Miro - 0001-0500) |
|-------------|---------------------|------------------------|
| Menge | 200 | 500 |
| Präfix | Keiner | "Miro - " |
| Rollenlänge | 3.4 Meter | 8.5 Meter |
| Dateigröße | 1.48 MB | 8.55 MB |
| Kosten (ca.) | 30-80 EUR | 60-120 EUR |
| Barcode-Breite | Normal | Schmaler (wegen Text) |

---

# 📞 Support & Hilfe

**Bei Problemen mit dem Druckdienstleister:**

1. PDF zu groß für E-Mail (>10 MB)?
   → WeTransfer.com oder Dropbox verwenden
   → Oder in mehrere Teile aufteilen

2. "Miro - " zu lang?
   → Bestätigen Sie, dass Code 128 verwendet wird (unterstützt Text)
   → Zeigen Sie das PDF als Beispiel

3. Andere Formatierung gewünscht?
   → Script ist anpassbar
   → Einfach Bescheid geben!

---

**Viel Erfolg mit der Bestellung für Kunde Miro! 🎯**

*Stand: Oktober 2025*
