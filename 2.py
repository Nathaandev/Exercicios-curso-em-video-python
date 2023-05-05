def notasaluno(*notas, sit=False):
    alunosnot = {}
    alunosnot['total'] = len(notas)
    alunosnot['maior'] = max(notas)
    alunosnot['menor'] = min(notas)
    alunosnot['media'] = sum(notas) / len(notas)
    print(alunosnot)




notasaluno(3,9,10,2.2)
