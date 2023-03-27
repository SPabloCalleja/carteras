# GROBID

## GROBID SERVER

To run GROBID SERVER the best option is to do through Docker. First, install docker and then run the image through the command


```console
docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```


## GROBID CLIENT


To install the Python library: 


```console
git clone https://github.com/kermitt2/grobid_client_python
cd grobid_client_python
python3 setup.py install
```

Then, the Python code can be executed:

```console
python grobid_exec.py
```
