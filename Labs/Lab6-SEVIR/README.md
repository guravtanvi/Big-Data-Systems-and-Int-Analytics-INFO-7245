## Big Data Systems and Int Analytics

## Labs

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 6 - SEVIR Notebook

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1vNgqhgxmw1UFJa9jKwn07PDTA4H4dlGgdeN5dnIyTXY#0

## About

**This lab demonstrates analyzing the results of training, visualizing the results on Synthetic Radar Data from SEVIR Dataset (Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology) using the pretrained models.**

## SEVIR Dataset


SEVIR is a collection of temporally and spatially aligned image sequences depicting weather events captured over the contiguous US (CONUS) by GOES-16 satellite and the mosaic of NEXRAD radars. Figure 1 shows a set of frames taken from a SEVIR event. SEVIR contains five image types: GOES-16 0.6 µm visible satellite channel (vis), 6.9 µm and 10.7 µm infrared channels (ir069, ir107), a radar mosaic of vertically integrated liquid (vil), and total lightning flashes collected by the GOES-16 geostationary lightning mapper (GLM) (lght).

![sevir-table](https://user-images.githubusercontent.com/59846364/109205287-64717180-7774-11eb-8f87-6018b7cdfc02.PNG)


Each event in SEVIR consists of a 4-hour length sequence of images sampled in 5 minute steps. The lightning modality is the only non-image type, and is represented by a collection of GLM lightning flashes captured in the 4 hour time window. SEVIR events cover 384 km x 384 km patches sampled at locations throughout the continental U.S. (CONUS). The pixel resolution in the images differ by image type, and were chosen to closely match the resolution of the original data. Since the patch dimension of 384 km is constant across sensors, the size of each image differs (as shown in Table 1).


![sevir-lab](https://user-images.githubusercontent.com/59846364/109205058-15c3d780-7774-11eb-937c-ae2ad6451fcf.PNG)



## Requirements

**Download the pretrained models and sample testing data:** 

```
wget -O models/synrad/gan_mae_weights.h5 "https://www.dropbox.com/s/d1e2p36nu4sqq7m/gan_mae_weights.h5?dl=1"
wget -O models/synrad/mse_vgg_weights.h5 "https://www.dropbox.com/s/a39ig25nxkrmbkx/mse_vgg_weights.h5?dl=1"
wget -O models/synrad/mse_weights.h5 "https://www.dropbox.com/s/6cqtrv2yliwcyh5/mse_weights.h5?dl=1"
wget -O data/sample/synrad_testing.h5 "https://www.dropbox.com/s/7o3jyeenhrgrkql/synrad_testing.h5?dl=1"
```




## Test Results

`AnalyzeSyntheticRadar.ipynb`

Reproducing Reference Notebook: https://github.com/MIT-AI-Accelerator/neurips-2020-sevir/blob/master/notebooks/AnalyzeSyntheticRadar.ipynb

After running the trained models on samples from the test set, we used the basic color maps and loaded part (1000 data points) of the test dataset, ran the model and finally plotted output loss along with inputs using default cmap which ideally resulted in the following cmap:

Three examples of the synthetic weather radar model trained using three different loss functions. MSE leads to an accurate, albeit overly smoothed, prediction. The content and adversarial losses are able to provide additional textures that are visually more similar to the target.


![sevir-result](https://user-images.githubusercontent.com/59846364/109205677-eb264e80-7774-11eb-841c-2a0fa4ad7097.PNG)





