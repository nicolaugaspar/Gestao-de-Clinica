# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:42:41 2022

@author: Utilizador
"""



class Especialidade:
    __idEspecialidade = 0
    __nomeEspecialidade = ""
    __preco = 0
    def __init__(self, idEspecialidade, nomeEspecialidade, preco):
        self.__idEspecialidade = idEspecialidade
        self.__nomeEspecialidade = nomeEspecialidade
        self.__preco = preco
    def __str__(self):        
        message = "Código Especialidade: {} ==> Nome Especialidade: {} ==> Preço Consulta: {}\n"
        return message.format(str(self.__idEspecialidade), self.__nomeEspecialidade, str(self.__preco))


    def getIdEspecialidade(self):
        return self.__idEspecialidade

    def getNomeEspecialidade(self):
        return self.__nomeEspecialidade
    def getPreco(self):
        return self.__preco
    def atualizarPreco(self, novoPreco):
        self.__preco = novoPreco
