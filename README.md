# dpa
dpa is Profile adder for Huawei dslam's with single Line command
## requirements
- python +3
- paramiko ssh
- Make sure you have a Stable Connection with your dslam ( check reachability and ssh before using this app )
### usage
usage ) python pch.py <ip> <username> <password> <profilenumber> <mindownrate> <maxdownrate> <minuprate> <maxuprate> [mindownsnr] [maxdownsnr] [minupsnr] [maxupsnr] [downtarget] [uptarget]
  
> [ ] is optional(leave it or fill all)
> <> Must be filled
  
### Example
python .\pch.py 10.11.12.13 admin admin123 12 31 12228 31 1024 0 31 0 31 12 12
### Contact
  contact with me on telegram for customization or other devices
  @ali_shjb

