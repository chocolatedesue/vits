python app.py -m /mydata/G_first.pth -c /mydata/config.json 


docker run -itd \
--name demo \
-p 7860:7860   \
-v  /root/workspace/vits/logs/senbaka44_fix:/mydata \
ccdesue/vits_demo   /bin/bash