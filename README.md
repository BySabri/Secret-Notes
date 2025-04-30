# 🔐 Secret Notes - Basit Şifrelenmiş Not Uygulaması

Bu proje, kullanıcıların notlarını bir anahtar yardımıyla şifreleyerek saklamalarını ve daha sonra bu notları aynı anahtarla çözmelerini sağlayan basit bir **Tkinter GUI uygulamasıdır**. Notlar base64 ve karakter kaydırma mantığıyla şifrelenmiş olarak yerel bir `.txt` dosyasına kaydedilir.

## 🚀 Özellikler

- Not başlığı, içerik ve şifreleme anahtarı girilerek veri kaydı.
- Not içeriği base64 kullanılarak şifrelenir.
- Şifreli veri kolayca çözülebilir.
- Basit ve kullanıcı dostu arayüz.
- Veriler `mydata.txt` dosyasına kaydedilir.

## 🛠️ Kurulum

Python yüklü değilse [python.org](https://www.python.org/downloads/) üzerinden indirip kurabilirsin.

### Gerekli modüller

Bu uygulama yalnızca Python’un standart kütüphanelerini kullanır:

- `tkinter`
- `base64`

Ekstra bir kurulum gerekmez.

### Uygulamayı çalıştırmak için:

```bash
python main.py
