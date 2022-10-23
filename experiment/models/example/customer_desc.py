def model(dbt, session):
    customers = dbt.ref("my_first_dbt_model")
    described = customers.describe()
    return described