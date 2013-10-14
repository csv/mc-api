#/bin/bash
mv ec2-utils/install-redis.sh ../
cd ../
sudo sh install-redis.sh
sudo yum install python27
sudo easy_intall pip
cd mc-api
sudo pip install -r requirements.pip
