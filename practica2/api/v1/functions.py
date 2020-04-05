
import pmdarima as pm


def prediction(df, hours, elements):
    df = df.head(elements)
    # The model will be trained
    model = pm.auto_arima(df, start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)

    # Forecast
    n_periods = hours
    fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
    return fc