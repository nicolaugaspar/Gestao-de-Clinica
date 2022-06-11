# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:40:01 2022

@author: Utilizador
"""

from Classes.Funcoes import Funcoes
from Classes.Menu import Menu




# INICIO PROGRAMA
class Main:

    dados = Funcoes.carregaDados()
    if len(dados) == 0:
        lista_Especialidades = []
        lista_Medicos = []
        lista_Pacientes = []
        lista_Consultas = []

        contadorMedicos = 0
        contadorPacientes = 0
        contadorConsultas = 0
        contadorEspecialidades = 0
    else:
        lista_Especialidades = dados["listaEspecialidades"]
        lista_Medicos = dados["listaMedicos"]
        lista_Pacientes = dados["listaPacientes"]
        lista_Consultas = dados["listaConsultas"]

        contadorMedicos = dados["contadorMedicos"]
        contadorPacientes = dados["contadorPacientes"]
        contadorConsultas = dados["contadorConsultas"]
        contadorEspecialidades = dados["contadorEspecialidades"]


    op1 = -1
    while op1 != 0:
        op1 = Menu.menuPrincipal()
        if op1 == 0:
            print("Fechar Programa")
        if op1 == 1:
            op2 = -1
            while op2 != 0:
                op2 = Menu.menuEspecialidades()
                if op2 == 0:
                    print("Menu Principal")
                elif op2 == 1:
                    novaEspecialidade = Funcoes.criarEspecialidade(contadorEspecialidades, lista_Especialidades)
                    if novaEspecialidade is None:
                        pass
                    else:
                        lista_Especialidades.append(novaEspecialidade)
                        contadorEspecialidades += 1
                    Funcoes.pausa()
                elif op2 == 2:
                    Funcoes.listarEspecialidades(lista_Especialidades)
                    Funcoes.pausa()
                elif op2 == 3:
                    Funcoes.atualizarPreco(lista_Especialidades)
                    Funcoes.pausa()
                elif op2 == 4:
                    Funcoes.listaTotaisEspecialidade(lista_Especialidades, lista_Consultas)
                    Funcoes.pausa()

        if op1 == 2:
            op2 = -1
            while op2 != 0:
                op2 = Menu.menuMedicos()
                if op2 == 0:
                    print("Menu Principal")
                elif op2 == 1:
                    novoMedico = Funcoes.criarMedico(contadorMedicos, lista_Especialidades, lista_Medicos)
                    if novoMedico is None:
                        pass
                    else:
                        lista_Medicos.append(novoMedico)
                        contadorMedicos += 1
                    Funcoes.pausa()
                elif op2 == 2:
                    Funcoes.atualizarMedico(lista_Medicos, lista_Especialidades)

                    Funcoes.pausa()
                elif op2 == 3:
                    Funcoes.listaMedicosEspecialidade(lista_Medicos, lista_Especialidades)
                    Funcoes.pausa()

        if op1 == 3:

            op2 = -1
            while op2 != 0:
                op2 = Menu.menuPacientes()
                if op2 == 0:
                    print("Menu Principal")
                elif op2 == 1:
                    novoPaciente = Funcoes.criarPaciente(contadorPacientes, lista_Pacientes, lista_Medicos)
                    if novoPaciente is None:
                        pass
                    else:
                        lista_Pacientes.append(novoPaciente)
                        contadorPacientes += 1
                    Funcoes.pausa()
                elif op2 == 2:
                    Funcoes.atualizarPaciente(lista_Pacientes, lista_Medicos)
                    Funcoes.pausa()
                elif op2 == 3:
                    Funcoes.listarPacientes(lista_Pacientes)
                    Funcoes.pausa()
                elif op2 == 4:
                     Funcoes.listaPacientesMedico(lista_Pacientes, lista_Medicos)
                     Funcoes.pausa()
                elif op2 == 5:
                    op3 = -1
                    while op3 != 0:
                        op3 = Menu.menuConsultaPaciente()
                        if op3 == 0:
                            pass
                        elif op3 == 1:
                            Funcoes.consultarPacienteNif(lista_Pacientes)
                            Funcoes.pausa()
                        elif op3 == 2:
                            Funcoes.consultarPacienteNCC(lista_Pacientes)
                            Funcoes.pausa()
                        elif op3 == 3:
                            Funcoes.consultarPacienteNSNS(lista_Pacientes)
                            Funcoes.pausa()
        if op1 == 4:
            op2 = -1
            while op2 != 0:
                op2 = Menu.menuConsultas()
                if op2 == 0:
                    print("Menu Principal")
                elif op2 == 1:
                    novaConsulta = Funcoes.criarConsulta(contadorConsultas, lista_Pacientes, lista_Medicos, lista_Especialidades)
                    if novaConsulta is None:
                        pass
                    else:
                        lista_Consultas.append(novaConsulta)
                        contadorConsultas += 1
                    Funcoes.pausa()
                elif op2 == 2:
                    Funcoes.realizarConsulta(lista_Consultas, lista_Especialidades)
                    Funcoes.pausa()
                elif op2 == 3:
                    Funcoes.listarConsultasMarcadas(lista_Consultas)
                    Funcoes.pausa()
                elif op2 == 4:
                    Funcoes.listarConsultasMedico(lista_Consultas, lista_Medicos)
                    Funcoes.pausa()
                elif op2 == 5:
                    Funcoes.listarConsultasEspecialidade(lista_Consultas, lista_Especialidades)
                    Funcoes.pausa()
                elif op2 == 6:
                    Funcoes.listarHistoricoPaciente(lista_Consultas, lista_Pacientes)
                    Funcoes.pausa()



    dados = {"listaEspecialidades":lista_Especialidades,"listaMedicos":lista_Medicos,"listaPacientes":lista_Pacientes,"listaConsultas":lista_Consultas,
             "contadorEspecialidades":contadorEspecialidades,"contadorMedicos":contadorMedicos,"contadorPacientes":contadorPacientes,"contadorConsultas":contadorConsultas}
    Funcoes.guardarDados(dados)


