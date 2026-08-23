"""Menguatkan materi HTML agar tidak terpotong di layar ponsel.

Penyebab utama terpotongnya bukan gambar atau rumus, melainkan TABEL. Materi ini sudah
mengecilkan font tabel pada layar sempit, tetapi tabel empat kolom tetap lebih lebar
daripada 360 piksel berapa pun fontnya — dan begitu satu elemen melebihi lebar layar,
SELURUH halaman dapat digeser ke samping. Teks biasa pun ikut terpotong saat dibaca.

Yang dikerjakan berkas ini:

    1. setiap <td> diberi data-kolom dari <th> yang sesuai, supaya tabel dapat menumpuk
       menjadi kartu tanpa kehilangan nama kolomnya;
    2. satu blok CSS ditambahkan di akhir <style>, ditandai agar dapat dikenali dan
       tidak pernah ditambahkan dua kali;
    3. kanvas dibuat mengikuti lebar induknya.

Isi materinya sendiri tidak disentuh: tidak ada kalimat, angka, atau rumus yang diubah.
"""

import re
import sys
from pathlib import Path

PENANDA = 'penguat-ponsel-studentpro'

CSS = """
/* ===== %s =====
   Tabel yang tidak menumpuk adalah sebab paling sering halaman materi terpotong di
   ponsel: satu tabel empat kolom lebih lebar daripada layarnya, dan begitu ada satu
   elemen yang melebihi lebar, seluruh halaman dapat digeser ke samping — teks biasa
   pun ikut terpotong saat dibaca. */
html{-webkit-text-size-adjust:100%%; text-size-adjust:100%%}
body{overflow-wrap:break-word}
img,canvas,svg,video{max-width:100%%; height:auto}
table{max-width:100%%}

/* Rumus baris-tersendiri (\\[ ... \\] dan $$ ... $$) dirender MathJax sebagai satu blok
   yang tidak pernah dipatahkan. Rumus panjang karena itu bisa lebih lebar daripada layar
   ponsel. Yang digulir cukup rumusnya saja, bukan seluruh halaman. */
mjx-container{max-width:100%%}
mjx-container[display="true"]{overflow-x:auto; overflow-y:hidden; padding:2px 0 6px}

@media (max-width:560px){
  /* Tiap baris menjadi satu kartu, dengan nama kolomnya sendiri. Menggulir mendatar
     sengaja tidak dipakai: yang tersembunyi biasanya justru kolom terakhir, dan di
     tabel materi kolom terakhir hampir selalu kolom jawabannya. */
  table thead{position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0)}
  table, table tbody, table tr, table td{display:block; width:100%%}
  table tr{border:1px solid var(--garis,#e2e8f0); border-radius:12px;
           margin-bottom:12px; overflow:hidden; background:#fff}
  table td{border:0; border-bottom:1px solid var(--garis,#e2e8f0); padding:10px 13px}
  table tr td:last-child{border-bottom:0}
  table td[data-kolom]::before{
    content:attr(data-kolom); display:block; font-size:.68rem; font-weight:800;
    letter-spacing:.08em; text-transform:uppercase; color:var(--redup,#64748b);
    margin-bottom:3px;
  }
}

@media (max-width:380px){
  body{padding-left:12px; padding-right:12px; font-size:15px}
  h1{font-size:1.3rem} h2{font-size:1.08rem} h3{font-size:1rem}
  .kotak{padding:12px 13px}
}
/* ===== akhir %s ===== */
""" % (PENANDA, PENANDA)


def _beri_label_kolom(html: str) -> int:
    """Menyalin judul kolom ke setiap sel. Mengembalikan jumlah sel yang diberi label."""
    jumlah = 0

    def olah_tabel(m):
        nonlocal jumlah
        tabel = m.group(0)
        judul = [re.sub(r'<[^>]+>', '', t).strip()
                 for t in re.findall(r'<th\b[^>]*>(.*?)</th>', tabel, re.S | re.I)]
        if not judul:
            return tabel

        def olah_baris(mb):
            nonlocal jumlah
            baris = mb.group(0)
            i = [0]

            def olah_sel(ms):
                nonlocal jumlah
                pembuka = ms.group(1)
                if 'data-kolom' in pembuka:
                    i[0] += 1
                    return ms.group(0)
                label = judul[i[0]] if i[0] < len(judul) else ''
                i[0] += 1
                if not label:
                    return ms.group(0)
                jumlah += 1
                aman = label.replace('"', '&quot;')
                sisip = pembuka[:-1] + f' data-kolom="{aman}">'
                return sisip + ms.group(2)

            return re.sub(r'(<td\b[^>]*>)(.*?)(?=<td\b|</tr>)', olah_sel, baris,
                          flags=re.S | re.I)

        return re.sub(r'<tr\b[^>]*>.*?</tr>', olah_baris, tabel, flags=re.S | re.I)

    return re.sub(r'<table\b.*?</table>', olah_tabel, html, flags=re.S | re.I), jumlah


def kuatkan(jalur: Path) -> dict:
    asli = jalur.read_text(encoding='utf-8')
    kerja = asli
    diganti = False
    if PENANDA in kerja:
        # Blok lama dibuang lebih dulu supaya versi baru menggantikannya. Kalau blok lama
        # hanya dilewati, setiap perbaikan berikutnya tidak akan pernah sampai ke berkas.
        a = kerja.find('/* ===== ' + PENANDA)
        b = kerja.find('===== */', kerja.find('akhir ' + PENANDA))
        if a >= 0 and b > a:
            # Sela bekas potongan dirapikan; kalau tidak, tiap kali dijalankan berkasnya
            # bertambah dua baris kosong dan hasilnya tidak pernah sama dua kali.
            kerja = (kerja[:a].rstrip(' \t\n') + '\n'
                     + kerja[b + len('===== */'):].lstrip(' \t\n'))
            diganti = True

    baru, sel = _beri_label_kolom(kerja)

    # CSS disisipkan tepat sebelum </style> terakhir supaya menang atas aturan sebelumnya
    # tanpa perlu !important.
    i = baru.rfind('</style>')
    if i < 0:
        return {'berkas': jalur.name, 'status': 'tidak ada <style>', 'sel': sel}
    baru = baru[:i] + CSS + baru[i:]

    if baru == asli:
        return {'berkas': jalur.name, 'status': 'sudah sama', 'sel': 0}
    jalur.write_text(baru, encoding='utf-8')
    return {'berkas': jalur.name, 'status': 'diperbarui' if diganti else 'dikuatkan', 'sel': sel,
            'selisih': len(baru) - len(asli)}


if __name__ == '__main__':
    akar = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    for f in sorted(akar.rglob('*.html')):
        h = kuatkan(f)
        print(f"  {h['status']:16} {h.get('sel', 0):4} sel berlabel  {h['berkas'][:52]}")
