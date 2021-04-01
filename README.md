# Ps4 Syscon Read-Write helper

A python script using SYSGLITCH to dump Ps4 syscon and validate it - extract  512kb firmware and convert it to motorola s28 file format - write stock RL78 (using rl78flash)
Its time saving tool you will just need this script to read and write no need for other extrnal tools.

# How to use it : 
Step 1 [Read]:<br />
You must first check SYSGLITCH guide : https://github.com/VV1LD/SYSGLITCH then after you connect your syscon correctley run the script and go for step 1 <br />
if everythings goes well you will get a "syscon" full dump 3mb<~ and "syscon.mot" 512kb , if anything went wrong the script should show you "check your connections Something Wrong"<br />

Step 2 [Write]:<br />
you will need stock RL78 also check rl78flash: https://github.com/msalau/rl78flash then after you connect your RL78 correctley run the script and go for step 2

# Credits :
special thanks to VVildCard777 - Fail0verflow - droogie - juansbeck -Zecoxao - M4j0r - SSL - msalau <br />
Also special thanks to Abkarino for his always support
