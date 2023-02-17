class Elevador():
    
    """Sistema de elevador, com capacidade para 5 pessoas, em um prédio com 7 andares.
            Ele:    
                Não se movimentará para baixo se ja estiver no terreo.
                Não se movimentará para cima se ja estiver no ultimo andar.
                Calcula quantas pessoas ainda estão no elevador.
                Informa o andar em que o elevador está.
    """
    def __init__(self, capacidade, total_andares):
        self.__capacidade = capacidade
        self.__total_andares = total_andares
        self.andar_atual = 0
        self.total_pessoas = 0

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        self.__capacidade = capacidade

    def get_total_andares(self):
        return self.__total_andares

    def set_total_andares(self, total_andares):
        self.__total_andares = total_andares
        
    
    """Função para entrar no elevador, recebe o total de pessoas que desejam entrar e qual andar querem ir."""
    def entrar(self):
        print("\nNo elevador há {} pessoas, e seu máximo é 5.".format(self.total_pessoas))
        p_entrar = int(input("\nQuantas pessoas deseja(m) entrar? "))
        novquant = p_entrar + self.total_pessoas
        
        if novquant <= self.__capacidade:
            self.total_pessoas = novquant
            andar = int(input("\nDigite o número do andar desejado: "))
            if  (andar <= 7) and (andar > 0):
                print("\nO elevador está indo para o {}º andar.".format(andar))
                self.andar_atual = andar
                return self.sair()

            if (andar > self.__total_andares) or (andar < 0):
                print("\nNão há esse andar.")
            
            if andar == self.andar_atual:
                print("\nO elevador já está no {}º andar.".format(andar))
                self.andar_atual = andar
            
            
        else:
            print("Limite excedido!")
            

    """Função sair, recebe o total de pessoas que desejam sair, e apresenta quantas ainda restam e qual andar ainda está o elevador.."""
    def sair(self):
        p_sair = int(input("\nQuantas pessoas deseja sair? "))
        novquant = self.total_pessoas - p_sair
        if novquant > 0:
            self.total_pessoas = novquant
            print("\nRestaram {} pessoa(s) no elevador, ele está no {}º andar.".format(self.total_pessoas, self.andar_atual))
        else:
            print("\nNão há ninguém no elevador! Ele está no {}º andar.".format(self.andar_atual))
            
            
                
    """Função subir, para ir até o andar desejado"""
    def subir(self):
        if self.andar_atual < self.__total_andares:
            return self.entrar()
        else:
            print("\nO elevador está no último andar.")
            
            
            
            
    """Função descer, para ir até o andar desejado."""
    def descer(self): 
        if self.andar_atual == 0:
            print("\nO elevador está no terreo.")
            
        else:
            if self.total_pessoas > 0:
                andar = int(input("\nDigite o número do andar desejado: "))
                print("\nO elevador está no {}º andar.".format(andar)) 
                self.andar_atual = andar
                return self.sair()
            
            if self.total_pessoas == 0:
                return self.entrar()
            
            else:
                print("\nNão há esse andar.")
        