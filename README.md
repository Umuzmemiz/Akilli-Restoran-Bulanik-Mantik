# 🍽️ Akıllı Restoran Ambiyans Kontrolörü (Bulanık Mantık)

<img width="1896" height="635" alt="image" src="https://github.com/user-attachments/assets/9b47609c-a727-484d-8a2b-a162efdcd129" />

<img width="1815" height="598" alt="image" src="https://github.com/user-attachments/assets/8858a389-170d-4577-af0c-ee73016460b5" />

<img width="1823" height="752" alt="image" src="https://github.com/user-attachments/assets/8310823f-bd9c-4782-a881-b6bb1addb1d3" />




Bu proje, bir restoranın fiziksel ortam koşullarını (müşteri yoğunluğu, gürültü ve gün ışığı) anlık olarak analiz ederek, içerideki **Aydınlatma Parlaklığını** ve **Müzik Ses Seviyesini** insan mantığına en uygun şekilde otomatik ayarlayan **Bulanık Mantık (Fuzzy Logic)** tabanlı bir karar destek sistemidir. 

Geleneksel kesin sınırları olan (1/0 veya Aç/Kapat) algoritmaların aksine, bu sistem "biraz kalabalık", "hafif uğultulu" gibi insani kavramları modelleyerek yumuşak geçişler sağlar ve maksimum müşteri konforunu hedefler.

---

## 🎯 Projenin Amacı
Hizmet sektöründe müşteri memnuniyetini etkileyen en önemli faktörlerden biri mekanın ambiyansıdır. Bu proje ile;
* Ortamın doğal ışık seviyesine göre yapay aydınlatmayı kısarak **enerji tasarrufu sağlamak**,
* Rahatsız edici dış gürültüyü uygun müzik seviyesiyle **maskelemek**,
* Restoranın doluluk oranına göre en uygun atmosferi (örneğin; tenha saatlerde loş ve romantik, kalabalık saatlerde aydınlık ve canlı) **dinamik olarak sunmak** amaçlanmıştır.

---

## ⚙️ Sistem Değişkenleri ve Mimari
Sistem, karar mekanizması olarak 15 özel kuraldan oluşan bir **Mamdani Çıkarım Sistemi** ve durulaştırma (defuzzification) için **Ağırlık Merkezi (Centroid)** yöntemini kullanmaktadır.

### 📥 Girdiler (Antecedents)
* 👥 **Müşteri Yoğunluğu (%):** Tenha, Normal, Kalabalık
* 🔊 **Ortam Gürültüsü (dB):** Sessiz, Uğultulu, Gürültülü
* ☀️ **Doğal Işık Seviyesi (%):** Karanlık, Loş, Aydınlık

### 📤 Çıktılar (Consequents)
* 💡 **Aydınlatma Parlaklığı (%):** Loş, Normal, Parlak
* 🎵 **Müzik Ses Seviyesi (%):** Kısık, Orta, Yüksek

---

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python 3.x
* **Bulanık Mantık Motoru:** `scikit-fuzzy`
* **Web Arayüzü (GUI):** `streamlit`
* **Veri İşleme ve Görselleştirme:** `numpy`, `matplotlib`

---

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Gerekli kütüphaneleri sisteminize yükleyin:
```bash
pip install streamlit numpy scikit-fuzzy matplotlib
