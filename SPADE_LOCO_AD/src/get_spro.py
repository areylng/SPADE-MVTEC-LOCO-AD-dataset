from O_evaluation.evaluate_experiment import EVAL_ME
import cv2


def Get_SPRO_Fun(output_segments,data_type):


    if data_type=='juice_bottle':
        spilt = [94,94+142]
        img_size = [800,1600]
        img_max_com = 0.925
    if data_type == 'splicing_connectors':
        spilt = [119, 119 + 108]
        img_size = [1700, 850]
        img_max_com = 0.79
    if data_type == 'screw_bag':
        spilt = [122, 122 + 137]
        img_size = [1600, 1100]
        img_max_com = 0.70
    if data_type == 'pushpins':
        spilt = [138, 138 + 91]
        img_size = [1700, 1000]
        img_max_com = 0.91
    if data_type == 'breakfast_box':
        spilt = [102, 102 + 83]
        img_size = [1600, 1280]
        img_max_com = 0.86





    output_segments_NEW = output_segments

    all_index_img = 0
    index_img = 0
    for ikik in range(0,spilt[0]):
        temp = output_segments_NEW[ikik]
        temp = cv2.resize(temp, (img_size[0], img_size[1]))
        tt = str(index_img)
        if len(tt)==1:
            tt='00'+tt
        if len(tt)==2:
            tt='0'+tt

        # B = temp
        # B[B>=fgf]=1
        # B[B < fgf] = 0
        # kerne2 = np.ones((11, 11), np.uint8)
        # B = cv2.erode(B, kerne2, iterations=1)
        # kerne2 = np.ones((3, 3), np.uint8)
        # B = cv2.dilate(B, kerne2, iterations=1)
        # temp = B*temp

        #temp=temp*MAX_MAX[all_index_img]
        cv2.imwrite(f'log_metris/{data_type}/test/good/{tt}.tiff', temp)
        #plt.imsave(f'log_metris/model_name/{data_type}/test/good/{tt}.tiff', temp,cmap=cm.gray)
        index_img+=1
        all_index_img+=1

    index_img = 0
    for ikik in range(spilt[0],spilt[1]):
        temp = output_segments_NEW[ikik]
        temp = cv2.resize(temp,(img_size[0], img_size[1]))
        tt = str(index_img)
        if len(tt)==1:
            tt='00'+tt
        if len(tt)==2:
            tt='0'+tt

        # B = temp
        # B[B>=fgf]=1
        # B[B < fgf] = 0
        # kerne2 = np.ones((11, 11), np.uint8)
        # B = cv2.erode(B, kerne2, iterations=1)
        # kerne2 = np.ones((3, 3), np.uint8)
        # B = cv2.dilate(B, kerne2, iterations=1)
        # temp = B*temp
        #temp = temp * MAX_MAX[all_index_img]
        #plt.imsave(f'log_metris/model_name/{data_type}/test/logical_anomalies/{tt}.tiff', temp,cmap=cm.gray)
        cv2.imwrite(f'log_metris/{data_type}/test/logical_anomalies/{tt}.tiff', temp)
        index_img+=1
        all_index_img += 1
    index_img = 0
    for ikik in range(spilt[1], output_segments.shape[0]):
        temp = output_segments_NEW[ikik]
        temp = cv2.resize(temp, (img_size[0], img_size[1]))
        tt = str(index_img)
        if len(tt)==1:
            tt='00'+tt
        if len(tt)==2:
            tt='0'+tt
        # B = temp
        # B[B>=fgf]=1
        # B[B < fgf] = 0
        # kerne2 = np.ones((11, 11), np.uint8)
        # B = cv2.erode(B, kerne2, iterations=1)
        # kerne2 = np.ones((3, 3), np.uint8)
        # B = cv2.dilate(B, kerne2, iterations=1)
        # temp = B*temp
        #temp = temp * MAX_MAX[all_index_img]
        cv2.imwrite(f'log_metris/{data_type}/test/structural_anomalies/{tt}.tiff', temp)
        #plt.imsave(f'log_metris/model_name/{data_type}/test/structural_anomalies/{tt}.tiff', temp,cmap=cm.gray)

        index_img+=1
        all_index_img += 1

    print('generate done')

    #if img_max>0.9

    EVAL_ME(data_type=data_type)