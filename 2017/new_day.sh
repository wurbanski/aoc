#!/bin/bash

DAY=${1}
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR
test -d day${DAY} && exit 1
cp -rf template day${DAY}
cd day${DAY}
mv day{X,${DAY}}.py
mv test_day{X,${DAY}}.py
sed -i "s/\([dD]ay\)X/\1${DAY}/g" *.py
popd
