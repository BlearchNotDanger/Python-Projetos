slr = float(input('qual o salário do funcionário? R$ '))
r = slr + (slr * 7 / 100)
print('um funcionário que ganhava {:.2f} com reajuste de 7% vai ganhar {:.2f}'.format(slr,r))