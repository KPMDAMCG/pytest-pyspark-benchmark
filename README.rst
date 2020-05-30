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

    # Local spark, one pytest session
    $ pytest test_pyspark.py --durations 5y

    # Local spark, 8 pytest sessions
    $ pytest test_pyspark.py --durations 5 -n 8

    # Remote spark, one pytest session
    $ pytest test_pyspark.py --durations 5 --pyspark spark://localhost:7077

    # Remote spark, 8 pytest sessions
    $ pytest test_pyspark.py --durations 5 --pyspark spark://localhost:7077 -n 8

Server mode setup
=================

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

