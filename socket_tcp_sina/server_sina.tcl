proc print {msg} {
return [clock format [clock seconds]]\t$msg
}
proc compute {args} {
return "expr\($args)=[expr $args]"
}

fileevent $socketid readable [list readcallback $socketid]
fileevent $socketid writable [list writecallback $socketid]
socket -server callback 9999;
proc callback {socketid addr port} {
fconfigure $socketid -blocking 0 -buffering line;#非阻塞模式 按行flush
fileevent $socketid readable [list readcallback $socketid];
}
proc readcallback {socketid} {
if {[eof $socketid] || [catch {gets $socketid line} err]} {
close $socketid;
} else {
#deal with line; suppose line is tcl scripts eval it and return the results
puts line=$line
if {[catch {eval $line} err]} {
puts $socketid $err
} else {
puts $socketid $err
}
}
}
vwait forever