def notas(*num, sit=False):
    resp = dict()
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    media = sum(num)/ len(num)
    resp['media'] = media
    if sit:
        if 0 <= media < 3:
            resp['situação'] = 'Ruim'
        if 3 <= media < 5:
            resp['situação'] = 'Regular'
        if 5 <= media < 6:
            resp['situação'] = 'Mediocre'
        if 6 <= media < 8:
            resp['situação'] = 'Razoável'
        if 8 <= media <= 10:
            resp['situação'] = 'Boa'
    return resp

#Programa Principal
resp = notas(8.6, 7, 9.7, sit = False)
print(resp)