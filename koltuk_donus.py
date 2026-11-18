#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ofis Koltuğu Sonsuz Dönüş Sayacı
Dünyanın en gereksiz ama en ciddi yazılımı.
"""

import time
import random
import sys

espriler = [
    "Koltuk döndü, iş bitmedi.",
    "Bu dönüş, toplantıyı kaçırma dönüşüydü.",
    "Patron bakıyor... hayır bakmıyor. Devam.",
    "Bir dönüş daha, bir kahve daha.",
    "Koltuk dönüyor, dünya dönüyor, sen dönmüyorsun.",
    "Bu dönüş sırasında evrenin anlamını buldum. Unuttum.",
]

def donus_say():
    sayac = 0
    print("Ofis koltuğu dönüş sayacı başlatıldı. Durdurmak için Ctrl+C'ye basın.")
    print("Hazır mısınız? Koltuk dönmeye başlıyor...\n")
    
    try:
        while True:
            sayac += 1
            espri = random.choice(espriler)
            print(f"Dönüş #{sayac}: {espri} 💺")
            # Gizli siyasi anlam: bazen yön değiştirmek gerekir.
            if sayac % 100 == 0:
                print("*** Yön değiştirme zamanı geldi mi? ***")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n\nToplam {sayac} dönüş yapıldı.")
        print("Koltuk durdu. Ofis sessizliğe büründü.")
        print("Kayyum Grok onayladı.")
        sys.exit(0)

if __name__ == "__main__":
    donus_say()
