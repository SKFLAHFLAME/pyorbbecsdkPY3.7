# CMake generated Testfile for 
# Source directory: /home/pi/pyorbbecsdk
# Build directory: /home/pi/pyorbbecsdk/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_context "/usr/bin/python3.7" "-v" "/home/pi/pyorbbecsdk/test/test_context.py")
set_tests_properties(test_context PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/pyorbbecsdk/CMakeLists.txt;90;add_test;/home/pi/pyorbbecsdk/CMakeLists.txt;0;")
add_test(test_device "/usr/bin/python3.7" "-v" "/home/pi/pyorbbecsdk/test/test_device.py")
set_tests_properties(test_device PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/pyorbbecsdk/CMakeLists.txt;90;add_test;/home/pi/pyorbbecsdk/CMakeLists.txt;0;")
add_test(test_pipeline "/usr/bin/python3.7" "-v" "/home/pi/pyorbbecsdk/test/test_pipeline.py")
set_tests_properties(test_pipeline PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/pyorbbecsdk/CMakeLists.txt;90;add_test;/home/pi/pyorbbecsdk/CMakeLists.txt;0;")
add_test(test_sensor_control "/usr/bin/python3.7" "-v" "/home/pi/pyorbbecsdk/test/test_sensor_control.py")
set_tests_properties(test_sensor_control PROPERTIES  _BACKTRACE_TRIPLES "/home/pi/pyorbbecsdk/CMakeLists.txt;90;add_test;/home/pi/pyorbbecsdk/CMakeLists.txt;0;")
