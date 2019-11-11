import numpy as np
# import matplotlib.pyplot as pt

def media_movel(X,tam_janela):
    mv = np.zeros(len(X))
  
    for i in range(0,len(X)-tam_janela):
        mv[i+tam_janela] = X[0+i:tam_janela+i].mean()
  
    return mv

def std_movel(X,tam_janela):
    mv = np.zeros(len(X))
  
    for i in range(0,len(X)-tam_janela):
        mv[i+tam_janela] = X[0+i:tam_janela+i].std()
  
    return mv
  
def imprimeAnosTemperaturaOutlier(tj, X, mv, mv_sd):
    anosTempAcima = []
    anosTempAbaixo = []
    for ano in range(tj, len(X)):
        if (X[ano] < mv[ano] - mv_sd[ano]):
            anosTempAbaixo.append(ano)
        elif (X[ano] > mv[ano] + mv_sd[ano]):
            anosTempAcima.append(ano)

    print('Anos acima: ', anosTempAcima)
    print('Anos abaixo: ', anosTempAbaixo)
  
Temperatura = np.random.normal(0,1,100) + 30 + 0.01 * np.array(range(0,100))
tj = 5
mv = media_movel(Temperatura, tj)
mv_sd = std_movel(Temperatura, tj)

imprimeAnosTemperaturaOutlier(tj, Temperatura, mv, mv_sd)