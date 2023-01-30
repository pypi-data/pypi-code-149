__author__ = 'tsungyi'

import numpy as np
import datetime
import time
from collections import defaultdict
from . import mask as maskUtils
import copy


class COCOeval:
    # Interface for evaluating detection on the Microsoft COCO dataset.
    # The usage for CocoEval is as follows:
    #  cocoGt=..., cocoDt=...       # load dataset and results
    #  E = CocoEval(cocoGt,cocoDt); # initialize CocoEval object
    #  E.params.recThrs = ...;      # set parameters as desired
    #  E.evaluate();                # run per image evaluation
    #  E.accumulate();              # accumulate per image results
    #  E.summarize();               # display summary metrics of results
    # For example usage see evalDemo.m and http://mscoco.org/.
    #
    # The evaluation parameters are as follows (defaults in brackets):
    #  imgIds     - [all] N img ids to use for evaluation
    #  catIds     - [all] K cat ids to use for evaluation
    #  iouThrs    - [.5:.05:.95] T=10 IoU thresholds for evaluation
    #  recThrs    - [0:.01:1] R=101 recall thresholds for evaluation
    #  areaRng    - [...] A=4 object area ranges for evaluation
    #  maxDets    - [1 10 100] M=3 thresholds on max detections per image
    #  iouType    - ['segm'] set iouType to 'segm', 'bbox' or 'keypoints'
    #  iouType replaced the now DEPRECATED useSegm parameter.
    #  useCats    - [1] if true use category labels for evaluation
    # Note: if useCats=0 category labels are ignored as in proposal scoring.
    # Note: multiple areaRngs [Ax2] and maxDets [Mx1] can be specified.
    #
    # evaluate(): evaluates detections on every image and every category and
    # concats the results into the "evalImgs" with fields:
    #  dtIds      - [1xD] id for each of the D detections (dt)
    #  gtIds      - [1xG] id for each of the G ground truths (gt)
    #  dtMatches  - [TxD] matching gt id at each IoU or 0
    #  gtMatches  - [TxG] matching dt id at each IoU or 0
    #  dtScores   - [1xD] confidence of each dt
    #  gtIgnore   - [1xG] ignore flag for each gt
    #  dtIgnore   - [TxD] ignore flag for each dt at each IoU
    #
    # accumulate(): accumulates the per-image, per-category evaluation
    # results in "evalImgs" into the dictionary "eval" with fields:
    #  params     - parameters used for evaluation
    #  date       - date evaluation was performed
    #  counts     - [T,R,K,A,M] parameter dimensions (see above)
    #  precision  - [TxRxKxAxM] precision for every evaluation setting
    #  recall     - [TxKxAxM] max recall for every evaluation setting
    # Note: precision and recall==-1 for settings with no gt objects.
    #
    # See also coco, mask, pycocoDemo, pycocoEvalDemo
    #
    # Microsoft COCO Toolbox.      version 2.0
    # Data, paper, and tutorials available at:  http://mscoco.org/
    # Code written by Piotr Dollar and Tsung-Yi Lin, 2015.
    # Licensed under the Simplified BSD License [see coco/license.txt]
    def __init__(self, cocoGt=None, cocoDt=None, iouType='segm'):
        '''
        Initialize CocoEval using coco APIs for gt and dt
        :param cocoGt: coco object with ground truth annotations
        :param cocoDt: coco object with detection results
        :return: None
        '''
        if not iouType:
            print('iouType not specified. use default iouType segm')
        self.cocoGt = cocoGt  # ground truth COCO API
        self.cocoDt = cocoDt  # detections COCO API
        self.evalImgs = defaultdict(list)  # per-image per-category evaluation results [KxAxI] elements
        self.eval = {}  # accumulated evaluation results
        self._gts = defaultdict(list)  # gt for evaluation
        self._dts = defaultdict(list)  # dt for evaluation
        self.params = Params(iouType=iouType)  # parameters
        self._paramsEval = {}  # parameters for evaluation
        self.stats = []  # result summarization
        self.ious = {}  # ious between all gts and dts
        if not cocoGt is None:
            self.params.imgIds = sorted(cocoGt.getImgIds())
            self.params.catIds = sorted(cocoGt.getCatIds())

    def _prepare(self):
        '''
        Prepare ._gts and ._dts for evaluation based on params
        :return: None
        '''

        def _toMask(anns, coco):
            # modify ann['segmentation'] by reference
            for ann in anns:
                rle = coco.annToRLE(ann)
                ann['segmentation'] = rle

        p = self.params
        if p.useCats:
            gts = self.cocoGt.loadAnns(self.cocoGt.getAnnIds(imgIds=p.imgIds, catIds=p.catIds))
            dts = self.cocoDt.loadAnns(self.cocoDt.getAnnIds(imgIds=p.imgIds, catIds=p.catIds))
        else:
            gts = self.cocoGt.loadAnns(self.cocoGt.getAnnIds(imgIds=p.imgIds))
            dts = self.cocoDt.loadAnns(self.cocoDt.getAnnIds(imgIds=p.imgIds))

        # convert ground truth to mask if iouType == 'segm'
        if p.iouType == 'segm':
            _toMask(gts, self.cocoGt)
            _toMask(dts, self.cocoDt)
        # set ignore flag
        for gt in gts:
            gt['ignore'] = gt['ignore'] if 'ignore' in gt else 0
            gt['ignore'] = 'iscrowd' in gt and gt['iscrowd']
            if p.iouType == 'keypoints':
                gt['ignore'] = (gt['num_keypoints'] == 0) or gt['ignore']
        self._gts = defaultdict(list)  # gt for evaluation
        self._dts = defaultdict(list)  # dt for evaluation
        for gt in gts:
            self._gts[gt['image_id'], gt['category_id']].append(gt)
        for dt in dts:
            self._dts[dt['image_id'], dt['category_id']].append(dt)
        self.evalImgs = defaultdict(list)  # per-image per-category evaluation results
        self.eval = {}  # accumulated evaluation results

    def evaluate(self):
        '''
        Run per image evaluation on given images and store results (a list of dict) in self.evalImgs
        :return: None
        '''
        tic = time.time()
        print('Running per image evaluation...')
        p = self.params
        # add backward compatibility if useSegm is specified in params
        if not p.useSegm is None:
            p.iouType = 'segm' if p.useSegm == 1 else 'bbox'
            print('useSegm (deprecated) is not None. Running {} evaluation'.format(p.iouType))
        print('Evaluate annotation type *{}*'.format(p.iouType))
        p.imgIds = list(np.unique(p.imgIds))
        if p.useCats:
            p.catIds = list(np.unique(p.catIds))
        p.maxDets = sorted(p.maxDets)
        self.params = p

        self._prepare()
        # loop through images, area range, max detection number
        catIds = p.catIds if p.useCats else [-1]

        if p.iouType == 'segm' or p.iouType == 'bbox':
            computeIoU = self.computeIoU
        elif p.iouType == 'keypoints':
            computeIoU = self.computeOks
        self.ious = {(imgId, catId): computeIoU(imgId, catId) \
                     for imgId in p.imgIds
                     for catId in catIds}

        evaluateImg = self.evaluateImg
        maxDet = p.maxDets[-1]
        self.evalImgs = [evaluateImg(imgId, catId, areaRng, maxDet)
                         for catId in catIds
                         for areaRng in p.areaRng
                         for imgId in p.imgIds
                         ]
        self._paramsEval = copy.deepcopy(self.params)
        toc = time.time()
        print('DONE (t={:0.2f}s).'.format(toc - tic))

    def computeIoU(self, imgId, catId):
        p = self.params
        if p.useCats:
            gt = self._gts[imgId, catId]
            dt = self._dts[imgId, catId]
        else:
            gt = [_ for cId in p.catIds for _ in self._gts[imgId, cId]]
            dt = [_ for cId in p.catIds for _ in self._dts[imgId, cId]]
        if len(gt) == 0 and len(dt) == 0:
            return []
        inds = np.argsort([-d['score'] for d in dt], kind='mergesort')
        dt = [dt[i] for i in inds]
        if len(dt) > p.maxDets[-1]:
            dt = dt[0:p.maxDets[-1]]

        if p.iouType == 'segm':
            g = [g['segmentation'] for g in gt]
            d = [d['segmentation'] for d in dt]
        elif p.iouType == 'bbox':
            g = [g['bbox'] for g in gt]
            d = [d['bbox'] for d in dt]
        else:
            raise Exception('unknown iouType for iou computation')

        # compute iou between each dt and gt region
        iscrowd = [int(o['iscrowd']) for o in gt]
        ious = maskUtils.iou(d, g, iscrowd)
        return ious

    def computeOks(self, imgId, catId):
        p = self.params
        # dimention here should be Nxm
        gts = self._gts[imgId, catId]
        dts = self._dts[imgId, catId]
        inds = np.argsort([-d['score'] for d in dts], kind='mergesort')
        dts = [dts[i] for i in inds]
        if len(dts) > p.maxDets[-1]:
            dts = dts[0:p.maxDets[-1]]
        # if len(gts) == 0 and len(dts) == 0:
        if len(gts) == 0 or len(dts) == 0:
            return []
        ious = np.zeros((len(dts), len(gts)))
        sigmas = p.kpt_oks_sigmas
        vars = (sigmas * 2) ** 2
        k = len(sigmas)
        # compute oks between each detection and ground truth object
        for j, gt in enumerate(gts):
            # create bounds for ignore regions(double the gt bbox)
            g = np.array(gt['keypoints'])
            xg = g[0::3];
            yg = g[1::3];
            vg = g[2::3]
            k1 = np.count_nonzero(vg > 0)
            bb = gt['bbox']
            x0 = bb[0] - bb[2];
            x1 = bb[0] + bb[2] * 2
            y0 = bb[1] - bb[3];
            y1 = bb[1] + bb[3] * 2
            for i, dt in enumerate(dts):
                d = np.array(dt['keypoints'])
                xd = d[0::3];
                yd = d[1::3]
                if k1 > 0:
                    # measure the per-keypoint distance if keypoints visible
                    dx = xd - xg
                    dy = yd - yg
                else:
                    # measure minimum distance to keypoints in (x0,y0) & (x1,y1)
                    z = np.zeros((k))
                    dx = np.max((z, x0 - xd), axis=0) + np.max((z, xd - x1), axis=0)
                    dy = np.max((z, y0 - yd), axis=0) + np.max((z, yd - y1), axis=0)
                e = (dx ** 2 + dy ** 2) / vars / (gt['area'] + np.spacing(1)) / 2
                if k1 > 0:
                    e = e[vg > 0]
                ious[i, j] = np.sum(np.exp(-e)) / e.shape[0]
        return ious

    def evaluateImg(self, imgId, catId, aRng, maxDet):
        '''
        perform evaluation for single category and image
        :return: dict (single image results)
        '''
        params = self.params
        if params.useCats:
            ground_truth = self._gts[imgId, catId]
            detections = self._dts[imgId, catId]
        else:
            ground_truth = [_ for cId in params.catIds for _ in self._gts[imgId, cId]]
            detections = [_ for cId in params.catIds for _ in self._dts[imgId, cId]]
        if len(ground_truth) == 0 and len(detections) == 0:
            return None

        for gt_data in ground_truth:
            gt_data['_ignore'] = gt_data['ignore'] or (gt_data['area'] < aRng[0] or gt_data['area'] > aRng[1])

        # Sort detections with the highest score first and ground truth with ignore flag last
        gt_sorted_indexes = np.argsort([g['_ignore'] for g in ground_truth], kind='mergesort')
        ground_truth = [ground_truth[i] for i in gt_sorted_indexes]
        dt_sorted_indexes = np.argsort([-d['score'] for d in detections], kind='mergesort')
        detections = [detections[i] for i in dt_sorted_indexes[0:maxDet]]
        gt_iscrowd = [int(o['iscrowd']) for o in ground_truth]

        # load computed ious
        ious = self.ious[imgId, catId][:, gt_sorted_indexes] if len(self.ious[imgId, catId]) > 0 else self.ious[
            imgId, catId]

        iou_thresh_count = len(params.iouThrs)
        ground_truth_count = len(ground_truth)
        detection_count = len(detections)

        ground_truth_matches = np.zeros((iou_thresh_count, ground_truth_count))
        detection_matches = np.zeros((iou_thresh_count, detection_count))
        ground_truth_ignore = np.array([g['_ignore'] for g in ground_truth])
        detection_ignore = np.zeros((iou_thresh_count, detection_count))
        eps = np.finfo(float).eps

        if not len(ious) == 0:
            for iou_thresh_ind, iou_thresh in enumerate(params.iouThrs):
                for detection_ind, d in enumerate(detections):
                    # Information about best match so far (m=-1 -> unmatched)
                    iou = min([iou_thresh, 1 - eps])
                    gt_match_index = -1

                    for gt_index in range(len(ground_truth)):
                        # If this ground truth detection already matched and not a crowd then continue
                        if ground_truth_matches[iou_thresh_ind, gt_index] > 0 and not gt_iscrowd[gt_index]:
                            continue
                        # If dt matched to reg gt, and on ignore gt, stop
                        if gt_match_index > -1 and ground_truth_ignore[gt_match_index] == 0 and ground_truth_ignore[
                            gt_index] == 1:
                            break
                        # Continue to next gt unless better match made
                        if ious[detection_ind, gt_index] < iou:
                            continue
                        # If match successful and best so far, store appropriately
                        iou = ious[detection_ind, gt_index]
                        gt_match_index = gt_index

                    # If no match then continue else store id of match for both dt and gt
                    if gt_match_index == -1:
                        continue

                    detection_ignore[iou_thresh_ind, detection_ind] = ground_truth_ignore[gt_match_index]
                    detection_matches[iou_thresh_ind, detection_ind] = ground_truth[gt_match_index]['id']
                    ground_truth_matches[iou_thresh_ind, gt_match_index] = d['id']

        # set unmatched detections outside of area range to ignore
        a = np.array([d['area'] < aRng[0] or d['area'] > aRng[1] for d in detections]).reshape((1, len(detections)))

        detection_ignore = np.logical_or(detection_ignore,
                                         np.logical_and(detection_matches == 0, np.repeat(a, iou_thresh_count, 0)))
        # store results for given image and category
        return {
            'image_id': imgId,
            'category_id': catId,
            'aRng': aRng,
            'maxDet': maxDet,
            'dtIds': [d['id'] for d in detections],
            'gtIds': [g['id'] for g in ground_truth],
            'dtMatches': detection_matches,
            'gtMatches': ground_truth_matches,
            'dtScores': [d['score'] for d in detections],
            'gtIgnore': ground_truth_ignore,
            'dtIgnore': detection_ignore,
        }

    def accumulate(self, p=None):
        '''
        Accumulate per image evaluation results and store the result in self.eval
        :param p: input params for evaluation
        :return: None
        '''
        print('Accumulating evaluation results...')
        tic = time.time()

        if not self.evalImgs:
            print('Please run evaluate() first')
        # allows input customized parameters

        if p is None:
            p = self.params

        p.catIds = p.catIds if p.useCats == 1 else [-1]
        iou_len = len(p.iouThrs)
        rec_lvls_len = len(p.recThrs)
        class_len = len(p.catIds) if p.useCats else 1
        area_len = len(p.areaRng)
        mdets_len = len(p.maxDets)
        precision = -np.ones(
            (iou_len, rec_lvls_len, class_len, area_len, mdets_len))  # -1 for the precision of absent categories
        recall = -np.ones((iou_len, class_len, area_len, mdets_len))
        scores = -np.ones((iou_len, rec_lvls_len, class_len, area_len, mdets_len))
        confusion_matrix = -np.ones((iou_len, class_len, area_len, mdets_len, 4))  # [TxKxAxMx[TP, FP, FN, TN]]

        # Create dictionary for future indexing
        _pe = self._paramsEval
        catIds = _pe.catIds if _pe.useCats else [-1]
        setK = set(catIds)
        setA = set(map(tuple, _pe.areaRng))
        setM = set(_pe.maxDets)
        setI = set(_pe.imgIds)
        # get inds to evaluate

        class_ind_list = [n for n, k in enumerate(p.catIds) if k in setK]
        m_list = [m for n, m in enumerate(p.maxDets) if m in setM]
        area_ind_list = [n for n, a in enumerate(map(lambda x: tuple(x), p.areaRng)) if a in setA]
        image_ind_list = [n for n, i in enumerate(p.imgIds) if i in setI]
        image_list_count = len(_pe.imgIds)
        area_list_count = len(_pe.areaRng)
        eps = np.finfo(float).eps

        # retrieve evaluation image at each category, area range, and max number of detections
        for class_ind in class_ind_list:
            Nk = class_ind * area_list_count * image_list_count

            for area_ind in area_ind_list:
                Na = area_ind * image_list_count
                for max_det_ind, max_det in enumerate(m_list):
                    eval_imgs = [self.evalImgs[Nk + Na + i] for i in image_ind_list]
                    eval_imgs = [e for e in eval_imgs if not e is None]

                    if len(eval_imgs) == 0:
                        continue
                    det_scores = np.concatenate([img['dtScores'][0:max_det] for img in eval_imgs])

                    # different sorting method generates slightly different results.
                    # mergesort is used to be consistent as Matlab implementation.
                    sort_inds = np.argsort(-det_scores, kind='mergesort')

                    det_matches = np.concatenate([img['dtMatches'][:, 0:max_det] for img in eval_imgs], axis=1)[:,
                                  sort_inds]
                    det_ignores = np.concatenate([img['dtIgnore'][:, 0:max_det] for img in eval_imgs], axis=1)[:,
                                  sort_inds]

                    # Ignored elements
                    gt_ignores = np.concatenate([img['gtIgnore'] for img in eval_imgs])
                    gt_include_count = np.count_nonzero(gt_ignores == 0)  # Number not ignored
                    if gt_include_count == 0:
                        continue

                    # positive=det_matches, negative=!det_matches
                    # negative=!det_ignores, positive=det_ignores
                    tps = np.logical_and(det_matches, np.logical_not(det_ignores))
                    fps = np.logical_and(np.logical_not(det_matches), np.logical_not(det_ignores))
                    tns = np.logical_and(np.logical_not(det_matches), det_ignores)
                    fns = np.logical_and(det_matches, det_ignores)

                    confusion_matrix[:, class_ind, area_ind, max_det_ind, :] = np.asarray(
                        [tps.sum(axis=1), fps.sum(axis=1), fns.sum(axis=1), tns.sum(axis=1)]
                    ).T

                    # True/False positive sum at each IoU Range
                    tp_sum = np.cumsum(tps, axis=1).astype(dtype=np.float)
                    fp_sum = np.cumsum(fps, axis=1).astype(dtype=np.float)

                    for iou_thresh_ind, (true_positives, false_positives) in enumerate(zip(tp_sum, fp_sum)):
                        true_positives = np.array(true_positives)
                        false_positives = np.array(false_positives)
                        detection_count = len(true_positives)

                        det_recall = true_positives / gt_include_count
                        det_precision = true_positives / (false_positives + true_positives + eps).tolist()

                        precision_at_rec_lvl = np.zeros((rec_lvls_len,)).tolist()
                        score_at_rec_lvl = np.zeros((rec_lvls_len,)).tolist()

                        recall[iou_thresh_ind, class_ind, area_ind, max_det_ind] = det_recall[
                            -1] if detection_count else 0

                        # Interpolate so that precision is always the highest value found at any recall level
                        for i in range(detection_count - 1, 0, -1):
                            if det_precision[i] > det_precision[i - 1]:
                                det_precision[i - 1] = det_precision[i]

                        # Find where the closest recall level position for each recall value
                        recall_insertion_indexes = np.searchsorted(det_recall, p.recThrs, side='left')
                        try:
                            det_scores_sorted = det_scores[sort_inds]
                            # Get the interpolated precision value at each recall level
                            for recall_level, recall_idx in enumerate(recall_insertion_indexes):
                                # Insert the highest precision value at the current recall level
                                precision_at_rec_lvl[recall_level] = det_precision[recall_idx]
                                score_at_rec_lvl[recall_level] = det_scores_sorted[recall_idx]
                        except:
                            pass
                        precision[iou_thresh_ind, :, class_ind, area_ind, max_det_ind] = np.array(precision_at_rec_lvl)
                        scores[iou_thresh_ind, :, class_ind, area_ind, max_det_ind] = np.array(score_at_rec_lvl)
        self.eval = {
            'params': p,
            'counts': [iou_len, rec_lvls_len, class_len, area_len, mdets_len],
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'confusion_matrix': confusion_matrix,
            'precision': precision,
            'recall': recall,
            'scores': scores,
        }
        toc = time.time()
        print('DONE (t={:0.2f}s).'.format(toc - tic))

    def summarize(self):
        '''
        Compute and display summary metrics for evaluation results.
        Note this functin can *only* be applied on the default parameter setting
        '''

        def _summarize(ap=1, iouThr=None, areaRng='all', maxDets=100):
            p = self.params
            iStr = ' {:<18} {} @[ IoU={:<9} | area={:>6s} | maxDets={:>3d} ] = {:0.3f}'
            titleStr = 'Average Precision' if ap == 1 else 'Average Recall'
            typeStr = '(AP)' if ap == 1 else '(AR)'
            iouStr = '{:0.2f}:{:0.2f}'.format(p.iouThrs[0], p.iouThrs[-1]) \
                if iouThr is None else '{:0.2f}'.format(iouThr)

            aind = [i for i, aRng in enumerate(p.areaRngLbl) if aRng == areaRng]
            mind = [i for i, mDet in enumerate(p.maxDets) if mDet == maxDets]
            if ap == 1:
                # dimension of precision: [TxRxKxAxM]
                s = self.eval['precision']
                # IoU
                if iouThr is not None:
                    t = np.where(iouThr == p.iouThrs)[0]
                    s = s[t]
                s = s[:, :, :, aind, mind]
            else:
                # dimension of recall: [TxKxAxM]
                s = self.eval['recall']
                if iouThr is not None:
                    t = np.where(iouThr == p.iouThrs)[0]
                    s = s[t]
                s = s[:, :, aind, mind]
            if len(s[s > -1]) == 0:
                mean_s = -1
            else:
                mean_s = np.mean(s[s > -1])
            print(iStr.format(titleStr, typeStr, iouStr, areaRng, maxDets, mean_s))
            return mean_s

        def _summarizeDets():
            stats = np.zeros((12,))
            stats[0] = _summarize(1)
            stats[1] = _summarize(1, iouThr=.5, maxDets=self.params.maxDets[2])
            stats[2] = _summarize(1, iouThr=.75, maxDets=self.params.maxDets[2])
            stats[3] = _summarize(1, areaRng='small', maxDets=self.params.maxDets[2])
            stats[4] = _summarize(1, areaRng='medium', maxDets=self.params.maxDets[2])
            stats[5] = _summarize(1, areaRng='large', maxDets=self.params.maxDets[2])
            stats[6] = _summarize(0, maxDets=self.params.maxDets[0])
            stats[7] = _summarize(0, maxDets=self.params.maxDets[1])
            stats[8] = _summarize(0, maxDets=self.params.maxDets[2])
            stats[9] = _summarize(0, areaRng='small', maxDets=self.params.maxDets[2])
            stats[10] = _summarize(0, areaRng='medium', maxDets=self.params.maxDets[2])
            stats[11] = _summarize(0, areaRng='large', maxDets=self.params.maxDets[2])
            return stats

        def _summarizeKps():
            stats = np.zeros((10,))
            stats[0] = _summarize(1, maxDets=20)
            stats[1] = _summarize(1, maxDets=20, iouThr=.5)
            stats[2] = _summarize(1, maxDets=20, iouThr=.75)
            stats[3] = _summarize(1, maxDets=20, areaRng='medium')
            stats[4] = _summarize(1, maxDets=20, areaRng='large')
            stats[5] = _summarize(0, maxDets=20)
            stats[6] = _summarize(0, maxDets=20, iouThr=.5)
            stats[7] = _summarize(0, maxDets=20, iouThr=.75)
            stats[8] = _summarize(0, maxDets=20, areaRng='medium')
            stats[9] = _summarize(0, maxDets=20, areaRng='large')
            return stats

        if not self.eval:
            raise Exception('Please run accumulate() first')
        iouType = self.params.iouType
        if iouType == 'segm' or iouType == 'bbox':
            summarize = _summarizeDets
        elif iouType == 'keypoints':
            summarize = _summarizeKps
        self.stats = summarize()

    def __str__(self):
        self.summarize()


class Params:
    '''
    Params for coco evaluation api
    '''

    def setDetParams(self):
        self.imgIds = []
        self.catIds = []
        # np.arange causes trouble.  the data point on arange is slightly larger than the true value
        self.iouThrs = np.linspace(.5, 0.95, int(np.round((0.95 - .5) / .05)) + 1, endpoint=True)
        self.recThrs = np.linspace(.0, 1.00, int(np.round((1.00 - .0) / .01)) + 1, endpoint=True)
        self.maxDets = [1, 10, 100]
        self.areaRng = [[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]
        self.areaRngLbl = ['all', 'small', 'medium', 'large']
        self.useCats = 1

    def setKpParams(self):
        self.imgIds = []
        self.catIds = []
        # np.arange causes trouble.  the data point on arange is slightly larger than the true value
        self.iouThrs = np.linspace(.5, 0.95, int(np.round((0.95 - .5) / .05)) + 1, endpoint=True)
        self.recThrs = np.linspace(.0, 1.00, int(np.round((1.00 - .0) / .01)) + 1, endpoint=True)
        self.maxDets = [20]
        self.areaRng = [[0 ** 2, 1e5 ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]
        self.areaRngLbl = ['all', 'medium', 'large']
        self.useCats = 1
        self.kpt_oks_sigmas = np.array(
            [.26, .25, .25, .35, .35, .79, .79, .72, .72, .62, .62, 1.07, 1.07, .87, .87, .89, .89]) / 10.0

    def __init__(self, iouType='segm'):
        if iouType == 'segm' or iouType == 'bbox':
            self.setDetParams()
        elif iouType == 'keypoints':
            self.setKpParams()
        else:
            raise Exception('iouType not supported')
        self.iouType = iouType
        # useSegm is deprecated
        self.useSegm = None
