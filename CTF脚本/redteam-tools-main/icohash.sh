#!/bin/bash
target="$1"
start(){
     echo "$target hash:"
     curl -s -L -k $target | python3 -c 'import mmh3,sys,codecs; print(mmh3.hash(codecs.encode(sys.stdin.buffer.read(),"base64")))'
}
start
exit 1