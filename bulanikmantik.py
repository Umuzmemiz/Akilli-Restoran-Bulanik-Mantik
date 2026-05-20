import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

st.set_page_config(page_title="Akıllı Restoran Ambiyans Sistemi", layout="wide")

# --- 1. BULANIK MANTIK SİSTEMİ TANIMLAMALARI ---
# Giriş Değişkenleri (Antecedents)
musteri = ctrl.Antecedent(np.arange(0, 101, 1), 'Müşteri Yoğunluğu (%)')
gurultu = ctrl.Antecedent(np.arange(40, 101, 1), 'Ortam Gürültüsü (dB)')
isik = ctrl.Antecedent(np.arange(0, 101, 1), 'Doğal Işık (%)')

# Çıkış Değişkenleri (Consequents)
aydinlatma = ctrl.Consequent(np.arange(0, 101, 1), 'Aydınlatma Parlaklığı (%)')
muzik = ctrl.Consequent(np.arange(0, 101, 1), 'Müzik Ses Seviyesi (%)')

# Üyelik Fonksiyonları (Üçgen - trimf)
musteri['Tenha'] = fuzz.trimf(musteri.universe, [0, 0, 50])
musteri['Normal'] = fuzz.trimf(musteri.universe, [20, 50, 80])
musteri['Kalabalık'] = fuzz.trimf(musteri.universe, [50, 100, 100])

gurultu['Sessiz'] = fuzz.trimf(gurultu.universe, [40, 40, 65])
gurultu['Uğultulu'] = fuzz.trimf(gurultu.universe, [55, 70, 85])
gurultu['Gürültülü'] = fuzz.trimf(gurultu.universe, [75, 100, 100])

isik['Karanlık'] = fuzz.trimf(isik.universe, [0, 0, 40])
isik['Loş'] = fuzz.trimf(isik.universe, [20, 50, 80])
isik['Aydınlık'] = fuzz.trimf(isik.universe, [60, 100, 100])

aydinlatma['Loş'] = fuzz.trimf(aydinlatma.universe, [0, 0, 50])
aydinlatma['Normal'] = fuzz.trimf(aydinlatma.universe, [25, 50, 75])
aydinlatma['Parlak'] = fuzz.trimf(aydinlatma.universe, [50, 100, 100])

muzik['Kısık'] = fuzz.trimf(muzik.universe, [0, 0, 40])
muzik['Orta'] = fuzz.trimf(muzik.universe, [30, 50, 70])
muzik['Yüksek'] = fuzz.trimf(muzik.universe, [60, 100, 100])

# Kurallar (Örnek olarak ilk 5 kuralı ekledim, raporuna göre hepsini ekleyebilirsin)
kural1 = ctrl.Rule(musteri['Kalabalık'] & gurultu['Gürültülü'] & isik['Karanlık'], (aydinlatma['Parlak'], muzik['Yüksek']))
kural2 = ctrl.Rule(musteri['Kalabalık'] & gurultu['Gürültülü'] & isik['Aydınlık'], (aydinlatma['Loş'], muzik['Yüksek']))
kural3 = ctrl.Rule(musteri['Kalabalık'] & gurultu['Uğultulu'] & isik['Loş'], (aydinlatma['Normal'], muzik['Orta']))
kural4 = ctrl.Rule(musteri['Tenha'] & gurultu['Sessiz'] & isik['Karanlık'], (aydinlatma['Loş'], muzik['Kısık']))
kural5 = ctrl.Rule(musteri['Normal'] & gurultu['Sessiz'] & isik['Aydınlık'], (aydinlatma['Loş'], muzik['Kısık']))
# NOT: Diğer 10 kuralı aynı bu formatta alt alta eklemelisin.

# Kontrol Sistemi
ambiyans_ctrl = ctrl.ControlSystem([kural1, kural2, kural3, kural4, kural5]) # Eklediğin kuralları buraya yaz
ambiyans_sim = ctrl.ControlSystemSimulation(ambiyans_ctrl)

# --- 2. STREAMLIT ARAYÜZÜ ---
st.title("🍽️ Akıllı Restoran Ambiyans Kontrolörü (Bulanık Mantık)")
st.markdown("Bu sistem ortamdaki **Müşteri Yoğunluğu**, **Gürültü** ve **Işık** seviyelerini alarak restoranın **Müzik** ve **Aydınlatma** seviyelerini bulanık mantıkla otomatik ayarlar.")

col1, col2 = st.columns(2)

with col1:
    st.header("Giriş Değişkenleri")
    val_musteri = st.slider("Müşteri Yoğunluğu (%)", 0, 100, 50)
    val_gurultu = st.slider("Ortam Gürültüsü (dB)", 40, 100, 60)
    val_isik = st.slider("Doğal Işık Seviyesi (%)", 0, 100, 50)
    
    hesapla_btn = st.button("Sistemi Çalıştır ve Hesapla", type="primary")

with col2:
    st.header("Sistem Çıktıları")
    if hesapla_btn:
        # Değerleri sisteme ver
        ambiyans_sim.input['Müşteri Yoğunluğu (%)'] = val_musteri
        ambiyans_sim.input['Ortam Gürültüsü (dB)'] = val_gurultu
        ambiyans_sim.input['Doğal Işık (%)'] = val_isik
        
        # Durulaştırma (Defuzzification) hesaplamasını yap (Centroid metodu varsayılandır)
        ambiyans_sim.compute()
        
        # Sonuçları göster
        st.metric(label="💡 Önerilen Aydınlatma Parlaklığı", value=f"% {ambiyans_sim.output['Aydınlatma Parlaklığı (%)']:.2f}")
        st.metric(label="🎵 Önerilen Müzik Ses Seviyesi", value=f"% {ambiyans_sim.output['Müzik Ses Seviyesi (%)']:.2f}")

st.divider()

# --- 3. GRAFİKSEL GÖSTERİMLER (Hocanın İstediği Kısım) ---
if hesapla_btn:
    st.subheader("Bulanıklaştırma ve Durulaştırma Grafikleri")
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        st.markdown("**Aydınlatma Durulaştırma Alanı**")
        fig_aydinlatma, ax_aydinlatma = plt.subplots(figsize=(6, 3))
        aydinlatma.view(sim=ambiyans_sim, ax=ax_aydinlatma)
        st.pyplot(fig_aydinlatma)
        
    with g_col2:
        st.markdown("**Müzik Durulaştırma Alanı**")
        fig_muzik, ax_muzik = plt.subplots(figsize=(6, 3))
        muzik.view(sim=ambiyans_sim, ax=ax_muzik)
        st.pyplot(fig_muzik)
        
    st.success("Hesaplama Centroid (Ağırlık Merkezi) metodu kullanılarak başarıyla tamamlandı.")