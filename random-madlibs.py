from madlibs_list import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    
    print(m)
    # m.madlib()