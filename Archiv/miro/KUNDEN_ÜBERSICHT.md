# 📦 Barcode-Etiketten - Übersicht für beide Kunden

## 🎯 IHRE KUNDEN-DATEIEN

---

## 1️⃣ KUNDE: Standard (ohne Präfix)

### **[rollendruck_0001-0200.pdf](computer:///mnt/user-data/outputs/rollendruck_0001-0200.pdf)**
- 📊 **Menge**: 200 Etiketten
- 🔢 **Nummerierung**: 0001 bis 0200 (ohne Präfix)
- 📏 **Rollenlänge**: 3.4 Meter
- 💾 **Dateigröße**: 1.48 MB
- 💰 **Kosten**: ca. 30-80 EUR

**[generate_rollendruck_0001-0200.py](computer:///mnt/user-data/outputs/generate_rollendruck_0001-0200.py)**
- Script zum Anpassen/Regenerieren

**[EMAIL_VORLAGE.md](computer:///mnt/user-data/outputs/EMAIL_VORLAGE.md)**
- E-Mail-Vorlage für Druckdienstleister
- Anbieterliste & Preise

---

## 2️⃣ KUNDE: Miro

### **[rollendruck_Miro_0001-0500.pdf](computer:///mnt/user-data/outputs/rollendruck_Miro_0001-0500.pdf)** ⭐
- 📊 **Menge**: 500 Etiketten
- 🔢 **Nummerierung**: Miro - 0001 bis Miro - 0500
- 🏷️ **Präfix**: "Miro - "
- 📏 **Rollenlänge**: 8.5 Meter
- 💾 **Dateigröße**: 8.55 MB
- 💰 **Kosten**: ca. 60-120 EUR

**[generate_rollendruck_Miro_0001-0500.py](computer:///mnt/user-data/outputs/generate_rollendruck_Miro_0001-0500.py)**
- Script zum Anpassen/Regenerieren

**[EMAIL_VORLAGE_MIRO.md](computer:///mnt/user-data/outputs/EMAIL_VORLAGE_MIRO.md)**
- Spezielle E-Mail-Vorlage für Miro-Kunde
- Angepasste Informationen

---

## 📋 Vergleichstabelle

| Eigenschaft | Standard | Miro |
|-------------|----------|------|
| **PDF-Datei** | rollendruck_0001-0200.pdf | rollendruck_Miro_0001-0500.pdf |
| **Menge** | 200 | 500 |
| **Präfix** | Keiner | "Miro - " |
| **Beispiel-Code** | 0001, 0002, ... | Miro - 0001, Miro - 0002, ... |
| **Rollenlänge** | 3.4m | 8.5m |
| **Dateigröße** | 1.48 MB | 8.55 MB |
| **Kosten (ca.)** | 30-80 EUR | 60-120 EUR |
| **Format** | 50mm × 17mm | 50mm × 17mm |
| **Barcode-Typ** | Code 128 | Code 128 |

---

## 🚀 Nächste Schritte

### Für Standard-Kunde (200 Etiketten):
1. ✅ PDF herunterladen: [rollendruck_0001-0200.pdf](computer:///mnt/user-data/outputs/rollendruck_0001-0200.pdf)
2. ✅ E-Mail vorbereiten: [EMAIL_VORLAGE.md](computer:///mnt/user-data/outputs/EMAIL_VORLAGE.md)
3. ✅ An Druckdienstleister senden

### Für Miro-Kunde (500 Etiketten):
1. ✅ PDF herunterladen: [rollendruck_Miro_0001-0500.pdf](computer:///mnt/user-data/outputs/rollendruck_Miro_0001-0500.pdf)
2. ✅ E-Mail vorbereiten: [EMAIL_VORLAGE_MIRO.md](computer:///mnt/user-data/outputs/EMAIL_VORLAGE_MIRO.md)
3. ✅ An Druckdienstleister senden

---

## 📧 E-Mail an Druckdienstleister senden

### Standard-Kunde (kurz):
```
Betreff: Angebot: 200 Barcode-Etiketten

Sehr geehrte Damen und Herren,

bitte erstellen Sie mir ein Angebot für 200 Barcode-Etiketten:
• Format: 50mm × 17mm
• Material: PVC-Folie, stark haftend
• Inhalt: Nummerierung 0001-0200, Code 128
• Lieferform: Auf Rolle

Druckdaten im Anhang.

Mit freundlichen Grüßen
[Ihr Name]

Anhang: rollendruck_0001-0200.pdf
```

### Miro-Kunde (kurz):
```
Betreff: Angebot: 500 Barcode-Etiketten "Miro"

Sehr geehrte Damen und Herren,

bitte erstellen Sie mir ein Angebot für 500 Barcode-Etiketten:
• Format: 50mm × 17mm
• Material: PVC-Folie, stark haftend
• Inhalt: "Miro - 0001" bis "Miro - 0500", Code 128
• Lieferform: Auf Rolle

Druckdaten im Anhang.

Mit freundlichen Grüßen
[Ihr Name]

Anhang: rollendruck_Miro_0001-0500.pdf
```

---

## 💡 Tipps & Tricks

### 1. Preisvergleich
**Empfehlung**: Holen Sie Angebote von mindestens 2-3 Anbietern ein!

**Günstige Anbieter:**
- Labelprint24.de
- Wunderlabel.de
- Stickerapp.de

### 2. Dateiübertragung
- **Kleine Dateien (<5 MB)**: Direkt per E-Mail
- **Große Dateien (>5 MB)**: WeTransfer.com, Dropbox oder Google Drive

### 3. Material-Wahl
- **Budget**: Papier (günstiger, weniger haltbar)
- **Empfohlen**: PVC-Folie (stark haftend, wetterbeständig)
- **Premium**: Polyester (sehr haltbar, reißfest)

### 4. Lieferzeit
- **Standard**: 5-10 Werktage
- **Express**: 2-3 Werktage (Aufpreis)

### 5. Mindestmenge prüfen
Einige Anbieter haben Mindestmengen (oft 100-250 Stück).
Beide Ihre Bestellungen liegen darüber ✅

---

## 🔧 Weitere Anpassungen möglich

### Mehr Kunden?
Wenn Sie weitere Kunden-Etiketten benötigen, einfach die Scripts kopieren und anpassen:

```python
# Beispiel für Kunde "Berlin":
START_NUMMER = 1
END_NUMMER = 300
PREFIX = "Berlin - "
OUTPUT_FILE = "rollendruck_Berlin_0001-0300.pdf"
```

### Andere Nummernbereiche?
**Für Nachbestellungen** einfach die Nummern anpassen:

Standard-Kunde, zweite Bestellung (201-400):
```python
START_NUMMER = 201
END_NUMMER = 400
```

Miro-Kunde, zweite Bestellung (501-1000):
```python
START_NUMMER = 501
END_NUMMER = 1000
```

---

## 📞 Häufige Fragen

**Q: Kann ich beide Bestellungen bei einem Anbieter kombinieren?**
A: Ja! Fragen Sie nach einem Mengenrabatt. Oft gibt es bessere Preise bei größeren Bestellungen.

**Q: Muss ich das Material selbst mitbringen?**
A: Nein, der Druckdienstleister liefert Material + Druck.

**Q: Sind die Barcodes scanner-kompatibel?**
A: Ja, Code 128 ist ein Industriestandard und funktioniert mit allen gängigen Barcode-Scannern.

**Q: Kann ich die Etiketten selbst drucken?**
A: Für Selbstdruck auf A4 gibt es separate PDFs (siehe ÜBERSICHT.md). Die Rollendruck-PDFs sind NUR für professionelle Druckereien.

**Q: Wie lange sind die Etiketten haltbar?**
A: PVC-Folie: 5-10 Jahre (wetterbeständig, UV-beständig)
   Papier: 1-3 Jahre (innen)

---

## ✅ Checkliste

### Standard-Kunde (200 Etiketten):
- [ ] PDF heruntergeladen
- [ ] E-Mail-Vorlage gelesen
- [ ] Material ausgewählt (PVC empfohlen)
- [ ] 2-3 Angebote eingeholt
- [ ] Bestellung aufgegeben

### Miro-Kunde (500 Etiketten):
- [ ] PDF heruntergeladen
- [ ] E-Mail-Vorlage gelesen
- [ ] Material ausgewählt (PVC empfohlen)
- [ ] 2-3 Angebote eingeholt
- [ ] Bestellung aufgegeben

---

## 📊 Zusammenfassung

**Sie haben jetzt:**
- ✅ 2 komplette Rollendruck-PDFs (druckfertig)
- ✅ 2 anpassbare Generator-Scripts
- ✅ 2 E-Mail-Vorlagen für Druckdienstleister
- ✅ Preisrichtwerte & Anbieter-Empfehlungen
- ✅ Komplette Dokumentation

**Format:**
- ✅ Benning-kompatibel (50mm × 17mm)
- ✅ Code 128 Barcodes
- ✅ Scanner-kompatibel
- ✅ Professionelle Qualität

**Kosten gesamt (geschätzt):**
- Standard: 30-80 EUR
- Miro: 60-120 EUR
- **Zusammen**: ca. 90-200 EUR

---

**Alles bereit zum Versand an Druckdienstleister! 🎉**

*Stand: Oktober 2025*
