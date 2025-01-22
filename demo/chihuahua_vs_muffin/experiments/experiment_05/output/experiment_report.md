# <span style="color:rgb(105, 169, 201);">Experiment Report: Chihuahua vs Muffin Test Experiment</span>

## <span style="color:rgb(105, 169, 201);">Metadata</span>

*    *Description*: In this experiment, transfer learning techniques is used with MobileNetV2 as the base model.

*    *Start Time*: 2024-10-23 08:22:04

*    *Total Duration*: 0:38:27.281

*    *Directory*: [Link](./.)


<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">Initial Visualizations</span>

![history_of_best_3_trials](./history_of_best_3_trials.png)

## <span style="color:rgb(105, 169, 201);">Summary</span>

### <span style="color:rgb(105, 169, 201);">Hyperparameters</span>

|               | dense_units   | dropout_rate  | learning_rate | Chapters      |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| trial_21      | 512           | 0.3730        | 1.3844e-04    | [Chapter](#trial_21) | 
| trial_15      | 512           | 0.3499        | 1.7879e-04    | [Chapter](#trial_15) | 
| trial_17      | 512           | 0.0149        | 5.9917e-05    | [Chapter](#trial_17) | 
| trial_37      | 512           | 0.4726        | 3.1889e-04    | [Chapter](#trial_37) | 
| trial_39      | 512           | 0.1508        | 4.2027e-05    | [Chapter](#trial_39) | 
| trial_81      | 256           | 0.3878        | 3.8357e-05    | [Chapter](#trial_81) | 
| trial_100     | 256           | 0.4836        | 6.5734e-05    | [Chapter](#trial_100) | 
| trial_3       | 512           | 0.0843        | 2.7931e-04    | [Chapter](#trial_3) | 
| trial_33      | 512           | 0.2181        | 5.2672e-05    | [Chapter](#trial_33) | 
| trial_40      | 512           | 0.4087        | 7.6301e-05    | [Chapter](#trial_40) | 
| trial_46      | 256           | 0.4707        | 5.6318e-05    | [Chapter](#trial_46) | 
| trial_55      | 256           | 0.4742        | 1.2641e-04    | [Chapter](#trial_55) | 
| trial_61      | 256           | 0.0412        | 9.2436e-05    | [Chapter](#trial_61) | 
| trial_4       | 512           | 0.4680        | 7.1570e-05    | [Chapter](#trial_4) | 
| trial_5       | 512           | 0.0783        | 5.5250e-04    | [Chapter](#trial_5) | 
| trial_6       | 512           | 0.2954        | 7.1180e-04    | [Chapter](#trial_6) | 
| trial_10      | 256           | 0.3988        | 9.6096e-04    | [Chapter](#trial_10) | 
| trial_16      | 128           | 0.1997        | 4.7826e-05    | [Chapter](#trial_16) | 
| trial_28      | 512           | 0.3810        | 1.0984e-04    | [Chapter](#trial_28) | 
| trial_36      | 512           | 0.4317        | 1.1203e-04    | [Chapter](#trial_36) | 
| trial_49      | 512           | 0.0922        | 2.6655e-04    | [Chapter](#trial_49) | 
| trial_54      | 256           | 0.4976        | 6.5576e-05    | [Chapter](#trial_54) | 
| trial_73      | 512           | 0.3555        | 3.9509e-05    | [Chapter](#trial_73) | 
| trial_76      | 512           | 0.3458        | 3.0282e-05    | [Chapter](#trial_76) | 
| trial_85      | 512           | 0.4411        | 1.0764e-04    | [Chapter](#trial_85) | 
| trial_1       | 512           | 0.2624        | 7.9696e-05    | [Chapter](#trial_1) | 
| trial_8       | 512           | 0.1308        | 5.8907e-04    | [Chapter](#trial_8) | 
| trial_9       | 256           | 0.3292        | 7.0295e-05    | [Chapter](#trial_9) | 
| trial_12      | 128           | 0.3482        | 9.1874e-05    | [Chapter](#trial_12) | 
| trial_14      | 256           | 0.2000        | 1.9858e-04    | [Chapter](#trial_14) | 
| trial_25      | 512           | 0.3976        | 3.2110e-05    | [Chapter](#trial_25) | 
| trial_34      | 512           | 0.1719        | 8.2208e-05    | [Chapter](#trial_34) | 
| trial_43      | 512           | 0.3694        | 2.9045e-05    | [Chapter](#trial_43) | 
| trial_48      | 512           | 0.2353        | 1.5418e-04    | [Chapter](#trial_48) | 
| trial_50      | 256           | 0.4913        | 7.0991e-05    | [Chapter](#trial_50) | 
| trial_63      | 512           | 0.2742        | 3.3489e-05    | [Chapter](#trial_63) | 
| trial_64      | 512           | 0.3187        | 6.1486e-05    | [Chapter](#trial_64) | 
| trial_70      | 512           | 0.4798        | 2.1450e-05    | [Chapter](#trial_70) | 
| trial_79      | 512           | 0.2290        | 2.2220e-05    | [Chapter](#trial_79) | 
| trial_82      | 512           | 0.4596        | 5.1544e-05    | [Chapter](#trial_82) | 
| trial_84      | 512           | 0.4149        | 8.5533e-05    | [Chapter](#trial_84) | 
| trial_86      | 512           | 0.4647        | 5.6658e-05    | [Chapter](#trial_86) | 
| trial_95      | 256           | 0.3430        | 4.8117e-05    | [Chapter](#trial_95) | 
| trial_98      | 512           | 0.4677        | 4.4193e-05    | [Chapter](#trial_98) | 
| trial_13      | 256           | 0.4925        | 4.6471e-05    | [Chapter](#trial_13) | 
| trial_23      | 512           | 0.4549        | 1.6903e-05    | [Chapter](#trial_23) | 
| trial_24      | 512           | 0.4988        | 3.9520e-05    | [Chapter](#trial_24) | 
| trial_27      | 512           | 0.3048        | 2.3184e-05    | [Chapter](#trial_27) | 
| trial_29      | 512           | 0.4617        | 3.6306e-05    | [Chapter](#trial_29) | 
| trial_30      | 512           | 0.2459        | 6.4885e-05    | [Chapter](#trial_30) | 
| trial_45      | 512           | 0.3954        | 3.6010e-05    | [Chapter](#trial_45) | 
| trial_53      | 256           | 0.4248        | 4.6276e-05    | [Chapter](#trial_53) | 
| trial_58      | 256           | 0.4091        | 4.9585e-05    | [Chapter](#trial_58) | 
| trial_72      | 512           | 0.3449        | 3.1388e-05    | [Chapter](#trial_72) | 
| trial_75      | 512           | 0.3820        | 2.4419e-05    | [Chapter](#trial_75) | 
| trial_83      | 512           | 0.4323        | 6.9865e-05    | [Chapter](#trial_83) | 
| trial_87      | 512           | 0.3099        | 5.6631e-05    | [Chapter](#trial_87) | 
| trial_97      | 256           | 0.4031        | 5.2903e-05    | [Chapter](#trial_97) | 
| trial_99      | 512           | 0.1753        | 3.9522e-05    | [Chapter](#trial_99) | 
| trial_32      | 512           | 0.2554        | 6.3071e-05    | [Chapter](#trial_32) | 
| trial_47      | 512           | 0.3365        | 1.9859e-05    | [Chapter](#trial_47) | 
| trial_52      | 256           | 0.4495        | 7.5983e-05    | [Chapter](#trial_52) | 
| trial_60      | 256           | 0.3935        | 4.2434e-05    | [Chapter](#trial_60) | 
| trial_62      | 256           | 0.3612        | 2.6502e-05    | [Chapter](#trial_62) | 
| trial_69      | 512           | 0.4175        | 1.1297e-05    | [Chapter](#trial_69) | 
| trial_78      | 512           | 0.2987        | 1.4558e-05    | [Chapter](#trial_78) | 
| trial_89      | 256           | 0.4017        | 4.4728e-05    | [Chapter](#trial_89) | 
| trial_90      | 256           | 0.3985        | 4.4637e-05    | [Chapter](#trial_90) | 
| trial_91      | 128           | 0.4522        | 5.7990e-05    | [Chapter](#trial_91) | 
| trial_92      | 256           | 0.4234        | 7.1652e-05    | [Chapter](#trial_92) | 
| trial_93      | 256           | 0.3772        | 2.8308e-05    | [Chapter](#trial_93) | 
| trial_96      | 512           | 0.4037        | 4.1627e-05    | [Chapter](#trial_96) | 
| trial_18      | 512           | 0.4185        | 2.8536e-05    | [Chapter](#trial_18) | 
| trial_22      | 512           | 0.4479        | 2.8183e-05    | [Chapter](#trial_22) | 
| trial_35      | 512           | 0.2926        | 2.6328e-05    | [Chapter](#trial_35) | 
| trial_38      | 512           | 0.3230        | 1.9300e-05    | [Chapter](#trial_38) | 
| trial_42      | 512           | 0.4298        | 3.0103e-05    | [Chapter](#trial_42) | 
| trial_51      | 128           | 0.4874        | 9.2223e-05    | [Chapter](#trial_51) | 
| trial_7       | 128           | 0.4203        | 2.0133e-05    | [Chapter](#trial_7) | 
| trial_19      | 512           | 0.4279        | 2.2084e-05    | [Chapter](#trial_19) | 
| trial_31      | 512           | 0.2478        | 1.4445e-05    | [Chapter](#trial_31) | 
| trial_41      | 256           | 0.2815        | 2.2112e-05    | [Chapter](#trial_41) | 
| trial_56      | 512           | 0.4466        | 2.4985e-05    | [Chapter](#trial_56) | 
| trial_57      | 256           | 0.3823        | 3.5187e-05    | [Chapter](#trial_57) | 
| trial_65      | 512           | 0.3793        | 1.7097e-05    | [Chapter](#trial_65) | 
| trial_71      | 512           | 0.2040        | 1.6559e-05    | [Chapter](#trial_71) | 
| trial_74      | 512           | 0.3808        | 2.4129e-05    | [Chapter](#trial_74) | 
| trial_77      | 512           | 0.4065        | 1.7912e-05    | [Chapter](#trial_77) | 
| trial_80      | 512           | 0.3357        | 2.6248e-05    | [Chapter](#trial_80) | 
| trial_88      | 512           | 0.3713        | 3.1777e-05    | [Chapter](#trial_88) | 
| trial_2       | 256           | 0.1134        | 2.6026e-05    | [Chapter](#trial_2) | 
| trial_20      | 512           | 0.4441        | 1.0340e-05    | [Chapter](#trial_20) | 
| trial_68      | 512           | 0.4878        | 1.9085e-05    | [Chapter](#trial_68) | 
| trial_94      | 256           | 0.2660        | 3.4252e-05    | [Chapter](#trial_94) | 
| trial_59      | 128           | 0.4607        | 3.5020e-05    | [Chapter](#trial_59) | 
| trial_66      | 512           | 0.3833        | 1.6344e-05    | [Chapter](#trial_66) | 
| trial_11      | 512           | 0.4780        | 1.1353e-05    | [Chapter](#trial_11) | 
| trial_44      | 512           | 0.3652        | 1.2883e-05    | [Chapter](#trial_44) | 
| trial_67      | 512           | 0.4352        | 1.3043e-05    | [Chapter](#trial_67) | 
| trial_26      | 512           | 0.4442        | 1.5032e-05    | [Chapter](#trial_26) | 


### <span style="color:rgb(105, 169, 201);">Test Results</span>

|           | accuracy  | precision | recall    | f1        | Chapters  |
| --------- | --------- | --------- | --------- | --------- | --------- |
| trial_21  | 0.9910    | 0.9910    | 0.9910    | 0.9910    | [Chapter](#trial_21) | 
| trial_15  | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_15) | 
| trial_17  | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_17) | 
| trial_37  | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_37) | 
| trial_39  | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_39) | 
| trial_81  | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_81) | 
| trial_100 | 0.9899    | 0.9899    | 0.9899    | 0.9899    | [Chapter](#trial_100) | 
| trial_3   | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_3) | 
| trial_33  | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_33) | 
| trial_40  | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_40) | 
| trial_46  | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_46) | 
| trial_55  | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_55) | 
| trial_61  | 0.9888    | 0.9888    | 0.9888    | 0.9888    | [Chapter](#trial_61) | 
| trial_4   | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_4) | 
| trial_5   | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_5) | 
| trial_6   | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_6) | 
| trial_10  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_10) | 
| trial_16  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_16) | 
| trial_28  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_28) | 
| trial_36  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_36) | 
| trial_49  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_49) | 
| trial_54  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_54) | 
| trial_73  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_73) | 
| trial_76  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_76) | 
| trial_85  | 0.9877    | 0.9877    | 0.9877    | 0.9877    | [Chapter](#trial_85) | 
| trial_1   | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_1) | 
| trial_8   | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_8) | 
| trial_9   | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_9) | 
| trial_12  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_12) | 
| trial_14  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_14) | 
| trial_25  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_25) | 
| trial_34  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_34) | 
| trial_43  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_43) | 
| trial_48  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_48) | 
| trial_50  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_50) | 
| trial_63  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_63) | 
| trial_64  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_64) | 
| trial_70  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_70) | 
| trial_79  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_79) | 
| trial_82  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_82) | 
| trial_84  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_84) | 
| trial_86  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_86) | 
| trial_95  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_95) | 
| trial_98  | 0.9866    | 0.9866    | 0.9866    | 0.9866    | [Chapter](#trial_98) | 
| trial_13  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_13) | 
| trial_23  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_23) | 
| trial_24  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_24) | 
| trial_27  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_27) | 
| trial_29  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_29) | 
| trial_30  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_30) | 
| trial_45  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_45) | 
| trial_53  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_53) | 
| trial_58  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_58) | 
| trial_72  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_72) | 
| trial_75  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_75) | 
| trial_83  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_83) | 
| trial_87  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_87) | 
| trial_97  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_97) | 
| trial_99  | 0.9854    | 0.9854    | 0.9854    | 0.9854    | [Chapter](#trial_99) | 
| trial_32  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_32) | 
| trial_47  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_47) | 
| trial_52  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_52) | 
| trial_60  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_60) | 
| trial_62  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_62) | 
| trial_69  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_69) | 
| trial_78  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_78) | 
| trial_89  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_89) | 
| trial_90  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_90) | 
| trial_91  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_91) | 
| trial_92  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_92) | 
| trial_93  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_93) | 
| trial_96  | 0.9843    | 0.9843    | 0.9843    | 0.9843    | [Chapter](#trial_96) | 
| trial_18  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_18) | 
| trial_22  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_22) | 
| trial_35  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_35) | 
| trial_38  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_38) | 
| trial_42  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_42) | 
| trial_51  | 0.9832    | 0.9832    | 0.9832    | 0.9832    | [Chapter](#trial_51) | 
| trial_7   | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_7) | 
| trial_19  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_19) | 
| trial_31  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_31) | 
| trial_41  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_41) | 
| trial_56  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_56) | 
| trial_57  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_57) | 
| trial_65  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_65) | 
| trial_71  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_71) | 
| trial_74  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_74) | 
| trial_77  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_77) | 
| trial_80  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_80) | 
| trial_88  | 0.9821    | 0.9821    | 0.9821    | 0.9821    | [Chapter](#trial_88) | 
| trial_2   | 0.9810    | 0.9810    | 0.9810    | 0.9810    | [Chapter](#trial_2) | 
| trial_20  | 0.9810    | 0.9810    | 0.9810    | 0.9810    | [Chapter](#trial_20) | 
| trial_68  | 0.9810    | 0.9810    | 0.9810    | 0.9810    | [Chapter](#trial_68) | 
| trial_94  | 0.9810    | 0.9810    | 0.9810    | 0.9810    | [Chapter](#trial_94) | 
| trial_59  | 0.9798    | 0.9798    | 0.9798    | 0.9798    | [Chapter](#trial_59) | 
| trial_66  | 0.9798    | 0.9798    | 0.9798    | 0.9798    | [Chapter](#trial_66) | 
| trial_11  | 0.9787    | 0.9787    | 0.9787    | 0.9787    | [Chapter](#trial_11) | 
| trial_44  | 0.9787    | 0.9787    | 0.9787    | 0.9787    | [Chapter](#trial_44) | 
| trial_67  | 0.9787    | 0.9787    | 0.9787    | 0.9787    | [Chapter](#trial_67) | 
| trial_26  | 0.9765    | 0.9765    | 0.9765    | 0.9765    | [Chapter](#trial_26) | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_21</span>

*    *Start Time*: 2024-10-23 08:29:46

*    *Duration*: 22.219

*    *Directory*: [Link](./trial_21)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.37297082287883704   |
| learning_rate         | 0.0001384397871457689 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9910    | 
| precision | 1.0000    | 0.9875    | 0.9910    | 
| recall    | 1.0000    | 0.9875    | 0.9910    | 
| f1        | 1.0000    | 0.9875    | 0.9910    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_21/model_summary.png)

![confusion_matrix](./trial_21/confusion_matrix.png)

![training_history](./trial_21/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9916       | 0.9916       | 0.9916       | 477          | 
| muffin       | 0.9904       | 0.9904       | 0.9904       | 416          | 
| micro avg    | 0.9910       | 0.9910       | 0.9910       | 893          | 
| macro avg    | 0.9910       | 0.9910       | 0.9910       | 893          | 
| weighted avg | 0.9910       | 0.9910       | 0.9910       | 893          | 
| samples avg  | 0.9910       | 0.9910       | 0.9910       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_15</span>

*    *Start Time*: 2024-10-23 08:27:29

*    *Duration*: 21.757

*    *Directory*: [Link](./trial_15)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.3498629787301412    |
| learning_rate         | 0.0001787861330161876 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9899    | 
| precision | 1.0000    | 0.9875    | 0.9899    | 
| recall    | 1.0000    | 0.9875    | 0.9899    | 
| f1        | 1.0000    | 0.9875    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_15/model_summary.png)

![confusion_matrix](./trial_15/confusion_matrix.png)

![training_history](./trial_15/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9916       | 0.9906       | 477          | 
| muffin       | 0.9904       | 0.9880       | 0.9892       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9900       | 0.9898       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_17</span>

*    *Start Time*: 2024-10-23 08:28:14

*    *Duration*: 21.756

*    *Directory*: [Link](./trial_17)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.014878109879033652   |
| learning_rate          | 5.9917108510509317e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9899    | 
| precision | 1.0000    | 0.9891    | 0.9899    | 
| recall    | 1.0000    | 0.9891    | 0.9899    | 
| f1        | 1.0000    | 0.9891    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_17/model_summary.png)

![confusion_matrix](./trial_17/confusion_matrix.png)

![training_history](./trial_17/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9916       | 0.9906       | 477          | 
| muffin       | 0.9904       | 0.9880       | 0.9892       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9900       | 0.9898       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_37</span>

*    *Start Time*: 2024-10-23 08:35:51

*    *Duration*: 20.820

*    *Directory*: [Link](./trial_37)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4726499428054811     |
| learning_rate          | 0.00031889400925616323 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9899    | 
| precision | 1.0000    | 0.9891    | 0.9899    | 
| recall    | 1.0000    | 0.9891    | 0.9899    | 
| f1        | 1.0000    | 0.9891    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_37/model_summary.png)

![confusion_matrix](./trial_37/confusion_matrix.png)

![training_history](./trial_37/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9916       | 0.9906       | 477          | 
| muffin       | 0.9904       | 0.9880       | 0.9892       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9900       | 0.9898       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_39</span>

*    *Start Time*: 2024-10-23 08:36:36

*    *Duration*: 21.335

*    *Directory*: [Link](./trial_39)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.1508362457263543    |
| learning_rate         | 4.202743652731754e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9906    | 0.9899    | 
| precision | 0.9997    | 0.9906    | 0.9899    | 
| recall    | 0.9997    | 0.9906    | 0.9899    | 
| f1        | 0.9997    | 0.9906    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_39/model_summary.png)

![confusion_matrix](./trial_39/confusion_matrix.png)

![training_history](./trial_39/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9916       | 0.9906       | 477          | 
| muffin       | 0.9904       | 0.9880       | 0.9892       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9900       | 0.9898       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_81</span>

*    *Start Time*: 2024-10-23 08:52:38

*    *Duration*: 21.149

*    *Directory*: [Link](./trial_81)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 256                  |
| dropout_rate         | 0.38778698593275246  |
| learning_rate        | 3.83569205117789e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9991    | 0.9859    | 0.9899    | 
| precision | 0.9991    | 0.9859    | 0.9899    | 
| recall    | 0.9991    | 0.9859    | 0.9899    | 
| f1        | 0.9991    | 0.9859    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_81/model_summary.png)

![confusion_matrix](./trial_81/confusion_matrix.png)

![training_history](./trial_81/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9916       | 0.9906       | 477          | 
| muffin       | 0.9904       | 0.9880       | 0.9892       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9900       | 0.9898       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_100</span>

*    *Start Time*: 2024-10-23 09:00:07

*    *Duration*: 21.233

*    *Directory*: [Link](./trial_100)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.4836133389966789    |
| learning_rate         | 6.573374917041436e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9875    | 0.9899    | 
| precision | 0.9997    | 0.9875    | 0.9899    | 
| recall    | 0.9997    | 0.9875    | 0.9899    | 
| f1        | 0.9997    | 0.9875    | 0.9899    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_100/model_summary.png)

![confusion_matrix](./trial_100/confusion_matrix.png)

![training_history](./trial_100/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9875       | 0.9937       | 0.9906       | 477          | 
| muffin       | 0.9927       | 0.9856       | 0.9891       | 416          | 
| micro avg    | 0.9899       | 0.9899       | 0.9899       | 893          | 
| macro avg    | 0.9901       | 0.9896       | 0.9899       | 893          | 
| weighted avg | 0.9899       | 0.9899       | 0.9899       | 893          | 
| samples avg  | 0.9899       | 0.9899       | 0.9899       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_3</span>

*    *Start Time*: 2024-10-23 08:22:59

*    *Duration*: 21.576

*    *Directory*: [Link](./trial_3)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.08429978400405025   |
| learning_rate         | 0.0002793144305653529 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9888    | 
| precision | 1.0000    | 0.9906    | 0.9888    | 
| recall    | 1.0000    | 0.9906    | 0.9888    | 
| f1        | 1.0000    | 0.9906    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_3/model_summary.png)

![confusion_matrix](./trial_3/confusion_matrix.png)

![training_history](./trial_3/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9895       | 0.9895       | 477          | 
| muffin       | 0.9880       | 0.9880       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9887       | 0.9887       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_33</span>

*    *Start Time*: 2024-10-23 08:34:22

*    *Duration*: 20.776

*    *Directory*: [Link](./trial_33)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.2180607039962844    |
| learning_rate         | 5.267201197600086e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9875    | 0.9888    | 
| precision | 0.9997    | 0.9875    | 0.9888    | 
| recall    | 0.9997    | 0.9875    | 0.9888    | 
| f1        | 0.9997    | 0.9875    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_33/model_summary.png)

![confusion_matrix](./trial_33/confusion_matrix.png)

![training_history](./trial_33/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9895       | 0.9895       | 477          | 
| muffin       | 0.9880       | 0.9880       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9887       | 0.9887       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_40</span>

*    *Start Time*: 2024-10-23 08:36:59

*    *Duration*: 21.168

*    *Directory*: [Link](./trial_40)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 512                  |
| dropout_rate         | 0.4087129735892046   |
| learning_rate        | 7.63009029761099e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9888    | 
| precision | 1.0000    | 0.9906    | 0.9888    | 
| recall    | 1.0000    | 0.9906    | 0.9888    | 
| f1        | 1.0000    | 0.9906    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_40/model_summary.png)

![confusion_matrix](./trial_40/confusion_matrix.png)

![training_history](./trial_40/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9875       | 0.9916       | 0.9895       | 477          | 
| muffin       | 0.9903       | 0.9856       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9889       | 0.9886       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_46</span>

*    *Start Time*: 2024-10-23 08:39:14

*    *Duration*: 21.188

*    *Directory*: [Link](./trial_46)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.4707118638297069    |
| learning_rate         | 5.631849360621576e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9859    | 0.9888    | 
| precision | 0.9994    | 0.9859    | 0.9888    | 
| recall    | 0.9994    | 0.9859    | 0.9888    | 
| f1        | 0.9994    | 0.9859    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_46/model_summary.png)

![confusion_matrix](./trial_46/confusion_matrix.png)

![training_history](./trial_46/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9875       | 0.9916       | 0.9895       | 477          | 
| muffin       | 0.9903       | 0.9856       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9889       | 0.9886       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_55</span>

*    *Start Time*: 2024-10-23 08:42:39

*    *Duration*: 21.320

*    *Directory*: [Link](./trial_55)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.4741560241283936     |
| learning_rate          | 0.00012641427064081926 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9888    | 
| precision | 1.0000    | 0.9906    | 0.9888    | 
| recall    | 1.0000    | 0.9906    | 0.9888    | 
| f1        | 1.0000    | 0.9906    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_55/model_summary.png)

![confusion_matrix](./trial_55/confusion_matrix.png)

![training_history](./trial_55/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9875       | 0.9916       | 0.9895       | 477          | 
| muffin       | 0.9903       | 0.9856       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9889       | 0.9886       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_61</span>

*    *Start Time*: 2024-10-23 08:44:56

*    *Duration*: 20.937

*    *Directory*: [Link](./trial_61)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 256                  |
| dropout_rate         | 0.04116007444355935  |
| learning_rate        | 9.24357044353985e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9888    | 
| precision | 1.0000    | 0.9906    | 0.9888    | 
| recall    | 1.0000    | 0.9906    | 0.9888    | 
| f1        | 1.0000    | 0.9906    | 0.9888    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_61/model_summary.png)

![confusion_matrix](./trial_61/confusion_matrix.png)

![training_history](./trial_61/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9895       | 0.9895       | 477          | 
| muffin       | 0.9880       | 0.9880       | 0.9880       | 416          | 
| micro avg    | 0.9888       | 0.9888       | 0.9888       | 893          | 
| macro avg    | 0.9887       | 0.9887       | 0.9887       | 893          | 
| weighted avg | 0.9888       | 0.9888       | 0.9888       | 893          | 
| samples avg  | 0.9888       | 0.9888       | 0.9888       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_4</span>

*    *Start Time*: 2024-10-23 08:23:21

*    *Duration*: 21.483

*    *Directory*: [Link](./trial_4)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.4680168863573586    |
| learning_rate         | 7.157047207151639e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9922    | 0.9877    | 
| precision | 0.9997    | 0.9922    | 0.9877    | 
| recall    | 0.9997    | 0.9922    | 0.9877    | 
| f1        | 0.9997    | 0.9922    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_4/model_summary.png)

![confusion_matrix](./trial_4/confusion_matrix.png)

![training_history](./trial_4/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_5</span>

*    *Start Time*: 2024-10-23 08:23:43

*    *Duration*: 21.562

*    *Directory*: [Link](./trial_5)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.07827462948739278   |
| learning_rate         | 0.0005524964939387456 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9877    | 
| precision | 1.0000    | 0.9891    | 0.9877    | 
| recall    | 1.0000    | 0.9891    | 0.9877    | 
| f1        | 1.0000    | 0.9891    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_5/model_summary.png)

![confusion_matrix](./trial_5/confusion_matrix.png)

![training_history](./trial_5/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_6</span>

*    *Start Time*: 2024-10-23 08:24:05

*    *Duration*: 21.820

*    *Directory*: [Link](./trial_6)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.29543369776324463   |
| learning_rate         | 0.0007118010766530988 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9877    | 
| precision | 1.0000    | 0.9906    | 0.9877    | 
| recall    | 1.0000    | 0.9906    | 0.9877    | 
| f1        | 1.0000    | 0.9906    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_6/model_summary.png)

![confusion_matrix](./trial_6/confusion_matrix.png)

![training_history](./trial_6/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_10</span>

*    *Start Time*: 2024-10-23 08:25:37

*    *Duration*: 21.519

*    *Directory*: [Link](./trial_10)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.3988108945579785    |
| learning_rate         | 0.0009609575441407858 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9877    | 
| precision | 1.0000    | 0.9906    | 0.9877    | 
| recall    | 1.0000    | 0.9906    | 0.9877    | 
| f1        | 1.0000    | 0.9906    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_10/model_summary.png)

![confusion_matrix](./trial_10/confusion_matrix.png)

![training_history](./trial_10/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9874       | 0.9885       | 477          | 
| muffin       | 0.9856       | 0.9880       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9876       | 0.9877       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_16</span>

*    *Start Time*: 2024-10-23 08:27:51

*    *Duration*: 22.034

*    *Directory*: [Link](./trial_16)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 128                   |
| dropout_rate          | 0.1996611639069833    |
| learning_rate         | 4.782575734681498e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9975    | 0.9859    | 0.9877    | 
| precision | 0.9975    | 0.9859    | 0.9877    | 
| recall    | 0.9975    | 0.9859    | 0.9877    | 
| f1        | 0.9975    | 0.9859    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_16/model_summary.png)

![confusion_matrix](./trial_16/confusion_matrix.png)

![training_history](./trial_16/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9895       | 0.9885       | 477          | 
| muffin       | 0.9880       | 0.9856       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9877       | 0.9875       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_28</span>

*    *Start Time*: 2024-10-23 08:32:27

*    *Duration*: 21.869

*    *Directory*: [Link](./trial_28)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.3809758064792372    |
| learning_rate         | 0.0001098387636226933 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9877    | 
| precision | 1.0000    | 0.9891    | 0.9877    | 
| recall    | 1.0000    | 0.9891    | 0.9877    | 
| f1        | 1.0000    | 0.9891    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_28/model_summary.png)

![confusion_matrix](./trial_28/confusion_matrix.png)

![training_history](./trial_28/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9874       | 0.9885       | 477          | 
| muffin       | 0.9856       | 0.9880       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9876       | 0.9877       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_36</span>

*    *Start Time*: 2024-10-23 08:35:29

*    *Duration*: 21.104

*    *Directory*: [Link](./trial_36)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.43170926310932817    |
| learning_rate          | 0.00011203017744595551 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9877    | 
| precision | 1.0000    | 0.9875    | 0.9877    | 
| recall    | 1.0000    | 0.9875    | 0.9877    | 
| f1        | 1.0000    | 0.9875    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_36/model_summary.png)

![confusion_matrix](./trial_36/confusion_matrix.png)

![training_history](./trial_36/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_49</span>

*    *Start Time*: 2024-10-23 08:40:22

*    *Duration*: 20.705

*    *Directory*: [Link](./trial_49)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.09217618197653099   |
| learning_rate         | 0.0002665494075470057 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9877    | 
| precision | 1.0000    | 0.9891    | 0.9877    | 
| recall    | 1.0000    | 0.9891    | 0.9877    | 
| f1        | 1.0000    | 0.9891    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_49/model_summary.png)

![confusion_matrix](./trial_49/confusion_matrix.png)

![training_history](./trial_49/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9895       | 0.9885       | 477          | 
| muffin       | 0.9880       | 0.9856       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9877       | 0.9875       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_54</span>

*    *Start Time*: 2024-10-23 08:42:15

*    *Duration*: 21.441

*    *Directory*: [Link](./trial_54)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.49759303307516434   |
| learning_rate         | 6.557601844650474e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9877    | 
| precision | 0.9997    | 0.9891    | 0.9877    | 
| recall    | 0.9997    | 0.9891    | 0.9877    | 
| f1        | 0.9997    | 0.9891    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_54/model_summary.png)

![confusion_matrix](./trial_54/confusion_matrix.png)

![training_history](./trial_54/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_73</span>

*    *Start Time*: 2024-10-23 08:49:31

*    *Duration*: 21.177

*    *Directory*: [Link](./trial_73)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.3555426514924586     |
| learning_rate          | 3.9508998773954047e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9906    | 0.9877    | 
| precision | 0.9997    | 0.9906    | 0.9877    | 
| recall    | 0.9997    | 0.9906    | 0.9877    | 
| f1        | 0.9997    | 0.9906    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_73/model_summary.png)

![confusion_matrix](./trial_73/confusion_matrix.png)

![training_history](./trial_73/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9895       | 0.9885       | 477          | 
| muffin       | 0.9880       | 0.9856       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9877       | 0.9875       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_76</span>

*    *Start Time*: 2024-10-23 08:50:41

*    *Duration*: 21.042

*    *Directory*: [Link](./trial_76)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.345841062578444      |
| learning_rate          | 3.0282110791216976e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9877    | 
| precision | 0.9997    | 0.9891    | 0.9877    | 
| recall    | 0.9997    | 0.9891    | 0.9877    | 
| f1        | 0.9997    | 0.9891    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_76/model_summary.png)

![confusion_matrix](./trial_76/confusion_matrix.png)

![training_history](./trial_76/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9895       | 0.9874       | 0.9885       | 477          | 
| muffin       | 0.9856       | 0.9880       | 0.9868       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9876       | 0.9877       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_85</span>

*    *Start Time*: 2024-10-23 08:54:11

*    *Duration*: 21.029

*    *Directory*: [Link](./trial_85)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.44109290889221453    |
| learning_rate          | 0.00010763541276588227 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9922    | 0.9877    | 
| precision | 1.0000    | 0.9922    | 0.9877    | 
| recall    | 1.0000    | 0.9922    | 0.9877    | 
| f1        | 1.0000    | 0.9922    | 0.9877    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_85/model_summary.png)

![confusion_matrix](./trial_85/confusion_matrix.png)

![training_history](./trial_85/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9916       | 0.9885       | 477          | 
| muffin       | 0.9903       | 0.9832       | 0.9867       | 416          | 
| micro avg    | 0.9877       | 0.9877       | 0.9877       | 893          | 
| macro avg    | 0.9879       | 0.9874       | 0.9876       | 893          | 
| weighted avg | 0.9877       | 0.9877       | 0.9877       | 893          | 
| samples avg  | 0.9877       | 0.9877       | 0.9877       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_1</span>

*    *Start Time*: 2024-10-23 08:22:04

*    *Duration*: 30.008

*    *Directory*: [Link](./trial_1)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.2624114358502948    |
| learning_rate         | 7.969597262267634e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9866    | 
| precision | 1.0000    | 0.9891    | 0.9866    | 
| recall    | 1.0000    | 0.9891    | 0.9866    | 
| f1        | 1.0000    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_1/model_summary.png)

![confusion_matrix](./trial_1/confusion_matrix.png)

![training_history](./trial_1/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_8</span>

*    *Start Time*: 2024-10-23 08:24:52

*    *Duration*: 21.735

*    *Directory*: [Link](./trial_8)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.1307636892195046    |
| learning_rate         | 0.0005890714206015307 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9866    | 
| precision | 1.0000    | 0.9891    | 0.9866    | 
| recall    | 1.0000    | 0.9891    | 0.9866    | 
| f1        | 1.0000    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_8/model_summary.png)

![confusion_matrix](./trial_8/confusion_matrix.png)

![training_history](./trial_8/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9874       | 0.9874       | 477          | 
| muffin       | 0.9856       | 0.9856       | 0.9856       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9865       | 0.9865       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_9</span>

*    *Start Time*: 2024-10-23 08:25:14

*    *Duration*: 21.742

*    *Directory*: [Link](./trial_9)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.3292201193965158    |
| learning_rate         | 7.029537736162967e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9866    | 
| precision | 0.9997    | 0.9891    | 0.9866    | 
| recall    | 0.9997    | 0.9891    | 0.9866    | 
| f1        | 0.9997    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_9/model_summary.png)

![confusion_matrix](./trial_9/confusion_matrix.png)

![training_history](./trial_9/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9874       | 0.9874       | 477          | 
| muffin       | 0.9856       | 0.9856       | 0.9856       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9865       | 0.9865       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_12</span>

*    *Start Time*: 2024-10-23 08:26:21

*    *Duration*: 21.290

*    *Directory*: [Link](./trial_12)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 128                   |
| dropout_rate          | 0.34815267373225034   |
| learning_rate         | 9.187434166164443e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9875    | 0.9866    | 
| precision | 0.9997    | 0.9875    | 0.9866    | 
| recall    | 0.9997    | 0.9875    | 0.9866    | 
| f1        | 0.9997    | 0.9875    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_12/model_summary.png)

![confusion_matrix](./trial_12/confusion_matrix.png)

![training_history](./trial_12/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_14</span>

*    *Start Time*: 2024-10-23 08:27:06

*    *Duration*: 21.987

*    *Directory*: [Link](./trial_14)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.20003419531135136    |
| learning_rate          | 0.00019858388415220065 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9866    | 
| precision | 1.0000    | 0.9891    | 0.9866    | 
| recall    | 1.0000    | 0.9891    | 0.9866    | 
| f1        | 1.0000    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_14/model_summary.png)

![confusion_matrix](./trial_14/confusion_matrix.png)

![training_history](./trial_14/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_25</span>

*    *Start Time*: 2024-10-23 08:31:17

*    *Duration*: 21.888

*    *Directory*: [Link](./trial_25)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.39764931776526286    |
| learning_rate          | 3.2109528653206545e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9891    | 0.9866    | 
| precision | 0.9994    | 0.9891    | 0.9866    | 
| recall    | 0.9994    | 0.9891    | 0.9866    | 
| f1        | 0.9994    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_25/model_summary.png)

![confusion_matrix](./trial_25/confusion_matrix.png)

![training_history](./trial_25/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9874       | 0.9874       | 477          | 
| muffin       | 0.9856       | 0.9856       | 0.9856       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9865       | 0.9865       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_34</span>

*    *Start Time*: 2024-10-23 08:34:44

*    *Duration*: 21.220

*    *Directory*: [Link](./trial_34)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.17190958015271368   |
| learning_rate         | 8.220839878308844e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9866    | 
| precision | 1.0000    | 0.9906    | 0.9866    | 
| recall    | 1.0000    | 0.9906    | 0.9866    | 
| f1        | 1.0000    | 0.9906    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_34/model_summary.png)

![confusion_matrix](./trial_34/confusion_matrix.png)

![training_history](./trial_34/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_43</span>

*    *Start Time*: 2024-10-23 08:38:06

*    *Duration*: 21.109

*    *Directory*: [Link](./trial_43)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.36943303438175445    |
| learning_rate          | 2.9045082135588245e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9984    | 0.9891    | 0.9866    | 
| precision | 0.9984    | 0.9891    | 0.9866    | 
| recall    | 0.9984    | 0.9891    | 0.9866    | 
| f1        | 0.9984    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_43/model_summary.png)

![confusion_matrix](./trial_43/confusion_matrix.png)

![training_history](./trial_43/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9834       | 0.9916       | 0.9875       | 477          | 
| muffin       | 0.9903       | 0.9808       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9868       | 0.9862       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_48</span>

*    *Start Time*: 2024-10-23 08:40:00

*    *Duration*: 21.075

*    *Directory*: [Link](./trial_48)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.23531825762468442    |
| learning_rate          | 0.00015417964513227822 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9922    | 0.9866    | 
| precision | 1.0000    | 0.9922    | 0.9866    | 
| recall    | 1.0000    | 0.9922    | 0.9866    | 
| f1        | 1.0000    | 0.9922    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_48/model_summary.png)

![confusion_matrix](./trial_48/confusion_matrix.png)

![training_history](./trial_48/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_50</span>

*    *Start Time*: 2024-10-23 08:40:45

*    *Duration*: 20.924

*    *Directory*: [Link](./trial_50)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.4912893792446536    |
| learning_rate         | 7.099086820467418e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9866    | 
| precision | 0.9997    | 0.9891    | 0.9866    | 
| recall    | 0.9997    | 0.9891    | 0.9866    | 
| f1        | 0.9997    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_50/model_summary.png)

![confusion_matrix](./trial_50/confusion_matrix.png)

![training_history](./trial_50/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_63</span>

*    *Start Time*: 2024-10-23 08:45:42

*    *Duration*: 20.804

*    *Directory*: [Link](./trial_63)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.2742267436792667    |
| learning_rate         | 3.348863238587228e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9875    | 0.9866    | 
| precision | 0.9997    | 0.9875    | 0.9866    | 
| recall    | 0.9997    | 0.9875    | 0.9866    | 
| f1        | 0.9997    | 0.9875    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_63/model_summary.png)

![confusion_matrix](./trial_63/confusion_matrix.png)

![training_history](./trial_63/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9834       | 0.9916       | 0.9875       | 477          | 
| muffin       | 0.9903       | 0.9808       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9868       | 0.9862       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_64</span>

*    *Start Time*: 2024-10-23 08:46:05

*    *Duration*: 21.285

*    *Directory*: [Link](./trial_64)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.31869402281028714   |
| learning_rate         | 6.148599596779192e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9866    | 
| precision | 1.0000    | 0.9875    | 0.9866    | 
| recall    | 1.0000    | 0.9875    | 0.9866    | 
| f1        | 1.0000    | 0.9875    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_64/model_summary.png)

![confusion_matrix](./trial_64/confusion_matrix.png)

![training_history](./trial_64/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9874       | 0.9874       | 477          | 
| muffin       | 0.9856       | 0.9856       | 0.9856       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9865       | 0.9865       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_70</span>

*    *Start Time*: 2024-10-23 08:48:23

*    *Duration*: 20.821

*    *Directory*: [Link](./trial_70)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.47978812577570157    |
| learning_rate          | 2.1450448596466712e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9950    | 0.9891    | 0.9866    | 
| precision | 0.9950    | 0.9891    | 0.9866    | 
| recall    | 0.9950    | 0.9891    | 0.9866    | 
| f1        | 0.9950    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_70/model_summary.png)

![confusion_matrix](./trial_70/confusion_matrix.png)

![training_history](./trial_70/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_79</span>

*    *Start Time*: 2024-10-23 08:51:51

*    *Duration*: 21.206

*    *Directory*: [Link](./trial_79)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.2290329227560618     |
| learning_rate          | 2.2220489627034217e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9975    | 0.9891    | 0.9866    | 
| precision | 0.9975    | 0.9891    | 0.9866    | 
| recall    | 0.9975    | 0.9891    | 0.9866    | 
| f1        | 0.9975    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_79/model_summary.png)

![confusion_matrix](./trial_79/confusion_matrix.png)

![training_history](./trial_79/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9874       | 0.9874       | 0.9874       | 477          | 
| muffin       | 0.9856       | 0.9856       | 0.9856       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9865       | 0.9865       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_82</span>

*    *Start Time*: 2024-10-23 08:53:01

*    *Duration*: 20.728

*    *Directory*: [Link](./trial_82)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.45955507713388793    |
| learning_rate          | 5.1543911055239724e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9866    | 
| precision | 0.9997    | 0.9891    | 0.9866    | 
| recall    | 0.9997    | 0.9891    | 0.9866    | 
| f1        | 0.9997    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_82/model_summary.png)

![confusion_matrix](./trial_82/confusion_matrix.png)

![training_history](./trial_82/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_84</span>

*    *Start Time*: 2024-10-23 08:53:48

*    *Duration*: 21.206

*    *Directory*: [Link](./trial_84)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.4149387707870665    |
| learning_rate         | 8.553330943422604e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9866    | 
| precision | 1.0000    | 0.9906    | 0.9866    | 
| recall    | 1.0000    | 0.9906    | 0.9866    | 
| f1        | 1.0000    | 0.9906    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_84/model_summary.png)

![confusion_matrix](./trial_84/confusion_matrix.png)

![training_history](./trial_84/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_86</span>

*    *Start Time*: 2024-10-23 08:54:35

*    *Duration*: 21.263

*    *Directory*: [Link](./trial_86)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.46470019053602923    |
| learning_rate          | 5.6657742801569646e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9922    | 0.9866    | 
| precision | 0.9997    | 0.9922    | 0.9866    | 
| recall    | 0.9997    | 0.9922    | 0.9866    | 
| f1        | 0.9997    | 0.9922    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_86/model_summary.png)

![confusion_matrix](./trial_86/confusion_matrix.png)

![training_history](./trial_86/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_95</span>

*    *Start Time*: 2024-10-23 08:58:08

*    *Duration*: 21.299

*    *Directory*: [Link](./trial_95)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 256                  |
| dropout_rate         | 0.34298465091440145  |
| learning_rate        | 4.81166016688479e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9891    | 0.9866    | 
| precision | 0.9994    | 0.9891    | 0.9866    | 
| recall    | 0.9994    | 0.9891    | 0.9866    | 
| f1        | 0.9994    | 0.9891    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_95/model_summary.png)

![confusion_matrix](./trial_95/confusion_matrix.png)

![training_history](./trial_95/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9814       | 0.9937       | 0.9875       | 477          | 
| muffin       | 0.9927       | 0.9784       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9870       | 0.9860       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_98</span>

*    *Start Time*: 2024-10-23 08:59:20

*    *Duration*: 21.146

*    *Directory*: [Link](./trial_98)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.46773348294272665   |
| learning_rate         | 4.419328732857195e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9875    | 0.9866    | 
| precision | 0.9994    | 0.9875    | 0.9866    | 
| recall    | 0.9994    | 0.9875    | 0.9866    | 
| f1        | 0.9994    | 0.9875    | 0.9866    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_98/model_summary.png)

![confusion_matrix](./trial_98/confusion_matrix.png)

![training_history](./trial_98/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9895       | 0.9874       | 477          | 
| muffin       | 0.9879       | 0.9832       | 0.9855       | 416          | 
| micro avg    | 0.9866       | 0.9866       | 0.9866       | 893          | 
| macro avg    | 0.9867       | 0.9863       | 0.9865       | 893          | 
| weighted avg | 0.9866       | 0.9866       | 0.9866       | 893          | 
| samples avg  | 0.9866       | 0.9866       | 0.9866       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_13</span>

*    *Start Time*: 2024-10-23 08:26:43

*    *Duration*: 21.864

*    *Directory*: [Link](./trial_13)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.49252397089297045   |
| learning_rate         | 4.647064078616779e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9991    | 0.9891    | 0.9854    | 
| precision | 0.9991    | 0.9891    | 0.9854    | 
| recall    | 0.9991    | 0.9891    | 0.9854    | 
| f1        | 0.9991    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_13/model_summary.png)

![confusion_matrix](./trial_13/confusion_matrix.png)

![training_history](./trial_13/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9916       | 0.9864       | 477          | 
| muffin       | 0.9903       | 0.9784       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9858       | 0.9850       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_23</span>

*    *Start Time*: 2024-10-23 08:30:32

*    *Duration*: 21.975

*    *Directory*: [Link](./trial_23)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4549081297169313     |
| learning_rate          | 1.6902568080827105e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9947    | 0.9875    | 0.9854    | 
| precision | 0.9947    | 0.9875    | 0.9854    | 
| recall    | 0.9947    | 0.9875    | 0.9854    | 
| f1        | 0.9947    | 0.9875    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_23/model_summary.png)

![confusion_matrix](./trial_23/confusion_matrix.png)

![training_history](./trial_23/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9916       | 0.9864       | 477          | 
| muffin       | 0.9903       | 0.9784       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9858       | 0.9850       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_24</span>

*    *Start Time*: 2024-10-23 08:30:55

*    *Duration*: 21.896

*    *Directory*: [Link](./trial_24)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.49878765733810654   |
| learning_rate         | 3.952030104345121e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9906    | 0.9854    | 
| precision | 0.9994    | 0.9906    | 0.9854    | 
| recall    | 0.9994    | 0.9906    | 0.9854    | 
| f1        | 0.9994    | 0.9906    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_24/model_summary.png)

![confusion_matrix](./trial_24/confusion_matrix.png)

![training_history](./trial_24/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_27</span>

*    *Start Time*: 2024-10-23 08:32:04

*    *Duration*: 21.989

*    *Directory*: [Link](./trial_27)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.30477403789907076   |
| learning_rate         | 2.318374365780824e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9991    | 0.9891    | 0.9854    | 
| precision | 0.9991    | 0.9891    | 0.9854    | 
| recall    | 0.9991    | 0.9891    | 0.9854    | 
| f1        | 0.9991    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_27/model_summary.png)

![confusion_matrix](./trial_27/confusion_matrix.png)

![training_history](./trial_27/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_29</span>

*    *Start Time*: 2024-10-23 08:32:49

*    *Duration*: 22.463

*    *Directory*: [Link](./trial_29)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.46173954185919874    |
| learning_rate          | 3.6306078734837315e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9891    | 0.9854    | 
| precision | 0.9994    | 0.9891    | 0.9854    | 
| recall    | 0.9994    | 0.9891    | 0.9854    | 
| f1        | 0.9994    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_29/model_summary.png)

![confusion_matrix](./trial_29/confusion_matrix.png)

![training_history](./trial_29/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_30</span>

*    *Start Time*: 2024-10-23 08:33:13

*    *Duration*: 22.129

*    *Directory*: [Link](./trial_30)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.24587512950015097   |
| learning_rate         | 6.488483616352618e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9906    | 0.9854    | 
| precision | 1.0000    | 0.9906    | 0.9854    | 
| recall    | 1.0000    | 0.9906    | 0.9854    | 
| f1        | 1.0000    | 0.9906    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_30/model_summary.png)

![confusion_matrix](./trial_30/confusion_matrix.png)

![training_history](./trial_30/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_45</span>

*    *Start Time*: 2024-10-23 08:38:52

*    *Duration*: 20.788

*    *Directory*: [Link](./trial_45)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.39540503612922046   |
| learning_rate         | 3.600985307344948e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9891    | 0.9854    | 
| precision | 0.9994    | 0.9891    | 0.9854    | 
| recall    | 0.9994    | 0.9891    | 0.9854    | 
| f1        | 0.9994    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_45/model_summary.png)

![confusion_matrix](./trial_45/confusion_matrix.png)

![training_history](./trial_45/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_53</span>

*    *Start Time*: 2024-10-23 08:41:53

*    *Duration*: 20.874

*    *Directory*: [Link](./trial_53)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.42479549383515847   |
| learning_rate         | 4.627558308920554e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9981    | 0.9891    | 0.9854    | 
| precision | 0.9981    | 0.9891    | 0.9854    | 
| recall    | 0.9981    | 0.9891    | 0.9854    | 
| f1        | 0.9981    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_53/model_summary.png)

![confusion_matrix](./trial_53/confusion_matrix.png)

![training_history](./trial_53/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_58</span>

*    *Start Time*: 2024-10-23 08:43:47

*    *Duration*: 21.290

*    *Directory*: [Link](./trial_58)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.4090904234949702     |
| learning_rate          | 4.9584634639340204e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9854    | 
| precision | 0.9997    | 0.9891    | 0.9854    | 
| recall    | 0.9997    | 0.9891    | 0.9854    | 
| f1        | 0.9997    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_58/model_summary.png)

![confusion_matrix](./trial_58/confusion_matrix.png)

![training_history](./trial_58/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_72</span>

*    *Start Time*: 2024-10-23 08:49:09

*    *Duration*: 20.680

*    *Directory*: [Link](./trial_72)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.34490183168503535    |
| learning_rate          | 3.1388262919109246e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9906    | 0.9854    | 
| precision | 0.9994    | 0.9906    | 0.9854    | 
| recall    | 0.9994    | 0.9906    | 0.9854    | 
| f1        | 0.9994    | 0.9906    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_72/model_summary.png)

![confusion_matrix](./trial_72/confusion_matrix.png)

![training_history](./trial_72/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9916       | 0.9864       | 477          | 
| muffin       | 0.9903       | 0.9784       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9858       | 0.9850       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_75</span>

*    *Start Time*: 2024-10-23 08:50:18

*    *Duration*: 21.284

*    *Directory*: [Link](./trial_75)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.3819852054237187     |
| learning_rate          | 2.4418983769808748e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9978    | 0.9875    | 0.9854    | 
| precision | 0.9978    | 0.9875    | 0.9854    | 
| recall    | 0.9978    | 0.9875    | 0.9854    | 
| f1        | 0.9978    | 0.9875    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_75/model_summary.png)

![confusion_matrix](./trial_75/confusion_matrix.png)

![training_history](./trial_75/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9854       | 0.9874       | 0.9864       | 477          | 
| muffin       | 0.9855       | 0.9832       | 0.9844       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9854       | 0.9853       | 0.9854       | 893          | 
| weighted avg | 0.9854       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_83</span>

*    *Start Time*: 2024-10-23 08:53:24

*    *Duration*: 20.981

*    *Directory*: [Link](./trial_83)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.43230926153980137   |
| learning_rate         | 6.986509072830372e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9854    | 
| precision | 1.0000    | 0.9875    | 0.9854    | 
| recall    | 1.0000    | 0.9875    | 0.9854    | 
| f1        | 1.0000    | 0.9875    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_83/model_summary.png)

![confusion_matrix](./trial_83/confusion_matrix.png)

![training_history](./trial_83/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_87</span>

*    *Start Time*: 2024-10-23 08:54:58

*    *Duration*: 21.312

*    *Directory*: [Link](./trial_87)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.3099414236402392     |
| learning_rate          | 5.6630939847702524e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9891    | 0.9854    | 
| precision | 1.0000    | 0.9891    | 0.9854    | 
| recall    | 1.0000    | 0.9891    | 0.9854    | 
| f1        | 1.0000    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_87/model_summary.png)

![confusion_matrix](./trial_87/confusion_matrix.png)

![training_history](./trial_87/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_97</span>

*    *Start Time*: 2024-10-23 08:58:56

*    *Duration*: 21.574

*    *Directory*: [Link](./trial_97)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.40308957002035894   |
| learning_rate         | 5.290346177015095e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9994    | 0.9875    | 0.9854    | 
| precision | 0.9994    | 0.9875    | 0.9854    | 
| recall    | 0.9994    | 0.9875    | 0.9854    | 
| f1        | 0.9994    | 0.9875    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_97/model_summary.png)

![confusion_matrix](./trial_97/confusion_matrix.png)

![training_history](./trial_97/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9916       | 0.9864       | 477          | 
| muffin       | 0.9903       | 0.9784       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9858       | 0.9850       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_99</span>

*    *Start Time*: 2024-10-23 08:59:44

*    *Duration*: 20.928

*    *Directory*: [Link](./trial_99)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.175252793639213      |
| learning_rate          | 3.9522254339898235e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9854    | 
| precision | 0.9997    | 0.9891    | 0.9854    | 
| recall    | 0.9997    | 0.9891    | 0.9854    | 
| f1        | 0.9997    | 0.9891    | 0.9854    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_99/model_summary.png)

![confusion_matrix](./trial_99/confusion_matrix.png)

![training_history](./trial_99/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9895       | 0.9864       | 477          | 
| muffin       | 0.9879       | 0.9808       | 0.9843       | 416          | 
| micro avg    | 0.9854       | 0.9854       | 0.9854       | 893          | 
| macro avg    | 0.9856       | 0.9851       | 0.9854       | 893          | 
| weighted avg | 0.9855       | 0.9854       | 0.9854       | 893          | 
| samples avg  | 0.9854       | 0.9854       | 0.9854       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_32</span>

*    *Start Time*: 2024-10-23 08:33:59

*    *Duration*: 21.257

*    *Directory*: [Link](./trial_32)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.2554172602383897    |
| learning_rate         | 6.307066167514853e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 1.0000    | 0.9875    | 0.9843    | 
| precision | 1.0000    | 0.9875    | 0.9843    | 
| recall    | 1.0000    | 0.9875    | 0.9843    | 
| f1        | 1.0000    | 0.9875    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_32/model_summary.png)

![confusion_matrix](./trial_32/confusion_matrix.png)

![training_history](./trial_32/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_47</span>

*    *Start Time*: 2024-10-23 08:39:37

*    *Duration*: 21.314

*    *Directory*: [Link](./trial_47)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.33648935595104096   |
| learning_rate         | 1.985872849744353e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9953    | 0.9906    | 0.9843    | 
| precision | 0.9953    | 0.9906    | 0.9843    | 
| recall    | 0.9953    | 0.9906    | 0.9843    | 
| f1        | 0.9953    | 0.9906    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_47/model_summary.png)

![confusion_matrix](./trial_47/confusion_matrix.png)

![training_history](./trial_47/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9793       | 0.9916       | 0.9854       | 477          | 
| muffin       | 0.9902       | 0.9760       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9848       | 0.9838       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_52</span>

*    *Start Time*: 2024-10-23 08:41:30

*    *Duration*: 21.284

*    *Directory*: [Link](./trial_52)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.4494865543599071    |
| learning_rate         | 7.598301801980728e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9843    | 
| precision | 0.9997    | 0.9891    | 0.9843    | 
| recall    | 0.9997    | 0.9891    | 0.9843    | 
| f1        | 0.9997    | 0.9891    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_52/model_summary.png)

![confusion_matrix](./trial_52/confusion_matrix.png)

![training_history](./trial_52/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9874       | 0.9854       | 477          | 
| muffin       | 0.9855       | 0.9808       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9844       | 0.9841       | 0.9842       | 893          | 
| weighted avg | 0.9843       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_60</span>

*    *Start Time*: 2024-10-23 08:44:33

*    *Duration*: 21.149

*    *Directory*: [Link](./trial_60)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.39354215127719533   |
| learning_rate         | 4.243379739172321e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9981    | 0.9891    | 0.9843    | 
| precision | 0.9981    | 0.9891    | 0.9843    | 
| recall    | 0.9981    | 0.9891    | 0.9843    | 
| f1        | 0.9981    | 0.9891    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_60/model_summary.png)

![confusion_matrix](./trial_60/confusion_matrix.png)

![training_history](./trial_60/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9874       | 0.9854       | 477          | 
| muffin       | 0.9855       | 0.9808       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9844       | 0.9841       | 0.9842       | 893          | 
| weighted avg | 0.9843       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_62</span>

*    *Start Time*: 2024-10-23 08:45:19

*    *Duration*: 21.079

*    *Directory*: [Link](./trial_62)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.36123171188871395   |
| learning_rate         | 2.650223222168248e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9953    | 0.9891    | 0.9843    | 
| precision | 0.9953    | 0.9891    | 0.9843    | 
| recall    | 0.9953    | 0.9891    | 0.9843    | 
| f1        | 0.9953    | 0.9891    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_62/model_summary.png)

![confusion_matrix](./trial_62/confusion_matrix.png)

![training_history](./trial_62/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9773       | 0.9937       | 0.9854       | 477          | 
| muffin       | 0.9926       | 0.9736       | 0.9830       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9850       | 0.9836       | 0.9842       | 893          | 
| weighted avg | 0.9845       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_69</span>

*    *Start Time*: 2024-10-23 08:48:00

*    *Duration*: 21.091

*    *Directory*: [Link](./trial_69)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4175081029473965     |
| learning_rate          | 1.1297334059161129e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9906    | 0.9891    | 0.9843    | 
| precision | 0.9906    | 0.9891    | 0.9843    | 
| recall    | 0.9906    | 0.9891    | 0.9843    | 
| f1        | 0.9906    | 0.9891    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_69/model_summary.png)

![confusion_matrix](./trial_69/confusion_matrix.png)

![training_history](./trial_69/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_78</span>

*    *Start Time*: 2024-10-23 08:51:28

*    *Duration*: 21.001

*    *Directory*: [Link](./trial_78)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.2987290456087326     |
| learning_rate          | 1.4558488937695981e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9944    | 0.9844    | 0.9843    | 
| precision | 0.9944    | 0.9844    | 0.9843    | 
| recall    | 0.9944    | 0.9844    | 0.9843    | 
| f1        | 0.9944    | 0.9844    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_78/model_summary.png)

![confusion_matrix](./trial_78/confusion_matrix.png)

![training_history](./trial_78/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9793       | 0.9916       | 0.9854       | 477          | 
| muffin       | 0.9902       | 0.9760       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9848       | 0.9838       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_89</span>

*    *Start Time*: 2024-10-23 08:55:46

*    *Duration*: 21.210

*    *Directory*: [Link](./trial_89)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.40166549302181703   |
| learning_rate         | 4.472827058679623e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9987    | 0.9875    | 0.9843    | 
| precision | 0.9987    | 0.9875    | 0.9843    | 
| recall    | 0.9987    | 0.9875    | 0.9843    | 
| f1        | 0.9987    | 0.9875    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_89/model_summary.png)

![confusion_matrix](./trial_89/confusion_matrix.png)

![training_history](./trial_89/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9874       | 0.9854       | 477          | 
| muffin       | 0.9855       | 0.9808       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9844       | 0.9841       | 0.9842       | 893          | 
| weighted avg | 0.9843       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_90</span>

*    *Start Time*: 2024-10-23 08:56:09

*    *Duration*: 21.413

*    *Directory*: [Link](./trial_90)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.39851293472332594   |
| learning_rate         | 4.463734526008971e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9987    | 0.9922    | 0.9843    | 
| precision | 0.9987    | 0.9922    | 0.9843    | 
| recall    | 0.9987    | 0.9922    | 0.9843    | 
| f1        | 0.9987    | 0.9922    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_90/model_summary.png)

![confusion_matrix](./trial_90/confusion_matrix.png)

![training_history](./trial_90/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_91</span>

*    *Start Time*: 2024-10-23 08:56:33

*    *Duration*: 20.991

*    *Directory*: [Link](./trial_91)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 128                   |
| dropout_rate          | 0.4521993710777526    |
| learning_rate         | 5.798958175745282e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9959    | 0.9859    | 0.9843    | 
| precision | 0.9959    | 0.9859    | 0.9843    | 
| recall    | 0.9959    | 0.9859    | 0.9843    | 
| f1        | 0.9959    | 0.9859    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_91/model_summary.png)

![confusion_matrix](./trial_91/confusion_matrix.png)

![training_history](./trial_91/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_92</span>

*    *Start Time*: 2024-10-23 08:56:57

*    *Duration*: 21.340

*    *Directory*: [Link](./trial_92)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 256                  |
| dropout_rate         | 0.4234111774988462   |
| learning_rate        | 7.16516950697305e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9843    | 
| precision | 0.9997    | 0.9891    | 0.9843    | 
| recall    | 0.9997    | 0.9891    | 0.9843    | 
| f1        | 0.9997    | 0.9891    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_92/model_summary.png)

![confusion_matrix](./trial_92/confusion_matrix.png)

![training_history](./trial_92/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_93</span>

*    *Start Time*: 2024-10-23 08:57:20

*    *Duration*: 21.179

*    *Directory*: [Link](./trial_93)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.377242687199327      |
| learning_rate          | 2.8307555769685253e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9947    | 0.9875    | 0.9843    | 
| precision | 0.9947    | 0.9875    | 0.9843    | 
| recall    | 0.9947    | 0.9875    | 0.9843    | 
| f1        | 0.9947    | 0.9875    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_93/model_summary.png)

![confusion_matrix](./trial_93/confusion_matrix.png)

![training_history](./trial_93/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_96</span>

*    *Start Time*: 2024-10-23 08:58:32

*    *Duration*: 21.421

*    *Directory*: [Link](./trial_96)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.40371571994873595    |
| learning_rate          | 4.1626665217130035e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9906    | 0.9843    | 
| precision | 0.9997    | 0.9906    | 0.9843    | 
| recall    | 0.9997    | 0.9906    | 0.9843    | 
| f1        | 0.9997    | 0.9906    | 0.9843    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_96/model_summary.png)

![confusion_matrix](./trial_96/confusion_matrix.png)

![training_history](./trial_96/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9813       | 0.9895       | 0.9854       | 477          | 
| muffin       | 0.9879       | 0.9784       | 0.9831       | 416          | 
| micro avg    | 0.9843       | 0.9843       | 0.9843       | 893          | 
| macro avg    | 0.9846       | 0.9839       | 0.9842       | 893          | 
| weighted avg | 0.9844       | 0.9843       | 0.9843       | 893          | 
| samples avg  | 0.9843       | 0.9843       | 0.9843       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_18</span>

*    *Start Time*: 2024-10-23 08:28:37

*    *Duration*: 22.111

*    *Directory*: [Link](./trial_18)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.41850228623510344    |
| learning_rate          | 2.8536446734542353e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9981    | 0.9906    | 0.9832    | 
| precision | 0.9981    | 0.9906    | 0.9832    | 
| recall    | 0.9981    | 0.9906    | 0.9832    | 
| f1        | 0.9981    | 0.9906    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_18/model_summary.png)

![confusion_matrix](./trial_18/confusion_matrix.png)

![training_history](./trial_18/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9793       | 0.9895       | 0.9844       | 477          | 
| muffin       | 0.9878       | 0.9760       | 0.9819       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9835       | 0.9827       | 0.9831       | 893          | 
| weighted avg | 0.9833       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_22</span>

*    *Start Time*: 2024-10-23 08:30:09

*    *Duration*: 22.045

*    *Directory*: [Link](./trial_22)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.44792604915790446    |
| learning_rate          | 2.8183415668140906e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9978    | 0.9906    | 0.9832    | 
| precision | 0.9978    | 0.9906    | 0.9832    | 
| recall    | 0.9978    | 0.9906    | 0.9832    | 
| f1        | 0.9978    | 0.9906    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_22/model_summary.png)

![confusion_matrix](./trial_22/confusion_matrix.png)

![training_history](./trial_22/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9793       | 0.9895       | 0.9844       | 477          | 
| muffin       | 0.9878       | 0.9760       | 0.9819       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9835       | 0.9827       | 0.9831       | 893          | 
| weighted avg | 0.9833       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_35</span>

*    *Start Time*: 2024-10-23 08:35:06

*    *Duration*: 21.387

*    *Directory*: [Link](./trial_35)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.2926226204881526     |
| learning_rate          | 2.6327528577677017e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9991    | 0.9859    | 0.9832    | 
| precision | 0.9991    | 0.9859    | 0.9832    | 
| recall    | 0.9991    | 0.9859    | 0.9832    | 
| f1        | 0.9991    | 0.9859    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_35/model_summary.png)

![confusion_matrix](./trial_35/confusion_matrix.png)

![training_history](./trial_35/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9833       | 0.9853       | 0.9843       | 477          | 
| muffin       | 0.9831       | 0.9808       | 0.9819       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9832       | 0.9830       | 0.9831       | 893          | 
| weighted avg | 0.9832       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_38</span>

*    *Start Time*: 2024-10-23 08:36:14

*    *Duration*: 20.919

*    *Directory*: [Link](./trial_38)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.3230135735755826    |
| learning_rate         | 1.930034078695228e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9937    | 0.9875    | 0.9832    | 
| precision | 0.9937    | 0.9875    | 0.9832    | 
| recall    | 0.9937    | 0.9875    | 0.9832    | 
| f1        | 0.9937    | 0.9875    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_38/model_summary.png)

![confusion_matrix](./trial_38/confusion_matrix.png)

![training_history](./trial_38/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9773       | 0.9916       | 0.9844       | 477          | 
| muffin       | 0.9902       | 0.9736       | 0.9818       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9837       | 0.9826       | 0.9831       | 893          | 
| weighted avg | 0.9833       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_42</span>

*    *Start Time*: 2024-10-23 08:37:44

*    *Duration*: 21.079

*    *Directory*: [Link](./trial_42)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.429782411318927      |
| learning_rate          | 3.0103469814009053e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9987    | 0.9906    | 0.9832    | 
| precision | 0.9987    | 0.9906    | 0.9832    | 
| recall    | 0.9987    | 0.9906    | 0.9832    | 
| f1        | 0.9987    | 0.9906    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_42/model_summary.png)

![confusion_matrix](./trial_42/confusion_matrix.png)

![training_history](./trial_42/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9812       | 0.9874       | 0.9843       | 477          | 
| muffin       | 0.9855       | 0.9784       | 0.9819       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9834       | 0.9829       | 0.9831       | 893          | 
| weighted avg | 0.9832       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_51</span>

*    *Start Time*: 2024-10-23 08:41:07

*    *Duration*: 21.018

*    *Directory*: [Link](./trial_51)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 128                   |
| dropout_rate          | 0.48740510209775534   |
| learning_rate         | 9.222321316683178e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9997    | 0.9891    | 0.9832    | 
| precision | 0.9997    | 0.9891    | 0.9832    | 
| recall    | 0.9997    | 0.9891    | 0.9832    | 
| f1        | 0.9997    | 0.9891    | 0.9832    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_51/model_summary.png)

![confusion_matrix](./trial_51/confusion_matrix.png)

![training_history](./trial_51/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9793       | 0.9895       | 0.9844       | 477          | 
| muffin       | 0.9878       | 0.9760       | 0.9819       | 416          | 
| micro avg    | 0.9832       | 0.9832       | 0.9832       | 893          | 
| macro avg    | 0.9835       | 0.9827       | 0.9831       | 893          | 
| weighted avg | 0.9833       | 0.9832       | 0.9832       | 893          | 
| samples avg  | 0.9832       | 0.9832       | 0.9832       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_7</span>

*    *Start Time*: 2024-10-23 08:24:27

*    *Duration*: 23.807

*    *Directory*: [Link](./trial_7)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 128                   |
| dropout_rate          | 0.420268175071424     |
| learning_rate         | 2.013323535809419e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9884    | 0.9844    | 0.9821    | 
| precision | 0.9884    | 0.9844    | 0.9821    | 
| recall    | 0.9884    | 0.9844    | 0.9821    | 
| f1        | 0.9884    | 0.9844    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_7/model_summary.png)

![confusion_matrix](./trial_7/confusion_matrix.png)

![training_history](./trial_7/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_19</span>

*    *Start Time*: 2024-10-23 08:29:00

*    *Duration*: 21.985

*    *Directory*: [Link](./trial_19)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.42789838205012715    |
| learning_rate          | 2.2083880170354025e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9962    | 0.9891    | 0.9821    | 
| precision | 0.9962    | 0.9891    | 0.9821    | 
| recall    | 0.9962    | 0.9891    | 0.9821    | 
| f1        | 0.9962    | 0.9891    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_19/model_summary.png)

![confusion_matrix](./trial_19/confusion_matrix.png)

![training_history](./trial_19/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9772       | 0.9895       | 0.9833       | 477          | 
| muffin       | 0.9878       | 0.9736       | 0.9806       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9825       | 0.9815       | 0.9820       | 893          | 
| weighted avg | 0.9822       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_31</span>

*    *Start Time*: 2024-10-23 08:33:36

*    *Duration*: 20.905

*    *Directory*: [Link](./trial_31)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.2478321279349705     |
| learning_rate          | 1.4444587503272052e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9947    | 0.9891    | 0.9821    | 
| precision | 0.9947    | 0.9891    | 0.9821    | 
| recall    | 0.9947    | 0.9891    | 0.9821    | 
| f1        | 0.9947    | 0.9891    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_31/model_summary.png)

![confusion_matrix](./trial_31/confusion_matrix.png)

![training_history](./trial_31/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_41</span>

*    *Start Time*: 2024-10-23 08:37:21

*    *Duration*: 21.320

*    *Directory*: [Link](./trial_41)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.28150916358604805    |
| learning_rate          | 2.2112280316430957e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9956    | 0.9875    | 0.9821    | 
| precision | 0.9956    | 0.9875    | 0.9821    | 
| recall    | 0.9956    | 0.9875    | 0.9821    | 
| f1        | 0.9956    | 0.9875    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_41/model_summary.png)

![confusion_matrix](./trial_41/confusion_matrix.png)

![training_history](./trial_41/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9812       | 0.9853       | 0.9833       | 477          | 
| muffin       | 0.9831       | 0.9784       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9822       | 0.9818       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_56</span>

*    *Start Time*: 2024-10-23 08:43:02

*    *Duration*: 21.312

*    *Directory*: [Link](./trial_56)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4465505326886864     |
| learning_rate          | 2.4985339986144867e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9962    | 0.9875    | 0.9821    | 
| precision | 0.9962    | 0.9875    | 0.9821    | 
| recall    | 0.9962    | 0.9875    | 0.9821    | 
| f1        | 0.9962    | 0.9875    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_56/model_summary.png)

![confusion_matrix](./trial_56/confusion_matrix.png)

![training_history](./trial_56/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_57</span>

*    *Start Time*: 2024-10-23 08:43:25

*    *Duration*: 20.993

*    *Directory*: [Link](./trial_57)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.3822743621870885    |
| learning_rate         | 3.518681469076561e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9975    | 0.9891    | 0.9821    | 
| precision | 0.9975    | 0.9891    | 0.9821    | 
| recall    | 0.9975    | 0.9891    | 0.9821    | 
| f1        | 0.9975    | 0.9891    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_57/model_summary.png)

![confusion_matrix](./trial_57/confusion_matrix.png)

![training_history](./trial_57/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9772       | 0.9895       | 0.9833       | 477          | 
| muffin       | 0.9878       | 0.9736       | 0.9806       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9825       | 0.9815       | 0.9820       | 893          | 
| weighted avg | 0.9822       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_65</span>

*    *Start Time*: 2024-10-23 08:46:28

*    *Duration*: 21.033

*    *Directory*: [Link](./trial_65)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.3792502377823683    |
| learning_rate         | 1.709664451817053e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9944    | 0.9891    | 0.9821    | 
| precision | 0.9944    | 0.9891    | 0.9821    | 
| recall    | 0.9944    | 0.9891    | 0.9821    | 
| f1        | 0.9944    | 0.9891    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_65/model_summary.png)

![confusion_matrix](./trial_65/confusion_matrix.png)

![training_history](./trial_65/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_71</span>

*    *Start Time*: 2024-10-23 08:48:46

*    *Duration*: 20.842

*    *Directory*: [Link](./trial_71)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter       | Value                |
| -------------------- | -------------------- |
| dense_units          | 512                  |
| dropout_rate         | 0.20404534679600567  |
| learning_rate        | 1.65588951200883e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9944    | 0.9859    | 0.9821    | 
| precision | 0.9944    | 0.9859    | 0.9821    | 
| recall    | 0.9944    | 0.9859    | 0.9821    | 
| f1        | 0.9944    | 0.9859    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_71/model_summary.png)

![confusion_matrix](./trial_71/confusion_matrix.png)

![training_history](./trial_71/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_74</span>

*    *Start Time*: 2024-10-23 08:49:55

*    *Duration*: 21.162

*    *Directory*: [Link](./trial_74)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.3807571660972885     |
| learning_rate          | 2.4128773899546423e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9972    | 0.9859    | 0.9821    | 
| precision | 0.9972    | 0.9859    | 0.9821    | 
| recall    | 0.9972    | 0.9859    | 0.9821    | 
| f1        | 0.9972    | 0.9859    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_74/model_summary.png)

![confusion_matrix](./trial_74/confusion_matrix.png)

![training_history](./trial_74/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9772       | 0.9895       | 0.9833       | 477          | 
| muffin       | 0.9878       | 0.9736       | 0.9806       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9825       | 0.9815       | 0.9820       | 893          | 
| weighted avg | 0.9822       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_77</span>

*    *Start Time*: 2024-10-23 08:51:05

*    *Duration*: 21.146

*    *Directory*: [Link](./trial_77)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.4065218139303472    |
| learning_rate         | 1.791178358168555e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9950    | 0.9859    | 0.9821    | 
| precision | 0.9950    | 0.9859    | 0.9821    | 
| recall    | 0.9950    | 0.9859    | 0.9821    | 
| f1        | 0.9950    | 0.9859    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_77/model_summary.png)

![confusion_matrix](./trial_77/confusion_matrix.png)

![training_history](./trial_77/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9772       | 0.9895       | 0.9833       | 477          | 
| muffin       | 0.9878       | 0.9736       | 0.9806       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9825       | 0.9815       | 0.9820       | 893          | 
| weighted avg | 0.9822       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_80</span>

*    *Start Time*: 2024-10-23 08:52:15

*    *Duration*: 20.895

*    *Directory*: [Link](./trial_80)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.33567484538066134    |
| learning_rate          | 2.6247992542590503e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9978    | 0.9891    | 0.9821    | 
| precision | 0.9978    | 0.9891    | 0.9821    | 
| recall    | 0.9978    | 0.9891    | 0.9821    | 
| f1        | 0.9978    | 0.9891    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_80/model_summary.png)

![confusion_matrix](./trial_80/confusion_matrix.png)

![training_history](./trial_80/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_88</span>

*    *Start Time*: 2024-10-23 08:55:22

*    *Duration*: 21.151

*    *Directory*: [Link](./trial_88)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.37132090000481177   |
| learning_rate         | 3.177687855006244e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9987    | 0.9875    | 0.9821    | 
| precision | 0.9987    | 0.9875    | 0.9821    | 
| recall    | 0.9987    | 0.9875    | 0.9821    | 
| f1        | 0.9987    | 0.9875    | 0.9821    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_88/model_summary.png)

![confusion_matrix](./trial_88/confusion_matrix.png)

![training_history](./trial_88/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9792       | 0.9874       | 0.9833       | 477          | 
| muffin       | 0.9854       | 0.9760       | 0.9807       | 416          | 
| micro avg    | 0.9821       | 0.9821       | 0.9821       | 893          | 
| macro avg    | 0.9823       | 0.9817       | 0.9820       | 893          | 
| weighted avg | 0.9821       | 0.9821       | 0.9821       | 893          | 
| samples avg  | 0.9821       | 0.9821       | 0.9821       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_2</span>

*    *Start Time*: 2024-10-23 08:22:34

*    *Duration*: 24.230

*    *Directory*: [Link](./trial_2)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 256                    |
| dropout_rate           | 0.11335966061241398    |
| learning_rate          | 2.6026128455996584e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9962    | 0.9875    | 0.9810    | 
| precision | 0.9962    | 0.9875    | 0.9810    | 
| recall    | 0.9962    | 0.9875    | 0.9810    | 
| f1        | 0.9962    | 0.9875    | 0.9810    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_2/model_summary.png)

![confusion_matrix](./trial_2/confusion_matrix.png)

![training_history](./trial_2/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9812       | 0.9832       | 0.9822       | 477          | 
| muffin       | 0.9807       | 0.9784       | 0.9795       | 416          | 
| micro avg    | 0.9810       | 0.9810       | 0.9810       | 893          | 
| macro avg    | 0.9809       | 0.9808       | 0.9809       | 893          | 
| weighted avg | 0.9810       | 0.9810       | 0.9810       | 893          | 
| samples avg  | 0.9810       | 0.9810       | 0.9810       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_20</span>

*    *Start Time*: 2024-10-23 08:29:22

*    *Duration*: 22.213

*    *Directory*: [Link](./trial_20)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4440579190933088     |
| learning_rate          | 1.0339583539131823e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9878    | 0.9875    | 0.9810    | 
| precision | 0.9878    | 0.9875    | 0.9810    | 
| recall    | 0.9878    | 0.9875    | 0.9810    | 
| f1        | 0.9878    | 0.9875    | 0.9810    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_20/model_summary.png)

![confusion_matrix](./trial_20/confusion_matrix.png)

![training_history](./trial_20/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9733       | 0.9916       | 0.9823       | 477          | 
| muffin       | 0.9902       | 0.9688       | 0.9793       | 416          | 
| micro avg    | 0.9810       | 0.9810       | 0.9810       | 893          | 
| macro avg    | 0.9817       | 0.9802       | 0.9808       | 893          | 
| weighted avg | 0.9811       | 0.9810       | 0.9809       | 893          | 
| samples avg  | 0.9810       | 0.9810       | 0.9810       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_68</span>

*    *Start Time*: 2024-10-23 08:47:37

*    *Duration*: 20.930

*    *Directory*: [Link](./trial_68)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.48783591226737677   |
| learning_rate         | 1.908518229919593e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9944    | 0.9859    | 0.9810    | 
| precision | 0.9944    | 0.9859    | 0.9810    | 
| recall    | 0.9944    | 0.9859    | 0.9810    | 
| f1        | 0.9944    | 0.9859    | 0.9810    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_68/model_summary.png)

![confusion_matrix](./trial_68/confusion_matrix.png)

![training_history](./trial_68/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9752       | 0.9895       | 0.9823       | 477          | 
| muffin       | 0.9878       | 0.9712       | 0.9794       | 416          | 
| micro avg    | 0.9810       | 0.9810       | 0.9810       | 893          | 
| macro avg    | 0.9815       | 0.9803       | 0.9809       | 893          | 
| weighted avg | 0.9811       | 0.9810       | 0.9810       | 893          | 
| samples avg  | 0.9810       | 0.9810       | 0.9810       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_94</span>

*    *Start Time*: 2024-10-23 08:57:44

*    *Duration*: 21.020

*    *Directory*: [Link](./trial_94)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 256                   |
| dropout_rate          | 0.26597813048668306   |
| learning_rate         | 3.425150625695044e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9975    | 0.9875    | 0.9810    | 
| precision | 0.9975    | 0.9875    | 0.9810    | 
| recall    | 0.9975    | 0.9875    | 0.9810    | 
| f1        | 0.9975    | 0.9875    | 0.9810    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_94/model_summary.png)

![confusion_matrix](./trial_94/confusion_matrix.png)

![training_history](./trial_94/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9752       | 0.9895       | 0.9823       | 477          | 
| muffin       | 0.9878       | 0.9712       | 0.9794       | 416          | 
| micro avg    | 0.9810       | 0.9810       | 0.9810       | 893          | 
| macro avg    | 0.9815       | 0.9803       | 0.9809       | 893          | 
| weighted avg | 0.9811       | 0.9810       | 0.9810       | 893          | 
| samples avg  | 0.9810       | 0.9810       | 0.9810       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_59</span>

*    *Start Time*: 2024-10-23 08:44:11

*    *Duration*: 20.786

*    *Directory*: [Link](./trial_59)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 128                    |
| dropout_rate           | 0.4606890123413379     |
| learning_rate          | 3.5020321804385535e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9934    | 0.9875    | 0.9798    | 
| precision | 0.9934    | 0.9875    | 0.9798    | 
| recall    | 0.9934    | 0.9875    | 0.9798    | 
| f1        | 0.9934    | 0.9875    | 0.9798    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_59/model_summary.png)

![confusion_matrix](./trial_59/confusion_matrix.png)

![training_history](./trial_59/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9732       | 0.9895       | 0.9813       | 477          | 
| muffin       | 0.9877       | 0.9688       | 0.9782       | 416          | 
| micro avg    | 0.9798       | 0.9798       | 0.9798       | 893          | 
| macro avg    | 0.9805       | 0.9791       | 0.9797       | 893          | 
| weighted avg | 0.9800       | 0.9798       | 0.9798       | 893          | 
| samples avg  | 0.9798       | 0.9798       | 0.9798       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_66</span>

*    *Start Time*: 2024-10-23 08:46:51

*    *Duration*: 21.025

*    *Directory*: [Link](./trial_66)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.3833154196834341    |
| learning_rate         | 1.634410508999156e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9947    | 0.9859    | 0.9798    | 
| precision | 0.9947    | 0.9859    | 0.9798    | 
| recall    | 0.9947    | 0.9859    | 0.9798    | 
| f1        | 0.9947    | 0.9859    | 0.9798    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_66/model_summary.png)

![confusion_matrix](./trial_66/confusion_matrix.png)

![training_history](./trial_66/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9771       | 0.9853       | 0.9812       | 477          | 
| muffin       | 0.9830       | 0.9736       | 0.9783       | 416          | 
| micro avg    | 0.9798       | 0.9798       | 0.9798       | 893          | 
| macro avg    | 0.9801       | 0.9794       | 0.9797       | 893          | 
| weighted avg | 0.9799       | 0.9798       | 0.9798       | 893          | 
| samples avg  | 0.9798       | 0.9798       | 0.9798       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_11</span>

*    *Start Time*: 2024-10-23 08:25:59

*    *Duration*: 21.623

*    *Directory*: [Link](./trial_11)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter        | Value                 |
| --------------------- | --------------------- |
| dense_units           | 512                   |
| dropout_rate          | 0.47798041416634385   |
| learning_rate         | 1.135292534178908e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9928    | 0.9891    | 0.9787    | 
| precision | 0.9928    | 0.9891    | 0.9787    | 
| recall    | 0.9928    | 0.9891    | 0.9787    | 
| f1        | 0.9928    | 0.9891    | 0.9787    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_11/model_summary.png)

![confusion_matrix](./trial_11/confusion_matrix.png)

![training_history](./trial_11/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9751       | 0.9853       | 0.9802       | 477          | 
| muffin       | 0.9830       | 0.9712       | 0.9770       | 416          | 
| micro avg    | 0.9787       | 0.9787       | 0.9787       | 893          | 
| macro avg    | 0.9790       | 0.9782       | 0.9786       | 893          | 
| weighted avg | 0.9788       | 0.9787       | 0.9787       | 893          | 
| samples avg  | 0.9787       | 0.9787       | 0.9787       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_44</span>

*    *Start Time*: 2024-10-23 08:38:29

*    *Duration*: 21.254

*    *Directory*: [Link](./trial_44)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.365182597129303      |
| learning_rate          | 1.2883070605895913e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9931    | 0.9906    | 0.9787    | 
| precision | 0.9931    | 0.9906    | 0.9787    | 
| recall    | 0.9931    | 0.9906    | 0.9787    | 
| f1        | 0.9931    | 0.9906    | 0.9787    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_44/model_summary.png)

![confusion_matrix](./trial_44/confusion_matrix.png)

![training_history](./trial_44/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9712       | 0.9895       | 0.9803       | 477          | 
| muffin       | 0.9877       | 0.9663       | 0.9769       | 416          | 
| micro avg    | 0.9787       | 0.9787       | 0.9787       | 893          | 
| macro avg    | 0.9795       | 0.9779       | 0.9786       | 893          | 
| weighted avg | 0.9789       | 0.9787       | 0.9787       | 893          | 
| samples avg  | 0.9787       | 0.9787       | 0.9787       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_67</span>

*    *Start Time*: 2024-10-23 08:47:14

*    *Duration*: 20.948

*    *Directory*: [Link](./trial_67)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.4351654716716183     |
| learning_rate          | 1.3042658639188106e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9912    | 0.9859    | 0.9787    | 
| precision | 0.9912    | 0.9859    | 0.9787    | 
| recall    | 0.9912    | 0.9859    | 0.9787    | 
| f1        | 0.9912    | 0.9859    | 0.9787    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_67/model_summary.png)

![confusion_matrix](./trial_67/confusion_matrix.png)

![training_history](./trial_67/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9751       | 0.9853       | 0.9802       | 477          | 
| muffin       | 0.9830       | 0.9712       | 0.9770       | 416          | 
| micro avg    | 0.9787       | 0.9787       | 0.9787       | 893          | 
| macro avg    | 0.9790       | 0.9782       | 0.9786       | 893          | 
| weighted avg | 0.9788       | 0.9787       | 0.9787       | 893          | 
| samples avg  | 0.9787       | 0.9787       | 0.9787       | 893          | 



<div style="page-break-after: always;"></div>

## <span style="color:rgb(105, 169, 201);">trial_26</span>

*    *Start Time*: 2024-10-23 08:31:40

*    *Duration*: 22.256

*    *Directory*: [Link](./trial_26)

### <span style="color:rgb(105, 169, 201);">Hyperparameters:</span>

| Hyperparameter         | Value                  |
| ---------------------- | ---------------------- |
| dense_units            | 512                    |
| dropout_rate           | 0.44421113381181854    |
| learning_rate          | 1.5031842129389874e-05 |


### <span style="color:rgb(105, 169, 201);">Evaluation Metrics:</span>

|           | train     | val       | test      |
| --------- | --------- | --------- | --------- |
| accuracy  | 0.9931    | 0.9875    | 0.9765    | 
| precision | 0.9931    | 0.9875    | 0.9765    | 
| recall    | 0.9931    | 0.9875    | 0.9765    | 
| f1        | 0.9931    | 0.9875    | 0.9765    | 



<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Figures:</span>

![model_summary](./trial_26/model_summary.png)

![confusion_matrix](./trial_26/confusion_matrix.png)

![training_history](./trial_26/training_history.png)


<div style="page-break-after: always;"></div>

### <span style="color:rgb(105, 169, 201);">Detailed Report of Test Set:</span>

|              | precision    | recall       | f1-score     | support      |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| chihuahua    | 0.9730       | 0.9832       | 0.9781       | 477          | 
| muffin       | 0.9805       | 0.9688       | 0.9746       | 416          | 
| micro avg    | 0.9765       | 0.9765       | 0.9765       | 893          | 
| macro avg    | 0.9768       | 0.9760       | 0.9764       | 893          | 
| weighted avg | 0.9765       | 0.9765       | 0.9765       | 893          | 
| samples avg  | 0.9765       | 0.9765       | 0.9765       | 893          | 

