from Classes.Funcoes import Funcoes


class Menu:
    @staticmethod
    def menuPrincipal():
        print("+======================+")
        print("|        MENU          |")
        print("|======================|")
        print("| 1 - Especialidades   |")
        print("| 2 - Médicos          |")
        print("| 3 - Pacientes        |")
        print("| 4 - Consultas        |")
        print("|                      |")
        print("| 0 - Sair             |")
        print("+======================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 4)

    @staticmethod
    def menuEspecialidades():
        print("+==============================+")
        print("|         ESPECIALIDADES       |")
        print("|==============================|")
        print("| 1 - Criar Nova               |")
        print("| 2 - Listar Especialidades    |")
        print("| 3 - Atualizar Preço          |")
        print("| 4 - Totais por especialidade |")
        print("| 0 - Menu Principal           |")
        print("+==============================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 4)

    @staticmethod
    def menuMedicos():
        print("+======================================+")
        print("|               MÉDICOS                |")
        print("|======================================|")
        print("| 1 - Criar Novo Médico                |")
        print("| 2 - Atualizar Médico                 |")
        print("| 3 - Listar Médicos por Especialidade |")
        print("| 0 - Menu Principal                   |")
        print("+======================================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 3)

    @staticmethod
    def menuPacientes():
        print("+=================================+")
        print("|            PACIENTES            |")
        print("|=================================|")
        print("| 1 - Criar Novo Paciente         |")
        print("| 2 - Atualizar Paciente          |")
        print("| 3 - Listar Pacientes            |")
        print("| 4 - Listar Pacientes de Médico  |")
        print("| 5 - Consultar um Paciente       |")
        print("| 0 - Menu Principal              |")
        print("+=================================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 5)

    @staticmethod
    def menuConsultaPaciente():
        print("+========================================+")
        print("|           CONSULTAR PACIENTE           |")
        print("+========================================+")
        print("|1 - Por NIF                             |")
        print("|2 - Por Cartão de Cidadão               |")
        print("|3 - Por Nº de Utente                    |")
        print("|                                        |")
        print("|0 - Voltar ao menu anterior             |")
        print("+========================================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 3)

    @staticmethod
    def menuConsultas():
        print("+=========================================+")
        print("|               CONSULTAS                 |")
        print("|=========================================|")
        print("| 1 - Criar Nova Consulta                 |")
        print("| 2 - Atualizar Consulta                  |")
        print("| 3 - Listar todas Consultas Marcadas     |")
        print("| 4 - Listar Consultas um Médico          |")
        print("| 5 - Listar Consultas uma Especialidade  |")
        print("| 6 - Listar Histórico Paciente           |")
        print("| 0 - Menu Principal                      |")
        print("+=========================================+")
        return Funcoes.pedeIntMinMax("Opção: ", 0, 6)

