def son_yüz_basamak_analizi(dosya_yolu):
    print("\n--- NEXUSFLOW: 50M BASAMAKLI DEVLERİN MÜHÜRLERİ ---\n")
    
    with open(dosya_yolu, "r") as f:
        for i, satir in enumerate(f, 1):
            # Satır sonundaki boşlukları ve \n karakterini temizle
            temiz_satir = satir.strip()
            
            if temiz_satir:
                # Sayının son 100 karakterini al
                son_yüz = temiz_satir[-100:]
                print(f"Sayı #{i} (Son 100 Basamak):")
                print(f"...{son_yüz}\n")
            
    print("--- ANALİZ TAMAMLANDI ---")
    input("kapat")
# Dosya adını buraya yaz
son_yüz_basamak_analizi("nexus_giant_primes_50000000dig.txt")
