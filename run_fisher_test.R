library(spatstat)
library(spatstat.data)

args <- commandArgs(trailingOnly = TRUE)
cell_size <- as.integer(args[1])  

data(finpines)

H <- hextess(finpines, cell_size)
hQ <- quadratcount(finpines, tess = H)

png("/Users/jorgeandresjolahernandez/Desktop/Curso_Mod_Espacial/web_curso/static/graph.png")  # Define la ruta donde quieres guardar la imagen

# Generar el gráfico
plot(hQ)

# Crear la matriz para el test de Fisher
swp <- matrix(finpines$marks$height, nrow = cell_size, byrow = T)

# Realizar el test de Fisher
result <- fisher.test(swp, simulate.p.value = TRUE, B = 10000)

# Mostrar el resultado
print(result)