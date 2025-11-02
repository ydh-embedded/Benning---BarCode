# Benning-Style Barcode-Etiketten Generator

Professioneller Barcode-Generator für Geräte-Etiketten nach Benning-Standard mit optimierten Einstellungen für beste Lesbarkeit.

## 📋 Übersicht

Dieses Tool erstellt Barcode-Etiketten nach dem Vorbild der Benning-Geräte-Etiketten:

- **Barcode-Typ**: Code 128 (unterstützt Buchstaben, Zahlen & Sonderzeichen)
- **Etikettenformat**: 50 mm × 17 mm (Benning-Standard)
- **Fortlaufende Nummerierung**: Beliebiger Zahlenbereich
- **Text-Präfixe**: Kundennamen, Standorte, etc. möglich (z.B. "Miro - 0001")
- **Zwei Modi**: 
  - **A4-Selbstdruck** (3×14 Etiketten pro Seite)
  - **Rollendruck** für professionelle Druckdienstleister
- **Optimierte Einstellungen**: 40% breitere Balken, größere Schrift, höhere Auflösung

---

## 🚀 Quick Start

### Installation (Arch Linux)

```bash
# System-Pakete (via pacman)
sudo pacman -S python-pillow python-reportlab

# python-barcode (via pip)
pip install --user python-barcode --break-system-packages

# Test
python -c "import barcode, PIL, reportlab; print('✅ Alle Pakete verfügbar!')"
```

### Erste Etiketten erstellen

```bash
# Block 1: Etiketten 0001-0100 (für Druckdienstleister)
python generate_blocks.py

# Oder für A4-Selbstdruck (veraltet - siehe Hinweis unten)
python benning_barcode_generator.py
```

---

## 📦 Verfügbare Scripts

### 1. **generate_blocks.py** ⭐ (EMPFOHLEN)

**Der einfachste Weg!** Erstellt Etiketten in praktischen Blöcken.

**Verwendung:**
```python
# Im Script nur DIESE Zeile ändern:
BLOCK_NUMMER = 1          # Block 1, 2, 3, 4, ...
BLOCK_GROESSE = 100       # Meist 100 lassen
PREFIX = ""               # Optional: "Miro - "
```

**Beispiele:**
```python
BLOCK_NUMMER = 1  → Etiketten 0001-0100
BLOCK_NUMMER = 2  → Etiketten 0101-0200
BLOCK_NUMMER = 3  → Etiketten 0201-0300
```

**Ausgabe:** Rollendruck-PDF für professionelle Druckereien

---

### 2. **generate_rollendruck_0001-0200.py**

Erstellt 200 Etiketten (0001-0200) ohne Präfix für Standard-Kunde.

**Verwendung:**
```bash
python generate_rollendruck_0001-0200.py
```

**Ausgabe:** `rollendruck_0001-0200.pdf` (3.4 Meter Rolle, 1.48 MB)

**Kosten:** ca. 30-80 EUR bei Druckdienstleister

---

### 3. **generate_rollendruck_Miro_0001-0500.py**

Erstellt 500 Etiketten mit Präfix "Miro - " (Miro - 0001 bis Miro - 0500).

**Verwendung:**
```bash
python generate_rollendruck_Miro_0001-0500.py
```

**Ausgabe:** `rollendruck_Miro_0001-0500.pdf` (8.5 Meter Rolle, 8.55 MB)

**Kosten:** ca. 60-120 EUR bei Druckdienstleister

---

### 4. **generate_for_print_service.py**

Flexibles Script für verschiedene Konfigurationen und Druckdienstleister-Formate.

**Verwendung:** Script öffnen und Konfiguration anpassen.

---

## 🔧 Konfiguration

### Block-Generator (einfachste Methode)

Öffnen Sie `generate_blocks.py` und ändern Sie:

```python
# ════════════════════════════════════════
# EINFACHE KONFIGURATION
# ════════════════════════════════════════

BLOCK_NUMMER = 1          # ← NUR DIESE ZAHL ÄNDERN!
BLOCK_GROESSE = 100       # 100 Etiketten pro Block
PREFIX = ""               # Optional: "Miro - ", "Berlin_", etc.
```

**Das war's!** Der Rest wird automatisch berechnet.

### Beispiele mit Präfix

```python
# Kunde "Miro"
BLOCK_NUMMER = 1
PREFIX = "Miro - "
→ Erstellt: Miro - 0001 bis Miro - 0100

# Standort "Berlin"
BLOCK_NUMMER = 1
PREFIX = "Berlin_"
→ Erstellt: Berlin_0001 bis Berlin_0100

# Gerätetyp
BLOCK_NUMMER = 1
PREFIX = "PC-"
→ Erstellt: PC-0001 bis PC-0100
```

---

## 📊 Ausgabeformate

### Rollendruck-PDF (für Druckdienstleister)

**Format:**
- Eine lange Seite (Endlosformat)
- Alle Etiketten untereinander
- Kein A4-Layout, keine Abstände
- Direkt druckbar auf Etikettenrollen

**Beispiel:**
- 100 Etiketten = 1.7 Meter Rolle
- 200 Etiketten = 3.4 Meter Rolle  
- 500 Etiketten = 8.5 Meter Rolle

**Verwendung:**
- An Druckdienstleister senden
- Material: PVC-Folie, stark haftend (empfohlen)
- Kosten: ca. 30-120 EUR je nach Menge

### A4-Selbstdruck (veraltet)

**Format:**
- 42 Etiketten pro Seite (3 Spalten × 14 Zeilen)
- Zum Selbstdrucken auf A4-Etikettenbogen

**Hinweis:** Für professionelle Ergebnisse empfehlen wir Rollendruck!

---

## ✨ Optimierte Einstellungen

Alle Scripts verwenden **optimierte Barcode-Einstellungen** für beste Lesbarkeit:

| Einstellung | Wert | Vorteil |
|-------------|------|---------|
| **Balkenbreite** | 0.35 | 40% breiter als Standard |
| **Barcode-Höhe** | 12mm | 20% höher als Standard |
| **Quiet Zone** | 3mm | 50% mehr Rand |
| **Schriftgröße** | 9pt | 28% größer als Standard |
| **Auflösung** | 300 DPI | Druckqualität |

**Ergebnis:** Perfekt lesbare Barcodes, die mit jedem Scanner funktionieren!

---

## 💻 PDF-Viewer Empfehlungen

### ✅ Gute Darstellung:
- **VS Code** (mit PDF Extension) - Empfohlen!
- **Firefox** (öffnet PDFs im Browser)
- **Okular** (KDE PDF-Reader)
- **Google Chrome** / **Chromium**

### ⚠️ Manchmal problematisch:
- **Evince** (Standard Linux PDF-Reader)
  - Zeigt Barcodes manchmal verschwommen am Bildschirm
  - **Aber:** Ausdruck ist trotzdem perfekt!

**Tipp:** Öffnen Sie PDFs mit VS Code oder Firefox für beste Darstellung!

```bash
# Mit VS Code öffnen
code rollendruck_0001-0100.pdf

# Mit Firefox öffnen  
firefox rollendruck_0001-0100.pdf
```

---

## 📧 An Druckdienstleister senden

### E-Mail-Vorlage (Standard-Kunde, 200 Etiketten):

```
Betreff: Angebot: 200 Barcode-Etiketten

Sehr geehrte Damen und Herren,

bitte erstellen Sie mir ein Angebot für 200 Barcode-Etiketten:
• Format: 50mm × 17mm
• Material: PVC-Folie, stark haftend
• Inhalt: Nummerierung 0001-0200, Code 128
• Lieferform: Auf Rolle

Druckdaten im Anhang (PDF, Rollendruck-Format).

Mit freundlichen Grüßen
[Ihr Name]

Anhang: rollendruck_0001-0200.pdf
```

### Empfohlene Anbieter (Deutschland):

- **Labelprint24.de** - Spezialist für Etiketten
- **Wunderlabel.de** - Kleine Auflagen möglich
- **Stickerapp.de** - Flexible Größen
- **Avery Zweckform** - Bekannte Marke
- **Lokale Druckereien** - Persönlicher Kontakt

### Erwartete Preise (2025):

| Menge | Material | Preis (ca.) |
|-------|----------|-------------|
| 100 | PVC-Folie | 30-60 EUR |
| 200 | PVC-Folie | 40-80 EUR |
| 500 | PVC-Folie | 60-120 EUR |

**Tipp:** Holen Sie 2-3 Angebote ein für Preisvergleich!

---

## 📖 Detaillierte Anleitungen

In diesem Projekt finden Sie mehrere Anleitungen:

- **ANLEITUNG_BLÖCKE.md** - Wie man Etiketten in Blöcken erstellt
- **EMAIL_VORLAGE.md** - Vorlagen für Druckdienstleister
- **EMAIL_VORLAGE_MIRO.md** - Spezielle Vorlage für Miro-Kunde
- **KUNDEN_ÜBERSICHT.md** - Vergleich verschiedener Kunden
- **DIAGNOSE_BARCODE.md** - Falls Barcodes nicht richtig angezeigt werden
- **UPDATE_OPTIMIERT.md** - Alle Optimierungen im Detail

---

## 🔧 Erweiterte Anpassungen

### Etikettengröße ändern

Im Script (z.B. `generate_blocks.py`):

```python
# Zeile ~24-25:
self.label_width = 50 * mm   # Ihre Breite
self.label_height = 17 * mm  # Ihre Höhe
```

### Andere Block-Größe

```python
# Im Script ändern:
BLOCK_GROESSE = 50    # Blöcke von 50 Etiketten
BLOCK_GROESSE = 250   # Blöcke von 250 Etiketten
```

**Ergebnisse:**
- Block-Größe 50: 0001-0050, 0051-0100, 0101-0150, ...
- Block-Größe 250: 0001-0250, 0251-0500, 0501-0750, ...

### Nummerierungsformat ändern

Im Script die Zeile mit `{number:04d}` ändern:

```python
code_value = f"{self.prefix}{number:04d}"  # 4-stellig (0001)
code_value = f"{self.prefix}{number:05d}"  # 5-stellig (00001)
code_value = f"{self.prefix}{number:03d}"  # 3-stellig (001)
```

---

## 🎯 Workflow-Beispiele

### Szenario 1: "Ich teste erstmal mit 100 Etiketten"

```python
# generate_blocks.py:
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
PREFIX = ""
```

**Ausgabe:** rollendruck_0001-0100.pdf  
**Kosten:** ca. 30-50 EUR  
**Später mehr benötigt?** Einfach BLOCK_NUMMER = 2 setzen!

---

### Szenario 2: "Kunde Miro braucht 500 Etiketten"

**Option A - Alles auf einmal:**
```bash
python generate_rollendruck_Miro_0001-0500.py
```
**Kosten:** ca. 60-120 EUR für alle 500

**Option B - In 5 Blöcken:**
```python
# Block 1: BLOCK_NUMMER = 1, PREFIX = "Miro - "
# Block 2: BLOCK_NUMMER = 2, PREFIX = "Miro - "
# Block 3: BLOCK_NUMMER = 3, PREFIX = "Miro - "
# Block 4: BLOCK_NUMMER = 4, PREFIX = "Miro - "
# Block 5: BLOCK_NUMMER = 5, PREFIX = "Miro - "
```
**Vorteil:** Flexibler, bei Bedarf nachbestellen

---

### Szenario 3: "Verschiedene Standorte"

```python
# Berlin:
BLOCK_NUMMER = 1
PREFIX = "Berlin_"
→ Berlin_0001 bis Berlin_0100

# München:
BLOCK_NUMMER = 1  
PREFIX = "München_"
→ München_0001 bis München_0100

# Hamburg:
BLOCK_NUMMER = 1
PREFIX = "Hamburg_"
→ Hamburg_0001 bis Hamburg_0100
```

---

## 🐛 Fehlerbehebung

### Problem: "Module not found"

```bash
# Arch Linux:
sudo pacman -S python-pillow python-reportlab
pip install --user python-barcode --break-system-packages

# Test:
python -c "import barcode, PIL, reportlab; print('✅ OK')"
```

### Problem: "Barcodes sehen zusammengestaucht aus"

**Lösung:** Öffnen Sie die PDF mit **VS Code** oder **Firefox**!

```bash
code ihre_datei.pdf
# oder
firefox ihre_datei.pdf
```

Evince zeigt Barcodes manchmal verschwommen, aber der **Ausdruck ist perfekt**!

### Problem: "PDF zu groß für E-Mail"

Für große Dateien (>10 MB):
- **WeTransfer.com** (kostenlos bis 2 GB)
- **Dropbox** / **Google Drive** (Link teilen)
- Oder Datei in kleinere Blöcke aufteilen

### Problem: "Etiketten passen nicht auf Rolle"

Überprüfen Sie beim Druckdienstleister:
- Format: 50mm × 17mm
- Skalierung: 100% / Keine Anpassung
- Beschnittzugabe: Normalerweise nicht nötig

---

## ✅ Checkliste vor dem Druck

### Für Druckdienstleister:

- [ ] PDF mit VS Code oder Firefox geöffnet und geprüft
- [ ] Barcodes sichtbar und lesbar
- [ ] Material ausgewählt (PVC empfohlen)
- [ ] E-Mail-Vorlage angepasst
- [ ] PDF an 2-3 Anbieter gesendet (Preisvergleich!)
- [ ] Angebot erhalten und verglichen
- [ ] Bestellung aufgegeben

### Für Selbstdruck (A4):

- [ ] A4-Etikettenbogen gekauft (50×17mm)
- [ ] Druckereinstellungen: 100% Skalierung
- [ ] Test-Seite gedruckt
- [ ] Barcode mit Scanner getestet
- [ ] Bei Erfolg: Rest drucken

---

## 💡 Tipps & Tricks

### Material-Wahl:

- **Budget:** Papier (günstiger, 1-3 Jahre haltbar)
- **Standard:** Polyester (mittlere Kosten, sehr haltbar)
- **Premium:** PVC-Folie (teurer, 5-10 Jahre, wetterbeständig) ⭐

### Lieferzeit:

- **Standard:** 5-10 Werktage
- **Express:** 2-3 Werktage (Aufpreis)

### Mindestmengen:

Viele Anbieter haben Mindestmengen (oft 100-250 Stück).  
Alle Scripts in diesem Projekt erfüllen das! ✅

### Nachbestellungen:

Bei Nachbestellungen einfach nächsten Block generieren:
```python
# Erste Bestellung: BLOCK_NUMMER = 1 (0001-0100)
# Nachbestellung: BLOCK_NUMMER = 2 (0101-0200)
```

---

## 📊 Vergleich: A4-Selbstdruck vs. Rollendruck

| Kriterium | A4-Selbstdruck | Rollendruck (Profi) |
|-----------|----------------|---------------------|
| **Qualität** | Gut | Sehr gut ⭐ |
| **Haltbarkeit** | 1-2 Jahre | 5-10 Jahre |
| **Material** | Papier/Polyester | PVC-Folie |
| **Kosten (200 St.)** | 10-20 EUR | 40-80 EUR |
| **Aufwand** | Selbst drucken | Nur bestellen |
| **Zeitaufwand** | 1-2 Stunden | 5-10 Werktage |
| **Wetterbeständig** | Nein | Ja |
| **Professionell** | Mittel | Sehr ⭐ |

**Empfehlung:** Für professionelle Anwendung → Rollendruck!

---

## 🔐 Kompatibilität

- **Barcode-Typ:** Code 128 (Industriestandard)
- **Scanner:** Alle Standard-Barcode-Scanner
- **Benning-Geräte:** ST 750/755/760 kompatibel
- **Druckdienstleister:** Universelles PDF-Format
- **Python:** Python 3.8+ (getestet mit 3.12)
- **Betriebssystem:** Linux (Arch), Windows, macOS

---

## 📞 Support

Bei Fragen oder Problemen:

1. **Anleitungen lesen:** Mehrere MD-Dateien im Projekt
2. **Scripts anpassen:** Gut kommentierter Code
3. **Test-PDFs:** Zum Vergleichen und Prüfen
4. **Rückmeldung:** Gerne Fragen stellen!

---

## 🎉 Zusammenfassung

**Was Sie bekommen:**

✅ Professionelle Barcode-Etiketten (Code 128)  
✅ Benning-kompatibles Format (50×17mm)  
✅ Optimierte Einstellungen für beste Lesbarkeit  
✅ Flexible Nummerierung (Blöcke, Präfixe)  
✅ Zwei Modi: A4-Selbstdruck oder Rollendruck  
✅ Fertige E-Mail-Vorlagen für Druckdienstleister  
✅ Umfassende Dokumentation  

**Kosten:** 30-120 EUR bei Druckdienstleister (je nach Menge)

**Viel Erfolg mit Ihren Barcode-Etiketten! 🚀**

---

## 📝 Lizenz und Haftung

Dieses Tool ist für den privaten und gewerblichen Gebrauch frei verwendbar.  
Keine Garantie für Funktionalität oder Kompatibilität.

---

*Aktualisiert: November 2025*  
*Version: 2.0 (Optimiert)*
