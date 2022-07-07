# Machine_learning-_project
first machine learning project

Software needed
    1.Github Account(https://github.com)
    2.Heroku Account(https://dashboard.heroku.com/login)
    3.vs code IDE(https://code.visualstudio.com/download)
    4.GIT cli(https://git-scm.com/downloads)




creating conda enviornment
'''''
conda create -p venv python==3.7 -y
'''''
checking conda
''''
conda --version
''''
activate
'''
conda activate venv/
''
'''
pip install -r requirements.txt
''

Git 
1.add file
        git add# file name
        git add#f1,f2
        adding all files'''git add .
2.ignore file in gitignore
        check name of file or file by its name
3.Checking status
    git log
4.To create version or commit all the change
    git add.git commit-m
5.To send version/change to githubg
git push origin main
6.Get remote url
    git remote -v
    
"''''
To setup CI/CD pipeline we need 3 informations
    1.HEROKU_EMAIL- nimmymaths91@gmail.com
    2.API KEY- abc
    3.Heroku application name-ml-regressionapplnimmy

    Build docker image
    '''
    docker build -t  <image-name>:<tagname>.

    '''
    list docker images
    docker images
    ''''
    run images
    ''
    run docker images
    ....
    docker run -p 5000:5000 -e PORT=5000 f8c749e73678<image id>
    ''''
    To check running containners
    '''
    docker ps
    '''
To find container running
docker ps
......

To stop any  container
    '''
    docker stop <containerid>
    ''
'''
python setup.py install






