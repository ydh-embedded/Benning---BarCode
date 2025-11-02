#!/usr/bin/env python3
"""
Benning-Style Barcode-Etiketten - BLOCK-GENERATOR
Erstellt Etiketten in Blöcken von 100 (oder anderen Größen)

Beispiele:
- Block 1: 0001-0100
- Block 2: 0101-0200
- Block 3: 0201-0300
etc.
"""

import barcode
from barcode.writer import ImageWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from PIL import Image
import io
import os

class BarcodeBlockGenerator:
    """Generator für Barcode-Etiketten in Blöcken"""
    
    def __init__(self, start_number, end_number, prefix=""):
        self.start_number = start_number
        self.end_number = end_number
        self.prefix = prefix
        
        # Etikettenmaße (Benning Standard)
        self.label_width = 50 * mm
        self.label_height = 17 * mm
        
    def generate_barcode_image(self, number):
        """Generiert Barcode-Bild"""
        code_value = f"{self.prefix}{number:04d}"
        
        code128 = barcode.get_barcode_class('code128')
        writer = ImageWriter()
        writer.set_options({
            'module_width': 0.25,
            'module_height': 10,
            'quiet_zone': 2,
            'font_size': 7,
            'text_distance': 2,
            'write_text': True,
        })
        
        barcode_instance = code128(code_value, writer=writer)
        buffer = io.BytesIO()
        barcode_instance.write(buffer)
        buffer.seek(0)
        img = Image.open(buffer)
        
        return img, code_value
    
    def generate_pdf(self, output_filename):
        """Generiert Rollendruck-PDF"""
        total = self.end_number - self.start_number + 1
        total_height = total * self.label_height
        
        c = canvas.Canvas(output_filename, pagesize=(self.label_width, total_height))
        
        for idx, number in enumerate(range(self.start_number, self.end_number + 1)):
            img, code_value = self.generate_barcode_image(number)
            y_position = idx * self.label_height
            
            temp_img = f"/tmp/barcode_{number}.png"
            img.save(temp_img, format='PNG')
            
            c.drawImage(temp_img, 0, y_position,
                       width=self.label_width,
                       height=self.label_height,
                       preserveAspectRatio=True)
            
            os.remove(temp_img)
        
        c.save()
        
        file_size = os.path.getsize(output_filename) / (1024*1024)
        return total, file_size


def main():
    print("=" * 70)
    print("BENNING BARCODE-ETIKETTEN - BLOCK-GENERATOR")
    print("Erstellt Etiketten in praktischen Blöcken")
    print("=" * 70)
    print()
    
    # ═══════════════════════════════════════════════════════════════════
    # EINFACHE KONFIGURATION
    # ═══════════════════════════════════════════════════════════════════
    
    # Welchen Block möchten Sie erstellen?
    BLOCK_NUMMER = 1          # Block 1, 2, 3, 4, etc.
    BLOCK_GROESSE = 100       # Wie viele Etiketten pro Block? (meist 100)
    PREFIX = "Miro - "               # Optional: z.B. "Miro - "
    
    # ═══════════════════════════════════════════════════════════════════
    
    # Automatische Berechnung
    START_NUMMER = ((BLOCK_NUMMER - 1) * BLOCK_GROESSE) + 1
    END_NUMMER = BLOCK_NUMMER * BLOCK_GROESSE
    
    # Dateiname automatisch generieren
    if PREFIX:
        # Mit Präfix: z.B. "rollendruck_Miro_0001-0100.pdf"
        prefix_clean = PREFIX.strip().replace(" ", "").replace("-", "")
        OUTPUT_FILE = f"rollendruck_{prefix_clean}_{START_NUMMER:04d}-{END_NUMMER:04d}.pdf"
    else:
        # Ohne Präfix: z.B. "rollendruck_0001-0100.pdf"
        OUTPUT_FILE = f"rollendruck_{START_NUMMER:04d}-{END_NUMMER:04d}.pdf"
    
    print("Konfiguration:")
    print(f"  Block-Nummer: {BLOCK_NUMMER}")
    print(f"  Block-Größe: {BLOCK_GROESSE} Etiketten")
    print(f"  Nummernbereich: {START_NUMMER:04d} - {END_NUMMER:04d}")
    if PREFIX:
        print(f"  Präfix: '{PREFIX}'")
        print(f"  Beispiel: {PREFIX}{START_NUMMER:04d}")
    else:
        print(f"  Kein Präfix")
        print(f"  Beispiel: {START_NUMMER:04d}")
    print(f"  Ausgabedatei: {OUTPUT_FILE}")
    print()
    
    print("Generiere PDF...")
    
    import time
    start_time = time.time()
    
    generator = BarcodeBlockGenerator(
        start_number=START_NUMMER,
        end_number=END_NUMMER,
        prefix=PREFIX
    )
    
    total, file_size = generator.generate_pdf(OUTPUT_FILE)
    
    elapsed = time.time() - start_time
    
    print()
    print("=" * 70)
    print("✓ PDF ERFOLGREICH ERSTELLT!")
    print("=" * 70)
    print(f"  Datei: {OUTPUT_FILE}")
    print(f"  Etiketten: {total} Stück")
    print(f"  Von: {PREFIX}{START_NUMMER:04d}")
    print(f"  Bis: {PREFIX}{END_NUMMER:04d}")
    print(f"  Größe: {file_size:.2f} MB")
    print(f"  Rollenlänge: {total * 17 / 1000:.2f} Meter")
    print(f"  Generierungszeit: {elapsed:.1f} Sekunden")
    print("=" * 70)
    print()
    
    print("💡 WEITERE BLÖCKE ERSTELLEN:")
    print("-" * 70)
    print(f"  Block {BLOCK_NUMMER + 1}: BLOCK_NUMMER = {BLOCK_NUMMER + 1}")
    print(f"  → Nummern {END_NUMMER + 1:04d} bis {END_NUMMER + BLOCK_GROESSE:04d}")
    print()
    print(f"  Block {BLOCK_NUMMER + 2}: BLOCK_NUMMER = {BLOCK_NUMMER + 2}")
    print(f"  → Nummern {END_NUMMER + BLOCK_GROESSE + 1:04d} bis {END_NUMMER + 2*BLOCK_GROESSE:04d}")
    print()
    print("  Einfach BLOCK_NUMMER ändern und Script erneut ausführen!")
    print("=" * 70)


if __name__ == "__main__":
    main()
