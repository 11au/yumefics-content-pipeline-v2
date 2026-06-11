#!/bin/bash 
# tells system to run this file using bash

# Stores the full cron job string in a variable
CRON_JOB="0 9 1 * * /Users/lau/personal_projects/content_pipeline/venv/bin/python /Users/lau/personal/content_pipeline/generate.py >> /Users/lau/personal_projects/content_pipeline/output/pipeline.log 2>&1"

# copy existing cron jobs and add new one then save
#(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

#echo "Cron job added for generate.py - runs monthly at 9am"