import math

class Vector_R1:

  def __init__(self, coorx):
    self.x = coorx

  def sumar_escalar(self, escalar):
    return [self.x + escalar]

  def restar_escalar(self, escalar):
    return [self.x - escalar]

  def multiplicacion_escalar(self, escalar):
    return [self.x * escalar]

  def producto_punto(self, vector):
    return self.x * vector.x

  def division_escalar(self, escalar):
    return [self.x / escalar]

  def angulo_vectores(self, vector):
    return str(0) + "°"

  def normalizacion(self):
    potencia = self.x * self.x
    norma = math.sqrt(potencia)
    return [self.x / norma]
    
#--------------vectores R1---------------------#
vectorR1 = Vector_R1(5)
vectorR1_2 = Vector_R1(2)
#-----------------operaciones------------------#
print("R1",vectorR1.sumar_escalar(1))
print("R1",vectorR1.restar_escalar(1))
print("R1",vectorR1.multiplicacion_escalar(1))
print("R1",vectorR1.producto_punto(vectorR1_2))
print("R1",vectorR1.angulo_vectores(vectorR1))
print("R1",vectorR1.normalizacion())


class Vector_R2(Vector_R1):

  def __init__(self, coorx, coory):
    Vector_R1.__init__(self, coorx)
    self.y = coory

  def sumar_escalar(self, escalar):
    return [self.x + escalar, self.y + escalar]

  def restar_escalar(self, escalar):
    return [self.x - escalar, self.y - escalar]

  def multiplicacion_escalar(self, escalar):
    return [self.x * escalar, self.y * escalar]

  def division_escalar(self, escalar):
    return [self.x / escalar, self.y / escalar]

  def producto_punto(self, vector):
    return (self.x * vector.x ) + (self.y * vector.y)
    
  def normalizacion(self):
    aux1 = self.x * self.x
    aux2 = self.y * self.y
    norma = math.sqrt(aux1 + aux2)
    return [self.x / norma, self.y / norma]

  def norma(self):
    return math.sqrt(pow(self.x,2)+pow(self.y,2))

  def angulo_vectores(self,vector):
    modulo_v1 = self.norma()
    modulo_v2 = vector.norma()
    producto = self.producto_punto(vector)
    radianes = (producto/(modulo_v1 * modulo_v2))
    return math.degrees(math.acos(radianes))

#--------------vectores R2---------------------#
vectorR2 = Vector_R2(5, 2)
vectorR2_2 = Vector_R2(2, 2)
#-----------------operaciones------------------#
print("R2", vectorR2.sumar_escalar(1))
print("R2", vectorR2.restar_escalar(1))
print("R2", vectorR2.multiplicacion_escalar(2))
print("R2", vectorR2.division_escalar(2))
print("R2", vectorR2.norma())
print("R2", vectorR2.angulo_vectores(vectorR2_2))
print("R2", vectorR2.normalizacion())

class Vector_R3(Vector_R2):

  def __init__(self, coorx, coory, coorz):
    Vector_R2.__init__(self, coorx, coory)
    self.z = coorz
    
  def sumar_escalar(self, escalar):
    return [self.x + escalar, self.y + escalar, self.z+escalar]

  def restar_escalar(self, escalar):
    return [self.x - escalar, self.y - escalar, self.z - escalar]

  def multiplicacion_escalar(self, escalar):
    return [self.x * escalar, self.y * escalar, self.z * escalar]

  def producto_punto(self, vector):
    return self.x * vector.x + self.y * vector.y + self.z * vector.z

  def division_escalar(self, escalar):
    return [self.x / escalar, self.y / escalar, self.z / escalar]

  def norma(self):
    return math.sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
  def angulo_vectores(self, vector):
    norma_u = self.norma()
    norma_v = vector.norma()
    coseno_angulo = self.producto_punto(vector)/(norma_u*norma_v)
    return math.degrees(math.acos(coseno_angulo))
    
  def producto_cruz(self, vector):
    det2 = (self.x * vector.z) - (self.z * vector.x)
    det1 = (self.y * vector.z) - (self.z * vector.y)
    det3 = (self.x * vector.y) - (self.y * vector.x)
    return [det1, -det2, det3]

  def normalizacion(self):
    aux1 = self.x * self.x
    aux2 = self.y * self.y
    aux3 = self.z * self.z
    norma = math.sqrt(aux1 + aux2 + aux3)
    return [self.x / norma, self.y / norma, self.z /norma]
    

#--------------vectores R3---------------------#
vectorR3 = Vector_R3(1, 2, 3)
vectorR3_2 = Vector_R3(1, 2, 3)
v1 = Vector_R3(3,-1,2)
v2 = Vector_R3(-4,0,2)
#-----------------operaciones------------------#
print("R3", vectorR3.sumar_escalar(2))
print("R3", vectorR3.restar_escalar(2))
print("R3", vectorR3.multiplicacion_escalar(2))
print("R3", v1.producto_punto(v2))
print("R3", vectorR3.division_escalar(2))
print("R3", v1.angulo_vectores(v2))
print("R3", vectorR3.producto_cruz(vectorR3_2))
print("R3", vectorR3.normalizacion())
