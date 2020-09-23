# CARLA Dash

### Introduction
CARLA Dash gives the CARLA simulator a Tesla-Like GUI to visualize things such as speed, current gear, steering position, time and more! The CARLA Dash runs its own Django based server which interacts with the CARLA client through CAN messaging. A sample client which is compatiable with the dash is provided in my modified-carla-client repo.

### Execute
To execute, simply run:
```python3 manage.py runserver 8001```

The 8001 port is optional. I found that my setup of CARLA was utilizing port 8000, so I used another one to run Django, however feel free to use any port. Then just go to your web browser and naviagte to the port you just opened! 

```127.0.0.1:8001```