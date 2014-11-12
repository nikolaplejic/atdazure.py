# Using Microsoft Azure Services From Python on Linux

The idea is to run this on an Azure VM with Ubuntu 14.04, but in theory you can run this on your local machine or another "cloud" VM.

Examples cover Table Storage, SQL Database, Cache (Redis), and Service Bus. More to possibly come.

## SQL Database (Assuming Ubuntu / Debian)

`apt-get install unixodbc unixodbc-dev freetds-bin freetds-dev tdsodbc`

`/etc/odbcinst.ini`

    [FreeTDS]
    Description = FreeTDS Driver
    Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
    Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
    UsageCount = 1

`/etc/freetds/freetds.conf`

    # add this within the [global] section
    tds version = 7.1

    # add this at the end of the file
    # "azureSQL" can be changed to whatever you want
    [azureSQL]
      host = xxxxxxxx.database.windows.net
      port = 1433
      tds version = 7.1

`/etc/odbc.ini`

    # "azureSQL" is the same string as above
    [azure]
    Driver = FreeTDS
    Servername = azureSQL
    Database = mydb

## afterwards

    virtualenv --no-site-packages .
    source bin/activate
    pip install -r reqs.txt
    cp azurecfg.example.py azurecfg.py
    vim azurecfg.py # add your config settings...
    python app.py
