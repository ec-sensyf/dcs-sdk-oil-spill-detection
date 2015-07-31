## SenSyF SDK - Oil Spill Detection

### Description

This repository contains the SDK application for oil spills detection using Sentinel-1 data.

**IDEA**: Get Sentinel-1 data from the catalogue, for a time interval, tile the products and detect oil spills generating a KML file for each one.
      The parallelization on Hadoop for this usecase is performed by product during the first job (data access and tile) and by tile during the second job (oil spill detection) .

**Region of interest**: Mediterranean Sea

--------------

### Instructions

1. Before enter on the sandbox run on your local machine:

      ```bash
      ssh-add < username >.pem      
      ```

2. Enter on the sandbox:

      ```bash
      ssh -A -i < username.pem > sensyf-sdk@< sandbox_host >
      ```

3. Run the following commands:

      ```bash
      cd
      git clone https://github.com/ec-sensyf/dcs-sdk-oil-spill-detection.git
      cd dcs-sdk-cloud2
      mvn install
      ```

--------------

Copyright (C) DEIMOS Engenharia S.A.
