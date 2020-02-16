# http://blog.sina.com.cn/s/blog_690878d501018udj.html

set socketid [socket localhost 9999];
fconfigure $socketid -buffering line
puts $socketid "hello";
gets $socketid msg
% set msg
invalid command name "hello"
puts $socketid "print hello"
gets $socketid msg
% set msg
Fri Sep 03 11:28:47 +0800 2010  hello
puts $socketid "compute 1+1"
gets $socketid msg
% set msg
expr(1+1)=2
