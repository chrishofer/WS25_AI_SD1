import unittest
import statistics

class MyTestCase(unittest.TestCase):
    # Üblicherweise geben tearDown und setUp keinen Text aus - nur zur Illustration wie sie aufgerufen werden
    # Falls eine der Methoden nicht benötigt wird - nicht implementeiren
    @classmethod
    def setUpClass(cls):
        # wird nur einmal für die ganze Testklasse ausgeführt
        # verwenden wir nur für sehr aufwändige Initialisierung (Datenbanken, Dateien, aufwändige Weg Rquests)
        print("Einmalige initialisierung für klasse")
        # Datenbank erstellen

    def setUp(self):
        # setUp wird vor jedem Test einmal ausgeführt -> 3 mal
        # damit es keine Wechselwirkungen zwischen Tests gibt
        self.l1 = [10.0, 20.0, 30.0, 40.0]
        self.l_negative = [-10.0, 0.0, 10.0]
        self.l_empty = []
        print("Initialisierung vor jeder testmethode") # das illustriert nur wie oft es ausgeführt wird

    def tearDown(self):
        # wird nach jeder testmethode einmal ausgeführt
        print("aufräumen nach jeder testmethode")
        # Bsp: Temporäre Konfigurationsdatei löschen

    @classmethod
    def tearDownClass(cls):
        print("einmaliges aufräumen am ende der testklasse")
        # Bsp: Test Datenbank löschen

    def test_mean(self):
        # In Testmethode machen wir immer zwei Sachen
        # Zu testende Funktionalität aufrufen
        m = statistics.mean(self.l1)
        # Ergebnis vergleichen mit erwartetem Ergebnis
        # Erwartetes Ergebnis 25.0
        self.assertAlmostEqual(25.0, m)

    def test_mean_negative_values(self):
        m = statistics.mean(self.l_negative)
        self.assertAlmostEqual(0.0, m)

    def test_mean_empty_list(self):
        m = statistics.mean(self.l_empty)
        self.assertAlmostEqual(0.0, m)



if __name__ == '__main__':
    unittest.main()
