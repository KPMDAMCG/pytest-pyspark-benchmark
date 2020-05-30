import pyspark.sql.functions as F

import pytest


@pytest.mark.parametrize("date", ["2020-05-10 10:30:00"] * 100)
def test_to_date(spark_session, date):
    df = spark_session.createDataFrame([(date,)] * 100, ['t'])

    result = df.select(F.to_date(df.t).alias('date')).collect()

    assert result
