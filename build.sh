#!/bin/bash

export DEBUG=True
export SECRET_KEY="2HY>fXi!dQ&(9Vf.XghCa;L6G=Ul4r-Bwqh>ae0RG3vIh1ZJ%T"
export QLDB_ENABLED="TRUE"  # Toggles QLDB on or off.
export qldb_name="fEMR-OnChain-Test"
export ADMIN_NAME=""
export ADMIN_EMAIL=""
export EMAIL_HOST=""
export EMAIL_PORT=""
export EMAIL_USERNAME=""
export EMAIL_PASSWORD=""
export DEFAULT_FROM_EMAIL=""
export SERVER_EMAIL=""

function all() {
  pip3 install -r requirements.txt
  python3 -m safety check -r requirements.txt
  python3 manage.py check
  # documents
  migrate
  static
  run_tests
  pushd ./main/static/main/js
  npm install
  popd
  static
}

function run_tests() {
  python3 manage.py test main.tests
}

function clean() {
  rm -rf main/migrations/*
  files=$(find . -name "__pycache__")
  files2=$(find . -iregex ".*\.\(pyc\)")
  rm -rf ${files2}
  rm -rf ${files}
}

function migrate() {
  pwd
  python3 manage.py makemigrations main
  python3 manage.py makemigrations appMR
  python3 manage.py makemigrations
  python3 manage.py migrate
}

function makemigrations() {
  python3 manage.py makemigrations main
  python3 manage.py makemigrations appMR
  python3 manage.py makemigrations
}

function static() {
  python3 manage.py collectstatic
}

function run() {
  python3 manage.py runserver 0.0.0.0:8081
}

function documents() {
  pushd docs || exit
  make html
  cp -r build/html/* .
  popd
}

function reset_migrations() {
  python3 manage.py migrate --fake main
  python3 manage.py showmigrations
  rm -rf main/migrations
  python3 manage.py migrate --fake-initial
  python3 manage.py showmigrations
}

function setup() {
  python3 manage.py creategroups
  python3 manage.py createadmin
}

function createsuperuser() {
  python3 manage.py createsuperuser
}

function shell() {
  python3 manage.py shell
}

case "$1" in

startapp)
  python3 manage.py startapp $2
  ;;

clean)
  clean
  ;;

migrate)
  migrate
  ;;

test)
  run_tests
  ;;

run)
  run
  ;;

setup)
  all
  setup
  ;;

all-run)
  all
  run
  ;;

all)
  all
  ;;

reset_migrations)
  reset_migrations
  ;;

makemigrations)
  makemigrations
  ;;

createsuperuser)
  createsuperuser
  ;;

shell)
  shell
  ;;

esac
