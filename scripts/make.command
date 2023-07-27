#!/usr/bin/open -a Terminal
{ set +x; } 2>/dev/null

{ set -x; cd "${0%/*/*}"; { set +x; } 2>/dev/null; }

( set -x;make )
