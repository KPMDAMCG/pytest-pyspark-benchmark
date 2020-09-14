========================
Pytest pyspark benchmark
========================


Results
=======

Local spark, one pytest session
-------------------------------

+------------+----------+---------------+-----------+-------+--------+--------+----------+
| Machine    | CPU      | Cores/Threads | Total (s) | Setup | Call 1 | Call 2 | Teardown |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| Mac 2019   | i7-9750H | 6/12          | 10.78     | 2.67  | 2.40   | 0.08   | 1.01     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| Mac 2013   | i7-4558U | 2/4           | 16.06     | 4.11  | 3.89   | 0.13   | 1.01     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| Z800       | X5570    | 4/8           | 16.18     | 3.26  | 3.29   | 0.16   | 1.01     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| VDI Dima 1 |          |               | 263.30    | 11.06 | 9.47   | 7.07   | 0.99     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| CG Mac     | i9-9880H | 8/16          | 11.59     | 3.13  | 2.87   | 0.11   | 1.01     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+
| VDI Azure  | E5-2673v3|               | 141.94    | 10.28 | 7.71   | 1.54   | 1.01     |
+------------+----------+---------------+-----------+-------+--------+--------+----------+

Local spark, 4 pytest sessions
------------------------------

+------------+-----------+-------+--------+--------+----------+
| Machine    | Total (s) | Setup | Call 1 | Call 2 | Teardown |
+------------+-----------+-------+--------+--------+----------+
| Mac 2019   | 13.40     | 4.43  | 4.25   | 0.18   | 1.00     |
+------------+-----------+-------+--------+--------+----------+
| Mac 2013   | 32.96     | 11.06 | 11.39  | 0.61   | 1.00     |
+------------+-----------+-------+--------+--------+----------+
| Z800       | 21.21     | 6.68  | 5.90   | 0.42   | 1.00     |
+------------+-----------+-------+--------+--------+----------+
| VDI Dima 1 | 241.00    | 46.53 | 30.66  | 9.75   | 1.90     |
+------------+-----------+-------+--------+--------+----------+

Remote spark, one pytest session
--------------------------------

+----------+-----------+-------+--------+--------+----------+
| Machine  | Total (s) | Setup | Call 1 | Call 2 | Teardown |
+----------+-----------+-------+--------+--------+----------+
| Mac 2019 |           |       |        |        |          |
+----------+-----------+-------+--------+--------+----------+
| Mac 2013 | 23.73     | 4.59  | 5.89   | 0.23   | 1.00     |
+----------+-----------+-------+--------+--------+----------+
| Z800     | 22.55     | 3.57  | 4.93   | 0.23   | 1.01     |
+----------+-----------+-------+--------+--------+----------+

Remote spark, 4 pytest sessions
-------------------------------

+----------+-----------+-------+--------+--------+----------+
| Machine  | Total (s) | Setup | Call 1 | Call 2 | Teardown |
+----------+-----------+-------+--------+--------+----------+
| Mac 2019 |           |       |        |        |          |
+----------+-----------+-------+--------+--------+----------+
| Mac 2013 |  56.04    | 53.27 | 37.86  | 0.27   | 0.99     |
+----------+-----------+-------+--------+--------+----------+
| Z800     |  40.85    | 7.42  | 30.61  | 0.22   | 1.01     |
+----------+-----------+-------+--------+--------+----------+

Notes
=====

.. sysctl -n machdep.cpu.brand_string

Mac 2019
--------

:CPU: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz 6 cores, 12 threads
:Memory: 32GB
:Storage: 1TB NVMe
:OS: macOS

``pytest -n2`` and ``pytest -n4`` take about the same time. The execution time increases for larger ``-n``.

Mac 2013
--------

:CPU: Intel(R) Core(TM) i7-4558U CPU @ 2.80GHz 2 cores, 4 threads
:Memory: 8GB
:Storage: 500GB SSD
:OS: macOS Catalina 10.15.4

``pytest -n2`` took 22.10 seconds with local spark and 34.86 with remote spark.

Z800
----

:CPU: Intel(R) Xeon(R) CPU X5570 @ 2.93GHz
:Memory: 16GB
:Storage: 1TB HDD, 256GB SSD LVM cache
:OS: GNU/Linux

``pytest -n2`` took 16.12 seconds with local spark and 28.47 with remote spark.

CG MAC
------

:CPU: Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz
:Memory: 32GB
:Storage: 1TB NVMe
:OS: macOS Catalina 10.15.6

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

    # Local spark, 4 pytest sessions
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
    $ pytest test_pyspark.py --durations 5 --pyspark spark://0.0.0.0:7077

    # Remote spark, 4 pytest sessions
    $ pytest test_pyspark.py --durations 5 --pyspark spark://0.0.0.0:7077 -n 4

Server mode setup
=================

.. code-block:: bash


    # Start the master in one terminal
    $ spark-class org.apache.spark.deploy.master.Master
    ...
    20/05/30 09:03:58 INFO MasterWebUI: Bound MasterWebUI to 0.0.0.0, and started at http://z800:8080
    ...

    # Start a worker in another terminal
    $ spark-class org.apache.spark.deploy.worker.Worker spark://0.0.0.0:7077
    ...
    20/05/30 09:23:05 INFO Worker: Successfully registered with master spark://z800:7077
    ...
