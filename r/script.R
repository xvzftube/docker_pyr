library(forecast) # install2.r

x <- USAccDeaths %>%
  ets() %>%
  forecast()

print(x)
