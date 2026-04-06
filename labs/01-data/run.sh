make clean && make -j

if [ "$1" == "test" ]; then
  ./btest "$@"
else
  gdb -q
fi
