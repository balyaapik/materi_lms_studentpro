"""Memberi id pada judul yang belum punya, supaya daftar isi muncul di LMS.

prepare_book_html hanya memasukkan judul yang PUNYA id ke dalam daftar isi. Judul
tanpa id bukan sekadar tidak bisa ditautkan -- judul itu tidak ada sama sekali di
daftar isi, jadi materi dengan dua belas judul pun tampil tanpa daftar isi.

Gaya id mengikuti berkas yang sudah ada: h1 pertama menjadi "judul", sisanya slug
dari teks judulnya sendiri. Judul yang sudah punya id tidak disentuh, agar tautan
lama tidak putus.
"""

import re
import sys
import unicodedata
from pathlib import Path

ROMAWI = re.compile(r'<[^>]+>')


def slug(teks: str) -> str:
    teks = unicodedata.normalize('NFKD', teks)
    teks = ''.join(c for c in teks if not unicodedata.combining(c))
    teks = teks.replace('–', '-').replace('—', '-')
    teks = re.sub(r'[^a-zA-Z0-9]+', '-', teks).strip('-').lower()
    # Nomor urut di depan judul ("1. Apa itu...") dibuang: id yang diawali angka sah
    # di HTML5 tetapi menyulitkan pemakaian di CSS, dan nomornya bisa berubah.
    teks = re.sub(r'^\d+-', '', teks)
    return teks[:60] or 'bagian'


def beri_id(jalur: Path) -> dict:
    asli = jalur.read_text(encoding='utf-8')
    dipakai = set(re.findall(r'\bid\s*=\s*["\']([^"\']+)["\']', asli))
    tambah = [0]

    def olah(m):
        tingkat, atribut, isi = m.group(1), m.group(2) or '', m.group(3) or ''
        if re.search(r'\bid\s*=', atribut, re.I):
            return m.group(0)
        teks = re.sub(r'\s+', ' ', ROMAWI.sub('', isi)).strip()
        if not teks:
            return m.group(0)
        nama = 'judul' if tingkat == '1' and 'judul' not in dipakai else slug(teks)
        dasar, n = nama, 2
        while nama in dipakai:
            nama = f'{dasar}-{n}'
            n += 1
        dipakai.add(nama)
        tambah[0] += 1
        return f'<h{tingkat} id="{nama}"{atribut}>{isi}</h{tingkat}>'

    baru = re.sub(r'<h([1-6])\b([^>]*)>(.*?)</h\1>', olah, asli, flags=re.I | re.S)
    if baru == asli:
        return {'berkas': jalur.name, 'tambah': 0}
    jalur.write_text(baru, encoding='utf-8')
    return {'berkas': jalur.name, 'tambah': tambah[0]}


if __name__ == '__main__':
    akar = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    total = 0
    for f in sorted(akar.rglob('*.html')):
        h = beri_id(f)
        total += h['tambah']
        if h['tambah']:
            print(f"  +{h['tambah']:3} id   {h['berkas'][:56]}")
    print('total id baru:', total)
