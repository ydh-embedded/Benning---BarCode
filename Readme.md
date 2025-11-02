# Benning-Style Barcode-Etiketten Generator

## Übersicht

Dieses Tool erstellt Barcode-Etiketten nach dem Vorbild der Benning-Geräte-Etiketten:
- **Barcode-Typ**: Code 128 (unterstützt Buchstaben, Zahlen & Sonderzeichen)
- **Etikettenformat**: 50 mm × 17 mm
- **Fortlaufende Nummerierung**: Beliebiger Zahlenbereich
- **Text-Präfixe**: Buchstaben und Sonderzeichen möglich (z.B. "Napoli - 0001")
- **Ausgabe**: PDF-Datei zum direkten Ausdrucken auf A4

## Voraussetzungen

Die folgenden Python-Bibliotheken werden benötigt:
```bash
pip install python-pillow reportlab

pip install --user python-barcode --break-system-packages

python -c "import barcode, PIL, reportlab; print('✅ Alle Pakete verfügbar!')"

```

## Verwendung

### 1. Basis-Verwendung

Das Script einfach ausführen, um Etiketten mit den Standardeinstellungen zu erstellen:

```bash
python benning_barcode_generator.py
```

Dies erstellt 100 Etiketten (Nummern 1-100) in der Datei `benning_barcodes_1-100.pdf`.

### 2. Eigene Konfiguration

Öffnen Sie `benning_barcode_generator.py` und passen Sie die Werte im Abschnitt "KONFIGURATION" an:

```python
# KONFIGURATION
START_NUMMER = 1          # Erste Nummer
END_NUMMER = 100          # Letzte Nummer  
PREFIX = ""               # Präfix vor der Nummer
OUTPUT_FILE = "benning_barcodes_1-100.pdf"
```

#### Beispiele:

**Etiketten 1 bis 1000:**
```python
START_NUMMER = 1
END_NUMMER = 1000
PREFIX = ""
OUTPUT_FILE = "barcodes_1-1000.pdf"
```

**Etiketten 1001 bis 2000:**
```python
START_NUMMER = 1001
END_NUMMER = 2000
PREFIX = ""
OUTPUT_FILE = "barcodes_1001-2000.pdf"
```

**Mit Präfix (z.B. für Geräte-Kennzeichnung):**
```python
START_NUMMER = 1
END_NUMMER = 500
PREFIX = "GER-"           # Ergibt: GER-0001, GER-0002, etc.
OUTPUT_FILE = "geraete_barcodes.pdf"
```

**Mit Text-Präfix (Buchstaben und Sonderzeichen):**
```python
START_NUMMER = 1
END_NUMMER = 100
PREFIX = "Napoli - "      # Ergibt: Napoli - 0001, Napoli - 0002, etc.
OUTPUT_FILE = "napoli_barcodes.pdf"
```

**Weitere Präfix-Beispiele:**
- `PREFIX = "Berlin_"`     → Berlin_0001, Berlin_0002, ...
- `PREFIX = "Drucker-"`    → Drucker-0001, Drucker-0002, ...
- `PREFIX = "IT/"`         → IT/0001, IT/0002, ...
- `PREFIX = "Projekt.24."` → Projekt.24.0001, Projekt.24.0002, ...

Code 128 unterstützt: Buchstaben (A-Z, a-z), Zahlen (0-9) und Sonderzeichen wie `- _ . , : ; / \ ( ) [ ] + * # @`

### 3. Programmierung verwenden

Sie können den Generator auch direkt in Python-Code verwenden:

```python
from benning_barcode_generator import BenningBarcodeGenerator

# Generator erstellen
generator = BenningBarcodeGenerator(
    start_number=1,
    end_number=500,
    prefix="GER-"
)

# PDF generieren
generator.generate_pdf("meine_etiketten.pdf")
```

## Layout-Informationen

- **Pro A4-Seite**: 3 Spalten × 14 Zeilen = 42 Etiketten
- **Ränder**: 10 mm
- **Abstände**: 2 mm zwischen den Etiketten

## Druckhinweise

1. **Druckereinstellungen**:
   - Papierformat: A4
   - Skalierung: 100% / "Tatsächliche Größe" / "Ohne Skalierung"
   - Keine automatische Anpassung

2. **Etikettenbogen**:
   - Sie können spezielle Etikettenbogen verwenden
   - Oder auf normalem Papier drucken und zuschneiden
   - Etikettengröße: 50 mm × 17 mm

3. **Material-Empfehlung**:
   - Die originalen Benning-Etiketten sind PVC-Folie, stark haftend
   - Alternativ: Weiße Polyester-Etiketten oder robuste Papier-Etiketten

## Anpassungen

### Etikettenmaße ändern

Im Code in der Klasse `BenningBarcodeGenerator.__init__()`:

```python
self.label_width = 50 * mm   # Breite anpassen
self.label_height = 17 * mm  # Höhe anpassen
```

### Barcode-Darstellung ändern

In der Methode `generate_barcode_image()`:

```python
writer.set_options({
    'module_width': 0.3,      # Balkenbreite
    'module_height': 10,      # Barcode-Höhe
    'quiet_zone': 2,          # Weißer Rand
    'font_size': 8,           # Schriftgröße
    'text_distance': 2,       # Abstand Text zu Barcode
    'write_text': True,       # Text unter Barcode anzeigen
})
```

### Nummerierungsformat ändern

Im Code `code_value = f"{self.prefix}{number:04d}"` ändern:
- `:04d` = 4-stellig mit führenden Nullen (0001, 0002, ...)
- `:05d` = 5-stellig (00001, 00002, ...)
- `:03d` = 3-stellig (001, 002, ...)

## Fehlerbehebung

**Problem: "Module not found"**
```bash
pip install python-barcode pillow reportlab
```

**Problem: Etiketten passen nicht auf die Seite**
- Überprüfen Sie die Druckereinstellungen (100% Skalierung)
- Passen Sie ggf. die Ränder im Code an

**Problem: Barcodes nicht lesbar**
- Erhöhen Sie `module_width` für dickere Balken
- Drucken Sie in höherer Qualität
- Verwenden Sie einen besseren Drucker/höhere DPI

## Kompatibilität 

- **Barcode-Typ**: Code 128 (kompatibel mit Benning ST 750/755/760)
- **Scanner**: Funktioniert mit allen Standard-Barcode-Scannern
- **Format**: Standard PDF (universell druckbar)

## Lizenz und Haftung

Dieses Tool ist für den privaten und gewerblichen Gebrauch frei verwendbar.
Keine Garantie für Funktionalität oder Kompatibilität.

## Support

Bei Fragen oder Problemen können Sie:
1. Den Code anpassen (gut kommentiert)
2. Die Konfigurationswerte ändern
3. Mich um weitere Hilfe bitten

---

**Viel Erfolg mit Ihren Barcode-Etiketten! 📊**
