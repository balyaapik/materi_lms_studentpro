from pathlib import Path
import json, random, re, html

OUT = Path('SMA/PAPS/Verbal/Bank_Soal')
OUT.mkdir(parents=True, exist_ok=True)

SYN = [
('abadi','kekal'),('absah','sah'),('adaptif','luwes'),('afdal','utama'),('agung','mulia'),('akurat','tepat'),
('ambigu','taksa'),('andal','tepercaya'),('apatis','acuh'),('arif','bijak'),('autentik','asli'),('baku','standar'),
('cermat','teliti'),('dominan','menonjol'),('efisien','hemat'),('eksplisit','tersurat'),('fiktif','rekaan'),('fundamental','mendasar'),
('gamblang','jelas'),('harmonis','selaras'),('identik','sama'),('imparsial','netral'),('implisit','tersirat'),('inklusif','terbuka'),
('intensif','gencar'),('kredibel','terpercaya'),('konkret','nyata'),('konsisten','ajek'),('kontemporer','mutakhir'),('krusial','penting'),
('lazim','umum'),('legitim','sah'),('moderat','sedang'),('mutakhir','terbaru'),('objektif','netral'),('permanen','tetap'),
('progresif','maju'),('relevan','berkaitan'),('rentan','rawan'),('rigid','kaku'),('signifikan','berarti'),('sporadis','terpencar'),
('stagnan','mandek'),('subtil','halus'),('transparan','terbuka'),('valid','sahih'),('vital','penting'),('adaptasi','penyesuaian'),
('akselerasi','percepatan'),('alokasi','pembagian'),('asumsi','anggapan'),('evaluasi','penilaian'),('indikasi','petunjuk'),('inovasi','pembaruan'),
('interpretasi','penafsiran'),('kolaborasi','kerja sama'),('komprehensif','menyeluruh'),('konsekuensi','akibat'),('korelasi','hubungan'),('mitigasi','pengurangan risiko')]

ANT = [
('abadi','sementara'),('abstrak','konkret'),('aktif','pasif'),('aktual','usang'),('akurat','keliru'),('ambigu','tegas'),
('apatis','peduli'),('autentik','palsu'),('baku','tidak baku'),('cermat','ceroboh'),('dinamis','statis'),('efisien','boros'),
('eksplisit','implisit'),('eksternal','internal'),('fleksibel','kaku'),('formal','informal'),('harmonis','sumbang'),('inklusif','eksklusif'),
('konkret','abstrak'),('konsisten','berubah-ubah'),('konstruktif','destruktif'),('kontemporer','kuno'),('krusial','sepele'),('lazim','langka'),
('legal','ilegal'),('maksimal','minimal'),('mayoritas','minoritas'),('moderat','ekstrem'),('objektif','subjektif'),('optimistis','pesimistis'),
('permanen','sementara'),('progresif','regresif'),('rasional','irasional'),('relevan','menyimpang'),('rentan','tangguh'),('rigid','lentur'),
('signifikan','sepele'),('stabil','labil'),('transparan','tertutup'),('valid','invalid'),('adaptif','kaku'),('agresif','pasif'),
('anonim','dikenal'),('artifisial','alami'),('defisit','surplus'),('ekspansi','kontraksi'),('heterogen','homogen'),('imparsial','memihak'),
('independen','bergantung'),('inferior','superior'),('inovatif','konservatif'),('kompleks','sederhana'),('konvergen','divergen'),('masif','terbatas'),
('parsial','menyeluruh'),('produktif','mandul'),('proaktif','reaktif'),('stagnan','berkembang'),('tentatif','pasti'),('toleran','intoleran')]

ANA = [
('dokter : pasien','guru : murid'),('arsitek : bangunan','penulis : buku'),('kompas : arah','termometer : suhu'),('kunci : pintu','sandi : akun'),
('akar : pohon','fondasi : bangunan'),('mata : melihat','telinga : mendengar'),('pena : menulis','kuas : melukis'),('pilot : pesawat','nahkoda : kapal'),
('buku : perpustakaan','lukisan : galeri'),('ikan : air','burung : udara'),('api : panas','es : dingin'),('hujan : payung','terik : topi'),
('roda : mobil','sayap : pesawat'),('sarung tangan : tangan','sepatu : kaki'),('benih : tanaman','telur : unggas'),('sutradara : film','dirigen : orkestra'),
('pupuk : tanaman','vitamin : tubuh'),('kamera : foto','mikrofon : suara'),('pisau : memotong','jarum : menjahit'),('jam : waktu','timbangan : berat'),
('lebah : madu','sapi : susu'),('kapten : tim','ketua : organisasi'),('hakim : pengadilan','dokter : rumah sakit'),('hutan : pohon','laut : ikan'),
('garam : asin','gula : manis'),('cepat : lambat','tinggi : rendah'),('hemat : boros','rajin : malas'),('sebab : akibat','aksi : reaksi'),
('pertanyaan : jawaban','masalah : solusi'),('bensin : kendaraan','listrik : perangkat'),('mikroskop : kecil','teleskop : jauh'),('peta : lokasi','kalender : tanggal'),
('obat : penyakit','pemadam : kebakaran'),('rem : menghentikan','gas : mempercepat'),('printer : mencetak','scanner : memindai'),('wasit : pertandingan','moderator : diskusi'),
('kamera : fotografer','stetoskop : dokter'),('palu : tukang','cangkul : petani'),('kapas : kain','kayu : kertas'),('tepung : roti','tanah liat : gerabah'),
('kuncup : bunga','larva : kupu-kupu'),('huruf : kata','kata : kalimat'),('detik : menit','menit : jam'),('desa : kecamatan','kecamatan : kabupaten'),
('sel : jaringan','jaringan : organ'),('individu : populasi','populasi : komunitas'),('murid : kelas','pemain : tim'),('teori : praktik','rencana : pelaksanaan'),
('data : informasi','fakta : kesimpulan'),('riset : temuan','audit : laporan')]

PASSAGES = [
{
'title':'Perubahan Iklim dan Hujan Ekstrem','source':'BMKG','url':'https://www.bmkg.go.id/berita/utama/bmkg-perubahan-iklim-nyata-siklon-senyar-pecahkan-rekor-curah-hujan-tertinggi-sejak-1991',
'body':'''Perubahan iklim kini tidak lagi dibicarakan semata sebagai ancaman yang hanya akan terasa puluhan tahun mendatang. Perubahan pola suhu, curah hujan, dan kejadian cuaca ekstrem sudah diamati di banyak wilayah. BMKG menyoroti bahwa perubahan pada sistem iklim dapat meningkatkan peluang terjadinya hujan sangat lebat. Salah satu contoh yang mendapat perhatian adalah Siklon Tropis Senyar pada penghujung 2025, yang berkaitan dengan curah hujan luar biasa di sebagian Sumatra dan menghasilkan catatan hujan yang melampaui kondisi normal pada periode tertentu.

Namun, menghubungkan satu kejadian ekstrem dengan perubahan iklim perlu dilakukan secara hati-hati. Cuaca harian dipengaruhi banyak faktor, antara lain suhu permukaan laut, sirkulasi atmosfer, kelembapan, dan kondisi lokal. Perubahan iklim tidak berarti setiap hujan lebat selalu disebabkan oleh satu faktor tunggal. Yang lebih penting adalah mengamati kecenderungan jangka panjang: apakah kejadian ekstrem menjadi lebih sering, lebih intens, atau bergeser waktunya dibandingkan pola masa lalu. Data pengamatan yang panjang membantu membedakan variasi alami dengan perubahan yang lebih menetap.

Informasi tersebut memiliki konsekuensi praktis. Kota yang sebelumnya mengandalkan pola hujan lama mungkin perlu memperbarui kapasitas drainase dan tata ruang. Daerah pertanian dapat menyesuaikan kalender tanam ketika awal musim semakin sulit diprediksi. Pemerintah daerah juga perlu membuat sistem peringatan dini yang bukan hanya akurat secara ilmiah, tetapi mudah dipahami sehingga masyarakat mengetahui tindakan ketika risiko banjir atau longsor meningkat.

Upaya menghadapi perubahan iklim biasanya dibedakan menjadi mitigasi dan adaptasi. Mitigasi menekan penyebab perubahan iklim, misalnya dengan mengurangi emisi gas rumah kaca. Adaptasi berfokus pada pengurangan dampak, misalnya memperkuat infrastruktur, mengelola air, dan meningkatkan kesiapsiagaan. Keduanya tidak saling menggantikan. Mengurangi emisi penting untuk membatasi risiko masa depan, sedangkan adaptasi diperlukan karena sebagian dampak sudah dirasakan. Karena itu, data iklim, kebijakan, komunikasi risiko, dan kebiasaan masyarakat perlu berjalan bersama agar informasi ilmiah dapat berubah menjadi tindakan yang melindungi kehidupan sehari-hari.''',
'main':'perubahan iklim perlu dipahami melalui data jangka panjang dan direspons dengan mitigasi serta adaptasi','detail':'cuaca harian dipengaruhi banyak faktor sehingga satu kejadian ekstrem tidak boleh ditafsirkan secara sederhana','term':'pengurangan penyebab dan risiko','purpose':'menjelaskan perlunya respons berbasis data terhadap perubahan iklim','conclusion':'mitigasi dan adaptasi saling melengkapi dalam menghadapi perubahan iklim','implication':'kebijakan lokal perlu menyesuaikan perubahan risiko berdasarkan informasi iklim yang mutakhir'},
{
'title':'Transportasi Publik dan Udara Perkotaan','source':'Kementerian Perhubungan','url':'https://www.dephub.go.id/post/read/dari-krl-hingga-bus-listrik%2C-langkah-indonesia-mengejar-udara-lebih-bersih',
'body':'''Masalah transportasi perkotaan sering dipandang hanya dari sisi kemacetan. Padahal, pilihan moda perjalanan juga berhubungan dengan penggunaan energi dan kualitas udara. Kementerian Perhubungan mencatat bahwa transportasi darat menjadi penyumbang utama emisi dari sektor transportasi. Hal ini menunjukkan bahwa perbaikan mobilitas kota tidak cukup dilakukan dengan memperlebar jalan atau menambah ruang untuk kendaraan pribadi. Angkutan umum berkapasitas besar dapat membantu membuat perjalanan lebih efisien sekaligus menekan emisi per penumpang.

KRL, MRT, LRT, bus listrik, dan layanan pengumpan merupakan bagian dari sistem mobilitas yang lebih bersih. Akan tetapi, keberadaan moda baru tidak otomatis mengubah perilaku. Masyarakat mempertimbangkan waktu tempuh, biaya, kenyamanan, keamanan, kemudahan berpindah moda, dan jarak dari rumah ke halte atau stasiun. Jika perjalanan dengan angkutan umum memerlukan terlalu banyak perpindahan atau waktu tunggu terlalu lama, kendaraan pribadi tetap terasa lebih praktis.

Karena itu, integrasi menjadi penting. Integrasi bukan hanya penggunaan satu kartu pembayaran. Jadwal antarmoda perlu disusun agar penumpang tidak menunggu terlalu lama. Trotoar aman harus menghubungkan halte dengan permukiman dan pusat kegiatan. Informasi rute perlu mudah ditemukan. Akses bagi penyandang disabilitas, penerangan, dan fasilitas sepeda juga dapat memengaruhi keputusan masyarakat.

Peralihan ke kendaraan listrik dapat membantu menurunkan emisi langsung di jalan, terutama pada armada yang menempuh jarak panjang. Namun, manfaat lingkungan dipengaruhi juga oleh sumber listrik serta cara baterai diproduksi dan dikelola setelah masa pakainya berakhir. Dengan demikian, kebijakan transportasi bersih perlu dilihat sebagai sistem, bukan sekadar mengganti jenis mesin.

Pada akhirnya, kota berkelanjutan memerlukan kombinasi infrastruktur, layanan yang dapat diandalkan, dan perubahan kebiasaan. Angkutan umum akan lebih menarik ketika mampu bersaing dalam kenyamanan dan kepastian waktu. Perubahan kebiasaan perjalanan juga memerlukan evaluasi melalui data penumpang, waktu tempuh, keterjangkauan tarif, dan kualitas layanan. Pilihan perjalanan pribadi memiliki dampak kolektif terhadap kemacetan, penggunaan energi, dan kualitas udara kota.''',
'main':'transportasi bersih memerlukan integrasi layanan, infrastruktur, dan perubahan perilaku','detail':'kemudahan akses, jadwal, dan perpindahan moda memengaruhi pilihan masyarakat','term':'penggabungan berbagai unsur menjadi satu sistem','purpose':'menjelaskan bahwa mobilitas berkelanjutan memerlukan pendekatan sistem','conclusion':'keberhasilan angkutan umum ditentukan oleh kualitas jaringan secara keseluruhan','implication':'kota perlu memperbaiki perjalanan dari awal hingga akhir, bukan hanya menambah moda baru'},
{
'title':'Ekonomi Sirkular','source':'Bappenas','url':'https://greeneconomy.bappenas.go.id/home/ekonomi-sirkular-2/',
'body':'''Dalam model ekonomi linear, alur barang sering digambarkan secara sederhana: sumber daya diambil, produk dibuat, digunakan, lalu dibuang. Pola itu menjadi masalah ketika kebutuhan material terus meningkat sementara daya dukung lingkungan terbatas. Ekonomi sirkular menawarkan cara pandang berbeda. Bappenas menjelaskan pendekatan ini sebagai upaya meminimalkan penggunaan sumber daya, memperpanjang masa guna produk, dan mengembalikan sisa produksi maupun konsumsi ke dalam rantai nilai.

Daur ulang merupakan bagian ekonomi sirkular, tetapi bukan satu-satunya strategi. Semakin awal pemborosan dapat dicegah, semakin besar nilai yang dapat dipertahankan. Produk yang dirancang tahan lama dan mudah diperbaiki dapat digunakan bertahun-tahun. Barang yang masih layak dapat digunakan kembali. Komponen tertentu dapat dipulihkan untuk fungsi lain. Setelah pilihan tersebut tidak memungkinkan, barulah material didaur ulang atau diproses dengan cara lain.

Prinsip seperti menolak penggunaan yang tidak perlu, mengurangi material, menggunakan kembali, memperbaiki, memperbarui, dan mendaur ulang menunjukkan bahwa ekonomi sirkular menyentuh seluruh siklus hidup produk. Tanggung jawab tidak hanya berada pada konsumen. Produsen menentukan bahan, desain, kemudahan perbaikan, dan ketahanan produk. Pemerintah dapat membentuk standar, insentif, dan sistem pengumpulan. Konsumen menentukan apakah barang dipakai secara optimal atau cepat diganti.

Penerapan konsep ini tidak selalu mudah. Produk tahan lama dapat memiliki harga awal lebih tinggi. Sistem pengumpulan barang bekas membutuhkan logistik. Industri perlu memiliki pasar untuk material sekunder. Keberhasilan juga harus diukur secara hati-hati agar kegiatan yang hanya memindahkan masalah tidak dianggap sebagai perbaikan.

Meski demikian, ekonomi sirkular membuka peluang usaha pada jasa perbaikan, penyewaan, penjualan kembali, pengolahan material, dan desain modular. Informasi tentang daya tahan, suku cadang, dan cara mengembalikan produk dapat membantu konsumen mengambil keputusan. Produk tidak dipandang sebagai barang sekali pakai, melainkan sebagai kumpulan fungsi dan material yang nilainya dapat dipertahankan selama mungkin. Karena itu, ekonomi sirkular membutuhkan perubahan desain, kebijakan, pasar, dan kebiasaan secara bersamaan.''',
'main':'ekonomi sirkular mempertahankan nilai sumber daya selama mungkin melalui berbagai strategi','detail':'daur ulang hanya salah satu strategi dan pencegahan pemborosan dapat dilakukan lebih awal','term':'rangkaian proses yang mempertahankan nilai produk','purpose':'menjelaskan cakupan ekonomi sirkular yang lebih luas daripada daur ulang','conclusion':'ekonomi sirkular membutuhkan perubahan sistem, bukan hanya pengelolaan sampah','implication':'produsen, pemerintah, dan konsumen perlu berbagi peran dalam mempertahankan nilai material'},
{
'title':'Panas Bumi Indonesia','source':'Kementerian ESDM','url':'https://esdm.go.id/id/media-center/arsip-berita/kejar-potensi-panas-bumi-nomor-satu-dunia-bahlil-minta-pengembang-tak-tahan-konsesi',
'body':'''Indonesia berada di wilayah geologi yang memberikan potensi panas bumi sangat besar. Kementerian ESDM menyebut potensi nasional mencapai puluhan gigawatt, sedangkan kapasitas terpasang baru memanfaatkan sebagian kecilnya. Panas bumi memanfaatkan energi panas dari dalam bumi untuk menghasilkan uap atau fluida panas yang dapat digunakan dalam pembangkitan listrik. Berbeda dengan tenaga surya dan angin yang sangat bergantung pada kondisi cuaca saat itu, panas bumi dapat menyediakan listrik relatif stabil jika sumbernya terbukti dan fasilitas beroperasi baik.

Walaupun potensinya besar, pembangunan pembangkit panas bumi tidak dapat dilakukan terburu-buru. Eksplorasi diperlukan untuk memastikan karakter reservoir bawah tanah. Tahap ini membutuhkan biaya tinggi karena pengeboran belum tentu langsung menemukan sumber yang ekonomis. Setelah itu masih ada studi kelayakan, perizinan, pembangunan infrastruktur, dan pengelolaan dampak lingkungan serta sosial.

Pengembangan di kawasan tertentu juga memperlihatkan pentingnya pendekatan bertahap. Selain pertimbangan teknis dan keselamatan, kawasan sekitar proyek dapat memiliki nilai lingkungan, sosial, dan budaya yang perlu dilindungi. Pertanyaan tentang energi karena itu tidak berhenti pada berapa megawatt yang dapat dihasilkan, tetapi juga bagaimana proyek dibangun, siapa yang terdampak, dan bagaimana risiko dikelola.

Panas bumi memiliki keunggulan karena emisi operasionalnya umumnya lebih rendah daripada pembangkit fosil. Namun, istilah energi terbarukan tidak berarti tanpa dampak. Pembukaan akses jalan, penggunaan lahan, pengelolaan fluida, dan gangguan lokal tetap perlu dinilai. Tata kelola transparan serta komunikasi dengan masyarakat menjadi penting.

Kesenjangan antara potensi dan kapasitas terpasang menunjukkan bahwa sumber daya alam saja tidak menjamin keberhasilan. Diperlukan regulasi jelas, pembiayaan, kemampuan teknis, kepastian proyek, dan penerimaan sosial. Proses eksplorasi dan pembangunan dapat berlangsung bertahun-tahun sehingga kepastian kebijakan penting. Jika semua faktor dapat dikelola, panas bumi berpeluang menjadi sumber listrik rendah karbon penting bagi Indonesia, tetapi percepatan tetap harus berjalan bersama kehati-hatian.''',
'main':'potensi panas bumi besar tetapi pengembangannya membutuhkan kajian dan tata kelola','detail':'eksplorasi mahal karena hasil pengeboran belum tentu menghasilkan sumber yang ekonomis','term':'dukungan dan penerimaan masyarakat terhadap proyek','purpose':'menjelaskan peluang sekaligus tantangan pengembangan panas bumi','conclusion':'ketahanan energi perlu berjalan bersama perlindungan lingkungan dan masyarakat','implication':'percepatan proyek harus tetap menjaga kajian, keselamatan, dan komunikasi dengan warga'},
{
'title':'Pembatasan Gawai di Sekolah','source':'Kemendikdasmen','url':'https://internal-portal.kemdikbud.go.id/siaran-pers/15858-wujudkan-budaya-sekolah-aman-dan-nyaman-smpn-3-sidoarjo-batasi-penggunaan-gawai-murid',
'body':'''Gawai telah menjadi bagian dari kehidupan pelajar. Perangkat yang sama dapat dipakai untuk membaca buku digital, mencari informasi, berkomunikasi, mengerjakan tugas, menonton video, maupun mengakses media sosial. Karena memiliki banyak fungsi, perdebatan mengenai gawai di sekolah tidak sesederhana memilih antara membolehkan atau melarang. Tantangannya adalah memastikan teknologi mendukung proses belajar tanpa mengambil alih perhatian siswa.

Salah satu sekolah yang menerapkan pembatasan penggunaan gawai tetap mengakui manfaat literasi digital. Gawai tidak diposisikan sebagai benda yang sepenuhnya buruk, tetapi sebagai alat yang perlu digunakan secara proporsional. Ketika guru merancang aktivitas yang membutuhkan perangkat digital, gawai dapat dipakai. Di luar kebutuhan tersebut, penggunaannya dibatasi agar siswa tidak mudah terdistraksi oleh notifikasi, permainan, atau media sosial.

Kebijakan semacam ini memiliki beberapa alasan. Konsentrasi belajar membutuhkan kemampuan mempertahankan perhatian. Perangkat yang terus menawarkan rangsangan baru dapat membuat siswa lebih sering berpindah fokus. Interaksi tatap muka juga penting. Waktu istirahat yang seluruhnya dihabiskan di depan layar dapat mengurangi kesempatan berbicara, bermain, dan membangun hubungan sosial secara langsung.

Namun, pembatasan tidak akan efektif jika hanya mengandalkan hukuman. Siswa perlu memahami alasan aturan. Guru harus konsisten, sedangkan orang tua perlu mengetahui kapan anak dapat dihubungi. Sekolah juga harus menyediakan prosedur untuk keadaan darurat. Dengan demikian, aturan penggunaan gawai merupakan bagian dari tata kelola sekolah, bukan sekadar penyitaan perangkat.

Literasi digital tidak hanya berarti kemampuan menggunakan aplikasi. Siswa perlu belajar menilai kredibilitas informasi, menjaga privasi, memahami jejak digital, mengatur waktu layar, dan berkomunikasi secara bertanggung jawab. Sekolah juga perlu mengevaluasi aturan secara berkala karena kebijakan yang cocok untuk satu jenjang belum tentu tepat bagi jenjang lain. Tujuannya bukan menjauhkan siswa dari teknologi, tetapi membangun kemampuan mengendalikan teknologi sesuai kebutuhan sambil mempertahankan manfaatnya bagi pembelajaran.''',
'main':'pembatasan gawai perlu proporsional dan berjalan bersama literasi digital','detail':'aturan efektif memerlukan pemahaman siswa, konsistensi guru, dan komunikasi dengan orang tua','term':'sesuai kebutuhan dan tidak berlebihan','purpose':'menjelaskan pendekatan seimbang terhadap penggunaan gawai di sekolah','conclusion':'tujuan aturan ialah membangun kendali penggunaan teknologi, bukan menolak teknologi','implication':'sekolah perlu menyesuaikan aturan gawai dengan tujuan belajar dan kebutuhan siswa'},
{
'title':'Ketimpangan Kesehatan','source':'WHO Indonesia','url':'https://www.who.int/indonesia/news/detail/04-04-2025-new-who-publication-highlights-the-importance-of-health-inequality-monitoring-to-advance-health-equity',
'body':'''Rata-rata nasional sering digunakan untuk menggambarkan keadaan suatu negara. Namun, angka rata-rata dapat menyembunyikan perbedaan besar antarkelompok masyarakat. WHO menekankan pentingnya pemantauan ketimpangan kesehatan dengan menggunakan data yang dipilah berdasarkan wilayah, pendapatan, pendidikan, usia, jenis kelamin, dan karakteristik lain yang relevan. Tujuannya bukan sekadar membuat lebih banyak tabel, tetapi mengetahui kelompok mana yang tertinggal dan mengapa kebijakan yang sama dapat menghasilkan dampak berbeda.

Penurunan angka kematian ibu secara nasional, misalnya, merupakan kemajuan penting. Akan tetapi, ketika data dilihat per wilayah, perbedaan yang lebar dapat tetap terlihat. Daerah dengan akses fasilitas kesehatan terbatas, jarak jauh, kekurangan tenaga kesehatan, atau kondisi sosial ekonomi tertentu mungkin menghadapi risiko lebih tinggi. Jika pemerintah hanya melihat angka rata-rata, kebutuhan khusus wilayah tersebut dapat terlewat.

Data terpilah membantu kebijakan menjadi lebih tepat sasaran. Program kesehatan dapat diarahkan ke kelompok yang menghadapi hambatan terbesar. Anggaran dapat disesuaikan dengan kebutuhan, bukan sekadar dibagi rata. Evaluasi juga menjadi lebih bermakna karena tidak hanya bertanya apakah indikator nasional membaik, tetapi juga apakah kesenjangan berkurang.

Pengumpulan data rinci memiliki tantangan. Sistem pencatatan harus konsisten, petugas membutuhkan kapasitas, dan privasi wajib dijaga. Data yang terlalu sedikit pada kelompok tertentu dapat menghasilkan kesimpulan yang tidak stabil. Karena itu, kualitas data sama pentingnya dengan jumlah indikator. Pemantauan juga membutuhkan kehati-hatian dalam menafsirkan sebab karena akses layanan, lingkungan, pendidikan, pendapatan, kebiasaan, dan kualitas layanan dapat saling berhubungan.

Data yang baik pada akhirnya harus diikuti tindakan. Mengetahui kesenjangan tidak otomatis menguranginya. Temuan perlu diterjemahkan menjadi prioritas program, pembiayaan, peningkatan layanan, dan evaluasi berulang. Tujuan akhirnya adalah keadilan kesehatan: sistem dinilai bukan hanya dari tingginya rata-rata capaian, tetapi juga dari kemampuan memastikan kelompok yang paling sulit dijangkau tidak tertinggal.''',
'main':'data kesehatan terpilah diperlukan untuk melihat ketimpangan yang tersembunyi','detail':'rata-rata dapat menutupi perbedaan besar antara kelompok dan wilayah','term':'data yang diuraikan menurut kelompok atau karakteristik tertentu','purpose':'menjelaskan pentingnya pemantauan ketimpangan untuk kebijakan kesehatan','conclusion':'keadilan kesehatan memerlukan perhatian pada kelompok yang tertinggal','implication':'kebijakan kesehatan perlu diarahkan berdasarkan kebutuhan yang terlihat dari data terpilah'},
{
'title':'Batik sebagai Warisan Budaya','source':'UNESCO','url':'https://ich.unesco.org/en/RL/indonesian-batik-00170',
'body':'''Batik sering dikenali melalui motif pada kain, tetapi maknanya lebih luas daripada produk tekstil. UNESCO mencatat batik Indonesia sebagai warisan budaya takbenda karena pengetahuan, teknik, simbolisme, dan praktik sosial di sekitarnya hidup dalam masyarakat. Proses pembuatan batik tradisional melibatkan malam atau lilin sebagai perintang warna. Pengrajin menutup bagian tertentu pada kain, melakukan pewarnaan, lalu menghilangkan malam. Untuk menghasilkan beberapa warna, proses tersebut dapat diulang.

Keberagaman motif batik memperlihatkan pertemuan berbagai pengaruh budaya. Bentuk tumbuhan, hewan, pola geometris, unsur kaligrafi, dan ragam hias dari berbagai tradisi dapat muncul dalam desain. Motif tidak hanya berfungsi sebagai dekorasi. Di sejumlah komunitas, warna dan pola tertentu berkaitan dengan tahap kehidupan, upacara, kedudukan sosial, atau identitas daerah. Batik karena itu dapat menjadi medium yang membawa ingatan dan nilai budaya.

Warisan budaya tidak bertahan hanya karena pernah diakui. Keberlanjutannya bergantung pada pewarisan keterampilan kepada generasi baru, baik melalui keluarga, komunitas, sanggar, museum, maupun pendidikan. Pelatihan batik bagi pelajar penting karena generasi muda tidak hanya melihat produk jadi, tetapi juga memahami sejarah, keterampilan, dan nilai yang menyertainya.

Di sisi lain, batik terus beradaptasi. Pengrajin bereksperimen dengan desain, warna, dan produk baru agar batik tetap relevan. Adaptasi tidak selalu berarti meninggalkan tradisi. Budaya yang hidup biasanya berubah sambil mempertahankan unsur yang dianggap penting oleh komunitasnya.

Tantangannya adalah menjaga keseimbangan. Jika permintaan pasar meningkat tetapi pengetahuan tentang teknik dan makna tradisional menghilang, nilai budaya dapat berkurang. Sebaliknya, jika tradisi dipertahankan terlalu kaku, generasi baru mungkin merasa tidak memiliki ruang untuk berkreasi. Konsumen juga berperan ketika memahami proses dan nilai karya. Pengakuan internasional dapat meningkatkan kebanggaan, tetapi keberlanjutan sesungguhnya bergantung pada komunitas yang terus membuat, memakai, mengajarkan, dan memberi makna pada batik.''',
'main':'batik merupakan warisan hidup yang mencakup teknik, makna, pewarisan, dan adaptasi','detail':'pengakuan formal tidak cukup tanpa pewarisan keterampilan kepada generasi baru','term':'proses meneruskan pengetahuan dan keterampilan kepada generasi berikutnya','purpose':'menjelaskan batik sebagai warisan budaya yang hidup','conclusion':'pelestarian batik memerlukan keseimbangan antara kesinambungan dan pembaruan','implication':'pelestarian perlu melibatkan pengrajin, generasi muda, dan masyarakat sebagai pengguna'},
{
'title':'Budaya Jamu','source':'UNESCO','url':'https://ich.unesco.org/en/RL/jamu-wellness-culture-01972',
'body':'''Jamu dikenal sebagai ramuan berbahan tumbuhan yang telah lama digunakan dalam kehidupan masyarakat Indonesia. UNESCO memasukkan budaya jamu ke dalam daftar Warisan Budaya Takbenda Kemanusiaan pada 2023. Pengakuan tersebut tidak hanya merujuk pada minuman atau ramuan yang dihasilkan, tetapi juga mencakup pengetahuan mengenai bahan, cara meracik, praktik penggunaan, hubungan sosial antara pembuat dan pengguna, serta cara pengetahuan diwariskan.

Bahan jamu dapat berasal dari tanaman, rempah, akar, rimpang, daun, dan bahan alami lain. Pengetahuan tradisional menentukan bahan yang digunakan, cara memprosesnya, dan penyesuaian ramuan terhadap kebutuhan. Banyak pembuat jamu memperoleh keterampilan melalui keluarga atau lingkungan sekitar, meskipun kini pengetahuan jamu juga dipelajari dalam pendidikan dan penelitian.

Salah satu aspek penting budaya jamu adalah hubungan sosial. Penjual atau peracik sering mengenal kebiasaan pelanggannya dan membangun kepercayaan dari waktu ke waktu. Dalam bentuk tradisional, membeli jamu dapat menjadi ruang percakapan, pertukaran pengalaman, dan pemeliharaan hubungan komunitas. Jamu karena itu memiliki dimensi sosial selain fungsi yang dikaitkan dengan kebugaran dan kesehatan.

Keberadaan jamu di masa kini menghadapi tantangan baru. Konsumen semakin menuntut informasi mengenai kebersihan, keamanan bahan, komposisi, dan mutu. Ketika jamu diproduksi dalam skala industri, standar pengolahan dan pelabelan menjadi semakin penting. Di sisi lain, komersialisasi yang terlalu jauh dari praktik asal dapat membuat pengetahuan lokal kehilangan konteks.

Pengakuan budaya tidak berarti setiap klaim kesehatan mengenai jamu otomatis terbukti secara ilmiah. Tradisi dan penelitian ilmiah memiliki cara pembuktian berbeda dan dapat saling memberi informasi. Pelestarian juga terkait keberlanjutan tanaman bahan jamu dan proses belajar antargenerasi. Karena itu, menjaga budaya jamu bukan hanya mempertahankan resep, tetapi memelihara ekosistem pengetahuan, pelaku, bahan, hubungan sosial, serta tuntutan keamanan konsumen masa kini.''',
'main':'jamu merupakan praktik budaya yang mencakup ramuan, pengetahuan, hubungan sosial, dan pewarisan','detail':'pengakuan budaya tidak sama dengan pembuktian ilmiah semua klaim kesehatan','term':'pengembangan produk atau praktik untuk kepentingan pasar','purpose':'menjelaskan budaya jamu beserta tantangan pelestariannya','conclusion':'tradisi jamu dapat bertahan jika nilai budaya dan tuntutan modern diseimbangkan','implication':'pelestarian jamu perlu menjaga pengetahuan tradisional sekaligus standar keamanan konsumen'},
{
'title':'Keamanan Anak di Ruang Digital','source':'UNICEF Indonesia','url':'https://www.unicef.org/indonesia/id/perlindungan-anak/laporan/pengetahuan-dan-kebiasaan-daring-anak-di-indonesia-sebuah-kajian-dasar-2023',
'body':'''Internet memberi anak dan remaja peluang besar untuk belajar, berkomunikasi, bermain, dan berkarya. Namun, ruang digital juga membawa risiko yang tidak selalu mudah dikenali. UNICEF Indonesia melaporkan penggunaan internet yang sangat tinggi di kalangan anak dan sebagian besar mengaksesnya setiap hari. Aktivitas daring meliputi media sosial, hiburan, komunikasi, pencarian informasi, dan pembelajaran. Tingginya penggunaan membuat kemampuan menjaga keamanan diri menjadi keterampilan penting.

Risiko daring dapat berupa perundungan siber, paparan konten yang tidak sesuai, penipuan, penyalahgunaan data pribadi, dan eksploitasi. Anak kadang menghadapi situasi yang membuat mereka tidak nyaman tetapi tidak tahu kepada siapa harus bercerita. Sebagian juga belum memahami bahwa foto, pesan, dan informasi pribadi yang dikirim melalui internet dapat disalin serta disebarkan di luar kendali mereka.

Karena itu, keamanan digital tidak cukup diajarkan sebagai daftar larangan. Anak perlu memahami cara mengelola privasi, membuat kata sandi yang kuat, mengenali manipulasi, memblokir akun yang mengganggu, menyimpan bukti bila terjadi pelecehan, dan mencari bantuan dari orang dewasa tepercaya. Kemampuan mengambil keputusan menjadi penting karena situasi daring sangat beragam dan aturan sederhana tidak selalu mencakup semua kemungkinan.

Orang tua dan guru juga memegang peran penting. Pengawasan yang hanya berupa larangan keras dapat membuat anak enggan bercerita ketika mengalami masalah. Sebaliknya, komunikasi terbuka membantu anak merasa aman meminta bantuan. Sekolah dapat memasukkan keamanan digital ke dalam pembelajaran literasi. Perusahaan teknologi dan pemerintah juga memiliki tanggung jawab karena desain layanan dan mekanisme pelaporan dapat memengaruhi keamanan pengguna muda.

Anak perlu diberi ruang berpartisipasi dalam pendekatan keamanan digital karena mereka mengenal platform dan situasi yang muncul dalam pergaulan daring. Tujuan akhirnya bukan membuat anak takut menggunakan internet. Perlindungan terbaik muncul ketika anak memiliki pengetahuan, orang dewasa menyediakan dukungan, dan platform serta kebijakan dirancang untuk mengurangi risiko sejak awal.''',
'main':'keamanan anak di internet memerlukan pengetahuan, dukungan orang dewasa, dan perlindungan sistem','detail':'daftar larangan saja tidak cukup karena anak perlu mengambil keputusan dalam situasi yang beragam','term':'rekam informasi atau aktivitas yang tertinggal setelah interaksi daring','purpose':'menjelaskan perlunya tanggung jawab bersama dalam keamanan digital','conclusion':'internet perlu digunakan secara sadar dan aman, bukan ditakuti','implication':'pendidikan keamanan digital perlu menggabungkan keterampilan anak, dukungan dewasa, dan desain platform'},
{
'title':'Kesenjangan Pembelajaran Digital','source':'UNICEF Indonesia','url':'https://www.unicef.org/indonesia/id/laporan/analisis-situasi-pembelajaran-digital-di-indonesia',
'body':'''Pembelajaran digital sering dianggap sebagai solusi untuk memperluas akses pendidikan. Materi dapat dibagikan cepat, siswa belajar dari berbagai sumber, dan guru memiliki lebih banyak pilihan media. Namun, manfaat tersebut tidak otomatis dirasakan semua anak secara sama. UNICEF menyoroti kesenjangan digital yang dipengaruhi akses perangkat, koneksi internet, keterampilan, kondisi ekonomi, wilayah tempat tinggal, dan dukungan di rumah maupun sekolah.

Memiliki telepon pintar tidak selalu berarti memiliki kondisi belajar digital yang memadai. Satu perangkat mungkin digunakan bersama beberapa anggota keluarga. Kuota internet dapat menjadi beban. Layar kecil tidak nyaman untuk membaca teks panjang atau mengerjakan tugas tertentu. Di wilayah dengan jaringan tidak stabil, video pembelajaran berkualitas tinggi sulit diakses. Karena itu, ukuran akses harus melihat kualitas dan keberlanjutan, bukan sekadar apakah seseorang pernah terhubung ke internet.

Keterampilan juga menjadi pembeda. Siswa yang terbiasa mencari informasi belum tentu mampu mengevaluasi sumber. Guru yang dapat menjalankan aplikasi belum tentu langsung mampu merancang pembelajaran digital yang efektif. Teknologi memberi dampak lebih besar jika dipadukan dengan strategi pedagogis yang jelas: tujuan belajar, aktivitas, umpan balik, dan dukungan bagi siswa yang kesulitan.

Kesenjangan digital dapat memperbesar ketimpangan yang sudah ada. Siswa dengan perangkat lebih baik, koneksi stabil, ruang belajar tenang, dan dukungan keluarga dapat memanfaatkan teknologi lebih maksimal. Siswa dengan keterbatasan justru berisiko tertinggal jika seluruh pembelajaran dipindahkan ke platform daring tanpa alternatif.

Karena itu, kebijakan pembelajaran digital perlu fleksibel. Materi berukuran kecil, akses luring, penggunaan perangkat bersama di sekolah, pelatihan guru, dan dukungan teknis dapat membantu. Evaluasi juga perlu melihat pengalaman siswa, guru, dan hasil belajar, bukan sekadar jumlah akun aktif. Teknologi pendidikan sebaiknya dipandang sebagai alat, bukan tujuan. Keberhasilan dinilai dari apakah siswa benar-benar lebih mudah belajar dan apakah kesenjangan dapat diperkecil.''',
'main':'pembelajaran digital berpotensi memperluas akses tetapi harus memperhatikan kesenjangan','detail':'kepemilikan perangkat saja tidak menjamin akses belajar digital yang memadai','term':'berkaitan dengan cara merancang dan melaksanakan pembelajaran','purpose':'menjelaskan syarat agar transformasi digital pendidikan lebih inklusif','conclusion':'teknologi pendidikan harus dinilai dari dampaknya pada belajar dan pemerataan','implication':'sekolah perlu menyediakan alternatif akses bagi siswa dengan perangkat atau jaringan terbatas'}]

# Ensure every adapted passage is genuinely long enough.
for p in PASSAGES:
    n = len(re.findall(r'\b\w+\b', p['body']))
    if n <= 300:
        raise ValueError(f"Passage too short: {p['title']} ({n} words)")


def vislen(s):
    return len(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip())


def choose_distractors(correct, pool, rng, n=4):
    cands = list(dict.fromkeys(x for x in pool if x != correct))
    cands.sort(key=lambda x: abs(vislen(x) - vislen(correct)))
    window = cands[:max(n, min(20, len(cands)))]
    return rng.sample(window, n)


def make_q(stem, correct, pool, rng, explanation):
    opts = [correct] + choose_distractors(correct, pool, rng, 4)
    rng.shuffle(opts)
    choices=[]
    for i,o in enumerate(opts):
        item={'label': chr(65+i), 'text': o}
        if o == correct:
            item['correct']=True
        choices.append(item)
    return {'type':'single_choice','content':f'<p>{stem}</p>','choices':choices,'explanation':f'<p>{explanation}</p>'}


def render(pkg, questions):
    headers={1:'Padanan Kata',13:'Lawan Kata',25:'Analogi Kata',35:'Pemahaman Wacana'}
    sections=[]
    for i,q in enumerate(questions,1):
        h=f"<div class='subhead'>{headers[i]}</div>" if i in headers else ''
        opts="<ol class='opsi'>"+''.join(f"<li>{c['text']}</li>" for c in q['choices'])+'</ol>'
        sections.append(f"{h}<section class='soal'><div class='qnum'>{i}.</div>{q['content']}{opts}</section>")
    bank={'schema':'studentpro-question-bank/v1','title':f'PAPS Verbal Paket {pkg:02d} — 5 Opsi','subject':'PAPS Verbal','questions':questions}
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PAPS Verbal Paket {pkg:02d}</title><style>*{{box-sizing:border-box}}body{{max-width:64rem;margin:2rem auto;padding:0 1rem;font:16px/1.65 system-ui,-apple-system,"Segoe UI",Arial;color:#111827}}header{{border-bottom:2px solid #0f172a;padding-bottom:1rem;margin-bottom:1.2rem}}h1{{margin:.1rem 0;font-size:1.8rem}}.meta{{color:#64748b}}.note{{background:#eff6ff;border-left:4px solid #2563eb;padding:.7rem .9rem;border-radius:6px;margin:1rem 0}}.subhead{{margin-top:1.4rem;background:#0f172a;color:#fff;padding:.55rem .8rem;border-radius:6px;font-weight:800}}.soal{{padding:1rem 0 1.3rem;border-bottom:1px solid #e5e7eb}}.qnum{{font-weight:850}}ol.opsi{{list-style:upper-alpha;margin:.5rem 0 0 1.25rem}}.wacana{{background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;padding:1rem 1.1rem}}.wacana p{{text-align:justify}}.source{{font-size:.88rem;color:#475569;border-top:1px solid #cbd5e1;padding-top:.6rem}}.refer{{font-style:italic;color:#64748b}}</style></head><body><header><h1>PAPS Verbal — Paket {pkg:02d}</h1><div class="meta">40 soal · 5 opsi A–E · waktu 30 menit</div></header><div class="note">12 Padanan Kata · 12 Lawan Kata · 10 Analogi Kata · 6 Pemahaman Wacana. Opsi benar dan pengecoh dibuat relatif seimbang panjangnya.</div>{''.join(sections)}<script type="application/json" id="studentpro-question-bank">{json.dumps(bank,ensure_ascii=False,separators=(',',':'))}</script></body></html>'''


syn_pool=[b for _,b in SYN]
ant_pool=[b for _,b in ANT]
ana_pool=[b for _,b in ANA]
fields=['main','detail','term','purpose','conclusion','implication']
field_stems=[
'Gagasan utama bacaan tersebut adalah ...',
'Pernyataan yang paling sesuai dengan isi bacaan adalah ...',
'Makna istilah penting dalam konteks bacaan paling dekat dengan ...',
'Tujuan utama penulis menyajikan bacaan tersebut adalah ...',
'Simpulan yang paling tepat berdasarkan bacaan adalah ...',
'Implikasi yang paling logis berdasarkan bacaan adalah ...']

for pkg in range(1,11):
    rng=random.Random(20260910+pkg)
    qs=[]
    for j in range(12):
        word,ans=SYN[((pkg-1)*6+j)%len(SYN)]
        qs.append(make_q(f'Padanan kata yang paling tepat untuk <strong>{html.escape(word)}</strong> adalah ...',ans,syn_pool,rng,f'{word} berpadanan makna dengan {ans}.'))
    for j in range(12):
        word,ans=ANT[((pkg-1)*6+j)%len(ANT)]
        qs.append(make_q(f'Lawan kata yang paling tepat untuk <strong>{html.escape(word)}</strong> adalah ...',ans,ant_pool,rng,f'Lawan makna {word} adalah {ans}.'))
    for j in range(10):
        left,right=ANA[((pkg-1)*4+j)%len(ANA)]
        qs.append(make_q(f'Hubungan kata pada pasangan <strong>{html.escape(left)}</strong> setara dengan ...',right,ana_pool,rng,f'Hubungan {left} setara dengan {right}.'))

    p=PASSAGES[pkg-1]
    wc=len(re.findall(r'\b\w+\b',p['body']))
    passage="<div class='wacana'><h3>Bacaan untuk soal 35–40</h3><h4>"+html.escape(p['title'])+'</h4>'+''.join(f'<p>{html.escape(x)}</p>' for x in p['body'].split('\n\n'))+f"<p class='source'><strong>Sumber adaptasi:</strong> <a href='{p['url']}' target='_blank' rel='noopener'>{html.escape(p['source'])}</a>. Bacaan diparafrase dan disusun ulang untuk latihan. Jumlah kata: {wc}.</p></div>"
    for k,field in enumerate(fields):
        correct=p[field]
        pool=[x[field] for x in PASSAGES]
        q=make_q(field_stems[k],correct,pool,rng,'Jawaban ditentukan berdasarkan informasi dan hubungan gagasan dalam bacaan.')
        if k==0:
            q['content']=passage+q['content']
        else:
            q['content']="<p class='refer'>Berdasarkan bacaan pada soal 35.</p>"+q['content']
        qs.append(q)

    if len(qs)!=40 or any(len(q['choices'])!=5 for q in qs) or any(sum(bool(c.get('correct')) for c in q['choices'])!=1 for q in qs):
        raise ValueError(f'Validation failed for package {pkg}')
    (OUT/f'PAPS_Verbal_Paket_{pkg:02d}.html').write_text(render(pkg,qs),encoding='utf-8')

print('Generated 10 PAPS Verbal packages with 40 questions and 5 options each.')
