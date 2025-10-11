# OpenWeatherMap API Tapşırığı

## Tapşırıq Ümumi Baxışı

Bu tapşırıqda siz **OpenWeatherMap API**-dən istifadə edərək müəyyən bir şəhər üçün hava məlumatlarını əldə edən bir Python proqramı yaradacaqsınız. Proqram aşağıdakıları etməlidir:

1. Şəhərin adını giriş kimi qəbul etməlidir.  
2. OpenWeatherMap API-ə sorğu göndərərək hava məlumatlarını almalıdır.  
3. API cavabından müəyyən edilmiş məlumat sahələrini çıxarmalıdır.  
4. Məlumatları göstərilən formatda fayla yazmalıdır.  

---

## Tələblər

- **OpenWeatherMap API**-dən istifadə edin.  
- Python-un daxili modullarından və ya əlavə kitabxanalardan (məsələn, `requests`) istifadə edə bilərsiniz.  
- Məlumatları verilmiş fayl strukturuna uyğun formatlaşdırın.  
- Proqramın səhvləri düzgün idarə etdiyinə əmin olun (məsələn, səhv şəhər adları).  

---

## API Açarı və Sənədlər

1. Pulsuz API açarı əldə etmək üçün [OpenWeatherMap](https://openweathermap.org/) veb saytına qeydiyyatdan keçin.  
2. API sorğusunun strukturu haqqında ətraflı məlumat üçün [OpenWeatherMap API sənədləri](https://openweathermap.org/current)-ə baxın.  

---

## Çıxarılacaq Məlumat Sahələri

API cavabından aşağıdakı sahələri çıxarmalısınız:
- **Şəhər adı**: `name`  
- **Temperatur (Selsi ilə)**: `main.temp` sahəsini Kelvin-dən Selsi-ə çevirin (`temp_celsius = temp_kelvin - 273.15`).  
- **Hava təsviri**: `weather[0].description`  
- **Rütubət**: `main.humidity`  
- **Küləyin sürəti (m/s)**: `wind.speed`  

---

## Fayl Formatı

Məlumatları aşağıdakı formatda `weather_data.txt` adlı fayla yazın:

Nümunə Çıxış:
```
Şəhər: London
Ölkə: GB
Temperatur: 12.34 °C
Hava: açıq səma
Rütubət: 75 %
Küləyin sürəti: 3.1 m/s
```

---

## Səhv İdarəetməsi

Proqramınız aşağıdakı vəziyyətləri idarə etməlidir:
1. Şəhər adı səhv və ya tapılmayan zaman belə bir xəta mesajı göstərin:
   ```
   Şəhər tapılmadı. Zəhmət olmasa, adı yoxlayıb yenidən cəhd edin.
   ```

---

## Nümunə API Cavabı

Burada "London" şəhəri üçün OpenWeatherMap API-dən alınan nümunə cavab təqdim olunur:

```json
{
  "coord": { "lon": -0.13, "lat": 51.51 },
  "weather": [
    { "id": 800, "main": "Clear", "description": "clear sky", "icon": "01d" }
  ],
  "base": "stations",
  "main": {
    "temp": 289.92,
    "feels_like": 287.39,
    "temp_min": 288.71,
    "temp_max": 290.93,
    "pressure": 1013,
    "humidity": 71
  },
  "visibility": 10000,
  "wind": { "speed": 3.1, "deg": 240 },
  "clouds": { "all": 0 },
  "dt": 1605182400,
  "sys": {
    "type": 1,
    "id": 1414,
    "country": "GB",
    "sunrise": 1605162375,
    "sunset": 1605194395
  },
  "timezone": 0,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
```

---

## Təqdimat

1. `weather_fetcher.py` adlı bir Python skripti yaradın və tapşırığı orada tamamlayın.  
2. Müxtəlif şəhər adlarını sınaqdan keçirin.  
3. Aşağıdakı faylları repositoriyaya əlavə edin:
   - `weather_fetcher.py`  
   - `weather_data.txt` (ən azı 3 şəhər haqqında məlumatın daxil olduğu nümunə fayl)  
   - Bu `README.md` faylı  

---

## Əlavə Qeydlər

- Yaxşı kodlaşdırma təcrübələrinə riayət edin, məsələn, şərhlər və mənalı dəyişən adları istifadə edin.  
- Kodunuzu modulyar şəkildə yazın (mümkün olduqda funksiyalardan istifadə edin).  
- Proqramınızı müxtəlif mümkün hallar üçün yoxlayın.  

Uğurlar! 🚀  

