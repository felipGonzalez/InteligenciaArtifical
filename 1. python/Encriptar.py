

def run():
    while True:
    
       
        print('''
                ╔════════════════════════════════════════════════════════════╗
                ║                      C R I P T O G R A F I A               ║
                ║   [c]ifrar mensaje                                         ║
                ║   [d]ecifrar mensaje                                       ║
                ║   [s]alir                                                  ║
                ╚════════════════════════════════════════════════════════════╝               
            ''')

        command = str(input('¿Qué deseas hacer? '))
        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(' --> Mensaje cifrado: {}'.format(cypher_message))

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(' --> Mensaje decodificado: {}'.format(decypher_message))
        elif command == 's':
            print('Terminado')
            break
        else:
            print('¡Comando no encontrado!')

        print('')
        

if __name__ == '__main__':
    run()
    