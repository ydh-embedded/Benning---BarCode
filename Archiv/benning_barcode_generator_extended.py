#!/usr/bin/env python3
"""
Benning-Style Barcode-Etiketten Generator - ERWEITERTE VERSION
Erstellt Code 128 Barcodes mit fortlaufender Nummerierung und Text-Präfix
Unterstützt: Buchstaben, Zahlen, Sonderzeichen
"""

import barcode
from barcode.writer import ImageWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from PIL import Image
import io
import os

class BenningBarcodeGenerator:
    """Generator für Benning-ähnliche Barcode-Etiketten"""
    
    def __init__(self, start_number=1, end_number=100, prefix=""):
        """
        Initialisiert den Generator
        
        Args:
            start_number: Startnummer für die Nummerierung
            end_number: Endnummer für die Nummerierung
            prefix: Text-Präfix vor der Nummer (z.B. "Napoli - ", "GER-", "ABC_")
                   Kann Buchstaben, Zahlen, Leerzeichen und Sonderzeichen enthalten
        """
        self.start_number = start_number
        self.end_number = end_number
        self.prefix = prefix
        
        # Etikettenmaße (Benning Standard)
        self.label_width = 50 * mm
        self.label_height = 17 * mm
        
        # A4-Seite für Layout
        self.page_width, self.page_height = A4
        
        # Abstände und Ränder
        self.margin_left = 10 * mm
        self.margin_top = 10 * mm
        self.gap_x = 2 * mm
        self.gap_y = 2 * mm
        
    def generate_barcode_image(self, number):
        """
        Generiert ein Barcode-Bild für eine Nummer
        
        Args:
            number: Die zu kodierende Nummer
            
        Returns:
            PIL Image des Barcodes und der kodierte Text
        """
        # Text für Barcode zusammensetzen
        code_value = f"{self.prefix}{number:04d}"
        
        # Code 128 Barcode erstellen (unterstützt Buchstaben, Zahlen, Sonderzeichen)
        code128 = barcode.get_barcode_class('code128')
        
        # ImageWriter mit angepassten Optionen
        writer = ImageWriter()
        writer.set_options({
            'module_width': 0.25,     # Etwas schmaler für längere Texte
            'module_height': 10,
            'quiet_zone': 2,
            'font_size': 7,           # Etwas kleiner für längere Texte
            'text_distance': 2,
            'write_text': True,
        })
        
        # Barcode erstellen
        barcode_instance = code128(code_value, writer=writer)
        
        # In Bytes-Buffer speichern
        buffer = io.BytesIO()
        barcode_instance.write(buffer)
        buffer.seek(0)
        
        # Als PIL Image öffnen
        img = Image.open(buffer)
        
        return img, code_value
    
    def calculate_layout(self):
        """
        Berechnet, wie viele Etiketten auf eine A4-Seite passen
        
        Returns:
            (cols, rows): Anzahl der Spalten und Zeilen
        """
        available_width = self.page_width - (2 * self.margin_left)
        available_height = self.page_height - (2 * self.margin_top)
        
        cols = int(available_width / (self.label_width + self.gap_x))
        rows = int(available_height / (self.label_height + self.gap_y))
        
        return cols, rows
    
    def generate_pdf(self, output_filename="benning_barcodes.pdf"):
        """
        Generiert eine PDF-Datei mit allen Barcode-Etiketten
        
        Args:
            output_filename: Name der Ausgabedatei
        """
        c = canvas.Canvas(output_filename, pagesize=A4)
        
        cols, rows = self.calculate_layout()
        labels_per_page = cols * rows
        
        print(f"Layout: {cols} Spalten x {rows} Zeilen = {labels_per_page} Etiketten pro Seite")
        print(f"Generiere Etiketten von {self.start_number} bis {self.end_number}...")
        if self.prefix:
            print(f"Präfix: '{self.prefix}'")
        
        label_count = 0
        total_labels = self.end_number - self.start_number + 1
        
        for number in range(self.start_number, self.end_number + 1):
            # Position auf der Seite berechnen
            position_on_page = label_count % labels_per_page
            col = position_on_page % cols
            row = position_on_page // cols
            
            # Neue Seite beginnen, falls nötig
            if label_count > 0 and position_on_page == 0:
                c.showPage()
                print(f"  Neue Seite... ({label_count}/{total_labels} Etiketten)")
            
            # Barcode generieren
            img, code_value = self.generate_barcode_image(number)
            
            # Position berechnen (von oben links)
            x = self.margin_left + col * (self.label_width + self.gap_x)
            y = self.page_height - self.margin_top - (row + 1) * (self.label_height + self.gap_y)
            
            # Temporäre Bilddatei erstellen
            temp_img = f"/tmp/barcode_{number}.png"
            img.save(temp_img, format='PNG')
            
            # Barcode auf PDF zeichnen
            c.drawImage(temp_img, x, y, 
                       width=self.label_width, 
                       height=self.label_height,
                       preserveAspectRatio=True)
            
            # Temporäre Datei löschen
            os.remove(temp_img)
            
            label_count += 1
            
            if label_count % 10 == 0:
                print(f"  Fortschritt: {label_count}/{total_labels} Etiketten")
        
        # PDF speichern
        c.save()
        print(f"\n✓ PDF erfolgreich erstellt: {output_filename}")
        print(f"  Insgesamt {label_count} Etiketten auf {(label_count - 1) // labels_per_page + 1} Seite(n)")
        
        # Beispiel-Codes anzeigen
        if total_labels > 0:
            first_code = f"{self.prefix}{self.start_number:04d}"
            last_code = f"{self.prefix}{self.end_number:04d}"
            print(f"  Erster Code: {first_code}")
            print(f"  Letzter Code: {last_code}")


def main():
    """Hauptfunktion mit verschiedenen Beispielkonfigurationen"""
    
    print("=" * 70)
    print("Benning-Style Barcode-Etiketten Generator - ERWEITERTE VERSION")
    print("=" * 70)
    print()
    
    # ═══════════════════════════════════════════════════════════════════
    # KONFIGURATION - Hier können Sie Ihre Werte eintragen:
    # ═══════════════════════════════════════════════════════════════════
    
    START_NUMMER = 1          # Erste Nummer
    END_NUMMER = 50           # Letzte Nummer
    PREFIX = "Napoli - "      # Text-Präfix (mit Buchstaben, Zahlen, Sonderzeichen)
    OUTPUT_FILE = "benning_barcodes_napoli.pdf"
    
    # ═══════════════════════════════════════════════════════════════════
    
    print("Aktuelle Konfiguration:")
    print(f"  Start: {START_NUMMER}")
    print(f"  Ende: {END_NUMMER}")
    print(f"  Präfix: '{PREFIX}'")
    print(f"  Ausgabedatei: {OUTPUT_FILE}")
    print()
    
    # Generator erstellen und PDF generieren
    generator = BenningBarcodeGenerator(
        start_number=START_NUMMER,
        end_number=END_NUMMER,
        prefix=PREFIX
    )
    
    generator.generate_pdf(OUTPUT_FILE)
    
    print()
    print("=" * 70)
    print("HINWEISE:")
    print("=" * 70)
    print("  • Code 128 unterstützt: Buchstaben (A-Z, a-z), Zahlen (0-9)")
    print("  • Und Sonderzeichen wie: - _ . , : ; / \\ ( ) [ ] + * # @ !")
    print("  • Die Etiketten sind im Format 50mm x 17mm (Benning-Standard)")
    print("  • Drucken Sie mit 100% Skalierung (keine Anpassung)")
    print()
    
    print("=" * 70)
    print("WEITERE BEISPIELE FÜR PRÄFIXE:")
    print("=" * 70)
    print("  1. Standort-Kennzeichnung:")
    print("     PREFIX = 'Berlin - '       → Berlin - 0001, Berlin - 0002, ...")
    print("     PREFIX = 'Wiesbaden_'      → Wiesbaden_0001, Wiesbaden_0002, ...")
    print()
    print("  2. Geräte-Typen:")
    print("     PREFIX = 'Drucker-'        → Drucker-0001, Drucker-0002, ...")
    print("     PREFIX = 'PC-'             → PC-0001, PC-0002, ...")
    print("     PREFIX = 'Monitor-'        → Monitor-0001, Monitor-0002, ...")
    print()
    print("  3. Abteilungen:")
    print("     PREFIX = 'IT/'             → IT/0001, IT/0002, ...")
    print("     PREFIX = 'HR-'             → HR-0001, HR-0002, ...")
    print("     PREFIX = 'PROD_'           → PROD_0001, PROD_0002, ...")
    print()
    print("  4. Projekt-Codes:")
    print("     PREFIX = 'Projekt-Alpha-'  → Projekt-Alpha-0001, ...")
    print("     PREFIX = 'XYZ.2024.'       → XYZ.2024.0001, XYZ.2024.0002, ...")
    print()
    print("  5. Ohne Präfix (nur Nummern):")
    print("     PREFIX = ''                → 0001, 0002, 0003, ...")
    print()


if __name__ == "__main__":
    main()
