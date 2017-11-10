
k = 3
n = 8
s = [0,3,6,0,2,4,0,6]
f = [3,6,8,2,4,8,5,8]

def intersectan(a,b):
    if (s[b] < s[a] < f[b] or s[b] < f[a] < f[b] or s[a] < s[b] < f[a] or s[a] < f[b] < f[a]):
        return True
    return False

def proximasMovidas(vector):
    resp = []
    t = len(vector)
    maquinaApta = True
    for j in range(0,k):
        for i in range(0,len(vector)):
            if (vector[i] == j and intersectan(i,t)):
                maquinaApta = False
        if (maquinaApta): resp.append(j)

    return resp

def asignarMaquina(vector):
    pm = proximasMovidas(vector)
    for m in pm:
        if (len(vector) + 1 == n):
            vector.append(m)
            return vector

        vector2 = asignarMaquina(list(vector) + [m])
        if ( vector2 != None):
            return vector2

    return None

print(asignarMaquina([]))