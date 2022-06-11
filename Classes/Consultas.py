# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:40:24 2022

@author: Utilizador
"""
from Classes.DataHora import Data, Hora


class Consulta:
    __idConsulta = 0
    __idMedico = 0
    __nomeMedico = 0
    __idEspecialidade = 0
    __idPaciente = 0
    __nomePaciente = 0
    __especialidade = ""
    __dataConsulta = Data(0, 0, 0)
    __horaConsulta = Hora(0, 0)
    __valor = -1
    __dataPagamento = Data(0, 0, 0)
    __tipoPagamento = ""
    def __init__(self, idConsulta, idMedico, nomeMedico, idEspecialidade, idPaciente, nomePaciente, especialidade, dataConsulta, horaConsulta):
        self.__idConsulta = idConsulta
        self.__idMedico = idMedico
        self.__nomeMedico = nomeMedico
        self.__idEspecialidade = idEspecialidade
        self.__idPaciente = idPaciente
        self.__nomePaciente = nomePaciente
        self.__especialidade = especialidade
        self.__dataConsulta = dataConsulta
        self.__horaConsulta = horaConsulta

    def __str__(self):

        message = "Consulta nº: {} "
        if self.__valor >= 0:
            message += "(REALIZADA) "
        message += "- {}\n"\
              "Data Consulta: {} às {}\n" \
              "Médico: {} (ID {})\n" \
              "Paciente: {} (ID {})\n"
        message = message.format(str(self.__idConsulta), self.__especialidade, str(self.__dataConsulta), self.__horaConsulta,
                                 self.__nomeMedico, str(self.__idMedico), self.__nomePaciente, str(self.__idPaciente))
        if self.__valor >= 0:
            message2 = " Pagamento: {} - {} - {}\n"
            message2 = message2.format(str(self.__dataPagamento), str(self.__valor), self.__tipoPagamento)
        else:
            message2 = ""
        return message + message2


    def getIdMedico(self):
        return self.__idMedico

    def getIdPaciente(self):
        return self.__idPaciente

    def getIdConsulta(self):
        return self.__idConsulta

    def getIdEspecialidade(self):
        return self.__idEspecialidade

    def getValor(self):
        return self.__valor





    def atualizarConsulta(self, valor, dataPagamento, tipoPagamento):
        self.__valor = valor
        self.__dataPagamento = dataPagamento
        self.__tipoPagamento = tipoPagamento