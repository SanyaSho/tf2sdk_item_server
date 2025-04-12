#!/bin/bash
$PWD/protobuf-2.6.1/bin/win64/2015/staticcrt/release/protoc.exe --proto_path=$PWD --python_out=$PWD --proto_path=$PWD/protobuf-2.6.1/src $PWD/gcsdk.proto
