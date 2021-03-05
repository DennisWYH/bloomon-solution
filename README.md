# bloomon-solution
This repository contains a Docker image that can be build and run on any machine with Docker installed.
The application was written by Yunhai Wang. It is intended as a solution for bloomon's python interview task.
The command line applicaation is writen in Python3, to mimick a bouquet making process.

Please use below commands to run the Python command line application.
Environment: Make sure you have docker installed

Run:

```
sudo docker build -t bloomon-solution .
```
```
sudo docker run -it bloomon-solution BloomonBouquetMaker.py
```


Once you have run the above commands. You will be ask to key in values in the command line prompt.
Please follow the Bloonmon assignment task input format.

The application will be open to user's input all the time until interrupted.
User can keep inputing new flower arrival information, and as long as the flower numbers reach the criterial to make a bonquet,
a bonquet is made and print out via stdout.

The application can be interrupted and exited by Contrl z.

