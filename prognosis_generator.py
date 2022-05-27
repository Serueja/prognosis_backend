from prognosis_pull import Prognosis
from random import randint

#print(len(Prognosis.second_half))

def get_Prognosis():
    ans = Prognosis.first_half[randint(1,1000)%len(Prognosis.first_half)] + '\n\n' + Prognosis.second_half[randint(1,1000)%len(Prognosis.second_half)]
    return ans
