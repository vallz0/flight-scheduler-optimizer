library(dplyr)
library(ggplot2)
library(lubridate)

flights <- read.csv("flights.txt", header = FALSE, sep = ",", 
                    col.names = c("Origin", "Destination", "Departure", "Arrival", "Price"))

flights$Departure <- hms(flights$Departure)
flights$Arrival <- hms(flights$Arrival)

cat("Número total de voos disponíveis:", nrow(flights), "\n")
cat("Preço médio dos voos:", mean(flights$Price), "\n")
cat("Preço mais barato:", min(flights$Price), "\n")
cat("Preço mais caro:", max(flights$Price), "\n")

cheapest_flight <- flights %>% filter(Price == min(Price))
cat("Voo mais barato:\n")
print(cheapest_flight)

ggplot(flights, aes(x = Price)) +
  geom_histogram(binwidth = 50, fill = "blue", alpha = 0.7) +
  labs(title = "Distribuição de Preços dos Voos", x = "Preço", y = "Frequência") +
  theme_minimal()

ggplot(flights, aes(x = Departure)) +
  geom_histogram(binwidth = 1800, fill = "green", alpha = 0.7) + # Bin de 30 minutos
  labs(title = "Distribuição de Horários de Partida", x = "Horário de Partida", y = "Frequência") +
  scale_x_time(labels = scales::time_format("%H:%M")) +
  theme_minimal()

ggplot(flights, aes(x = Origin, y = Price)) +
  geom_boxplot(fill = "orange", alpha = 0.7) +
  labs(title = "Comparação de Preços por Origem", x = "Origem", y = "Preço") +
  theme_minimal()
