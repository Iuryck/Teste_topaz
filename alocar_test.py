import unittest
import os
from alocar import Alocator as aloc


class TestAlocador(unittest.TestCase, aloc):

    #Testando se variáveis foram iniciados corretamente
    def test_init(self):
        alocador = aloc()

        
        self.assertEqual([], alocador.users_ttask, "Should be []")
        self.assertEqual([], alocador.users_per_server, "Should be []")
        self.assertEqual([], alocador.servers, "Should be []")
        self.assertEqual([], alocador.servers, "Should be 0")

    #Testando os erros levantados na função read_input
    def test_read_error(self):
        

        os.rename('input.txt','input1.txt')
        alocador = aloc()
        
        self.assertRaises(FileNotFoundError, lambda: alocador._read_input())
        os.rename('input1.txt','input.txt')

        alocador = aloc()
        with open('input.txt', 'w') as input:
            input.write(f'11\n2\n1\n3\n0\n1\n0\n1')
        
        self.assertRaises(ValueError, lambda: alocador._read_input())




    #Testando o cálculo de custo das VMs
    def test_cost(self):
        alocador = aloc()
        with open('input.txt', 'w') as input:
            input.write(f'4\n2\n1\n3\n0\n1\n0\n1')
        alocador.iterating_ticks()
        self.assertEqual(14, alocador.cost, "Should be 14")

    #Testando a leitura do arquivo input
    def test_input(self):
        alocador = aloc()
        with open('input.txt', 'w') as input:
            input.write(f'4\n2\n1\n3\n0\n1\n0\n1')
        alocador._read_input()
        self.assertEqual(2, alocador.umax, "Should be 2")
    
    #Testando se o output sai como esperado
    def test_output(self):
        alocador = aloc()
        with open('input.txt', 'w') as input:
            input.write(f'4\n2\n1\n3\n0\n1\n0\n1')
        alocador.iterating_ticks()
        output = ['1', '2, 2', '2, 2', '2, 2, 1', '2, 2', '2', '2', '1', '1', '14']
        input = open('output.txt', 'r')
        Lines = input.readlines()
        Lines = [c.strip() for c in Lines]
        self.assertEqual(output, Lines, f"Should be {output}")
        input.close()





if __name__ == '__main__':
    unittest.main()