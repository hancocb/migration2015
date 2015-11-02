#!/usr/bin/perl
#    Copyright (C) 2000 Sinclair InterNetworking Services Pty Ltd
#    <nmis@sins.com.au> http://www.sins.com.au/nmis
# Version 1.0 - 1 April 2002
# Version 2.0 - 9 April 2002 - renames the files for you
# Converts DOS files to Unix
# ie. removes ^M

my $inputfile=shift || &oops("No such file") ;
unless (-f $inputfile) { &oops("$inputfile does not exist\n") ;}
my $outputfile="ThisIsATempFile" ;
open (IN,$inputfile) || die "Cannot open $inputfile" ;
open  (OUT,"> $outputfile") || die "Cannot write to $outputfile  - check permissions\n" ;
while (<IN>) {
	$_=~ s/\r//g ;
	print OUT ;
}
close (OUT) ;
close (IN) ;

if ( -f $outputfile ) { 
rename ($inputfile, "$inputfile.bak") || die "Cannot create .bak of $inputfile" ;
rename ($outputfile, $inputfile) || die "Cannot rename $outputfile to $inputfile" ;
}

exit ;

				


sub oops {
	my $error=shift ;
	print "$error\n" ;
	print "Usage: dos2unix.pl dosfile\n" ;
	exit ;
}
