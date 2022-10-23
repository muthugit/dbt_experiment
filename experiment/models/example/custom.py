def model(dbt, session):
    dbt.configure(materailized="view")
    return session.sql("select * from genres")