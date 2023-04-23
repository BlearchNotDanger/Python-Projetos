real=float(input('quanto de dinheiro voce tem na carteira? R$'))
dolar= real / 5.04
yines= real / 0.038
euros= real / 5.53
print('com{:.2f} você pode comprar U$${:.2f} e de yines {:.2f} e euro {:.2f}'.format(real,dolar,yines,euros))
