========================
Pytest pyspark benchmark
========================


Results
=======

Local spark, one pytest session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------+-----------+-------+--------+--------+----------+
| Machine  | CPU      | Cores   | Total (s) | Setup | Call 1 | Cal 2  | Teardown |
+----------+----------+---------+-----------+-------+--------+--------+----------+
| Mac 2019 | i7-9750H | 6/12    | 10.78     | 2.67  | 2.40   | 0.08   | 1.01     |
+----------+----------+---------+-----------+-------+--------+--------+----------+
| Mac      |          |         |           |       |        |        |          |
+----------+----------+---------+-----------+-------+--------+--------+----------+
| Z800     |          | 4/8     |           |       |        |        |          |
+----------+----------+---------+-----------+-------+--------+--------+----------+

Local spark, 4 pytest sessions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+-----------+-------+--------+--------+----------+
| Machine  | Total (s) | Setup | Call 1 | Cal 2  | Teardown |
+----------+-----------+-------+--------+--------+----------+
| Mac 2019 | 13.40     | 4.43  | 4.25   | 0.18   | 1.00     |
+----------+-----------+-------+--------+--------+----------+
| Mac      |           |       |        |        |          |
+----------+-----------+-------+--------+--------+----------+
| Z800     |           |       |        |        |          |
+----------+-----------+-------+--------+--------+----------+


Deployment
==========

.. code-block:: bash

   $ conda env create -f environment.yml
   $ conda activate pytest-pyspark-benchmark

Test execution
==============

.. code-block:: bash

    # Local spark, one pytest session
    $ pytest test_pyspark.py --durations 5
    ================================= test session starts ==================================
    platform darwin -- Python 3.6.10, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dmilajevs/Projects/pytest-pyspark-benchmark
    plugins: forked-1.1.2, xdist-1.32.0
    collected 100 items

    test_pyspark.py ................................................................ [ 64%]
    ....................................                                             [100%]

    =============================== slowest 5 test durations ===============================
    2.67s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    2.40s call     test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    1.01s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0099]
    0.08s call     test_pyspark.py::test_to_date[2020-05-10 10:30:009]
    0.08s call     test_pyspark.py::test_to_date[2020-05-10 10:30:008]
    ================================= 100 passed in 10.78s =================================

    # Local spark, 12 pytest sessions
    pytest test_pyspark.py --durations 15 -n 4
    ================================= test session starts ==================================
    platform darwin -- Python 3.6.10, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    rootdir: /Users/dmilajevs/Projects/pytest-pyspark-benchmark
    plugins: forked-1.1.2, xdist-1.32.0
    gw0 [100] / gw1 [100] / gw2 [100] / gw3 [100]
    ................................................................................ [ 80%]
    ....................                                                             [100%]
    ============================== slowest 15 test durations ===============================
    4.43s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    4.38s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:003]
    4.35s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:002]
    4.35s setup    test_pyspark.py::test_to_date[2020-05-10 10:30:001]
    4.25s call     test_pyspark.py::test_to_date[2020-05-10 10:30:000]
    4.13s call     test_pyspark.py::test_to_date[2020-05-10 10:30:001]
    4.13s call     test_pyspark.py::test_to_date[2020-05-10 10:30:002]
    4.10s call     test_pyspark.py::test_to_date[2020-05-10 10:30:003]
    1.00s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0099]
    0.99s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0095]
    0.99s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0097]
    0.99s teardown test_pyspark.py::test_to_date[2020-05-10 10:30:0098]
    0.18s call     test_pyspark.py::test_to_date[2020-05-10 10:30:0035]
    0.17s call     test_pyspark.py::test_to_date[2020-05-10 10:30:0042]
    0.16s call     test_pyspark.py::test_to_date[2020-05-10 10:30:0041]
    ================================= 100 passed in 13.40s =================================

    # Remote spark, one pytest session
    $ pytest test_pyspark.py --durations 5 --pyspark spark://localhost:7077

    # Remote spark, 8 pytest sessions
    $ pytest test_pyspark.py --durations 5 --pyspark spark://localhost:7077 -n 8

Server mode setup
=================

.. code-block:: bash

    $ curl http://apache.spinellicreations.com/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz | tar -xvf -

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


Notes
=====

.. sysctl -n machdep.cpu.brand_string

Mac 2019
--------

:CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz 6 cores, 12 threads
:Memory: 32GB
:Storage: 1TB NVMe

``pytest -n2`` and ``pytest -n 4`` take about the same time. The execution time increases for larger ``-n``.
