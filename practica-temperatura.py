temperatura=float(input('¿A cuántos grados estamos?'))

if temperatura > 34:
    print('ta juerte el calor')
elif temperatura > 30 and temperatura < 35:
    print('ya empieza a hacer más calor')
elif temperatura > 24 and temperatura < 31:
    print('se antoja un pozolito con dulce')
elif temperatura <25:
    print('¿ya hace frio no?, hay que sacar el abrigo')