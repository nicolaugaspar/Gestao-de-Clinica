# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:01:45 2022

@author: Utilizador
"""
from Classes.DataHora import Data


class Pessoa:
    _nome = ""
    _nif = 0
    _morada = ""
    _telefone = 0
    def __init__(self, nome, nif, morada, telefone):

        self._nome = nome
        self._nif = nif
        self._morada = morada
        self._telefone = telefone

    def __str__(self):
        message = "Tipo: {}\nNome: {}\nNif: {}\nMorada: {}\nTelefone: {}\n"
        return message.format(type(self).__name__, self._nome, str(self._nif), self._morada, str(self._telefone))

    def getNome(self):
        return self._nome
    def getNif(self):
        return self._nif
    def getTelefone(self):
        return self._telefone
    def getMorada(self):
        return self._morada

class Medico(Pessoa):
    __idMedico = 0
    __numOrdMedicos = 0
    __idEspecialidade = 0
    __nomeEspecialidade = ""
    __dataAdmissao = Data(0, 0, 0)

    def __init__(self, nome, nif, morada, telefone, idMedico, numOrdMedicos, idEspecialidade, nomeEspecialidade, dataAdmissao):
        super().__init__(nome, nif, morada, telefone)
        self.__idMedico = idMedico
        self.__numOrdMedicos = numOrdMedicos
        self.__idEspecialidade = idEspecialidade
        self.__nomeEspecialidade = nomeEspecialidade
        self.__dataAdmissao = dataAdmissao

    def __str__(self):
        message = "Médico de {} ({}): {} (ID {})\n" \
                  "  NIF: {} ==> Telefone: {} ==> Morada: {}\n" \
                  "  Número da ordem: {} ==> Admitido a {}"
        return message.format(self.__nomeEspecialidade, str(self.__idEspecialidade), self._nome, str(self.__idMedico),
                              str(self._nif), str(self._telefone), self._morada,
                              str(self.__numOrdMedicos), str(self.__dataAdmissao))

    def getIdMedico(self):
        return self.__idMedico
    def getIdEspecialidade(self):
        return self.__idEspecialidade

    def getNumOrdMedicos(self):
        return self.__numOrdMedicos
    def getNomeEspecialidade(self):
        return self.__nomeEspecialidade
    def getDataAdmissao(self):
        return self.__dataAdmissao

    def atualizar(self, nome, nif, morada, telefone, numOrdMedicos, idEspecialidade, nomeEspecialidade, dataAdmissao):
        self._nome = nome
        self._nif = nif
        self._morada = morada
        self._telefone = telefone
        self.__numOrdMedicos = numOrdMedicos
        self.__idEspecialidade = idEspecialidade
        self.__nomeEspecialidade = nomeEspecialidade
        self.__dataAdmissao = dataAdmissao

class Paciente(Pessoa):

    __idPaciente = 0
    __dataNasc = Data(0, 0, 0)
    __nCC = 0
    __nSNS = 0
    __idMedico = 0
    def __init__(self, nome, nif, morada, telefone, idPaciente, dataNasc, nCC, nSNS, idMedico):
        super().__init__(nome, nif, morada, telefone)
        self.__idPaciente = idPaciente
        self.__dataNasc = dataNasc
        self.__nCC = nCC
        self.__nSNS = nSNS
        self.__idMedico = idMedico
    def __str__(self):
        message = "Paciente: {} (Nº {}), acompanhado por médico de ID {}\n" \
                  "  Nascido a: {} ==> Telefone: {} ==> Morada: {}\n" \
                  "  CC: {} ==> NIF: {} ==> Nº Utente: {}"
        return message.format(self._nome, str(self.__idPaciente), str(self.__idMedico),
                              str(self.__dataNasc), str(self._telefone), self._morada,
                              str(self.__nCC), str(self._nif), str(self.__nSNS))

    def getnCC(self):
        return self.__nCC

    def getnSNS(self):
        return self.__nSNS
    def getIdMedico(self):
        return self.__idMedico
    def getDataNasc(self):
        return self.__dataNasc
    def getIdPaciente(self):
        return self.__idPaciente

    def atualizar(self, nome, nif, morada, telefone, dataNasc, nCC, nSNS, idMedico):
        self._nome = nome
        self._nif = nif
        self._morada = morada
        self._telefone = telefone
        self.__dataNasc = dataNasc
        self.__nCC = nCC
        self.__nSNS = nSNS
        self.__idMedico = idMedico