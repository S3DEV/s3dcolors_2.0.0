
# s3dcolors
---
This is a small centralised class libary for S3DEV colourmaps.  For complete design and functionality, refer to the class docstrings.


### V2 UPDATE
---
Version 2.0.0 introduces a complete overhaul from previous versions.  Aside from the module being renamed, the primary update is that this module is now a **class module**; so the results are no longer dictionary based, but class property based.


### INSTALLATION  
---  
Remember to replace s3dcolors\_**x.x.x** with the version you want.


#### LINUX
```bash
> sudo pip install git+https://github.com/s3dev/s3dcolors_x.x.x
```
or
```bash
> sudo python <path_to_package>/setup.py install
```

#### WINDOWS  
```bash
> pip install git+https://github.com/s3dev/s3dcolors_x.x.x
```
or 
```bash
> python <path_to_package>\setup.py install 
```

### USE
---
Here is a quick example of how the colours can be accessed, along with some parameter usage:

```python
>>> from s3dcolors.s3dcolors import CMaps
>>> cmap_clrs = CMaps.Colors(alpha=0.75, mode='rgb', drop_alpha=False)
>>> clrs_red = cmap_clrs.red
```

