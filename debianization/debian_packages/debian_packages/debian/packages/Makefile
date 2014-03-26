# Example Makefile for .deb package building
PACKAGES := mypackage
GPGKEY := xyz

all: $(PACKAGES)
.PHONY: all

define DEBUILD
	(env -u LANG debuild --linda -tc -pgpg -sgpg -k$(GPGKEY) \
	 --lintian-opts -i --linda-opts -i && \
	 gzip -f ../$@*.build && echo "built ok" > ../$@)
endef

mypackage:
	cd $@-1.0 && $(DEBUILD)

