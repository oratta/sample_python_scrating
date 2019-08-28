import urllib.request as req
import gzip, os, os.path

save_path = "./mnist"
base_url = "http://yann.lecun.com/exdb/mnist"

files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",]

if not os.path.exists(save_path): os.mkdir(save_path)

for f in files:
    url = base_url + "/" + f
    loc = save_path + "/" + f
    print("download:" + url)
    if not os.path.exists(loc):
        req.urlretrieve(url,loc)

    raw_file = save_path + "/" + f.replace(".gz", "")
    print("gzip:",f)
    with gzip.open(loc, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)

print("ok")