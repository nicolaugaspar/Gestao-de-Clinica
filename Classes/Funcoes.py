import os.path
import pickle

from Classes.Consultas import Consulta
from Classes.DataHora import Data, Hora
from Classes.Especialidades import Especialidade
from Classes.Pessoa_Medico_Paciente import Medico, Paciente


# FUNÇÕES UTEIS
class Funcoes:

    # region FUNÇÕES UTEIS
    @staticmethod
    def pedeIntMinMax(prompt, min, max):
        num = min - 1
        while num < min or num > max:
            num = int(input(prompt))
            if num < min or num > max:
                print(" Insira um número entre ", min, " e ", max)
        return num

    @staticmethod
    def pedeIntMin(prompt, min):
        num = min - 1
        while num < min:
            num = int(input(prompt))
            if num < min:
                print(" Insira um número a partir de ", min, ": ")
        return num

    @staticmethod
    def pedeString(prompt):
        return input(prompt)

    @staticmethod
    def pedeData(prompt):
        print(prompt)
        dia = Funcoes.pedeIntMinMax("Insira o dia: ", 1, 31)
        mes = Funcoes.pedeIntMinMax("Insira o mês: ", 1, 12)
        ano = Funcoes.pedeIntMin("Insira o ano: ", 1900)
        return Data(dia, mes, ano)

    @staticmethod
    def pedeHora(prompt):
        print(prompt)
        hora = Funcoes.pedeIntMinMax("Insira a hora: ", 0, 23)
        minuto = Funcoes.pedeIntMinMax("Insira os minutos: ", 0, 59)
        return Hora(hora, minuto)

    @staticmethod
    def pausa():
         input("Prima Enter para continuar")
    # endregion FUNÇÕES UTEIS

    # region FUNÇÕES PARA A ESPECIALIDADE
    # FUNÇÕES PARA A ESPECIALIDADE
    #VALIDAÇÕES
    @staticmethod
    def validarEspecialidades(lista_Especialidades, nomeEspecialidade):
        for especialidade in lista_Especialidades:
            if especialidade.getNomeEspecialidade().strip(" ").lower() == nomeEspecialidade.strip(" ").lower():
                return 0
        return 1
    # endregion FUNÇÕES PARA A ESPECIALIDADE

    # region MENU ESPECIALIDADES --> 1 - CRIAR ESPECIALIDADES
    #MENU ESPECIALIDADES --> 1 - CRIAR ESPECIALIDADES
    @staticmethod
    def criarEspecialidade(contadorEspecialidades, lista_Especialidades ):
        idEspecialidade = contadorEspecialidades + 1

        nomeEspecialidade = Funcoes.pedeString(" Insira o nome da nova Especialidade: ")

        if Funcoes.validarEspecialidades(lista_Especialidades, nomeEspecialidade) == 0:
            return None
        precoEspecialidade = Funcoes.pedeIntMin(" Insira o valor da consulta da " + nomeEspecialidade + ": ", 0)

        print(" Especialidade criada com sucesso!")

        return Especialidade(idEspecialidade, nomeEspecialidade, precoEspecialidade)
    # endregion MENU ESPECIALIDADES --> 1 - CRIAR ESPECIALIDADES

    # region MENU ESPECIALIDADES --> 2 - LISTAR ESPECIALIDADES
    #MENU ESPECIALIDADES --> 2 - LISTAR ESPECIALIDADES
    @staticmethod
    def listarEspecialidades(lista_Especialidades):
        if len(lista_Especialidades) == 0:
            print("Não existem especialidades registadas!")
            return
        print("LISTA ESPECIALIDADES")
        for especialidade in lista_Especialidades:
            print(especialidade)

    # endregion MENU ESPECIALIDADES --> 2 - LISTAR ESPECIALIDADES

    # region MENU ESPECIALIDADES --> 3 - ALTERAR PREÇO CONSULTAS
    #MENU ESPECIALIDADES --> 3 - ALTERAR PREÇO CONSULTAS
    @staticmethod
    def atualizarPreco(lista_Especialidades):
        if len(lista_Especialidades) == 0:
            print("Não existem especialidades registadas!")
            return

        Funcoes.listarEspecialidades(lista_Especialidades)
        idEspecialidade = Funcoes.pedeIntMinMax("Qual e especialidade que pretende alterar o preço?: ", 1, len(lista_Especialidades))
        posicao = idEspecialidade -1
        especialidade = lista_Especialidades[idEspecialidade - 1]
        novoPreco = Funcoes.pedeIntMin("Insira o novo valor para a " + especialidade.getNomeEspecialidade() + ": ", 0)
        lista_Especialidades[posicao].atualizarPreco(novoPreco)
        print("Preço actualizado com sucesso!")
    # endregion MENU ESPECIALIDADES --> 3 - ALTERAR PREÇO CONSULTAS

    # region MENU ESPECIALIDADES --> 4 - TOTAIS POR ESPECIALIDADES
    #MENU ESPECIALIDADES --> 4 - TOTAIS POR ESPECIALIDADES
    @staticmethod
    def listaTotaisEspecialidade(lista_Especialidades, lista_Consultas):
        if len(lista_Especialidades) == 0:
            print("Ainda não foram registadas especialidades.")
            return
        if len(lista_Consultas) == 0:
            print("Ainda não foram registadas consultas.")
            return
        for especialidade in lista_Especialidades:
            total = 0
            for consulta in lista_Consultas:
                if consulta.getIdEspecialidade == especialidade.getIdEspecialidade():
                    if consulta.getValor() >= 0:
                        total += consulta.getValor()
            message = "Total da especialidade {}: {}€\n"
            message.format(especialidade.getNomeEspecialidade(), total)
            print(message)

# endregion MENU ESPECIALIDADES --> 4 - TOTAIS POR ESPECIALIDADES

    # region FUNÇÕES PARA MÉDICOS
    # FUNÇÕES PARA MÉDICOS
    # VALIDAÇÕES MÉDICOS
    @staticmethod
    def validarMedicos(info, lista_Medicos, op):
        for medico in lista_Medicos:
            if op == 1:
                nif = info
                if medico.getNif() == nif:
                    print("Nif já registado!")
                    return 0
            if op == 2:
                telefone = info
                if medico.getTelefone() == telefone:
                    print("Telefone já registado!")
                    return 0
            if op == 3:
                numOrdMedicos = info
                if medico.getNumOrdMedicos() == numOrdMedicos:
                    print("Nº Ordem Médicos já registado!")
                    return 0
        return 1
    # endregion FUNÇÕES PARA MÉDICOS

    # region MENU MÉDICO --> 1 - CRIAR MÉDICO
    # MENU MÉDICO --> 1 - CRIAR MÉDICO
    @staticmethod
    def criarMedico(contadorMedicos, lista_Especialidades, lista_Medicos):
        if len(lista_Especialidades) == 0:
            print("Necessário criar ESPECIALIDADES!")
            return None
        idMedico = contadorMedicos + 1
        nif = Funcoes.pedeIntMin(" Insira NIF do NOVO Médico: ", 0)
        if Funcoes.validarMedicos(nif, lista_Medicos, 1) == 0:
            return None
        telefone = Funcoes.pedeIntMin(" Insira TELEFONE do NOVO Médico: ", 0)
        if Funcoes.validarMedicos(telefone, lista_Medicos, 2) == 0:
            return None
        numOrdMedicos = Funcoes.pedeIntMin(" Insira número cédula profissional: ", 0)
        if Funcoes.validarMedicos(numOrdMedicos, lista_Medicos, 3) == 0:
            return None
        nome = Funcoes.pedeString(" Insira o NOME do NOVO Médico: ")
        morada = Funcoes.pedeString(" Insira MORADA do NOVO Médico: ")
        #Mostrar lista de especialidades para poderem escolher de seguida
        Funcoes.listarEspecialidades(lista_Especialidades)
        idEspecialidade = Funcoes.pedeIntMinMax(" Insira especialidade: ", 1, len(lista_Especialidades))
        #Vamos verificar atravez do id da especialidade o nome da especialidade e acrescentar no Medico
        nomeEspecialidade = ""
        for especialidade in lista_Especialidades:
            if especialidade.getIdEspecialidade() == idEspecialidade:
                nomeEspecialidade = especialidade.getNomeEspecialidade()
        dataAdm = Funcoes.pedeData(" Insira data admissão do novo médico: ")
        print(" Novo MÉDICO criado com sucesso!")
        return Medico(nome, nif, morada, telefone, idMedico, numOrdMedicos, idEspecialidade, nomeEspecialidade, dataAdm)

# endregion MENU MÉDICO --> 1 - CRIAR MÉDICO

    # region MENU MÉDICOS --> 2 - ATUALIZAR MÉDICO
    # MENU MÉDICOS --> 2 - ATUALIZAR MÉDICO

    @staticmethod
    def listarMedicos(lista_Medicos):
        if len(lista_Medicos) == 0:
            print("Não exixte MÉDiCOS registados!")
            return
        for medico in lista_Medicos:
            print(medico.getIdMedico(), ":\n")
            print("LISTA MÉDICOS\n")
            for medico in lista_Medicos:
                print(medico)

    @staticmethod
    def atualizarMedico(lista_Medicos, lista_Especialidades):
        if len(lista_Medicos) == 0:
            print("Não exixte MÉDiCOS registados!")
            return
        Funcoes.listarMedicos(lista_Medicos)
        idMedico = Funcoes.pedeIntMinMax("ID médico a alterar: ", 1, len(lista_Medicos))
        posicao = idMedico - 1
        medico = lista_Medicos[posicao]

        # region ALTERAR NOME MÉDICO
        # ALTERAR NOME
        op = Funcoes.pedeIntMinMax("Pretende alterar o nome (" + medico.getNome() + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            nome = Funcoes.pedeString("Insira o nome: ")
        else:
            nome = medico.getNome()
        # ALTERAR NIF
        op = Funcoes.pedeIntMin("Pretende alterar o NIF(" + str(medico.getNif()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0)
        if op == 1:
            nif = Funcoes.pedeString("Insira o NIF: ")
            if Funcoes.validarMedicos(nif, lista_Medicos, 1) == 0:
                print("NIF não pode ser alterado!")
                nif = medico.getNif()
        else:
            nif = medico.getNif()
        # endregion

        # region ALTERAR MORADA MÉDICO
        # ALTERAR MORADA
        op = Funcoes.pedeIntMinMax("Pretende alterar morada (" + medico.getMorada() + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            morada = Funcoes.pedeString("Insira a nova morada: ")
        else:
            morada = medico.getMorada()
        # endregion ALTERAR MORADA MÉDICO

        # region ALTERAR TELEFONE
        # ALTERAR TELEFONE
        op = Funcoes.pedeIntMin("Pretende alterar o Telefone(" + str(medico.getTelefone()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0)
        if op == 1:
            telefone = Funcoes.pedeString("Insira o NIF: ")
            if Funcoes.validarMedicos(telefone, lista_Medicos, 2) == 0:
                print("Telefone não pode ser alterado!")
                telefone = medico.getTelefone()
        else:
            telefone = medico.getTelefone()
        # endregion ALTERAR TELEFONE

        # region ALTERAR Nº ORDEM MÉDICOS
        # ALTERAR Nº ORDEM MÉDICOS
        op = Funcoes.pedeIntMin("Pretende alterar o nº Ordem dos Médicos(" + str(medico.getNumOrdMedicos()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0)
        if op == 1:
            numOrdMedicos = Funcoes.pedeString("Insira o NIF: ")
            if Funcoes.validarMedicos(numOrdMedicos, lista_Medicos, 2) == 0:
                print("Nº Ordem Médicos não pode ser alterado!")
                numOrdMedicos = medico.getNumOrdMedicos()
        else:
            numOrdMedicos = medico.getNumOrdMedicos()
        # endregion ALTERAR Nº ORDEM MÉDICOS

        # region ALTERAR ESPECIALIDADE NO MÉDICO
        # ALTERAR ESPECIALIDADE NO MÉDICO
        op = Funcoes.pedeIntMinMax("Pretende alterar o ESPECIALIDADE (" + medico.getNomeEspecialidade()+ ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            Funcoes.listarEspecialidades(lista_Especialidades)
            idEspecialidade = Funcoes.pedeIntMinMax("Insira o ID Especialidade: ", 1, len(lista_Especialidades))
            nomeEspecialidade = ""
            for especialidade in lista_Especialidades:
                if especialidade.getIdEspecialidade == idEspecialidade:
                    nomeEspecialidade = especialidade.getNomeEspecialidade
                    break
        else:
            idEspecialidade = medico.getIdEspecialidade()
            nomeEspecialidade = medico.getNomeEspecialidade()
        # endregion ALTERAR ESPECIALIDADE NO MÉDICO

        # region ALTERAR MORADA NO MÉDICO
        # ALTERAR MORADA NO MÉDICO
        op = Funcoes.pedeIntMinMax("Pretende alterar data admissão (" + str(medico.getDataAdmissao()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            dataAdmissao = Funcoes.pedeData("Insira a nova morada: ")
        else:
            dataAdmissao = medico.getDataAdmissao()
        # endregion ALTERAR MORADA NO MÉDICO

        # region atualiza toodos os dados alterados
        # Aqui atualiza toodos os dados alterados
        lista_Medicos[posicao].atualizar(nome, nif, morada, telefone, numOrdMedicos, idEspecialidade, nomeEspecialidade, dataAdmissao)
        print(" Alterações com sucesso!")
       # endregion atualiza toodos os dados alterados

    # region MENU MÉDICOS --> 3 LISTAR MÉDICOS POR ESPECIALIDADES

    # MENU MÉDICOS --> 3 LISTAR MÉDICOS POR ESPECIALIDADES
    @staticmethod
    def listaMedicosEspecialidade(lista_Medicos, lista_Especialidades):
        if len(lista_Medicos) == 0:
            print("Não exixte MÉDICOS registados!")
            return

        mensagem = ""
        for especialidade in lista_Especialidades:

            mensagem += "ESPECIALIDADE: " + especialidade.getNomeEspecialidade()

            mensagem += ("LISTA MÉDICOS\n")
            for medico in lista_Medicos:
                if medico.getIdEspecialidade() == especialidade.getIdEspecialidade():

                    mensagem += str(medico) + "\n"

            mensagem += "\n"
        print(mensagem)

        op = Funcoes.pedeIntMinMax("Pretende exportar para ficheiro os dados?  Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 0:
            return
        else:
            with open("Lista_Medicos_Especialidade.txt", "w") as f:
                f.write(mensagem)
    # endregion MENU MÉDICOS --> 3 LISTAR MÉDICOS POR ESPECIALIDADES

    # region FUNÇÕES PARA PACIENTES
    # FUNÇÕES PARA PACIENTES
    # VALIDAÇÕES PACIENTES
    @staticmethod
    def validarPacientes(info, lista_Pacientes, op):
        for paciente in lista_Pacientes:
            if op == 1:
                nif = info
                if paciente.getNif() == nif:
                    print("Nif já registado!")
                    return 0
            if op == 2:
                nCC = info

            if op == 3:
                nSNS = info
                if paciente.getnSNS() == nSNS:
                    print("Nº Sistema Nacional de Saúde já registado!")
                    return 0
    # endregion FUNÇÕES PARA PACIENTES

    # region MENU PACIENTES --> 1 - CRIAR PACIENTE
    # MENU PACIENTES --> 1 - CRIAR PACIENTE
    @staticmethod
    def criarPaciente(contadorPacientes, lista_Pacientes, lista_Medicos):
        if len(lista_Medicos) == 0:
            print("Não exixtem MÉDiCOS registados!")
            return
        idPaciente = contadorPacientes + 1

        nif = Funcoes.pedeIntMin(" Insira NIF do NOVO Paciente: ", 0)
        if Funcoes.validarPacientes(nif, lista_Pacientes, 1) == 0:
            return None
        nCC = Funcoes.pedeIntMin(" Insira Cartão Cidadão nº: ", 0)
        if Funcoes.validarPacientes(nCC, lista_Pacientes, 2) == 0:
            return None
        nSNS = Funcoes.pedeIntMin(" Insira Número SNS do NOVO Paciente: ", 0)

        if Funcoes.validarPacientes(nSNS, lista_Pacientes, 3) == 0:
            return None
        # ASSOCIAR MÉDICO A PACIENTE
        for medico in lista_Medicos:
            print(medico)
        idMedico = Funcoes.pedeIntMinMax(" Insira ID do Médico para paciente: ", 1, len(lista_Medicos))

        nome = Funcoes.pedeString(" Insira o NOME do NOVO Paciente: ")
        morada = Funcoes.pedeString(" Insira MORADA do NOVO Paciente: ")
        telefone = Funcoes.pedeIntMin(" Insira TELEFONE do NOVO Paciente: ", 0)
        dataNasc = Funcoes.pedeData(" Insira Data Nascimento do NOVO Paciente: ")
        print(" NOVO PACIENTE criado com sucesso!")
        return Paciente(nome, nif, morada, telefone, idPaciente, dataNasc, nCC, nSNS, idMedico)
    # endregion MENU PACIENTES --> 1 - CRIAR PACIENTE

    # region MENU PACIENTES --> 2 - ATUALIZAR PACIENTES
    # MENU PACIENTES --> 2 - ATUALIZAR PACIENTES

    @staticmethod
    def atualizarPaciente(lista_Pacientes, lista_Medicos):
        if len(lista_Pacientes) == 0:
            print("Não exixte PACIENTES registados!")
            return
        Funcoes.listarPacientes(lista_Pacientes)
        idPaciente = Funcoes.pedeIntMinMax("ID paciente a alterar: ", 1, len(lista_Pacientes))
        posicao = idPaciente - 1
        paciente = lista_Pacientes[posicao]

        nomeMedico = ""
        for medico in lista_Medicos:
            if medico.getIdMedico() == paciente.getIdMedico():
                nomeMedico = medico.getNome()

        # region ALTERAR NOME PACIENTE
        # ALTERAR NOME PACIENTE
        op = Funcoes.pedeIntMinMax("Pretende alterar o nome (" + paciente.getNome() + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            nome = Funcoes.pedeString("Insira o nome: ")
        else:
            nome = paciente.getNome()
        # endregion ALTERAR NOME PACIENTE

        # region ALTERAR NIF PACIENTE
        # ALTERAR NIF PACIENTE
        op = Funcoes.pedeIntMin("Pretende alterar o NIF(" + str(paciente.getNif()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0)
        if op == 1:
            nif = Funcoes.pedeString("Insira o NIF: ")
            if Funcoes.validarPacientes(nif, lista_Pacientes, 1) == 0:
                print("NIF não pode ser alterado!")
                nif = paciente.getNif()
        else:
            nif = paciente.getNif()
        # endregion ALTERAR NIF PACIENTE

        # region ALTERAR MORADA PACIENTE
        # ALTERAR MORADA PACIENTE
        op = Funcoes.pedeIntMinMax("Pretende alterar morada (" + paciente.getMorada() + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            morada = Funcoes.pedeString("Insira a nova morada: ")
        else:
            morada = paciente.getMorada()
        # endregion ALTERAR MORADA PACIENTE

        # region ALTERAR TELEFONE PACIENTE
        # ALTERAR TELEFONE PACIENTE
        op = Funcoes.pedeIntMin("Pretende alterar o Telefone(" + str(paciente.getTelefone()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0)
        if op == 1:
            telefone = Funcoes.pedeString("Insira o Telefone: ")
        else:
            telefone = paciente.getTelefone()
        # endregion ALTERAR TELEFONE PACIENTE

        # region ALTERAR DATA NASCIMENTO PACIENTE
        # ALTERAR DATA NASCIMENTO PACIENTE
        op = Funcoes.pedeIntMinMax("Pretende alterar o data nascimento(" + str(paciente.getDataNasc()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            dataNasc = Funcoes.pedeData("Insira a nova Data Nasc: ")
        else:
            dataNasc = paciente.getDataNasc()
        # endregion ALTERAR DATA NASCIMENTO PACIENTE

        # region ALTERAR nCC PACIENTE
        # ALTERAR nCC
        op = Funcoes.pedeIntMinMax("Pretende alterar o Cartão Cidadão(" + str(paciente.getnCC()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            nCC = Funcoes.pedeString("Insira o CC: ")
            if Funcoes.validarPacientes(nCC, lista_Pacientes, 1) == 0:
                print("CC não pode ser alterado já existe!")
                nCC = paciente.getnCC()
        else:
            nCC = paciente.getnCC()
        # endregion ALTERAR nCC PACIENTE

        # region ALTERAR Nº UTENTE
        # ALTERAR Nº UTENTE

        op = Funcoes.pedeIntMinMax("Pretende alterar o SNS nº  (" + str(paciente.getnCC()) + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            nSNS = Funcoes.pedeIntMin("Insira o SNS: ", 0)
            if Funcoes.validarPacientes(nSNS, lista_Pacientes, 1) == 0:
                print("CC não pode ser alterado já existe!")
                nSNS = paciente.getnSNS()
        else:
            nSNS = paciente.getnSNS()
        # endregion ALTERAR Nº UTENTE

        # region ALTERAR NOME MÉDICO NO PACIENTE
        # ALTERAR NOME MÉDICO NO PACIENTE
        op = Funcoes.pedeIntMinMax("Pretende alterar o médico (" + nomeMedico + ")? Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 1:
            Funcoes.listarMedicos(lista_Medicos)
            idMedico = Funcoes.pedeIntMinMax("Insira ID do médico: ", 0, len(lista_Medicos))
        else:
            idMedico = paciente.getIdMedico()
        # endregion ALTERAR NOME MÉDICO NO PACIENTE

        # region ATUALIZA DADOS DO PACIENTE
        # Aqui atualiza todos os dados alterados
        lista_Pacientes[posicao].atualizar(nome, nif, morada, telefone, dataNasc, nCC, nSNS, idMedico)
        print(" Alterações com sucesso!")
        # endregion ATUALIZA DADOS DO PACIENTE
# endregion MENU PACIENTES --> 2 - ATUALIZAR PACIENTES

    # region MENU PACIENTES --> 3 - LISTAR PACIENTES
    # MENU PACIENTES --> 3 -  LISTAR PACIENTES
    @staticmethod
    def listarPacientes(lista_Pacientes):
        def criterio(e):
            return e.getNome()
        if len(lista_Pacientes) == 0:
            print("Não exixtem PACIENTES registados!")
            return
        listaOrdenada = lista_Pacientes.copy()
        listaOrdenada.sort(key=criterio)
        for paciente in listaOrdenada:
            print(paciente , "\n")
# endregion MENU PACIENTES --> 3 - LISTAR PACIENTES

    # region MENU PACIENTES --> 4 - CONSULTAR PACIENTES POR MÉDICO
    # MENU PACIENTES --> 4 - CONSULTAR PACIENTES POR MÉDICO
    @staticmethod
    def listaPacientesMedico(lista_Pacientes, lista_Medicos):
        if len(lista_Pacientes) == 0:
            print("Não exixtem PACIENTES registados!")
            return
        for medico in lista_Medicos:
            print(medico)
        idMedico = Funcoes.pedeIntMinMax(" Insira o ID do Médico: ", 1, len(lista_Medicos))
        encontrado = False
        for paciente in lista_Pacientes:
            if paciente.getIdMedico() == idMedico:
                print("Nome" + paciente.getNome() + " >> Data Nasc.: " + str(paciente.getDataNasc()))
                encontrado = True
        if not encontrado:
            print("Este médico não tem pacientes associados")
    # endregion MENU PACIENTES --> 4 - CONSULTAR PACIENTES POR MÉDICO

    # region MENU PACIENTES --> 5 - CONSULTAR PACIENTES
    # MENU PACIENTES --> 5 - CONSULTAR PACIENTES
    # region MENU PACIENTES --> 5.1 - CONSULTAR PACIENTES NIF
        # MENU PACIENTES --> 5.1 - CONSULTAR PACIENTES NIF
    @staticmethod
    def consultarPacienteNif (lista_Pacientes):
        nif = Funcoes.pedeIntMin(" Insira o Nif do paciente: ", 0)
        for paciente in lista_Pacientes:
            if paciente.getNif() == nif:
                print(paciente)
                return
    # endregion MENU PACIENTES --> 5.1 - CONSULTAR PACIENTES NIF

    # region MENU PACIENTES --> 5.2 - CONSULTAR PACIENTES CC
        # MENU PACIENTES --> 5.2 - CONSULTAR PACIENTES CC
    @staticmethod
    def consultarPacienteNCC (lista_Pacientes):
        nCC = Funcoes.pedeIntMin(" Insira o Nº Cartão Cidadão do paciente: ", 0)
        for paciente in lista_Pacientes:
            if paciente.getnCC() == nCC:
                print(paciente)
                return
    # endregion MENU PACIENTES --> 5.2 - CONSULTAR PACIENTES CC

    #region MENU PACIENTES --> 5.3 - CONSULTAR PACIENTES SNS
        # MENU PACIENTES --> 5.3 - CONSULTAR PACIENTES SNS
    @staticmethod
    def consultarPacienteNSNS (lista_Pacientes):
        nSNS = Funcoes.pedeIntMin(" Insira o Nº Sistema Nacional Saúde do paciente: ", 0)
        for paciente in lista_Pacientes:
            if paciente.getnSNS() == nSNS:
                print(paciente)
                return
    #endregion MENU PACIENTES --> 5.3 - CONSULTAR PACIENTES SNS
# endregion MENU PACIENTES --> 5 - CONSULTAR PACIENTES

    # region FUNÇÕES PARA CONSULTAS
    # FUNÇÕES PARA CONSULTAS


    # endregion FUNÇÕES PARA CONSULTAS

    # region MENU CONSULTAS --> 1 - CRIAR CONSULTA
    # VERIFICAÇÃO DE PACIENTES ,  MÉDICOS E ESPECIALIDADES
    @staticmethod
    def criarConsulta(contadorConsultas, lista_Pacientes, lista_Medicos, lista_Especialidades):
        if len(lista_Pacientes) == 0:
            print("Não exitem pacientes registados!")
            return None
        elif len(lista_Medicos) == 0:
            print("Não exitem médicos registados!")
            return None
        elif len(lista_Especialidades) == 0:
            print("Não exitem especialidades registadas!")
            return None

        idConsulta = contadorConsultas + 1

        # PEDIR PACIENTE
        for paciente in lista_Pacientes:
            print(paciente)
        idPaciente = Funcoes.pedeIntMinMax("Insira o ID do paciente:", 1, len(lista_Pacientes))
        nomePaciente = ""
        idMedico = ""
        for paciente in lista_Pacientes:
            if paciente.getIdPaciente() ==idPaciente:
                nomePaciente = paciente.getNome()
                idMedico = paciente.getIdMedico()
                break

        # DEFINIR MÉDICO e ESPECIALIDADE (CONSULTA)
        nomeMedico = ""
        idEspecialidade = 0
        especialidade = ""
        for medico in lista_Medicos:
            if medico.getIdMedico() == idMedico:
                nomeMedico = medico.getNome()
                idEspecialidade = medico.getIdEspecialidade()
                especialidade = medico.getNomeEspecialidade()

        # PEDIR RESTANTES DADOS DA CONSULTA
        dataConsulta = Funcoes.pedeData(" Insira DATA da NOVA Consulta ")
        horaConsulta = Funcoes.pedeHora(" Insira HORA da NOVA Consulta ")

        print("=== MARCAÇÃO da CONSULTA ====")
        print("\nIrá ser criada uma consulta de " + especialidade + " para o paciente " + nomePaciente
              + " com o médico " + nomeMedico + ", dia " + str(dataConsulta) + " às " + str(horaConsulta) + ".")
        op = Funcoes.pedeIntMinMax("Marcar consulta com estes dados?  Sim = 1 / Não = 0 \n Opção: ", 0, 1)
        if op == 0:
            print("Marcação CANCELADA!")
            return None

        print(" Nova CONSULTA criada com sucesso!")
        return Consulta(idConsulta, idMedico, nomeMedico, idEspecialidade, idPaciente, nomePaciente, especialidade, dataConsulta, horaConsulta)
# endregion MENU CONSULTAS --> 1 - CRIAR CONSULTA

    # region MENU CONSULTAS --> 2 - ATUALIZAR CONSULTA
    # MENU CONSULTAS --> 2 - ATUALIZAR CONSULTA
    @staticmethod
    def realizarConsulta(lista_Consultas, lista_Especialidades):
        # region PEDIR CONSULTA
        Funcoes.listarConsultasMarcadas(lista_Consultas)
        consultaValida = False
        consulta = None
        pos = 0
        while not consultaValida:
            idConsulta = Funcoes.pedeIntMinMax("Qual a consulta que pretende realizar?", 1, len(lista_Consultas))
            for i in range (len(lista_Consultas)):
                consulta = lista_Consultas[i]
                if consulta.getIdConsulta() == idConsulta:
                    if consulta.getValor() >= 0:
                        print("Selecione uma consulta válida!")
                        break
                    else:
                        pos = i
                        consultaValida = True
                        break
        # endregion
        # region DEFINIR VALOR DA CONSULTA
        valor = -1
        for especialidade in lista_Especialidades:
            if consulta.getIdEspecialidade() == especialidade.getIdEspecialidade():
                valor = especialidade.getPreco()
        # endregion
        # region PEDIR DATA E METODO DE PAGAMENTO
        dataPagamento = Funcoes.pedeData("Insira data de realização da consulta")
        op = Funcoes.pedeIntMinMax("Pagamento em dinheiro (1), multibanco (2) ou cheque (3)?", 1, 3)
        if op == 1:
            tipoPagamento = "Dinheiro"
        elif op == 2:
            tipoPagamento = "Multibanco"
        else:
            tipoPagamento = "Cheque"
        # endregion
        # region CONFIRMAÇÃO
        print(consulta)
        print("Realizada a " + str(dataPagamento) + ", " + str(valor) + " pagos com " + tipoPagamento + ".")
        op = Funcoes.pedeIntMinMax("Dar a consulta como realizada com estes dados? Sim = 1, Não = 0\nOpção: ", 0, 1)

        if op == 0:
            print("Operação cancelada.")
            return
        # endregion
        lista_Consultas[pos].atualizarConsulta(valor, dataPagamento, tipoPagamento)
# endregion MENU CONSULTAS --> 2 - ATUALIZAR CONSULTA

    # region MENU CONSULTAS --> 3 - LISTAR CONSULTAS MARCADAS
# MENU CONSULTAS --> 3 - LISTAR CONSULTAS MARCADAS
    @staticmethod
    def listarConsultasMarcadas(lista_Consultas):
        if len(lista_Consultas) == 0:
            print("Ainda não foram marcadas consultas!")
            return None
        print("Consultas marcadas:")
        for consulta in lista_Consultas:
            if consulta.getValor() < 0:
                print(consulta , "\n")
# endregion MENU CONSULTAS --> 3 - ISTAR CONSULTAS MARCADAS

    # region MENU CONSULTAS --> 4 - LISTAR CONSULTAS MARCADAS DE UM MÉDICO
    # MENU CONSULTAS --> 4 - LISTAR CONSULTAS MARCADAS DE UM MÉDICO
    @staticmethod
    def listarConsultasMedico(lista_Consultas, lista_Medicos):
        for medico in lista_Medicos:
            print(medico)
        idMedico = Funcoes.pedeIntMinMax("Insira o ID do méico a consultar: ", 1, len(lista_Medicos))



        print("Consultas marcadas:")
        for consulta in lista_Consultas:
            if consulta.getIdMedico() == idMedico:
                print(consulta, "\n")
    # endregion MENU CONSULTAS --> 4 - ISTAR CONSULTAS MARCADAS DE UM MÉDICO

    # region MENU CONSULTAS --> 5 - LISTAR CONSULTAS ESPECIALIDADES
    # MENU CONSULTAS --> 5 - LISTAR CONSULTAS ESPECIALIDADES
    @staticmethod
    def listarConsultasEspecialidade(lista_Consultas, lista_Especialidades):
        for especialidade in lista_Especialidades:
            print(especialidade)
        idEspecialidade = Funcoes.pedeIntMinMax("Insira o ID da especialidade a consultar: ", 1, len(lista_Especialidades))



        print("Consultas marcadas:")
        for consulta in lista_Consultas:
            if consulta.getIdEspecialidade() == idEspecialidade:
                print(consulta, "\n")
# endregion MENU CONSULTAS --> 5 - LISTAR CONSULTAS ESPECIALIDADES

    # region MENU CONSULTAS --> 6 - LISTAR HISTÓRICO PACIENTES
    # MENU CONSULTAS --> 6 - LISTAR HISTÓRICO PACIENTES
    @staticmethod
    def listarHistoricoPaciente(lista_Consultas, lista_Pacientes):
        for paciente in lista_Pacientes:
            print(paciente)
        idpaciente = Funcoes.pedeIntMinMax("Insira o ID do paciente a consultar: ", 1, len(lista_Pacientes))

        print("Consultas marcadas:")
        for consulta in lista_Consultas:
            if consulta.getIdPaciente() == idpaciente:
                print(consulta, "\n")
    # endregion MENU CONSULTAS --> 6 - LISTAR HISTÓRICO PACIENTES


    # region FICHEIROS


    @staticmethod
    def carregaDados():
        if os.path.exists("dados.bin"):
            with open("dados.bin", "rb") as f:
                return pickle.load(f)
        else:
            return {}
    @staticmethod
    def guardarDados(dados):
        with open("dados.bin", "wb") as f:
            pickle.dump(dados, f)

    # endregionFICHEIROS
