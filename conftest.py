from pyspark.sql import SparkSession

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--pyspark", default="local", help="Spark master."
    )


@pytest.fixture(scope="session")
def spark_master(request):
    return request.config.getoption("--pyspark")


@pytest.fixture(scope="session")
def spark_session(worker_id, spark_master):
    spark = (
        SparkSession.builder
        .master(spark_master)
        .appName(f"test-{worker_id}")
        .getOrCreate()
    )

    yield spark

    spark.stop()

