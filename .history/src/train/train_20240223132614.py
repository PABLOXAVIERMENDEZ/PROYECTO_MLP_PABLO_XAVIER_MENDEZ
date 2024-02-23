import numpy as np
import pandas as pd

dataset = r"C:\Users\Lucia\Desktop\PROYECTO_MLP_PABLO_XAVIER\PROYECTO_MLP_PABLO_XAVIER_MENDEZ\src\data\process\telecom.csv"
df = pd.read_csv(dataset, parse_dates=['DATE'])


calls_per_date_df = pd.DataFrame(calls_per_date, columns=["CALLS"])

calls_per_date_df.index = pd.to_datetime(calls_per_date_df.index).to_period('D')

print(calls_per_date_df)

moving_average = calls_per_date_df.rolling(
    window=90,       
    center=True,      
    min_periods=45,  
).mean()              

ax = calls_per_date_df.plot(style=".", color="0.5")
moving_average.plot(
    ax=ax, linewidth=3, title="llamadas diarias - 90 -Day Moving Average", legend=False,)

from statsmodels.tsa.deterministic import DeterministicProcess

dp = DeterministicProcess(
    index=calls_per_date_df.index,  
    constant=True,       
    order=1,             
    drop=True,           
)

X = dp.in_sample()

X.head()

from sklearn.linear_model import LinearRegression

y = calls_per_date_df["CALLS"]

# La intercepción es el mismo que el `const` característica de
# DeterministicProcess. LinearRegression se comporta mal con 
# características duplicadas, por lo que necesitamos estar seguros de excluirlos.
model = LinearRegression(fit_intercept=False)
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)

ax = calls_per_date_df.plot(style=".", color="0.5", title="llamadas diarias - Linear Trend")
_ = y_pred.plot(ax=ax, linewidth=3, label="Trend")

X = dp.out_of_sample(steps=30)

y_fore = pd.Series(model.predict(X), index=X.index)

y_fore.head()

calls_april = calls_per_date_df["2021-03":]
y_pred_april = y_pred["2021-03":]
y_fore_PRIL = y_fore["2021-03":]

# Configurar parámetros de gráfico
plot_params = {
    "kind": "line",
    "title": "Llamadas diarias - Pronóstico de tendencia lineal"
}

# Crear gráfico
ax = calls_april.plot(**plot_params)
ax = y_pred_april.plot(ax=ax, linewidth=3, label="Tendencia")
ax = y_fore_april.plot(ax=ax, linewidth=3, label="Pronóstico de tendencia", color="C3")

# Mostrar leyenda
ax.legend()

# Mostrar el gráfico
plt.show()

from sklearn.metrics import mean_absolute_error

# Suponiendo que 'y_true' son los valores reales y 'y_pred' son las predicciones del modelo
mae = mean_absolute_error(calls_per_date_df['CALLS'], y_pred)
print("Mean Absolute Error (MAE):", mae)