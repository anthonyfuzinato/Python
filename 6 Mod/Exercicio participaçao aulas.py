aula1={"1","1","2","4","1","7"}
aula2={"5","4","7","4","2","2"}
aula3={"7","1","7","1","3","7"}
alunos={"1","2","3","4","5","6","7"}

# Mostrar os alunos que participaram nas aulas
print (aula1 | aula2 | aula3)

# Mostrar os alunos que nao participaram 
print (alunos - (aula1 | aula2 | aula3))

# Mostrar os alunos que participaram nas 3 aulas
print (aula1 & aula2 & aula3)
