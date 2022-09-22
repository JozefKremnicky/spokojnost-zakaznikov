spokojny = [0]*24
nespokojny = [0]*24
subor = open ('subor/spokojnost_2.txt','r')
for riadok in subor:
    riadik=riadok.split()
    info=riadok.split()
    spokojnost=info[1]
    cas=info[0].split(':')
    hodina=int(cas[0])
    minuta=int(cas[1])
    if spokojnost == 'ano':
        spokojni[hodina] +=1
    else:
        nespokojny[hodina] +=1
pocet_spokojnych = sum(spokojny)
pocet_nespokojnych = sum(nespokojny)
spolu = pocet_spokojnych + pocet_nespokojnych
print('Vyjadrilo sa {}zakaznikov. '.format (spolu))
pocet_ok=max (spokoni)
hodina = spokojny.index(pocet_ok)
print('Najviac spokojnych zakaznikov .({}) je cez hodinu: {}'.format(pocet_ok,hodina)
  for pocet in nespokojni:
      if pocet >0:
          nespokojni2.append(pocet)
pocet_zle=min(nespokojni2)
hodina= nespokojny.index(pocet_zle)
print('Najmenej spokojnych zakaznikov .({}) je cez hodinu: {}'.format(pocet_zle,hodina)

percenta_spokojnosti = [0]*24
for i in range(24):
      pocet = spokojnosti[i]+nespokojni[i]
      if pocet > 0:
          percenta_spokojnosti[i]=spokojni [i] / pocet * 100
for i in range (24)
      if percenta_spokojnosti[i]>0:
          print('{}.hodine je spokojnych{:5.2f}%'.format(i,percenta_spokojnosti[i]))



      

      
          
      
      
      
      
