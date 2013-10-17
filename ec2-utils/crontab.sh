#!bin/bash
MAILTO="csvsoundsystem+mccrontab@gmail.com"
*/30 * * * * cd /home/ubuntu/mc-api/crawler/ && python crawl.py >> ../logs/crawl_log 2>> ../logs/crawl_err_log
