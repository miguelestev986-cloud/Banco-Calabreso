from datetime import datetime as dt, timedelta

print(dt.today())
print(dt.now())
data = dt.now()
semana_seguinte = data + timedelta(days=7)
print(semana_seguinte)