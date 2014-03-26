# This file contains everything that autoconf guessed for your system.
# if you want you can edit it, just don't re-run configure.

PACKAGE = apt

# C++ compiler options
CC = gcc
CPPFLAGS+= -D_FORTIFY_SOURCE=2 -DHAVE_CONFIG_H -D_REENTRANT -Wall
CXX = g++
CXXFLAGS+= -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security -Werror=format-security
NUM_PROCS = 4

# Linker stuff
PICFLAGS+= -fPIC -DPIC
LFLAGS+= -Wl,-Bsymbolic-functions -Wl,-z,relro
LEFLAGS+= 
SOCKETLIBS:= 
AR:=ar
RANLIB:=ranlib

# Dep generation - this only works for gnu stuff
GCC3DEP = yes
INLINEDEPFLAG = -MD

# Debian doc stuff
DEBIANDOC_HTML = /usr/bin/debiandoc2html
DEBIANDOC_TEXT = /usr/bin/debiandoc2text

DOXYGEN = /usr/bin/doxygen

# xsltproc for the man pages
XSLTPROC := /usr/bin/xsltproc

# po4a for the man pages
PO4A := /usr/bin/po4a

# Gettext settings
GMSGFMT = /usr/bin/msgfmt
XGETTEXT = /usr/bin/xgettext
MSGCOMM:=$(dir $(XGETTEXT))/msgcomm
MSGMERGE:=$(dir $(XGETTEXT))/msgmerge
BASH = /bin/sh

# Various library checks
PTHREADLIB = 
PYTHONLIB = @PYTHONLIB@
PYTHONVER = @PYTHONVER@
PYTHONPREFIX = @PYTHONPREFIX@
PYTHONEXECPREFIX = @PYTHONEXECPREFIX@
PYTHONINCLUDE = @PYTHONINCLUDE@
BDBLIB = -ldb
INTLLIBS = 

# Shim Headerfile control
HAVE_C9X = yes
HAVE_STATVFS = yes
HAVE_TIMEGM = 
NEED_SOCKLEN_T_DEFINE = 

# Shared library things
HOST_OS = linux-gnu
ifneq ($(words $(filter gnu% linux-gnu% kfreebsd-gnu% %-gnu,$(HOST_OS))),0)
   SONAME_MAGIC=-Wl,-soname -Wl,
   LFLAGS_SO=
else
   # Do not know how to create shared libraries here.
   ONLYSTATICLIBS = yes
endif
	
