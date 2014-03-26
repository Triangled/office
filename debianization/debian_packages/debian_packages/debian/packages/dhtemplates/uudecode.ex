#!/usr/bin/perl
# since .deb packages cannot (yet) add binary data, you have to uuencode
# it. This script is a tiny uudecode program, suitable to be added to the
# .deb package and called by debian/rules.
# It needs no additional dependencies since Perl is an essential package.
$_ = <> until ($mode,$file) = /^begin\s*(\d*)\s*(\S*)/;
open(OUT,"> $file") if $file ne "";
while (<>) {
    last if /^end/;
    next if /[a-z]/;
    next unless int((((ord() - 32) & 077) + 2) / 3) ==
                int(length() / 4);
    print OUT unpack "u", $_;
}
chmod oct $mode, $file;
