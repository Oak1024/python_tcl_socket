# https://blog.csdn.net/MingRiDeYueMing/article/details/18084745
# it seems like a client code
# create a socket connection
set ip localhost
set port 6699

set sock [socket $ip $port]
puts $sock

# send a msg to server
set cmd "openall"
puts $sock $cmd
flush $sock

# receive feedback from server
set rec [gets $sock]
puts $rec

# close socket connection
close $sock