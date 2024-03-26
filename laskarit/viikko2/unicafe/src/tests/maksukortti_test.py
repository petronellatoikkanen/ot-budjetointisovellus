import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    #Kortin saldo alussa oikein
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    #Kortin saldo alussa oikein euroina
    def test_kortin_saldo_alussa_oikein_euroina(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    #Rahan lataaminen kasvattaa saldoa oikein
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(self.maksukortti.saldo, 1500)

    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(900)

        self.assertEqual(self.maksukortti.saldo, 100)

    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1900)

        self.assertEqual(self.maksukortti.saldo, 1000)

    #Metodi palauttaa True, jos rahat riittivät ja muuten False
    def test_metodi_palauttaa_true_jos_rahat_riittävät_muuten_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(900), True)

    def test_metodi_palauttaa_false_jos_rahat_eivät_riitä(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1900), False)



    def test_str(self):
        self.assertEqual(self.maksukortti.__str__(), 'Kortilla on rahaa 10.00 euroa')