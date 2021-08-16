#!/bin/bash

# $1=length, default 10
function mutant-encrypt-random-hash() {
  local size
  local out
  [ -z "$1" ] && size=10 || size=$1
  out=$(
    head /dev/urandom | tr -dc A-Za-z0-9 | head -c $size
    echo ''
  )
  echo "$out"
}

# $1=file
# $2=password
function mutant-encrypt-encrypt() {
  # openssl enc -aes-256-cbc -in $1 -out $1.aes-256 -pass pass:$2
  tar --create --file - --gzip -- "$1" | \
  openssl aes-256-cbc -salt -out "$1.enc.aes-256-cbc"
}

# $1=filename in
# $2=filename out
function mutant-encrypt-decrypt() {
  # openssl enc -aes-256-cbc -d -in $1 >$2
  openssl aes-256-cbc -d -salt -in "$1" | \
  tar -v --extract --gzip --file -
}


# generate an ssh key
function mutant-ssh-generate-key() {
  local random_num
  dest_dir=$1
  random_num="$(mutant-encrypt-random-hash 10)"
  filename="/$dest_dir/$random_num"
  ssh-keygen -t rsa -b 4096 -f "$filename" -q -N ""
  echo "Key Generated: $random_num and $random_num.pub"
}


# generate an ssh key
function mutant-ssh-generate-key-static-name() {
  local random_num
  dest_dir=$1
  key_file="key"
  filename="/$dest_dir/$key_file"
  ssh-keygen -t rsa -b 4096 -f "$filename" -q -N ""
  chmod 600 "$filename"
  echo "Key Generated: $key_file and $key_file.pub"
}