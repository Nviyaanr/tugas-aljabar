import flet as ft
import numpy as np

alternatif = ["harga", "fitur", "diskon", "ketersediaan driver", "metode pembayaran", "user friendly"]
alternatif1 = ["Gojek", "Grab", "Maxim"]
# Matriks penilaian dari tabel kriteria utama
penilaian = np.array([[1, 5, 3, 4, 5, 5],
                     [1/5, 1, 1/3, 1/3, 3, 1/2],
                     [1/3, 3, 1, 3, 5, 4],
                     [1/4, 3, 1/3, 1, 3, 3],
                     [1/5, 1/3, 1/5, 1/3, 1, 1/3],
                     [1/5, 2, 1/4, 1/3, 3, 1]])

# Matriks penilaian dari tabel perbandigan harga
penilaian1 = np.array([[1, 2, 1/7],
                     [1/2, 1, 1/7],
                     [7, 7, 1],
                    ])
# Matriks penilaian dari tabel perbandigan Fitur
penilaian2 = np.array([[1, 2, 4],
                     [1/2, 1, 3],
                     [1/4, 1/3, 1],
                    ])
# Matriks penilaian dari tabel perbandigan Diskon
penilaian3 = np.array([[1, 3, 7],
                     [1/3, 1, 5],
                     [1/7, 1/5, 1],
                    ])
# Matriks penilaian dari tabel perbandingan Ketersediaan Driver
penilaian4 = np.array([[1, 5, 2],
                     [1/5, 1, 1/3],
                     [1/2, 3, 1],
                    ])
# Matriks penilaian dari tabel perbandigan Metode Pembayaran
penilaian5 = np.array([[1, 2, 5],
                     [1/2, 1, 5],
                     [1/5, 1/5, 1],
                    ])
# Matriks penilaian dari tabel perbandigan User Friendly
penilaian6 = np.array([[1, 3, 1/2],
                     [1/3, 1, 1/4],
                     [2, 4, 1],
                    ])

#jumlah tabel perbandingan kriteria urama
jumlah1 = penilaian[0][0] + penilaian[1][0] + penilaian[2][0] + penilaian[3][0] + penilaian[4][0] + penilaian[5][0]
jumlah2 = penilaian[0][1] + penilaian[1][1] + penilaian[2][1] + penilaian[3][1] + penilaian[4][1] + penilaian[5][1]
jumlah3 = penilaian[0][2] + penilaian[1][2] + penilaian[2][2] + penilaian[3][2] + penilaian[4][2] + penilaian[5][2]
jumlah4 = penilaian[0][3] + penilaian[1][3] + penilaian[2][3] + penilaian[3][3] + penilaian[4][3] + penilaian[5][3]
jumlah5 = penilaian[0][4] + penilaian[1][4] + penilaian[2][4] + penilaian[3][4] + penilaian[4][4] + penilaian[5][4]
jumlah6 = penilaian[0][5] + penilaian[1][5] + penilaian[2][5] + penilaian[3][5] + penilaian[4][5] + penilaian[5][5]
#jumlah tabel perbandingan harga
jumlah1a = penilaian1[0][0] + penilaian1[1][0] + penilaian1[2][0]
jumlah2a = penilaian1[0][1] + penilaian1[1][1] + penilaian1[2][1]
jumlah3a = penilaian1[0][2] + penilaian1[1][2] + penilaian1[2][2] 
#jumlah tabel perbandingan fitur
jumlah1b = penilaian2[0][0] + penilaian2[1][0] + penilaian2[2][0]
jumlah2b = penilaian2[0][1] + penilaian2[1][1] + penilaian2[2][1]
jumlah3b = penilaian2[0][2] + penilaian2[1][2] + penilaian2[2][2] 
#jumlah tabel perbandingan diskon
jumlah1c = penilaian3[0][0] + penilaian3[1][0] + penilaian3[2][0]
jumlah2c = penilaian3[0][1] + penilaian3[1][1] + penilaian3[2][1]
jumlah3c = penilaian3[0][2] + penilaian3[1][2] + penilaian3[2][2] 
#jumlah tabel perbandingan Ketersediaan Driver
jumlah1d = penilaian4[0][0] + penilaian4[1][0] + penilaian4[2][0]
jumlah2d = penilaian4[0][1] + penilaian4[1][1] + penilaian4[2][1]
jumlah3d = penilaian4[0][2] + penilaian4[1][2] + penilaian4[2][2] 
#jumlah tabel perbandingan Metode Pembayaran
jumlah1e = penilaian5[0][0] + penilaian5[1][0] + penilaian5[2][0]
jumlah2e = penilaian5[0][1] + penilaian5[1][1] + penilaian5[2][1]
jumlah3e = penilaian5[0][2] + penilaian5[1][2] + penilaian5[2][2] 
#jumlah tabel perbandingan User Friendly
jumlah1f = penilaian6[0][0] + penilaian6[1][0] + penilaian6[2][0]
jumlah2f = penilaian6[0][1] + penilaian6[1][1] + penilaian6[2][1]
jumlah3f = penilaian6[0][2] + penilaian6[1][2] + penilaian6[2][2] 

#hasil perhitungan nilai normalisasi tabel perbandingan kriteria utama
nilai1 = np.round((penilaian[0][0] / jumlah1), decimals=3)
nilai2 =  np.round((penilaian[1][0] / jumlah1), decimals=3)
nilai3 =  np.round((penilaian[2][0] / jumlah1), decimals=3)
nilai4 =  np.round((penilaian[3][0] / jumlah1), decimals=3)
nilai5 =  np.round((penilaian[4][0] / jumlah1), decimals=3)
nilai6 =  np.round((penilaian[5][0] / jumlah1), decimals=3)
nilai7 =  np.round((penilaian[0][1] / jumlah2), decimals=3)
nilai8 =  np.round((penilaian[1][1] / jumlah2), decimals=3)
nilai9 =  np.round((penilaian[2][1] / jumlah2), decimals=3)
nilai10 =  np.round((penilaian[3][1] / jumlah2), decimals=3)
nilai11 =  np.round((penilaian[4][1] / jumlah2), decimals=3)
nilai12 =  np.round((penilaian[5][1] / jumlah2), decimals=3)
nilai13 =  np.round((penilaian[0][2] / jumlah3), decimals=3)
nilai14 =  np.round((penilaian[1][2] / jumlah3), decimals=3)
nilai15 =  np.round((penilaian[2][2] / jumlah3), decimals=3)
nilai16 =  np.round((penilaian[3][2] / jumlah3), decimals=3)
nilai17 =  np.round((penilaian[4][2] / jumlah3), decimals=3)
nilai18 =  np.round((penilaian[5][2] / jumlah3), decimals=3)
nilai19 =  np.round((penilaian[0][3] / jumlah4), decimals=3)
nilai20 =  np.round((penilaian[1][3] / jumlah4), decimals=3)
nilai21 =  np.round((penilaian[2][3] / jumlah4), decimals=3)
nilai22 =  np.round((penilaian[3][3] / jumlah4), decimals=3)
nilai23 =  np.round((penilaian[4][3] / jumlah4), decimals=3)
nilai24 =  np.round((penilaian[5][3] / jumlah4), decimals=3)
nilai25 =  np.round((penilaian[0][4] / jumlah5), decimals=3)
nilai26 =  np.round((penilaian[1][4] / jumlah5), decimals=3)
nilai27 =  np.round((penilaian[2][4] / jumlah5), decimals=3)
nilai28 =  np.round((penilaian[3][4] / jumlah5), decimals=3)
nilai29 =  np.round((penilaian[4][4] / jumlah5), decimals=3)
nilai30 =  np.round((penilaian[5][4] / jumlah5), decimals=3)
nilai31 =  np.round((penilaian[0][5] / jumlah6), decimals=3)
nilai32 =  np.round((penilaian[1][5] / jumlah6), decimals=3)
nilai33 =  np.round((penilaian[2][5] / jumlah6), decimals=3)
nilai34 =  np.round((penilaian[3][5] / jumlah6), decimals=3)
nilai35 =  np.round((penilaian[4][5] / jumlah6), decimals=3)
nilai36 =  np.round((penilaian[5][5] / jumlah6), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan harga
nilai1a = np.round((penilaian1[0][0] / jumlah1a), decimals=3)
nilai2a =  np.round((penilaian1[1][0] / jumlah1a), decimals=3)
nilai3a =  np.round((penilaian1[2][0] / jumlah1a), decimals=3)
nilai4a =  np.round((penilaian1[0][1] / jumlah2a), decimals=3)
nilai5a =  np.round((penilaian1[1][1] / jumlah2a), decimals=3)
nilai6a =  np.round((penilaian1[2][1] / jumlah2a), decimals=3)
nilai7a =  np.round((penilaian1[0][2] / jumlah3a), decimals=3)
nilai8a =  np.round((penilaian1[1][2] / jumlah3a), decimals=3)
nilai9a =  np.round((penilaian1[2][2] / jumlah3a), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan fitur
nilai1b =  np.round((penilaian2[0][0] / jumlah1b), decimals=3)
nilai2b =  np.round((penilaian2[1][0] / jumlah1b), decimals=3)
nilai3b =  np.round((penilaian2[2][0] / jumlah1b), decimals=3)
nilai4b =  np.round((penilaian2[0][1] / jumlah2b), decimals=3)
nilai5b =  np.round((penilaian2[1][1] / jumlah2b), decimals=3)
nilai6b =  np.round((penilaian2[2][1] / jumlah2b), decimals=3)
nilai7b =  np.round((penilaian2[0][2] / jumlah3b), decimals=3)
nilai8b =  np.round((penilaian2[1][2] / jumlah3b), decimals=3)
nilai9b =  np.round((penilaian2[2][2] / jumlah3b), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan diskon
nilai1c =  np.round((penilaian3[0][0]  / jumlah1c), decimals=3)
nilai2c =  np.round((penilaian3[1][0] / jumlah1c), decimals=3)
nilai3c =  np.round((penilaian3[2][0] / jumlah1c), decimals=3)
nilai4c =  np.round((penilaian3[0][1] / jumlah2c), decimals=3)
nilai5c =  np.round((penilaian3[1][1] / jumlah2c), decimals=3)
nilai6c =  np.round((penilaian3[2][1] / jumlah2c), decimals=3)
nilai7c =  np.round((penilaian3[0][2] / jumlah3c), decimals=3)
nilai8c =  np.round((penilaian3[1][2] / jumlah3c), decimals=3)
nilai9c =  np.round((penilaian3[2][2] / jumlah3c), decimals=3)
nilai9c =  np.round((penilaian3[2][2] / jumlah3c), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan Ketersediaan Driver
nilai1d =  np.round((penilaian4[0][0] /jumlah1d), decimals=3)
nilai2d =  np.round((penilaian4[1][0] / jumlah1d), decimals=3)
nilai3d =  np.round((penilaian4[2][0] / jumlah1d), decimals=3)
nilai4d =  np.round((penilaian4[0][1] / jumlah2d), decimals=3)
nilai5d =  np.round((penilaian4[1][1] / jumlah2d), decimals=3)
nilai6d =  np.round((penilaian4[2][1] / jumlah2d), decimals=3)
nilai7d =  np.round((penilaian4[0][2] / jumlah3d), decimals=3)
nilai8d =  np.round((penilaian4[1][2] / jumlah3d), decimals=3)
nilai9d =  np.round((penilaian4[2][2] / jumlah3d), decimals=3)
nilai9d =  np.round((penilaian4[2][2] / jumlah3d), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan Metode Pembayaran
nilai1e =  np.round((penilaian5[0][0]  / jumlah1e), decimals=3)
nilai2e =  np.round((penilaian5[1][0] / jumlah1e), decimals=3)
nilai3e =  np.round((penilaian5[2][0] / jumlah1e), decimals=3)
nilai4e =  np.round((penilaian5[0][1] / jumlah2e), decimals=3)
nilai5e =  np.round((penilaian5[1][1] / jumlah2e), decimals=3)
nilai6e =  np.round((penilaian5[2][1] / jumlah2e), decimals=3)
nilai7e =  np.round((penilaian5[0][2] / jumlah3e), decimals=3)
nilai8e =  np.round((penilaian5[1][2] / jumlah3e), decimals=3)
nilai9e =  np.round((penilaian5[2][2] / jumlah3e), decimals=3)
#hasil perhitungan nilai normalisasi tabel perbandingan User Friendly
nilai1f =  np.round((penilaian6[0][0]  / jumlah1f), decimals=3)
nilai2f =  np.round((penilaian6[1][0] / jumlah1f), decimals=3)
nilai3f =  np.round((penilaian6[2][0] / jumlah1f), decimals=3)
nilai4f =  np.round((penilaian6[0][1] / jumlah2f), decimals=3)
nilai5f =  np.round((penilaian6[1][1] / jumlah2f), decimals=3)
nilai6f =  np.round((penilaian6[2][1] / jumlah2f), decimals=3)
nilai7f =  np.round((penilaian6[0][2] / jumlah3f), decimals=3)
nilai8f =  np.round((penilaian6[1][2] / jumlah3f), decimals=3)
nilai9f =  np.round((penilaian6[2][2] / jumlah3f), decimals=3)

#nilai vektor eigen dari tabel perbandingan kriteria harga
veigen1 = np.round(((nilai1 + nilai7 + nilai13 + nilai19 + nilai25 + nilai31)/6), decimals=3)
veigen2 = np.round(((nilai2 + nilai8 + nilai14 + nilai20 + nilai26 + nilai32)/6), decimals=3)
veigen3 = np.round(((nilai3 + nilai9 + nilai15 + nilai21 + nilai27 + nilai33)/6), decimals=3)
veigen4 = np.round(((nilai4 + nilai10 + nilai16 + nilai22 + nilai28 + nilai34)/6), decimals=3)
veigen5 = np.round(((nilai5 + nilai11 + nilai17 + nilai23 + nilai29 + nilai35)/6), decimals=3)
veigen6 = np.round(((nilai6 + nilai12 + nilai18 + nilai24 + nilai30 + nilai36)/6), decimals=3)
#nilai vektor eigen dari tabel perbandingan harga
veigen1a = np.round(((nilai1a + nilai4a + nilai7a)/3), decimals=3)
veigen2a = np.round(((nilai2a + nilai5a + nilai8a)/3), decimals=3)
veigen3a = np.round(((nilai3a + nilai6a + nilai9a)/3), decimals=3)
#nilai vektor eigen dari tabel perbandingan fitur
veigen1b = np.round(((nilai1b + nilai4b + nilai7b)/3), decimals=3)
veigen2b = np.round(((nilai2b + nilai5b + nilai8b)/3), decimals=3)
veigen3b = np.round(((nilai3b + nilai6b + nilai9b)/3), decimals=3)
#nilai vektor eigen dari tabel perbandingan diskon
veigen1c = np.round(((nilai1c + nilai4c + nilai7c)/3), decimals=3)
veigen2c = np.round(((nilai2c + nilai5c + nilai8c)/3), decimals=3)
veigen3c = np.round(((nilai3c + nilai6c + nilai9c)/3), decimals=3)
#nilai vektor eigen dari tabel perbandingan ketersediaan driver
veigen1d = np.round(((nilai1d + nilai4d + nilai7d)/3), decimals=3)
veigen2d = np.round(((nilai2d + nilai5d + nilai8d)/3), decimals=3)
veigen3d = np.round(((nilai3d + nilai6d + nilai9d)/3), decimals=3)
#nilai vektor eigen dari tabel perbandingan metode pembayaran
veigen1e = np.round(((nilai1e + nilai4e + nilai7e)/3), decimals=3)
veigen2e = np.round(((nilai2e + nilai5e + nilai8e)/3), decimals=3)
veigen3e = np.round(((nilai3e + nilai6e + nilai9e)/3), decimals=3)
#nilai vektor eigen dari tabel perbandingan user friendly
veigen1f = np.round(((nilai1f + nilai4f + nilai7f)/3), decimals=3)
veigen2f = np.round(((nilai2f + nilai5f + nilai8f)/3), decimals=3)
veigen3f = np.round(((nilai3f + nilai6f + nilai9f)/3), decimals=3)
#HASIL PERANGKINGAN
gojek = (veigen1*veigen1a)+(veigen2*veigen1b)+(veigen3*veigen1c)+(veigen4*veigen1d)+(veigen5*veigen1e)+(veigen6*veigen1f)
grab = (veigen1*veigen2a)+(veigen2*veigen2b)+(veigen3*veigen2c)+(veigen4*veigen2d)+(veigen5*veigen2e)+(veigen6*veigen2f)
maxim = (veigen1*veigen3a)+(veigen2*veigen3b)+(veigen3*veigen3c)+(veigen4*veigen3d)+(veigen5*veigen3e)+(veigen6*veigen3f)

#mencari nilai consistency ratio dari tabel perbandingan Kriteria utama
lamda = ((jumlah1*veigen1) + (jumlah2*veigen2) + (jumlah3*veigen3) + (jumlah4*veigen4) + (jumlah5*veigen5) + (jumlah6*veigen6))
n = len(alternatif)
random_index_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index = random_index_dict[n]
ci = (lamda - n) / (n - 1)
cr = (ci / 1.24)
#mencari nilai consistency ratio dari tabel perbandingan harga
lamda1 = ((jumlah1a*veigen1a) + (jumlah2a*veigen2a) + (jumlah3a*veigen3a))
n1 = len(alternatif1)
random_index_dict1 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index1 = random_index_dict1[n1]
ci1 = (lamda1 - n1) / (n1 - 1)
cr1 = (ci1 / 0.58)
#mencari nilai consistency ratio dari tabel perbandingan fitur
lamda2 = ((jumlah1b*veigen1b) + (jumlah2b*veigen2b) + (jumlah3b*veigen3b))
n2 = len(alternatif1)
random_index_dict2 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index2 = random_index_dict2[n2]
ci2 = (lamda2 - n2) / (n2 - 1)
cr2 = (ci2 / 0.58)
#mencari nilai consistency ratio dari tabel perbandingan Diskon
lamda3 = ((jumlah1c*veigen1c) + (jumlah2c*veigen2c) + (jumlah3c*veigen3c))
n3 = len(alternatif1)
random_index_dict3 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index3 = random_index_dict3[n3]
ci3 = (lamda3 - n3) / (n3 - 1)
cr3 = (ci3 / 0.58)
#mencari nilai consistency ratio dari tabel perbandingan Ketersediaan Driver
lamda4 = ((jumlah1d*veigen1d) + (jumlah2d*veigen2d) + (jumlah3d*veigen3d))
n4 = len(alternatif1)
random_index_dict4 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index4 = random_index_dict4[n4]
ci4 = (lamda4 - n4) / (n4 - 1)
cr4 = (ci4 / 0.58)
#mencari nilai consistency ratio dari tabel perbandingan Metode Pembayaran
lamda5 = ((jumlah1e*veigen1e) + (jumlah2e*veigen2e) + (jumlah3e*veigen3e))
n5 = len(alternatif1)
random_index_dict5 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index5 = random_index_dict5[n5]
ci5 = (lamda5 - n5) / (n5 - 1)
cr5 = (ci5 / 0.58)
#mencari nilai consistency ratio dari tabel perbandingan User Friendly
lamda6 = ((jumlah1f*veigen1f) + (jumlah2f*veigen2f) + (jumlah3f*veigen3f))
n6 = len(alternatif1)
random_index_dict6 = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
random_index6 = random_index_dict6[n6]
ci6 = (lamda6 - n6) / (n6 - 1)
cr6 = (ci6 / 0.58)

def main(page: ft.Page):
    
    page.title=("Vektor dan Nilai Eigen")
    page.scroll = ft.ScrollMode.AUTO    

    judul = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Nilai dan Vektor Eigen",
                     font_family="Impact",  
                      style=ft.TextThemeStyle.TITLE_LARGE,
                      color=ft.colors.YELLOW,
                        ))
    tittle = ft.Container(
    alignment=ft.alignment.center, margin=5,
    content=ft.Text("A. Tabel Kriteria Utama",
                    color=ft.colors.WHITE,
                    font_family="Impact",
                    )
    )
    tittle1 = ft.Container(
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("B. Tabel Alternatif Perbandingan Harga",
                        font_family="impact",
                        color=ft.colors.WHITE)
    )
    tittle2 = ft.Container(
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("C. Tabel ALternatif Perbandingan Fitur",
                        font_family="Impact",
                        color=ft.colors.WHITE)
    )
    tittle3 = ft.Container(
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("D. Tabel ALternatif Perbandingan Diskon",
                        font_family="Impact",
                        color=ft.colors.WHITE)
    )
    tittle4 = ft.Container(
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("E. Tabel ALternatif Perbandingan Ketersediaan Driver",
                        font_family="Impact",
                        color=ft.colors.WHITE)
    )
    tittle5 = ft.Container(
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("F. Tabel ALternatif Perbandingan Metode Pembayaran",
                        font_family="Impact",
                        color=ft.colors.WHITE)
    )
    tittle6 = ft.Container(  
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("G. Tabel ALternatif Perbandingan User Friendly",
                        font_family="Impact",
                        color=ft.colors.WHITE)
    )
    tittle7 = ft.Container(  
        alignment=ft.alignment.center, margin=5,
        content=ft.Text("Dari Semua Data Diatas Didapatkan Hasil Perangkingan : ",
                        font_family="Impact",
                        color=ft.colors.YELLOW )
    )
    
    #hasil consistency ratio tabel kriteria utama
    hasil = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan harga
    hasil1 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci1:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr1:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan Fitur
    hasil2 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci2:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr2:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan Diskon
    hasil3 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci3:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr3:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan Ketersediaan Driver
    hasil4 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci4:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr4:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan Metode Pemabayaran
    hasil5 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci5:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr5:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #hasil consistency ration tabel perbandingan User Friendly
    hasil6 = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("ci")),
                ft.DataColumn(ft.Text(f":    {ci6:.2f}")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("cr")),
                        ft.DataCell(ft.Text(f":  {cr6:.2f}")),
                    ],
                ),
                
            ],
            
        ),

    )
    #HASIL RANKING KETIGA APLIKASI
    rank = ft.Container(
        alignment=ft.alignment.center,
        content=ft.DataTable(
            column_spacing=40,
            columns=[
                ft.DataColumn(ft.Text("1. MAXIM")),
                ft.DataColumn(ft.Text(f":    {100*maxim:.2f}%")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("2. GOJEK")),
                        ft.DataCell(ft.Text(f":  {100*gojek:.2f}%")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("3. GRAB")),
                        ft.DataCell(ft.Text(f":  {100*grab:.2f}%")),
                    ],
                ),
            ],
            
        ),

    )
    
    #hasilvektor eigen tabel perbandingan tabel kriteria utama
    a = ft.Container(alignment=ft.alignment.center, content=ft.Text("Maka Hasil Consistency Rationya Adalah :"))
    spasi1 = ft.Text("")
    spasi = ft.Text("")
    data = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Harga")),
                ft.DataColumn(ft.Text("Fitur")),
                ft.DataColumn(ft.Text("Diskon")),
                ft.DataColumn(ft.Text("Ketersediaan Driver")),
                ft.DataColumn(ft.Text("Metode Pembayaran")),
                ft.DataColumn(ft.Text("User Friendly")),
                ft.DataColumn(ft.Text("V. Eigen"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Harga")),
                        ft.DataCell(ft.Text(nilai1)),
                        ft.DataCell(ft.Text(nilai7)),
                        ft.DataCell(ft.Text(nilai13)),
                        ft.DataCell(ft.Text(nilai19)),
                        ft.DataCell(ft.Text(nilai25)),
                        ft.DataCell(ft.Text(nilai31)),
                        ft.DataCell(ft.Text(veigen1))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Fitur")),
                        ft.DataCell(ft.Text(nilai2)),
                        ft.DataCell(ft.Text(nilai8)),
                        ft.DataCell(ft.Text(nilai14)),
                        ft.DataCell(ft.Text(nilai20)),
                        ft.DataCell(ft.Text(nilai26)),
                        ft.DataCell(ft.Text(nilai31)),
                        ft.DataCell(ft.Text(veigen2))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Diskon",)),
                        ft.DataCell(ft.Text(nilai3)),
                        ft.DataCell(ft.Text(nilai9)),
                        ft.DataCell(ft.Text(nilai15)),
                        ft.DataCell(ft.Text(nilai21)),
                        ft.DataCell(ft.Text(nilai27)),
                        ft.DataCell(ft.Text(nilai32)),
                        ft.DataCell(ft.Text(veigen3))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Ketersediaan Driver",)),
                        ft.DataCell(ft.Text(nilai4)),
                        ft.DataCell(ft.Text(nilai10)),
                        ft.DataCell(ft.Text(nilai16)),
                        ft.DataCell(ft.Text(nilai22)),
                        ft.DataCell(ft.Text(nilai28)),
                        ft.DataCell(ft.Text(nilai33)),
                        ft.DataCell(ft.Text(veigen4))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Metode Pembayaran",)),
                        ft.DataCell(ft.Text(nilai5)),
                        ft.DataCell(ft.Text(nilai11)),
                        ft.DataCell(ft.Text(nilai17)),
                        ft.DataCell(ft.Text(nilai23)),
                        ft.DataCell(ft.Text(nilai29)),
                        ft.DataCell(ft.Text(nilai34)),
                        ft.DataCell(ft.Text(veigen5))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("User Friendly",)),
                        ft.DataCell(ft.Text(nilai6)),
                        ft.DataCell(ft.Text(nilai12)),
                        ft.DataCell(ft.Text(nilai18)),
                        ft.DataCell(ft.Text(nilai24)),
                        ft.DataCell(ft.Text(nilai30)),
                        ft.DataCell(ft.Text(nilai36)),
                        ft.DataCell(ft.Text(veigen6))
                    ],
                ),
            ],
        ),)
    
    #hasil vektor eigen tabael perbandingan harga
    spasi1 = ft.Text("")
    data1 = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1a)),
                        ft.DataCell(ft.Text(nilai4a)),
                        ft.DataCell(ft.Text(nilai7a)),
                        ft.DataCell(ft.Text(veigen1a))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2a)),
                        ft.DataCell(ft.Text(nilai5a)),
                        ft.DataCell(ft.Text(nilai8a)),
                        ft.DataCell(ft.Text(veigen2a))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3a)),
                        ft.DataCell(ft.Text(nilai6a)),
                        ft.DataCell(ft.Text(nilai9a)),
                        ft.DataCell(ft.Text(veigen3a))
                    ],
                ),   
            ],
        ),)
    #hasil vektor eigen tabael perbandingan fitur
    spasi2 = ft.Text("")
    data2 = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1b)),
                        ft.DataCell(ft.Text(nilai4b)),
                        ft.DataCell(ft.Text(nilai7b)),
                        ft.DataCell(ft.Text(veigen1b))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2b)),
                        ft.DataCell(ft.Text(nilai5b)),
                        ft.DataCell(ft.Text(nilai8b)),
                        ft.DataCell(ft.Text(veigen2b))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3b)),
                        ft.DataCell(ft.Text(nilai6b)),
                        ft.DataCell(ft.Text(nilai9b)),
                        ft.DataCell(ft.Text(veigen3b))
                    ],
                ),   
            ],
        ),)
    #hasil vektor eigen tabael perbandingan diskon
    spasi3 = ft.Text("")
    data3 = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1c)),
                        ft.DataCell(ft.Text(nilai4c)),
                        ft.DataCell(ft.Text(nilai7c)),
                        ft.DataCell(ft.Text(veigen1c))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2c)),
                        ft.DataCell(ft.Text(nilai5c)),
                        ft.DataCell(ft.Text(nilai8c)),
                        ft.DataCell(ft.Text(veigen2c))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3c)),
                        ft.DataCell(ft.Text(nilai6c)),
                        ft.DataCell(ft.Text(nilai9c)),
                        ft.DataCell(ft.Text(veigen3c))
                    ],
                ),   
            ],
        ),)
    #hasil vektor eigen tabael perbandingan Ketersediaan Druver
    spasi4 = ft.Text("")
    data4= ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1d)),
                        ft.DataCell(ft.Text(nilai4d)),
                        ft.DataCell(ft.Text(nilai7d)),
                        ft.DataCell(ft.Text(veigen1d))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2d)),
                        ft.DataCell(ft.Text(nilai5d)),
                        ft.DataCell(ft.Text(nilai8d)),
                        ft.DataCell(ft.Text(veigen2d))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3d)),
                        ft.DataCell(ft.Text(nilai6d)),
                        ft.DataCell(ft.Text(nilai9d)),
                        ft.DataCell(ft.Text(veigen3d))
                    ],
                ),   
            ],
        ),)
    #hasil vektor eigen tabael perbandingan Metode Pembayaran
    spasi5 = ft.Text("")
    data5 = ft.Container(
        
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1e)),
                        ft.DataCell(ft.Text(nilai4e)),
                        ft.DataCell(ft.Text(nilai7e)),
                        ft.DataCell(ft.Text(veigen1e))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2e)),
                        ft.DataCell(ft.Text(nilai5e)),
                        ft.DataCell(ft.Text(nilai8e)),
                        ft.DataCell(ft.Text(veigen2e))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3e)),
                        ft.DataCell(ft.Text(nilai6e)),
                        ft.DataCell(ft.Text(nilai9e)),
                        ft.DataCell(ft.Text(veigen3e))
                    ],
                ),   
            ],
        ),)
    #hasil vektor eigen tabael perbandingan User Friendly
    spasi6 = ft.Text("")
    data6 = ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.DataTable(
                    column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("Gojek")),
                ft.DataColumn(ft.Text("Grab")),
                ft.DataColumn(ft.Text("Maxim")),
                ft.DataColumn(ft.Text("Vektor Eigen")),
                
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Gojek")),
                        ft.DataCell(ft.Text(nilai1f)),
                        ft.DataCell(ft.Text(nilai4f)),
                        ft.DataCell(ft.Text(nilai7f)),
                        ft.DataCell(ft.Text(veigen1f))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Grab")),
                        ft.DataCell(ft.Text(nilai2f)),
                        ft.DataCell(ft.Text(nilai5f)),
                        ft.DataCell(ft.Text(nilai8f)),
                        ft.DataCell(ft.Text(veigen2f))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Maxim",)),
                        ft.DataCell(ft.Text(nilai3f)),
                        ft.DataCell(ft.Text(nilai6f)),
                        ft.DataCell(ft.Text(nilai9f)),
                        ft.DataCell(ft.Text(veigen3f))
                    ],
                ),   
            ],
        ),)

    page.add(judul, tittle, data, spasi, a, hasil, 
             tittle1, data1, spasi1, a, hasil1,
             tittle2, data2, spasi2, a, hasil2,
             tittle3, data3, spasi3, a, hasil3,
             tittle4, data4, spasi4, a, hasil4,
             tittle5, data5, spasi5, a, hasil5,
             tittle6, data6, spasi6, a, hasil6, 
             tittle7, rank
             )
    #page.add(rank)
       
ft.app(target=main)