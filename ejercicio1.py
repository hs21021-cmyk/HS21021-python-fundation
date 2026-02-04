salario = float(input("Ingrese su salario: "))

if salario >= 5000:
  bono = salario * 0.05
  print("Su bono es de: " + str(bono))
else:
  bono = salario * 0.15
  print("Su bono es de: " + str(bono))