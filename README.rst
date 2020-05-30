========================
Pytest pyspark benchmark
========================

Deployment
==========

.. code-block:: bash

   $ conda env create -f environment.yml
   $ conda activate pytest-pysaprk-benchmark

Test execution
==============

.. code-block:: bash

    $ pytest test_pyspark.py --durations 5
    ========================================== test session starts ==========================================
    platform linux -- Python 3.6.10, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    rootdir: /home/dima/Projects/pytest-pyspark-benchmark
    collected 50 items

    test_pyspark.py ..................................................                                [100%]

    ======================================= slowest 5 test durations ========================================
    3.30s call     test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    3.20s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    1.00s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0049]
    0.18s call     test_pyspark.py::test_to_date[2020-05-10 10:30:0011]
    0.16s call     test_pyspark.py::test_to_date[2020-05-10 10:30:002]
    ==================================== 50 passed, 2 warnings in 12.43s ====================================

Server mode
===========

.. code-block:: bash

    $ curl -O http://apache.spinellicreations.com/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
    $ tar xvf spark-2.4.5-bin-hadoop2.7.tgz


    # Start the master in one terminal
    $ spark-2.4.5-bin-hadoop2.7/sbin/start-master.sh
    $ tail -F spark-2.4.5-bin-hadoop2.7/logs/spark-dima-org.apache.spark.deploy.master.Master-1-z800.out
    ...
    20/05/30 09:03:58 INFO MasterWebUI: Bound MasterWebUI to 0.0.0.0, and started at http://z800:8080
    ...

    # Start a worker in another terminal
    $ spark-2.4.5-bin-hadoop2.7/sbin/start-slave.sh spark://z800:7077 --cores 8
    $ tail -F spark-2.4.5-bin-hadoop2.7/logs/spark-dima-org.apache.spark.deploy.worker.Worker-1-z800.out
    ...
    20/05/30 09:23:05 INFO Worker: Successfully registered with master spark://z800:7077
    ...

