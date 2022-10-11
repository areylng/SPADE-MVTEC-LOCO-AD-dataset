1. Download the MVTEC-LOCO-AD dataset from the MVTEC website. Then organize the MVTEC-LOCO-AD dataset into MVTEC-AD format. There may be multiple GTs for one image in the MVTEC-LOCO-AD dataset, we only need to take any one of them.
2. Change ````self.mvtec_folder_path```` in ````src/datasets/mvtec.py```` to your path of MVTEC LOCO AD dataset (**In MVTEC AD format**).
3. Change the ````--dateset_base_dir```` in ````src/O_evaluation/evaluate_experiment.py```` -> ````def parse_arguments()```` to your own MVTEC LOCO AD dataset path (the original LOCO dataset downloaded, **not in MVTEC AD format**).  
Change ````--anomaly_maps_dir```` to your own path (````log_metris```` folder is already included in this program!) .
4. Run main.py.   The evaluation code was taken from this [website](https://www.mvtec.com/company/research/datasets/mvtec-loco).

**There is generally no randomness in SPADE.  
The results of this project have a small difference in ROCAUC at the image level from the original paper, but a large difference at the pixel level.   
I don't know where is wrong, if you have any idea please leave a comment to discuss.**

|    |      Pixel-SPRO-AUC (Paper)      |  Pixel-SPRO-AUC (This Code) |  Image-ROC-AUC (Paper) |  Image-ROC-AUC (This Code) |
|----------|:-------------:|:------:|:------:|:------:|
| Breakfast Box |  0.372 | 0.143 | -|0.768 |
| Screw Bag |    0.331   |   0.421 | -|0.532 |
| Pushpins | 0.234 |    0.251 | -|0.569 |
| Splicing Connectors | 0.516 |   0.598 |- |0.778 |
| Juice Bottle |0.804 |    0.587 |- |0.88 |
| Mean |0.451 |   0.4 | 0.689 | 0.7054 |

 
