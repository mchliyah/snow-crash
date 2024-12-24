# Explanation for Level02
## Observations
1. after login to level02we can see the file level02.pcap which is a network capture file.
    It is a PCAP file which is a format used to store network traffic.
## Steps to Solve
1. we use the scp command to copy the file to our local machine.
```
    scp -P 4242 level02@xx.xx.xx.xx:/home/level02/level02.pcap ./level02.pcap
```
2. the wireshark is used to open the file and analyze the network traffic.
    after follow the request "tcp stream" we can see the password sent in the request.
    ```
        Linux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)

        ..wwwbugs login: l.le.ev.ve.el.lX.X
        ..
        Password: ft_wandr...NDRel.L0L
        .
    ```

3. the password ft_wandr...NDRel.L0L not working we suspect that the password is encoded or contain some special characters.
    we changed the data show to "hex Dump" and we can see the points are presented as 7f which means that the user is deliting some caracters after typin.
    we deleted the pints and the number of points caracters befor sowe got "ft_waNDReL0L" and here we go :
    ```
        level02@SnowCrash:~$ su flag02
        Password: 
        Don't forget to launch getflag !
        flag02@SnowCrash:~$ getflag
        Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
        flag02@SnowCrash:~$ 

    ```



