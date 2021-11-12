
class Alocator():

    def __init__(self):
        """
        Função init da classe para incializar variáveis
        """        
        self.users_ttask = []
        self.users_per_server = []
        self.servers = []
        self.cost = 0
        with open('output.txt', 'w') as self.output:
            self.output.write(f'')
        

    def _read_input(self):
        """
        Função que lê o arquivo "input.txt" que contém as informações que necessitamos para alocar
        máquinas virtuais de acordo com nosso objetivo
        """        

        try:
            input = open('input.txt', 'r')
            Lines = input.readlines()
            Lines = [c.strip() for c in Lines]
            self.ttask = int(Lines[0])
            self.umax = int(Lines[1])
            self.new_users = [ int(c) for c in Lines[2:]]
            input.close()

        except FileNotFoundError:
            raise FileNotFoundError('Verifique se há um arquivo "input.txt" no diretório')

    def __realocate(self):
        """Função que realoca as máquinas virtuais baseado no tempo restante para a máquina terminar sua tarefa, usuários
        com menos tempo restante serão alocados em um mesmo servidor para que aquele servidor possa ser desligado rapidamente.
        A função também calcula quantos servidores serão necessários, e quantos usuários terão em cada servidor.
        """        

        #Reiniciando variável com usuários em seus devidos servidores
        self.servers=[]

        #Calculando quantidade de servidores necessários
        n_servers = int(len(self.users_ttask)/self.umax)

        #Calculando quantos usuários terá por servidor
        self.users_per_server = [self.umax] * n_servers

        #Adicionando o resto de usuários que sobra da divisão comum entre usuários e umax
        if (len(self.users_ttask)%self.umax)>0:
            self.users_per_server.append(len(self.users_ttask)%self.umax)        

        #Ordenando usuários de maior ttask para menor
        self.users_ttask.sort(reverse=True)  


        #Alocando o ttask de cada usuário em uma lista servidor, e alocando cada servidor em uma lista de servidores
        for server in range(0,n_servers+1):
            
            
            server = self.users_ttask[server*self.umax : (server+1)*self.umax]

            if len(server)>0:
                self.servers.append(server)

        print(str(self.servers)[1:-1])


    def _write_line(self, line:int):
        """Função que escreve uma linha com dados no output.txt e pula para a próxima linha. A linha precisa
        ser um Integer visto que só esse tipo de dado é necessário para o nosso objetivo

        :param line: Linha com dados que será escrito no arquivo
        :type line: int
        """        

        with open('output.txt', 'a') as self.output:
            self.output.write(f'{line}\n')
        

    def __calculate_tick_cost(self):
        """Função que calcula o custo atual dos servidores que estão em uso, ou seja, o custo
        dos servidores no tick atual. E acrescenta ao custo total na variável self.cost da classe.
        """        

        self.cost = self.cost + (len(self.servers) * 1) 
        
        

    def iterating_ticks(self):
        """Função principal da classe, que executa tudo que é necessário para cumprir o objetivo desse teste.
        """        

        #Lê o arquivo input.txt
        self._read_input()

        #Iterando pelos usuários
        for users in self.new_users:
            
            #Remove 1 segundo do ttask de cada usuário, a cada tick, para simular tempo passando
            self.users_ttask = [c -1 for c in self.users_ttask]
            
            #Remove todos os usuários com Ttask = 0
            while (0 in self.users_ttask):
                self.users_ttask.remove(0)

            #Adicionando o ttask do novo usuário em nossa lista com todos os ttasks de todos os usuários
            for _ in range(0,users):
                self.users_ttask.append(self.ttask)
            
            #Realocando usuários
            self.__realocate()

            #Escrevendo quantos usuários terá em cada servidor
            self._write_line(str(self.users_per_server)[1:-1])

            #Calculando o custo no atual tempo/tick
            self.__calculate_tick_cost()

        #Depois que todos os usuários já foram alocados em seus servidores, resta apenas esperar todas as tarefas acabarem
        while len(self.users_ttask)>0:
            
            #Remove 1 segundo do ttask de cada usuário, a cada tick, para simular tempo passando
            self.users_ttask = [c -1 for c in self.users_ttask]

            #Remove todos os usuários com Ttask = 0
            while (0 in self.users_ttask):
                self.users_ttask.remove(0)

            #Quebra o loop se chegar a 0 tarefas rodando
            if len(self.users_ttask)==0: break

            #Realocando usuários
            self.__realocate()

            #Escrevendo quantos usuários terá em cada servidor
            self._write_line(str(self.users_per_server)[1:-1])

            #Calculando o custo no atual tempo/tick
            self.__calculate_tick_cost()


        self._write_line(self.cost)


            
if __name__ == '__main__':
    aloc = Alocator()
    aloc.iterating_ticks()



    
