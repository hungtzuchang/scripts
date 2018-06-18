#!/bin/sh

mv $1 ${1%ProcSpec}zip
unzip !$
rm OOI*

sed -n 3690,7337p ps_0.xml | sed 's/<double>//g' | sed 's/<.double>//g' > c1.tmp
sed -n 9,3656p ps_0.xml | sed 's/<double>//g' | sed 's/<.double>//g' > c2.tmp
sed -n 7613,11260p ps_0.xml | sed 's/<double>//g' | sed 's/<.double>//g' > >c3.tmp
paste c1.tmp c2.tmp c3.tmp > $2

rm c1.tmp c2.tmp c3.tmp

