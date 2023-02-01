from habana_frameworks.mediapipe.backend.nodes import opnode_tensor_info
from habana_frameworks.mediapipe.operators.media_nodes import MediaCPUNode
from habana_frameworks.mediapipe.media_types import dtype as dt
import numpy as np
import PIL.Image


class zoom(MediaCPUNode):
    """
    Class representing media zoom cpu node.

    """

    def __init__(self, name, guid, device, inputs, params, cparams, node_attr):
        """
        Constructor method.

        :params name: node name.
        :params guid: guid of node.
        :params device: device on which this node should execute.
        :params params: node specific params.
        :params cparams: backend params.
        :params node_attr: node output information
        """
        super().__init__(
            name, None, device, inputs, params, cparams, node_attr)
        self.patch_size = params['patch_size'].copy()
        self.patch_size_np = self.patch_size[::-1]
        self.num_channels = params['num_channels']

        if len(self.patch_size) != 3:
            raise ValueError("3D patch size expected")

    def set_params(self, params):
        """
        Setter method to set mediapipe specific params.

        :params params: mediapipe params of type "opnode_params".
        """
        self.batch_size = params.batch_size

    def gen_output_info(self):
        """
        Method to generate output type information.

        :returns : output tensor information of type "opnode_tensor_info".
        """
        self.img_shape = self.patch_size.copy()
        self.img_shape.append(self.num_channels)
        self.img_shape.append(self.batch_size)
        self.img_shape_np = self.img_shape[::-1]
        self.img_dtype = dt.FLOAT32
        self.lbl_shape = self.patch_size.copy()
        self.lbl_shape.append(1)  # labels channels is taken as one
        self.lbl_shape.append(self.batch_size)
        self.lbl_shape_np = self.lbl_shape[::-1]
        self.lbl_dtype = dt.UINT8
        out_info = []
        o = opnode_tensor_info(self.img_dtype, np.array(
            self.img_shape, dtype=np.uint32), "")
        out_info.append(o)
        o = opnode_tensor_info(self.lbl_dtype, np.array(
            self.lbl_shape, dtype=np.uint32), "")
        out_info.append(o)
        return out_info

    def __call__(self, img_sliced, lbl_sliced, cropped_patch):
        """
        Callable class method.

        :params img_sliced: image data
        :params lbl_sliced: label data
        :params cropped_patch: crop data
        """

        patch_size_np_ar = np.array(self.patch_size_np, dtype=dt.UINT32)

        img_resample = PIL.Image.Resampling.BICUBIC
        lbl_resample = PIL.Image.Resampling.NEAREST

        # [batch_size] + [num_channel] + self.patch_size_np
        img_zoom = img_sliced
        lbl_zoom = lbl_sliced

        cropped_patch_np_ar = np.flip(cropped_patch, axis=1)

        for i in range(self.batch_size):
            # if crop/zoom to be done
            if (np.array_equal(patch_size_np_ar, cropped_patch_np_ar[i]) == False):

                offset = ((patch_size_np_ar - cropped_patch_np_ar[i]) + 1) // 2

                cropped_img_shape = [self.num_channels] + \
                    list(cropped_patch_np_ar[i])  # CDHW
                cropped_lbl_shape = [1] + list(cropped_patch_np_ar[i])  # CDHW

                out_img_cropped = np.empty(
                    shape=cropped_img_shape, dtype=self.img_dtype)
                out_lbl_cropped = np.empty(
                    shape=cropped_lbl_shape, dtype=self.lbl_dtype)

                out_img_cropped = img_sliced[i][:,
                                                offset[0]:offset[0]+cropped_patch_np_ar[i][0],
                                                offset[1]:offset[1]+cropped_patch_np_ar[i][1],
                                                offset[2]:offset[2]+cropped_patch_np_ar[i][2]]

                out_lbl_cropped = lbl_sliced[i][:,
                                                offset[0]:offset[0]+cropped_patch_np_ar[i][0],
                                                offset[1]:offset[1]+cropped_patch_np_ar[i][1],
                                                offset[2]:offset[2]+cropped_patch_np_ar[i][2]]

                sizeXY = [self.patch_size_np[2], self.patch_size_np[1]]
                sizeXZ = [self.patch_size_np[2], self.patch_size_np[0]]

                tmp_img = np.zeros([out_img_cropped.shape[0], out_img_cropped.shape[1], self.patch_size_np[1],
                                   self.patch_size_np[2]], dtype=self.img_dtype)  # num_channel + sliced D + patchsize_h + patch_size_w
                tmp_lbl = np.zeros([out_lbl_cropped.shape[0], out_lbl_cropped.shape[1], self.patch_size_np[1],
                                   self.patch_size_np[2]], dtype=self.lbl_dtype)  # 1 + sliced D + patchsize_h + patch_size_w

                # Resize image along XY axis
                for c in range(out_img_cropped.shape[0]):
                    for z in range(out_img_cropped.shape[1]):
                        in_img_slice = out_img_cropped[c, z]
                        out_img_slice = np.array(PIL.Image.fromarray(
                            in_img_slice).resize(sizeXY, resample=img_resample))
                        tmp_img[c, z] = out_img_slice

                # Resize image along XZ axis
                for c in range(out_img_cropped.shape[0]):
                    for y in range(self.patch_size_np[1]):
                        in_img_slice = tmp_img[c, :, y]
                        out_img_slice = np.array(PIL.Image.fromarray(
                            in_img_slice).resize(sizeXZ, resample=img_resample))
                        img_zoom[i][c, :, y, :] = out_img_slice

                # Resize label along XY axis
                for c in range(out_lbl_cropped.shape[0]):
                    for z in range(out_lbl_cropped.shape[1]):
                        in_lbl_slice = out_lbl_cropped[c, z]
                        out_lbl_slice = np.array(PIL.Image.fromarray(
                            in_lbl_slice).resize(sizeXY, resample=lbl_resample))
                        tmp_lbl[c, z] = out_lbl_slice

                # Resize label along XZ axis
                for c in range(out_lbl_cropped.shape[0]):
                    for y in range(self.patch_size_np[1]):
                        in_lbl_slice = tmp_lbl[c, :, y]
                        out_lbl_slice = np.array(PIL.Image.fromarray(
                            in_lbl_slice).resize(sizeXZ, resample=lbl_resample))
                        lbl_zoom[i][c, :, y, :] = out_lbl_slice

        return img_zoom, lbl_zoom
