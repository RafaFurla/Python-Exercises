def notas(*n, sit=False):
    """
    → Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    maior = menor = soma = float(0)
    dicionario['total'] = len(n)
    for c, v in enumerate(n):
        soma += v
        if c == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = soma / len(n)
    if sit:
        if dicionario['media'] < 5.0:
            dicionario['situação'] = "RUIM"
        elif 5.0 <= dicionario['media'] < 7.0:
            dicionario['situação'] = "RAZOÁVEL"
        else:
            dicionario['situação'] = "BOA"
    return dicionario


dic = notas(3, 6.0, 5.5, 9.8, sit=True)
help(notas)
print(dic)
