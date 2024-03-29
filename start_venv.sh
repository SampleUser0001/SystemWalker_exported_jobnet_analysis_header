#!/bin/bash

source venv/bin/activate

pushd app > /dev/null

ln -s $(pwd)/src/dev.env $(pwd)/src/.env

# 引数の数に応じて変更する
# bash start.sh $1 $2 ...
bash start.sh $1 $2

unlink $(pwd)/src/.env

popd > /dev/null

deactivate