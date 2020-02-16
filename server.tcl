# https://blog.csdn.net/weixin_30433075/article/details/96757443
#https://www.cnblogs.com/greencolor/archive/2010/12/08/1900773.html

proc accept {chan addr port} {
puts "$addr:$port says [gets $chan]"
puts $chan goodbye
close $chan
}
socket -server accept 6699
vwait forever


# http://blog.sina.com.cn/s/blog_487685e50100m4mj.html
# TCL语言进行socket编程