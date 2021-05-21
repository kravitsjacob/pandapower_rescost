#I. File list
```
.
|    test.py - Python script to demonstrate mismatch
|    Dockerfile - Docker file to run python script


#II. How to Run
1. Download and Run Docker Desktop. For more information on Docker visit: https://docs.docker.com/desktop/. To ensure 
that it is installed correctly go to the command prompt/terminal and enter $ docker --version
2. Change to the current working directory using command prompt/terminal $ cd <insert_pathto_data>
3. Build the docker image by running $ docker build --tag pandapower_test .
4. Run the image $docker run pandapower_test 