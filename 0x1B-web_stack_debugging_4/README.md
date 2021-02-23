# 0x1B. Web stack debugging #4

## Learning objectives

Detect server problems using debbuging tools. In this case detect why from 2000 request to serve static content, 50% of the request were not completed. The key was the max of opened files allowed for nginx. This parameter was changed for 15 documents to 2000.