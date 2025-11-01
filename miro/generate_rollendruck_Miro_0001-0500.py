#!/usr/bin/env python3
"""
Benning-Style Barcode-Etiketten für DRUCKDIENSTLEISTER (Rollendruck)
KUNDE: Miro
Gerätenummern: Miro - 0001 bis Miro - 0500
"""

import barcode
from barcode.writer import ImageWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from PIL import Image
import io
import os

class PrintServiceBarcodeGenerator:
    """Generator für Druckdienstleister-geeignete Barcode-Etiketten"""
    
    def __init__(self, start_number=1, end_number=100, prefix=""):
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
            'module_width': 0.22,     # Etwas schmaler wegen längerem Text
            'module_height': 10,
            'quiet_zone': 2,
            'font_size': 6,           # Etwas kleiner wegen längerem Text
            'text_distance': 2,
            'write_text': True,
        })
        
        barcode_instance = code128(code_value, writer=writer)
        buffer = io.BytesIO()
        barcode_instance.write(buffer)
        buffer.seek(0)
        img = Image.open(buffer)
        
        return img, code_value
    
    def generate_continuous_roll_pdf(self, output_filename="rollendruck_etiketten.pdf"):
        """
        Generiert EIN PDF mit allen Etiketten UNTEREINANDER
        Ideal für Rollendruck ohne Seitenumbrüche
        """
        print("=" * 70)
        print("Generiere ROLLENDRUCK-PDF (Endlosformat)")
        print("=" * 70)
        print()
        
        total = self.end_number - self.start_number + 1
        
        # Gesamthöhe = Anzahl Etiketten × Höhe pro Etikett
        total_height = total * self.label_height
        
        print(f"Format: {self.label_width/mm:.1f}mm × {total_height/mm:.1f}mm")
        print(f"Anzahl Etiketten: {total}")
        if self.prefix:
            print(f"Präfix: '{self.prefix}'")
        print()
        
        # PDF mit Endlos-Höhe erstellen
        c = canvas.Canvas(output_filename, pagesize=(self.label_width, total_height))
        
        for idx, number in enumerate(range(self.start_number, self.end_number + 1)):
            img, code_value = self.generate_barcode_image(number)
            
            # Position (von unten nach oben)
            y_position = idx * self.label_height
            
            # Temporäre Bilddatei
            temp_img = f"/tmp/barcode_{number}.png"
            img.save(temp_img, format='PNG')
            
            # Barcode einfügen
            c.drawImage(temp_img, 0, y_position,
                       width=self.label_width,
                       height=self.label_height,
                       preserveAspectRatio=True)
            
            os.remove(temp_img)
            
            if (idx + 1) % 100 == 0 or (idx + 1) == total:
                print(f"  Fortschritt: {idx + 1}/{total} Etiketten")
        
        c.save()
        
        file_size = os.path.getsize(output_filename) / (1024*1024)
        print()
        print("=" * 70)
        print(f"✓ PDF erfolgreich erstellt: {output_filename}")
        print(f"  Dateigröße: {file_size:.2f} MB")
        print(f"  Format: {self.label_width/mm:.1f}mm breit × {total_height/mm:.1f}mm hoch")
        print(f"  Das sind {total_height/mm/1000:.2f} Meter Etikettenrolle")
        print("=" * 70)


def main():
    print("=" * 70)
    print("BENNING BARCODE-ETIKETTEN FÜR DRUCKDIENSTLEISTER")
    print("KUNDE: Miro")
    print("Format: 50mm × 17mm | Code 128 | Rollendruck")
    print("=" * 70)
    print()
    
    # ═══════════════════════════════════════════════════════════════════
    # KONFIGURATION - Kunde: Miro
    # ═══════════════════════════════════════════════════════════════════
    
    START_NUMMER = 1          # Erste Gerätenummer
    END_NUMMER = 500          # Letzte Gerätenummer (500 Etiketten)
    PREFIX = "Miro - "        # Präfix vor Nummer
    OUTPUT_FILE = "rollendruck_Miro_0001-0500.pdf"
    
    # ═══════════════════════════════════════════════════════════════════
    
    print("Konfiguration:")
    print(f"  Kunde: Miro")
    print(f"  Nummernbereich: {PREFIX}{START_NUMMER:04d} - {PREFIX}{END_NUMMER:04d}")
    print(f"  Anzahl Etiketten: {END_NUMMER - START_NUMMER + 1}")
    print(f"  Präfix: '{PREFIX}'")
    print(f"  Etikettenformat: 50mm × 17mm")
    print(f"  Ausgabedatei: {OUTPUT_FILE}")
    print()
    
    generator = PrintServiceBarcodeGenerator(
        start_number=START_NUMMER,
        end_number=END_NUMMER,
        prefix=PREFIX
    )
    
    import time
    start_time = time.time()
    
    print("Generiere ROLLENDRUCK-PDF (für Druckdienstleister)...")
    print()
    
    generator.generate_continuous_roll_pdf(OUTPUT_FILE)
    
    elapsed = time.time() - start_time
    print()
    print(f"⏱️  Generierungszeit: {elapsed:.1f} Sekunden")
    print()
    print("=" * 70)
    print("INFORMATIONEN FÜR DRUCKDIENSTLEISTER:")
    print("=" * 70)
    print("  • Kunde: Miro")
    print("  • Format pro Etikett: 50mm × 17mm")
    print("  • Barcode-Typ: Code 128")
    print("  • Inhalt: 'Miro - 0001' bis 'Miro - 0500'")
    print("  • Menge: 500 Stück")
    print("  • Material-Empfehlung: PVC-Folie, stark haftend")
    print("  • Farbe: Schwarz auf Weiß")
    print("  • Lieferform: Auf Rolle")
    print()
    print("📧 Diese Datei können Sie direkt an den Druckdienstleister senden:")
    print(f"   → {OUTPUT_FILE}")
    print()
    print("💰 Geschätzte Kosten (Deutschland, ca. 2025):")
    print("   • 500 Etiketten auf PVC-Folie: ca. 50-120 EUR")
    print("   • Je nach Anbieter und Qualität")
    print()
    print("🔧 Anpassungen im Script möglich:")
    print("   • Andere Nummernbereiche: START_NUMMER / END_NUMMER ändern")
    print("   • Anderer Präfix: PREFIX = 'Andere Firma - '")
    print("   • Andere Größe: label_width / label_height anpassen")
    print("=" * 70)
    print()
    print("📋 Beispiel-Codes:")
    print(f"   Erster: {PREFIX}{START_NUMMER:04d}")
    print(f"   Letzter: {PREFIX}{END_NUMMER:04d}")
    print("=" * 70)


if __name__ == "__main__":
    main()
