
def protected(func):

    def wrapper(password):
        if password == 'platzi'
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper

@protected
def protected_func():
    print('Tu contraseña en incorrecta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    #wrapper = protected(protected_func)
    #wrapper(password)

    protected_func(password)
    
    