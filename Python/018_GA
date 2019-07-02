import random
import operator

df= [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87,40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

class Individual():
        
    
    def __init__(self,df):
        self.steps = [random.randint(0, 1) for i in range(len(df))]
        self.fitness = 0
    
    def evaluate(self, df):
        res = [df[0][0]]
    
        for row in range(1, len(df)):
            pos = df[row-1].index(res[-1])
            step = self.steps[row]
            x = df[row][pos+step]
            res.append(x)
        self.fitness = sum(res)    
        return sum(res)
        
    def mutate(self, mrate=0.1):
        for i in range(len(self.steps)):
            if random.random() < mrate:
                self.steps[i] = int(not self.steps[i])
    
    def __repr__(self):
        return str(self.steps)+", fitness: "+str(self.fitness)

                
def gen_alg(df, pop_size, max_gen):
    
    def crossover(p1, p2, df):
    child = Individual(df)
    for i in range(len(df)):
        if random.random() > 0.5:
            child.steps[i] = p1.steps[i]
        else:
            child.steps[i] = p2.steps[i]
    child.evaluate(df)
    return child

    pop = [Individual(df) for i in range(pop_size)]
    for i in pop:
        i.evaluate(df)

    generation = 0
    
    while generation < max_gen:
        #Crossover and mutation
        children = [crossover(pop[i], pop[-i], df) for i in range(len(pop))]
        for child in children:
            child.mutate()

        combined_gen = pop + children

        #Ranking
        sorted_gen = sorted(combined_gen, key=operator.attrgetter('fitness'), reverse=True)
        current_best = sorted_gen[0]

        #Selecton
        pop = sorted_gen[:pop_size]

        generation += 1

    return [current_best, pop]

res = gen_alg(df, 50, 100)
res[0]
