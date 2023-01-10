# Web_File_Mgr_hw
## Setup
In order to set up the Docker containers and application, do the following:

1. Extract/unzip web_hw_files.zip: [https://github.com/elijahbartolome/Web_FMgr_soln/blob/master/web_hw_files.zip](https://github.com/elijahbartolome/Web_FMgr_soln/blob/master/web_hw_files.zip)

2. Paste the unzipped folder to db directory (so the directory structure will look like `Web_FMgr_soln/db/web_hw_files`)

3. Run `docker-compose up -d` in root directory (which should contain `docker-compose.yml`)

4. Go to [localhost:5000](localhost:5000) on a web browser

## How to use
* Click on a red folder to expand/collapse branches

* Click on a green file to preview contents. The preview will be in a panel at the top of the page

* Click on Download next to a green file to download the file