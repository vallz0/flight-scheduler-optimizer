import mlrose

pessoas:list= [("Lisboa","LIS"),
               ("Madrid","MAD"),
               ("Paris","CDG"),
               ("Dublin","DUB"),
               ("Bruxelas","BRU"),
               ("Londres","LHR")]

destino:str = "FCO"

voos:dict = {}
for linha in open("flights.txt"):
    origem, destino, saida, chegada, preco = linha.split(",")
    voos.setdefault((origem,destino), [])
    voos[(origem,destino)].append((saida,chegada,int(preco)))

def fitness_function(agenda:list) -> int:
    id_voo:int = -1
    total_preco:int = 0

    for i in range(len(agenda) // 2):
        origem:str = pessoas[i][1]
        id_voo +=  1
        ida = voos[(origem,destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    return  total_preco

agenda:list[int] = [1,2,3,2,7,3,6,3,2,4,5,3] # 10**12
fitness_function(agenda)

fitness = mlrose.CustomFitness(fitness_function)

problema = mlrose.DiscreteOpt(length=12,fitness_fn=fitness,
                              maximize = False,max_val = 10)

