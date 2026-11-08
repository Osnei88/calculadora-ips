import unittest

from calculadora import calcular_ip

class TestCalculadoraIP(unittest.TestCase):

    def test_rede_classe_c(self):
        resultado = calcular_ip("192.168.1.10/24")

        self.assertEqual(resultado["rede"], "192.168.1.0")
        self.assertEqual(resultado["broadcast"], "192.168.1.255")
        self.assertEqual(resultado["mascara"], "255.255.255.0")

    def test_rede_com_prefixo_21(self):
        resultado = calcular_ip("172.45.60.116/21")

        self.assertEqual(resultado["rede"], "172.45.56.0")
        self.assertEqual(resultado["primeiro_ip"], "172.45.56.1")
        self.assertEqual(resultado["ultimo_ip"], "172.45.63.254")
        self.assertEqual(resultado["broadcast"], "172.45.63.255")

    def test_rede_com_prefixo_26(self):
        resultado = calcular_ip("192.168.10.100/26")

        self.assertEqual(resultado["rede"], "192.168.10.64")
        self.assertEqual(resultado["broadcast"], "192.168.10.127")
        self.assertEqual(resultado["hosts_disponiveis"], 62)

    def test_rede_com_prefixo_30(self):
        resultado = calcular_ip("192.168.1.1/30")

        self.assertEqual(resultado["rede"], "192.168.1.0")
        self.assertEqual(resultado["hosts_disponiveis"], 2)

    def test_prefixo_31(self):
        resultado = calcular_ip("192.168.1.1/31")

        self.assertEqual(resultado["hosts_disponiveis"], 2)

    def test_prefixo_32(self):
        resultado = calcular_ip("192.168.1.1/32")

        self.assertEqual(resultado["hosts_disponiveis"], 1)

    def test_ip_invalido(self):
        with self.assertRaises(ValueError):
            calcular_ip("999.168.1.10/24")

    def test_ipv6_nao_permitido(self):
        with self.assertRaises(ValueError):
            calcular_ip("2001:db8::1/64")


if __name__ == "__main__":
    unittest.main()
