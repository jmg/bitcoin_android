DIR=${PWD}
cd ../python-for-android/dist/default/

python build.py \
    --dir=$DIR \
    --name=bitcoin \
    --version=1.0 \
    --permission INTERNET \
    --permission WRITE_EXTERNAL_STORAGE \
    --orientation=portrait \
    --package=org.demo.bitcoin \
    debug installd