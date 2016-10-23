import os
import paramiko
import sys
import subprocess

if len(sys.argv) != 2:
    print "args missing"
    sys.exit(1)


# user defined parameter below:
hostname = 'lp02.cci.rpi.edu'
password = sys.argv[1];
username = 'ACMEtany'
port = 22
outputnamePrefix = 'log_'
remoteDirPrefix = '/gpfs/u/scratch/ACME/ACMEtany/MSMSEpaper/'
localDir = '/Users/yixuantan/Documents/RPIresearches/Papers/MSMSE2016/SourceDataUpdatedOct2016/'
startFolderNumber = 1;
endFolderNumber = 10;
# user defined parameter above

lambdas = ['4', '16']
folderName = ['CuFilmRadhak/', 'CuFilmNewAlgo/', 'CuFilmGodfrey/']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)
sftp = ssh.open_sftp()

for lbd in lambdas:
    for folderNumber in range(startFolderNumber, endFolderNumber + 1, 1):
        for fdName in folderName:
            remoteDir = remoteDirPrefix + str(lbd) + 'lambda/' + str(fdName) + str(folderNumber) +'/'
            sftp.chdir(remoteDir)
            outputName = localDir + str(lbd) + 'lambda/' + str(fdName) + outputnamePrefix + str(folderNumber) + '.txt'
            fileName = remoteDir + 'log.log'
            print 'fileName is \n', fileName
            print 'outputname is \n', outputName
            sftp.get(fileName, outputName)
            

