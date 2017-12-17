import sys

import xlrd
from geopy.distance import great_circle

from calculo import calculo


class CalcProtecao:

    def __init__(self):
        self.sheet = None
        self.inter = []
        self.channel = 201
        self.lat = 0
        self.long = 0
        self.classe = 'B2'

    def readfile(self, filename):
        try:
            book = xlrd.open_workbook(filename)
        except FileNotFoundError:
            print("Impossivel abrir o arquivo")
            sys.exit(0)
        self.sheet = book.sheet_by_index(0)


    def setparams(self,channel,lat,long,classe):
        self.channel = channel
        self.lat = lat
        self.long = long
        self.classe = classe
    def calcinterf(self):
        interf = [0,1,-1,+2,-2,53,54,-53,-54]
        ch = [self.channel + val  for val in interf]
        for row in range(self.sheet.nrows):
            v = self.sheet.row_values(row)
            try:
                lat,long = float(v[16].replace(',','.')),float(v[17].replace(',','.'))
                channel = int(v[7])
            except ValueError:
                lat,long = 0,0
            else:
                dist = great_circle((lat, long), (self.lat, self.long)).kilometers
                if dist < 300 and channel in ch:
                    self.inter.append(v+[dist])

    def processinter(self):
        dcontprot = {'C':7.5,'B2':12.5,'B1':16.5,"A4":24,'A3':20}
        dcontint = {0:34,1:6,2:-27,53:90,54:90}
        poterp = {'C':0.3,'B2':1,'B1':3,'A4':5}
        haaterp = {'C':60,'B2':90,'B1':90,'A4':150}
        distp2 = dcontprot[self.classe]
        FM = 250
        memo = open('saida.txt','w')
        for erb in self.inter:
            channel = int(erb[7])
            classe = erb[10]
            cib = 64 - dcontint[abs(channel- self.channel)]
            distp1 = dcontprot[classe]
            pot = poterp[classe]
            haat = haaterp[classe]
            distint1 = 0
            distint2 = 0
            if cib > 0:
                distint1 = calculo.tvfmfs_metric(pot,haat,FM,cib,0,2,1,[])
                distint2 = calculo.tvfmfs_metric(poterp[self.classe],haaterp[self.classe],FM,cib,0,2,1,[])

            dtotal1 = distint1+distp1
            dtotal2 = distint2+ distp2
            dtotal = max(dtotal1,dtotal2)
            memo.write('B interferindo em A\n')
            d1 = 'Distancia protegida para o item {} ({}) = {} e distancia interferente = {}\n'.format(erb[0],erb[14],distp1,distint1)
            memo.write(d1)
            memo.write('A interferindo em B\n')
            d1 = 'Distancia protegida para a base  = {} e distancia interferente = {}\n'.format(distp2, distint2)
            memo.write(d1)
            memo.write('Distancia maxima = {} Distancia entre os 2 {}\n'.format(dtotal,erb[-1]))
            if dtotal < erb[-1]:
                memo.write('Não há problema')
            else:
                memo.write('Interferência')
            memo.write('\n\n')
        memo.close()





if __name__ == '__main__':
    c = CalcProtecao()
    c.readfile('Arquivo_entrada.xlsx')
    c.setparams(204,-7.9333333333333,-39.295833333333,'B2')
    c.calcinterf()
    c.processinter()
    '''
        Documentação para a função tvfmfs_metric(erp, haat, channel, field, distance, fs_or_dist, curve, flag)
        erp = ERP em KW
        haat = Altura de desobstrução em m (maior que 30m)
        channel = 250 para FM
        field = intensidade do campo em dBu
        distance = distance ao contorno em km
        fs_or_dist = O que vai ser calculado, 1 = distancia
        flags
    '''


