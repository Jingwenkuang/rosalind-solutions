1. Restart the Container
    % docker start data-check 

2. Attach to the Running Container 
    % docker exec -it data-check /bin/bash

Option A: Inspect Logs
    % docker logs data-check
Option B: Create a New Container
    % docker run -it --name new-data-check -v /your/host/data:/data gencommand_image:arm64 /bin/bash
check container status
    % docker ps -a 
If the container won't start, rebuild it:
    % docker rm data-check
    % docker run -it --name data-check -v /your/data:/data your_image