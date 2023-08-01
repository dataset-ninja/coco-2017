Dataset **COCO 2017** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/J/1a/IUgRHxaDmeicWEv4d7xNeFymUl3svXvcMHD9r1A5aiH8hlsGgKIpM80LLL4U3DxRTX1ci6mtrEZXrHeaXUVjUweyK1MER2Wwvu3Nd6Z9TvJzxE3tbjV7b5gL5X73.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='COCO 2017', dst_dir='~/dataset-ninja/')
```
The data in original format can be downloaded here:

- [2017 Train images [118K/18GB]](http://images.cocodataset.org/zips/train2017.zip)
- [2017 Val images [5K/1GB]](http://images.cocodataset.org/zips/val2017.zip)
- [2017 Test images [41K/6GB]](http://images.cocodataset.org/zips/test2017.zip)
- [2017 Train/Val annotations [241MB]](http://images.cocodataset.org/annotations/annotations_trainval2017.zip)
