Dataset **COCO 2017** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzIxNTFfQ09DTyAyMDE3L2NvY28tMjAxNy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJwc05HeXpTY2xmZ1lIL1QzN0ZKUUVwc3VyVVFCaXN5WmpYTnZjOEtGK1RJPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='COCO 2017', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [2017 Train images [118K/18GB]](http://images.cocodataset.org/zips/train2017.zip)
- [2017 Val images [5K/1GB]](http://images.cocodataset.org/zips/val2017.zip)
- [2017 Test images [41K/6GB]](http://images.cocodataset.org/zips/test2017.zip)
- [2017 Train/Val annotations [241MB]](http://images.cocodataset.org/annotations/annotations_trainval2017.zip)
