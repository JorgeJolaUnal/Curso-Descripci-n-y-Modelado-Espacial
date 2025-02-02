library(spatstat)
library(spatstat.data)

args <- commandArgs(trailingOnly = TRUE)
cell_size <- as.integer(args[1])  

data(finpines)

H <- hextess(finpines, cell_size)
hQ <- quadratcount(finpines, tess = H)

png("static/graph.png")  # Define la ruta donde quieres guardar la imagen

# Generar el gráfico
plot(hQ)

# Cerrar el dispositivo gráfico (esto guarda el archivo)
dev.off()
# Ejecutar el test de Chi-cuadrado
tS <- quadrat.test(finpines, cell_size, cell_size)

# Mostrar el resultado
print(tS)