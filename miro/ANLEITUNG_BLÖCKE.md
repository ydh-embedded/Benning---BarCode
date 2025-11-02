# 📦 ANLEITUNG: Etiketten in Blöcken erstellen

## 🎯 Super einfach mit dem Block-Generator!

Sie müssen nur **EINE ZAHL** ändern, der Rest passiert automatisch!

---

## 🚀 SO GEHT'S:

### Schritt 1: Script öffnen

Öffnen Sie: `generate_blocks.py`

### Schritt 2: Block-Nummer ändern

Suchen Sie diese Zeilen (ca. Zeile 92-94):

```python
# Welchen Block möchten Sie erstellen?
BLOCK_NUMMER = 1          # ← NUR DIESE ZAHL ÄNDERN!
BLOCK_GROESSE = 100       # Meist 100 lassen
PREFIX = ""               # Optional
```

### Schritt 3: Ausführen

```bash
python generate_blocks.py
```

**FERTIG!** ✅

---

## 📋 BEISPIELE:

### Block 1: Etiketten 0001-0100
```python
BLOCK_NUMMER = 1
```
→ Erstellt: `rollendruck_0001-0100.pdf`

---

### Block 2: Etiketten 0101-0200
```python
BLOCK_NUMMER = 2
```
→ Erstellt: `rollendruck_0101-0200.pdf`

---

### Block 3: Etiketten 0201-0300
```python
BLOCK_NUMMER = 3
```
→ Erstellt: `rollendruck_0201-0300.pdf`

---

### Block 4: Etiketten 0301-0400
```python
BLOCK_NUMMER = 4
```
→ Erstellt: `rollendruck_0301-0400.pdf`

---

### Block 5: Etiketten 0401-0500
```python
BLOCK_NUMMER = 5
```
→ Erstellt: `rollendruck_0401-0500.pdf`

---

## 🏷️ MIT PRÄFIX (z.B. "Miro - ")

### Block 1: Miro - 0001 bis Miro - 0100
```python
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
PREFIX = "Miro - "
```
→ Erstellt: `rollendruck_Miro_0001-0100.pdf`

---

### Block 2: Miro - 0101 bis Miro - 0200
```python
BLOCK_NUMMER = 2
BLOCK_GROESSE = 100
PREFIX = "Miro - "
```
→ Erstellt: `rollendruck_Miro_0101-0200.pdf`

---

## 🔧 ANDERE BLOCK-GRÖSSEN

### Blöcke von 50 Etiketten
```python
BLOCK_NUMMER = 1          # Block 1, 2, 3, ...
BLOCK_GROESSE = 50        # ← Auf 50 ändern
```

**Ergebnisse:**
- Block 1: 0001-0050
- Block 2: 0051-0100
- Block 3: 0101-0150
- etc.

---

### Blöcke von 250 Etiketten
```python
BLOCK_NUMMER = 1          # Block 1, 2, 3, ...
BLOCK_GROESSE = 250       # ← Auf 250 ändern
```

**Ergebnisse:**
- Block 1: 0001-0250
- Block 2: 0251-0500
- Block 3: 0501-0750
- etc.

---

## 💡 PRAKTISCHE SZENARIEN

### Szenario 1: "Ich bestelle erstmal 100 Etiketten"
```python
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
PREFIX = ""
```
→ 0001-0100 (ca. 20-50 EUR)

**Später mehr benötigt?**
```python
BLOCK_NUMMER = 2
```
→ 0101-0200 (nächste 100)

---

### Szenario 2: "Ich brauche 200, aber in 2 Bestellungen"
```python
# Bestellung 1:
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
```
→ 0001-0100

```python
# Bestellung 2:
BLOCK_NUMMER = 2
BLOCK_GROESSE = 100
```
→ 0101-0200

---

### Szenario 3: "Kunde Miro braucht 500, aufgeteilt in 5×100"

```python
# Bestellung 1: BLOCK_NUMMER = 1, PREFIX = "Miro - "
→ Miro - 0001 bis Miro - 0100

# Bestellung 2: BLOCK_NUMMER = 2, PREFIX = "Miro - "
→ Miro - 0101 bis Miro - 0200

# Bestellung 3: BLOCK_NUMMER = 3, PREFIX = "Miro - "
→ Miro - 0201 bis Miro - 0300

# Bestellung 4: BLOCK_NUMMER = 4, PREFIX = "Miro - "
→ Miro - 0301 bis Miro - 0400

# Bestellung 5: BLOCK_NUMMER = 5, PREFIX = "Miro - "
→ Miro - 0401 bis Miro - 0500
```

**Vorteil:** Kleinere Dateien, flexibler bestellen!

---

## 📊 ÜBERSICHT: Was wird automatisch berechnet?

| Block | Block-Größe 100 | Block-Größe 50 | Block-Größe 250 |
|-------|----------------|----------------|-----------------|
| 1 | 0001-0100 | 0001-0050 | 0001-0250 |
| 2 | 0101-0200 | 0051-0100 | 0251-0500 |
| 3 | 0201-0300 | 0101-0150 | 0501-0750 |
| 4 | 0301-0400 | 0151-0200 | 0751-1000 |
| 5 | 0401-0500 | 0201-0250 | 1001-1250 |

**Sie ändern nur BLOCK_NUMMER - der Rest ist automatisch!** ✅

---

## ✅ ZUSAMMENFASSUNG

### Was Sie ändern:
```python
BLOCK_NUMMER = X      # ← Nur diese Zahl!
```

### Was automatisch passiert:
✅ Start-Nummer wird berechnet  
✅ End-Nummer wird berechnet  
✅ Dateiname wird erstellt  
✅ PDF wird generiert  

### Ergebnis:
✅ Perfekte Rollendruck-PDF  
✅ Richtige Nummerierung  
✅ Korrekte Dateigröße  

---

## 💰 KOSTEN-KALKULATION

### Pro Block (100 Etiketten):
- Papier: ca. 15-30 EUR
- Polyester: ca. 25-50 EUR
- PVC: ca. 30-60 EUR

### 5 Blöcke (500 Etiketten):
- PVC: ca. 150-300 EUR gesamt
- **ODER** als eine Bestellung: 60-120 EUR (günstiger!)

**Tipp:** Große Mengen sind pro Etikett günstiger!

---

## ❓ HÄUFIGE FRAGEN

**Q: Warum Blöcke statt alles auf einmal?**
A: 
- Flexibler (erst 100 testen, dann mehr)
- Kleinere Dateien (einfacher zu versenden)
- Mehrere Bestellungen möglich
- Bei Fehler nur 1 Block betroffen

**Q: Kann ich Lücken lassen?**
A: Ja! Z.B. Block 1 und Block 3 bestellen, Block 2 auslassen.

**Q: Was wenn ich Block 2 nochmal brauche?**
A: Einfach BLOCK_NUMMER = 2 setzen und erneut generieren.

**Q: Welche Block-Größe ist am besten?**
A: 100 ist Standard. 50 für kleine Tests, 250 für große Bestellungen.

---

## 🎯 QUICK REFERENCE

```python
# Standard (ohne Präfix)
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
PREFIX = ""

# Mit Präfix
BLOCK_NUMMER = 1
BLOCK_GROESSE = 100
PREFIX = "Miro - "

# Kleinere Blöcke
BLOCK_NUMMER = 1
BLOCK_GROESSE = 50
PREFIX = ""

# Größere Blöcke
BLOCK_NUMMER = 1
BLOCK_GROESSE = 250
PREFIX = ""
```

---

**So einfach war Barcode-Generierung noch nie! 🎉**

*Stand: Oktober 2025*
