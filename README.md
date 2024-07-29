# Submission 1: Heart Attack Prediction
Nama: Nabila Kumala Gantari

Username dicoding: nkumala16

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Heart Attack Analysis & Prediction Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) |
| Masalah | Serangan jantung merupakan salah satu penyebab utama kematian global, dan identifikasi awal terhadap risiko serangan jantung dapat menyelamatkan banyak nyawa. Kemajuan teknologi dan analisis data dapat memainkan peran penting dalam mengidentifikasi individu yang berisiko tinggi terhadap serangan jantung sebelum gejala nyata muncul. Dengan tersedianya banyak referensi data medis, kita dapat menganalisis risiko serangan jantung dengan mempertimbangkan beberapa faktor kesehatan yang sekiranya berpengaruh, seperti usia, jenis kelamin, tekanan darah, jenis nyeri dada, dan sebagainya. |
| Solusi machine learning | Melakukan analisis klasifikasi dengan mengkategorikan tinggi atau rendahnya risiko seseorang mengalami serangan jantung. Faktor-faktor yang dipertimbangkan dalam proses klasifikasi adalah data usia, jenis kelamin, nyeri dada saat beraktivitas, jumlah pembuluh darah besar, tipe nyeri dada, tekanan darah istirahat, kolesterol, gula darah puasa, hasil elektrokardiografi istirahat, dan detak jantung maksimum. |
| Metode pengolahan | Analisis akan didasarkan pada kedua fitur yang ada pada dataset yang telah memiliki tipe data numerik untuk setiap fiturnya. Setelah itu, dilakukan splitting dataset untuk keperluan training dan evaluation dengan rasio 8:2. |
| Arsitektur model | Arsitektur model menggunakan Embedding model dengan library Tensorflow terhadap dataset. Kemudian, terdapat tiga Dense layers dengan jumlah unit masing-masing 256, 64, dan 16, serta menggunakan activation 'relu'. Terakhir, terdapat Dense layer dengan jumlah unit 1 dan fungsi activation 'sigmoid' untuk mengkategorikan teks pada kedua kategori yang ada pada fitur 'hrtatt'. Model tersebut kemudian di-compile dengan fungsi loss 'binary_crossentropy' dan metriks 'BinaryAccuracy()' menyesuaikan jumlah kategori yang ada, dan dioptimasi dengan Adam optimizer. |
| Metrik evaluasi | Metrik evaluasi yang digunakan adalah AUC, Precision, Recall, ExampleCount, dan BinaryAccuracy. |
| Performa model | Performa model berdasarkan hasil evaluasi training menunjukkan nilai accuracy sebesar 1.000 dan loss dengan nilai 0.3. Hasil tersebut menunjukkan bahwa model ML ini telah memiliki performa yang cukup baik dalam melakukan klasifikasi data. |
| Opsi deployment | ML pipeline ini diimplementasikan pada suatu cloud service melalui platform Railway. |
| Web app | [heart-attack-prediction-model](https://heart-attack-prediction-production.up.railway.app/v1/models/heart-attack-prediction-model/metadata)|
| Monitoring | Monitoring dilakukan menggunakan layanan Prometheus. Kita dapat melakukan monitoring status untuk setiap request yang dilakukan kepada server sistem operasi ML ini. |
