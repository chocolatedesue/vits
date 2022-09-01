python app.py -m /mydata/G_second.pth -c /mydata/config.json 


docker run -itd \
--name demo \
-p 7860:7860   \
-v  /home/ubuntu/workspace/vits/logs/19:/mydata \
ccdesue/vits_demo   /bin/bash