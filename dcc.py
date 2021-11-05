def main():
    dcc = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(dcc['llave1'])
    # print(dcc['llave2'])
    # print(dcc['llave3'])
    
    pobla_pais = {
        
        'Argentina': 44754785,
        'Brasil': 210378732,
        'Venezuela': 212342344,
            }
    # print(pobla_pais)
    
    # for pais in pobla_pais.keys():
    #     print(pais)
    
    # for pais in pobla_pais.values():
    #     print(pais)
    
    for pais, poblacion in pobla_pais.items():
        print(pais + ' ' + 'tiene' + ' ' + str(poblacion) + ' ' 'habitantes :v')
    
    
if __name__ == '__main__':
    main()