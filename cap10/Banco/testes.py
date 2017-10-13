from cliente import Cliente
from contas import Conta
from bancos import Banco

laender = Cliente("Laender Morais", "991510701")
amanda = Cliente("Amanda Rodrigues", "998616813")
lea = Conta([la ender, amanda], 1234, 5000)
tatu = Banco("Tatu")
tatu.abre_conta(lea)
tatu.lista_contas()
