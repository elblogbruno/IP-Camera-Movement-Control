# IP-Camera-Movement-Control
This python api allows you to control a chinese Camera movement.
Exactly the WansCam Model XHA402DA2, but maybe you can reverse engineer as I did thanks to the browser developer mode, and modify the api camera endpoints accordingly.
For example on this cam the url was like this

http://{CAMERA IP}/decoder_control.cgi?command={UP,DOWN,LEFT,STOP,CODE}

Also this camera needed to go up and in a short specified time period to send the STOP code, so that is why you are able to put a TIME variable when calling MoveCamera.
The less time the less the camera moves.
