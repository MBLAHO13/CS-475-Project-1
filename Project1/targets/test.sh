echo "Test 0"
python sol0.py | ./target0

echo "Test 1"
python sol1.py | ./target1

echo "Test 2"
./target2 $(python sol2.py)

echo "Test 3"
./target3 $(python sol3.py)

echo "Test 4"
python sol4.py > tmp; ./target4 tmp

echo "Test 5"
./target5 $(python sol5.py)

echo "Test 6"
./target6 $(python sol6.py)

echo "Test 7"
./target7 "$(python sol7.py 1)" "$(python sol7.py 2)" "$(python sol7.py 3)"

echo "Test 8"
./target8 "$(python sol8.py)"
