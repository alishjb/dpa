from sys import argv
import paramiko
import time
from paramiko import ssh_exception
def SSHfunction(ip,username,password,profilenumber,mindownrate,maxdownrate,minuprate,maxuprate,mindownsnr=0,maxdownsnr=31,minupsnr=0,maxupsnr=31,downtarget=12,uptarget=12):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=22, username=username, password=password)
        print('Connected to dslam,Please Wait...')
        remote = ssh.invoke_shell()
        time.sleep(1)
        remote.send('\n')
        time.sleep(1)
        remote.send('enable \n')
        time.sleep(1)
        remote.send('config \n')
        time.sleep(1)
        remote.send(f'adsl line-profile add {profilenumber} \n')
        print('25% done , please wait...')
        time.sleep(1)
        #setting adsl2+(default dslam number 1)
        remote.send('\n')
        time.sleep(.5)
        #setting basic conf with n    
        remote.send('\n')  
        time.sleep(.5)
        #setting channel mode to interleaved
        remote.send('\n')  
        time.sleep(.5)
        #delay = No
        remote.send('\n')  
        time.sleep(.5)
        #adapt on startup
        remote.send('\n')  
        time.sleep(.5)
        #adapt on startup
        remote.send('\n')  
        time.sleep(.5)
        #setting snr 
        remote.send(f'y')
        time.sleep(.5)
        remote.send('\n') 
        #sending downstream target snr
        print('50% done , please wait...')
        remote.send(f'{downtarget}')
        time.sleep(.5)
        remote.send('\n')  
        #sending downstream min target snr
        remote.send(f'{mindownsnr}')
        time.sleep(.5)
        remote.send('\n')  
        #sending downstream max target snr
        remote.send(f'{maxdownsnr}')
        time.sleep(.5)
        remote.send('\n')  
        #sending upstream target snr
        remote.send(f'{uptarget}')
        time.sleep(.5)
        remote.send('\n')  
        #sending upstream min target snr
        remote.send(f'{minupsnr}')
        time.sleep(.5)
        remote.send('\n')  
        #sending upstream max target snr
        remote.send(f'{maxupsnr}')
        time.sleep(.5)
        remote.send('\n')  
        #setting rate 
        remote.send(f'y')
        time.sleep(.5)
        remote.send('\n') 
        #minimum downstream rate
        remote.send(f'{mindownrate}')
        time.sleep(.5)
        remote.send('\n')  
        #maximum downstream rate
        remote.send(f'{maxdownrate}')
        time.sleep(.5)
        remote.send('\n')
        #minimum upstream rate
        remote.send(f'{minuprate}')
        time.sleep(.5)
        remote.send('\n')  
        #maximum upstream rate
        remote.send(f'{maxuprate}')
        print('75% done , almost there...')
        remote.send('\n')
        time.sleep(.5)
        remote.send('save \n')
        time.sleep(1)
        remote.send('quit \n')
        time.sleep(1)
        remote.send('quit \n')
        time.sleep(1)
        buff = remote.recv(65535)
        res = buff.decode()
        remote.send('y')
        time.sleep(1)
        remote.send('\n')
        result = str(res)
        successful = f"Add profile {profilenumber} successfully"
        exist='Failure: The profile has existed'
        if successful in result:
            return f'Profile {profilenumber} Added Successfully','without any error'
        if exist in result:
            return f'Profile number {profilenumber} existed,Use another Profile number','without any error'
        else:
            return 'Something Went Wrong,Try again',result

    except ssh_exception.AuthenticationException:
        return "Authentication Failed , please Check your Cred's"
def help():
    print('''
    -------------------------------------------
    -------------------------------------------
    -----------Profile Changer Usage-----------
    -------------------------------------------
    -------------------------------------------
    -Works on huawei ma5616(MA5616V800R312C00)(tested)
    -Works with python +3 (use 3.10.0)
    -Make sure 
    -h ) Show help Message
    -r ) requirement (Must be installed before use)
    -u ) usage
    usage ) python pch.py <ip> <username> <password> <profilenumber> <mindownrate> <maxdownrate> <minuprate> <maxuprate> [mindownsnr] [maxdownsnr] [minupsnr] [maxupsnr] [downtarget] [uptarget]
    *) [] is optional(leave it or fill all)
    *) <> Must be filled
    Example ) python .\pch.py 10.11.12.13 admin admin123 12 31 12228 31 1024 0 31 0 31 12 12
    ''')
def usage():
    print(
    '''
    usage ) python pch.py <ip> <username> <password> <profilenumber> <mindownrate> <maxdownrate> <minuprate> <maxuprate> [mindownsnr] [maxdownsnr] [minupsnr] [maxupsnr] [downtarget] [uptarget]
    *) [] is optional(leave it or fill all)
    *) <> Must be filled
    Example ) python .\pch.py 10.11.12.13 admin admin123 12 31 12228 31 1024 0 31 0 31 12 12
    ''')
if len(argv) == 1:
    help()
if argv[1] == '-h':
    help()
if argv[1] == '-u':
    usage()
if len(argv) > 1:
    try:
        ip=argv[1]
        usern=argv[2]
        passwd=argv[3]
        profilenumber=argv[4]
        mindownrate=argv[5]
        maxdownrate=argv[6]
        minuprate=argv[7]
        maxuprate=argv[8] 
        mindownsnr=argv[9] or None
        if int(mindownsnr) > 0:
            mindownsnr = '0'
        maxdownsnr=argv[10] or None
        if int(maxdownsnr) > 31:
            maxdownsnr = '31'
        minupsnr=argv[11] or None
        if int(minupsnr) < 0 :
            minupsnr ='0'
        maxupsnr=argv[12] or None
        if int(maxupsnr) > 31:
            maxupsnr='31'
        downtarget=argv[13] or None
        uptarget=argv[14] or None
        res,err = SSHfunction(ip,usern,passwd,profilenumber=profilenumber,mindownrate=mindownrate,maxdownrate=maxdownrate,minuprate=minuprate,maxuprate=maxuprate,mindownsnr=mindownsnr,maxdownsnr=maxdownsnr,minupsnr=minupsnr,maxupsnr=maxupsnr,downtarget=downtarget,uptarget=uptarget)
        print(res,err)
    except IndexError:
        print('Wrong input,Use -h for help')
