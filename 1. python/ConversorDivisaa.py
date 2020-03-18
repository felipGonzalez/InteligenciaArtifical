
def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 145.97 

    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos')

    ammount = float(input('Ingrese la cantidad de pesos colombianos'))

    result = foreing_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))


if __name__ == '__main__':
    run()
    